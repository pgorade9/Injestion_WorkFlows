import base64
import json
import logging
import os
import string
import time
import uuid
from typing import List, Optional
from deprecated import deprecated

import requests
from pydantic import BaseModel
from retry import retry

from src.filemetadata_templates.filemetadata_template import get_filemetadata_record_template
from src.schema_templates import (csv_parser_schema, wellbore_ingestor_schema, shapefile_ingestor_schema,
                                  doc_ingestor_schema, manifest_schema)
from src.wellbore_templates.wellbore_template import get_wellbore_template
import logging

from src.workflow_payload_templates.workflow_payload_templates import get_workflow_payload

logger = logging.getLogger(__name__)

mime_type = {
    'JPEG': 'image/jpeg',
    'PNG': 'image/png',
    'TIFF': 'image/tiff',
    'PDF': 'application/pdf',
    'MSWORD': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'MSEXCEL': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'MSPPTX': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'CSV': 'text/csv',
    'XLSX': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'LAS': 'application/vnd.las',
    'DLIS': 'application/octet-stream',
    'ZIP': 'application/x-zip'
}


@retry(exceptions=Exception, tries=2, delay=1, logger=logger)
def get_token(env_name):
    global platform
    if env_name.startswith("saas"):
        platform = "saas"
    elif env_name.startswith("ltops"):
        platform = "seds"
    elif env_name.startswith("seds_on"):
        platform = "seds"
    key_vault = {
        "saas": {
            "headers": {
                "content-type": "application/x-www-form-urlencoded"},
            "url": f"https://login.microsoftonline.com/{aad}/oauth2/v2.0/token",
            "payload": f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope={scope}"},
        "seds": {
            "headers": {
                "content-type": "application/x-www-form-urlencoded"},
            "url": "https://csi.slb.com/v2/token",
            "payload": f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope={scope}"
        },

    }
    print(key_vault.get(platform).get("url"))
    print(key_vault.get(platform).get("headers"))
    print(key_vault.get(platform).get("payload"))
    response = requests.request(method="POST", url=key_vault.get(platform).get("url"),
                                headers=key_vault.get(platform).get("headers"),
                                data=key_vault.get(platform).get("payload"))

    if response.status_code == 200:
        print(f"********* Token Generated Successfully ************")
        response_dict = json.loads(response.text)
        print("Bearer " + response_dict["access_token"])
        return "Bearer " + response_dict["access_token"]
    else:
        print(f"Error occurred while creating token. {response.text}")
        exit(1)


def configure_logging():
    logging.basicConfig(
        filename=f'.\\logs\\logfile_{data_partition_id}.log',
        level=logging.INFO,  # This is minimum level above which all logs will be seen
        format=f'%(asctime)s:%(levelname)s:{uuid.uuid4()}:%(message)s',
        filemode='a')


def create_wellbore():
    print(f"Creating Wellbore with kind {wellbore_kind}")
    logging.info(f"Creating Wellbore with kind {wellbore_kind}")
    url = f"{adme_dns_host}/api/os-wellbore-ddms/ddms/v3/wellbores"

    payload = get_wellbore_template(wellbore_kind, acl_domain, data_partition_id, acl_user=acl_user,
                                    own_acl_role=own_acl_role,
                                    view_acl_role=view_acl_role, legal=legal_tag)
    headers = {
        'data-partition-id': f'{data_partition_id}',
        'Authorization': f'{osdu_token}',
        'subscription-key': f'{happyme_subscription_key}'
        # 'Content-Type': 'application/json'
    }
    # request = requests.post(url=url,headers=headers, data=payload)
    # print(payload)
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200 and response.content:
        wellbore_id = json.loads(response.content)['recordIds'][0]
        print(wellbore_id)
        logging.info(f"Wellbore created with Id = {wellbore_id}")
        return wellbore_id
    else:
        print("Error occurred while creating wellbore ", response.status_code, response.text)


def create_file_metadata(wellbore_id=None):
    ## Step 1 - Get File Metadata Upload URL
    file_metadata_upload_url = f"{adme_dns_host}/api/file/v2/files/uploadURL"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'data-partition-id': data_partition_id,
        'frame-of-reference': 'none',
        'Authorization': osdu_token,
        # 'subscription-key': happyme_subscription_key
    }
    response = requests.request(method="GET", url=file_metadata_upload_url, headers=headers, timeout=TIME_OUT)
    print(response.text)
    if response.status_code == 401:
        print("Invalid or Expired Token")
        exit(1)

    elif response.status_code == 403:
        print(f"Access Denied {file_metadata_upload_url}")
        exit(1)

    file_service_upload_response = json.loads(response.text)
    signed_url_to_upload_file = file_service_upload_response['Location']['SignedURL']
    # global file_source_path
    file_source_path = file_service_upload_response['Location']['FileSource']

    ## Step 2 - Put File Metadata Upload URL
    file_size = os.path.getsize(local_file_path)
    input_file = open(local_file_path, "rb")
    payload = input_file.read()
    headers = {
        'x-ms-blob-type': 'BlockBlob'
    }
    if mime_type.get(file_type):
        headers.update({'Content-Type': f"{mime_type[file_type]}"})
    response = requests.request("PUT", signed_url_to_upload_file, headers=headers, data=payload, timeout=TIME_OUT)

    ## Step 3 - Post File Metadata Upload URL
    if 200 <= response.status_code <= 299:
        print("\nFile Uploaded on Cloud successfully. Response Status Code = " + "201")
        filemetadata_config = dict(file_source_path=file_source_path, wellbore_id=wellbore_id, filename=filename,
                                   target_kind=target_kind, file_type=file_type, mime_type=mime_type.get(file_type),
                                   file_size=file_size, authority=authority, acl_user=acl_user,
                                   own_acl_role=own_acl_role, view_acl_role=view_acl_role,
                                   ingestion_type=ingestion_type, data_partition_id=data_partition_id,
                                   acl_domain=acl_domain, legal_tag=legal_tag,
                                   definitive_trajectory=definitive_trajectory)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'data-partition-id': data_partition_id,
            'Authorization': osdu_token,
            'subscription-key': happyme_subscription_key
        }
        if ingestion_type == "Generic":
            create_file_metadata_url = f"{adme_dns_host}/api/file/v2/files/metadata"
            payload = json.dumps(
                get_filemetadata_record_template(**filemetadata_config), indent=2)
            print(payload)
            response = requests.request("POST", create_file_metadata_url, headers=headers, data=payload,
                                        timeout=TIME_OUT)
            if response.status_code == 201 and ingestion_type == "Generic":
                json_response = json.loads(response.text)
                # print("id = " + json_response['id'])
                return json_response['id']
            else:
                if response.text.find("legal") != -1:
                    print(f"Invalid legal tags = {legal_tag}")
                print(
                    f"Error occurred while creating Filemetadata. Response Status Code = {response.status_code} reason = {response.text}")
                exit(1)
        else:
            create_file_metadata_url = f"{adme_dns_host}/api/dataset/v1/registerDataset"
            payload = json.dumps({
                "datasetRegistries": [
                    get_filemetadata_record_template(**filemetadata_config)
                ]
            })

            response = requests.request("PUT", create_file_metadata_url, headers=headers, data=payload,
                                        timeout=TIME_OUT)
            if response.status_code == 201 and ingestion_type != "Generic":
                json_response = json.loads(response.text)
                # print("id = " + json_response['datasetRegistries'][0]['id'])
                return json_response['datasetRegistries'][0]['id']
            else:
                if response.text.find("legal") != -1:
                    print(f"Invalid legal tags = {legal_tag}")
                print(
                    f"Error occurred while creating Filemetadata. Response Status Code = {response.status_code} reason = {response.text}")
                exit(1)
        print(response.text)

    else:
        print(f"\nFile Uploading Failed. Response Status Code = {response.status_code} reason = {response.text}")
        exit(1)


def encode_client_credentials(client_id: str, client_secret: str) -> str:
    """
    Combines client_id and client_secret with a colon in between and Base64 encodes the result.

    :param client_id: OSDU client ID
    :param client_secret: OSDU client secret
    :return: Base64-encoded string of "client_id:client_secret"
    """
    credentials = f"{client_id}:{client_secret}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    return encoded_credentials


@deprecated("this method is moved into workflow templates")
def create_workflow_payload(file_id):
    random_uuid = str(uuid.uuid4())  # without string conversion uuid returns dict giving JSON Type Error
    payload = {"runId": random_uuid, "executionContext": {}}
    payload["executionContext"]["dataPartitionId"] = data_partition_id
    payload["executionContext"]["id"] = file_id
    payload["executionContext"]["sToken"] = encode_client_credentials(client_id=client_id, client_secret=client_secret)
    print(f"workflow {payload=}")
    return payload


def create_dag_ui_payload(message, dag_name):
    print("\nDAG RUN FROM UI PAYLOAD")
    run_id = str(uuid.uuid4())
    payload = {"run_id": run_id, "execution_context": message["executionContext"], "correlation_id": run_id,
               "authToken": osdu_token, "user_email_id": client_id,
               "workflow_name": dag_name
               }
    # dag_payload = {"run_id": message["runId"],
    #                "execution_context": message["executionContext"],
    #                "authToken": osdu_token, "user_email_id": client_id,
    #                "workflow_name": dag_name}
    print(json.dumps(payload, indent=2))


def register_workflow(dag: string):
    print("\nRegistering Workflow")
    workflow_url = f"{seds_dns_host}/api/workflow/v1/workflow"
    headers = {
        'Accept': 'application/json',
        'data-partition-id': data_partition_id,
        'Authorization': osdu_token,
        'Content-Type': 'application/json'
    }
    payload_dict = {"description": dag, "workflowName": dag, "registrationInstructions": {}}
    payload_dict["registrationInstructions"]["dagContent"] = ""
    payload_dict["registrationInstructions"]["dagName"] = dag
    # print(payload_dict)
    response = requests.request("POST", workflow_url, headers=headers, data=json.dumps(payload_dict), timeout=TIME_OUT)
    if response.status_code == 200:
        return print(response.text)
    else:
        # error = json.loads(response.text)
        print(f"Error occurred while registering dag. error = {response.text}")


@retry(exceptions=TimeoutError, tries=2, delay=12)
def trigger_workflow(message):
    print("\nTriggering_workflow")
    if env.startswith("seds_on_adme"):
        workflow_url = f"{adme_dns_host}/api/workflow/v1/workflow/{dag_name}/workflowRun"
    else:
        workflow_url = f"{seds_dns_host}/api/workflow/v1/workflow/{dag_name}/workflowRun"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'data-partition-id': data_partition_id,
        'Authorization': osdu_token,
        'subscription-key': happyme_subscription_key
    }
    payload = message
    # print(payload)
    response = requests.request("POST", workflow_url, headers=headers, data=json.dumps(payload), timeout=TIME_OUT)
    if response.status_code == 200:
        # print(f"{response.headers=}")
        workflow_response_json = response.json()
        workflow_response_json['correlation-id'] = response.headers['correlation-id']
        print(f"{workflow_response_json=}")
        return workflow_response_json
    elif response.text.find("Workflow with name") != -1 and response.status_code == 404:
        return response.text
    else:
        print(f"Error occurred in triggering workflow at {workflow_url}" + str(
            response.status_code) + "reason = " + response.text)
        print("retrying with delay of 12 seconds")
        raise TimeoutError()


def workflow_status(workflow_runId):
    print("\nWorkflow status ....")
    if env.startswith("seds_on_adme"):
        workflow_url = f"{adme_dns_host}/api/workflow/v1/workflow/{dag_name}/workflowRun/{workflow_runId}"
    else:
        workflow_url = f"{seds_dns_host}/api/workflow/v1/workflow/{dag_name}/workflowRun/{workflow_runId}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'data-partition-id': data_partition_id,
        'Authorization': osdu_token
    }
    response = requests.request("GET", workflow_url, headers=headers, timeout=TIME_OUT)
    print(response.text)
    return response.text


class GsmRecord(BaseModel):
    correlationId: str
    recordId: Optional[str] = None
    recordIdVersion: Optional[str] = None
    stage: str
    status: str
    message: Optional[str] = None
    errorCode: int
    userEmail: str
    timestamp: int


@retry(exceptions=Exception, tries=2, delay=0)
def global_status(correlation_Id, success_records, failed_records):
    print("\nGlobal Status Monitoring....")
    gsm_url = f"{seds_dns_host}/api/status-processor/v1/status/query"
    headers = {'data-partition-id': data_partition_id,
               'Content-Type': 'application/json',
               'Authorization': osdu_token}
    payload = '{"statusQuery": {"correlationId": "' + correlation_Id + '"}}'
    response = requests.request("POST", gsm_url, headers=headers, data=payload, timeout=TIME_OUT)
    print(response.text)  # for viewing in Terminal
    print(response.status_code)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        records = response_json["results"]
        gsm_records: List[GsmRecord] = [GsmRecord(**item) for item in records]
        # print(f"{gsm_records=}")

        for record in gsm_records:
            # if record.message:
            # if record.message.__contains__("Record ingestion successful") or record.stage == "INGESTOR_SYNC":
            if record.stage == "INGESTOR_SYNC" and record.status == "SUCCESS":
                print(f"correlationId = {record.correlationId}")
                print(f"Record Stored Successfully : {record.recordId}")
                if record.recordId not in success_records:
                    logging.info(f"Record Stored Successfully : {record.recordId}")
                    success_records.append(record.recordId)
            elif record.stage == "INGESTOR" and record.status == "FAILED":
                print(f"Record Ingestion Failed : {record.message}")
                if record.timestamp not in failed_records:
                    logging.info(f"{file_type} Ingestion Failed : {record.errorCode}")
                    failed_records.append(record.timestamp)
    else:
        print("Please wait !!")


def check_schema_exist(target_kind) -> (bool, string):
    url = f"{os.getenv("adme_dns_host")}/api/schema-service/v1/schema"
    payload = {}
    headers = {
        'data-partition-id': data_partition_id,
        'Authorization': osdu_token,
        'accept': 'application/json',
        'subscription-key': happyme_subscription_key
    }
    authority, source, entity_type, version = target_kind.split(":")[0:4]
    version_parts = version.split(".")
    schemaVersionMajor = version_parts[0]
    schemaVersionMinor = version_parts[1]
    schemaVersionPatch = version_parts[2]
    params = {"authority": f"{authority}",
              "source": f"{source}",
              "entityType": f"{entity_type}",
              "schemaVersionMajor": f"{schemaVersionMajor}",
              "schemaVersionMinor": f"{schemaVersionMinor}",
              "schemaVersionPatch": f"{schemaVersionPatch}"
              }
    response = requests.request("GET", url, headers=headers, data=payload, params=params, timeout=TIME_OUT)
    print(response.text)

    if response.status_code == 200:
        response_body = json.loads(response.content)
        print(f"{len(response_body.get("schemaInfos"))=}")
        if len(response_body.get("schemaInfos")) > 0:
            # schema_id = response_body.get("schemaInfos")[0].get("schemaIdentity").get("id")
            return True, response_body.get("schemaInfos")[0].get("schemaIdentity").get("id")
        else:
            print("Response Status Code = ", response.status_code)
            print("Response error message = ", response.text)
            return False, ""
    elif response.status_code == 404:
        return False, ""
    else:
        print("**** Schema check failed")
        print("Response Status Code = ", response.status_code)
        print("Response error message = ", response.text)
        exit(1)


def create_schema(target_kind, dag) -> (bool, string):
    url = f"{adme_dns_host}/api/schema-service/v1/schema"
    authority, source, entity_type, version = target_kind.split(":")[0:4]
    print(f"{authority, source, entity_type, version, target_kind}")
    major, minor, patch = version.split(".")
    print(f"{major, minor, patch}")
    schema_mapper = {"csv_parser_wf_status_gsm": csv_parser_schema.get_schema_template(),
                     "doc_ingestor_azure_ocr_wf": doc_ingestor_schema.get_schema_template(),
                     "wellbore_ingestion_wf_gsm": wellbore_ingestor_schema.get_schema_template_well_log() if file_type in [
                         "LAS", "LIS", "DLIS"] else wellbore_ingestor_schema.get_schema_template_trajectory(),
                     "shapefile_ingestor_wf_status_gsm": shapefile_ingestor_schema.get_schema_template(),
                     "Osdu_ingest": manifest_schema.get_schema_template(data_partition_id)
                     }
    payload = json.dumps({
        "schema": schema_mapper[dag],
        "schemaInfo": {
            "createdBy": "pgorade@slb.com",
            "schemaIdentity": {
                "authority": f"{authority}",
                "entityType": f"{entity_type}",
                "id": f"{target_kind}",
                "schemaVersionMajor": f"{major}",
                "schemaVersionMinor": f"{minor}",
                "schemaVersionPatch": f"{patch}",
                "source": f"{source}"
            },
            "scope": "INTERNAL",
            "status": "DEVELOPMENT"

        }
    })
    headers = {
        'data-partition-id': f'{data_partition_id}',
        'Authorization': f'{osdu_token}',
        'Content-Type': 'application/json'
    }
    authority, source, entity_type = target_kind.split(":")[0:3]
    params = {"authority": f"{authority}",
              "source": f"{source}",
              "entityType": f"{entity_type}"}
    print("got token = ", osdu_token)

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    response_body = json.loads(response.content)
    if response.status_code == 201:
        # schema_id = response_body.get("schemaInfos")[0].get("schemaIdentity").get("id")
        return response_body.get("schemaIdentity").get("id")
    else:
        print("Error occurred while creating schema ", response.status_code, response.text)


def validate_and_register(dag, data_partition):
    print("\nValidating Workflow ")
    workflow_url = f"{seds_dns_host}/api/workflow/v1/workflow/{dag}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'data-partition-id': data_partition,
        'Authorization': osdu_token
    }
    response = requests.request("GET", workflow_url, headers=headers, timeout=TIME_OUT)
    print(response.text)
    if response.status_code == 200:
        print("DAG ALREADY REGISTERED !!")
    elif response.status_code == 404:
        register_workflow(dag)
    else:
        print("DAG Validation failure")
        exit(1)


if __name__ == "__main__":
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    aad = os.getenv("AAD")
    scope = os.getenv("SCOPE")
    env = os.getenv("ENV")
    osdu_token = get_token(env)

    adme_dns_host = os.getenv("ADME_DNS_HOST")
    seds_dns_host = os.getenv("SEDS_DNS_HOST")

    dag_name = os.getenv("DAG_NAME")
    acl_user = os.getenv("ACL_USER")
    own_acl_role = os.getenv("OWN_ACL_ROLE")
    view_acl_role = os.getenv("VIEW_ACL_ROLE")
    acl_domain = os.getenv("ACL_DOMAIN")
    data_partition_id = os.getenv("DATA_PARTITION_ID")
    authority = f"{data_partition_id}"
    target_kind = os.getenv("TARGET_KIND")
    file_type = os.getenv("FILE_TYPE")
    ingestion_type = os.getenv("INGESTION_TYPE")

    if ingestion_type == "RockImage":
        ingestion_type = f"Image.{file_type}"
        authority = "osdu"

    definitive_trajectory = os.getenv("DEFINITIVE_TRAJECTORY")
    wellbore_kind = os.getenv("WELLBORE_KIND")
    wellbore_id = os.getenv("WELLBORE_ID")

    filename = os.getenv("FILENAME")
    legal_tag = os.getenv("LEGAL_TAG")
    happyme_subscription_key = os.getenv("HAPPYME_SUBSCRIPTION_KEY")

    TIME_OUT = 60
    configure_logging()

    logging.info(f"Beginning workflow execution for dag : {dag_name}")
    logging.info(f"File used for running workflow : {filename}")

    schema_exists, schema_id = check_schema_exist(target_kind)
    if not schema_exists:
        print(f"Schema does not exist for kind {target_kind}")
        logging.info(f"Schema does not exist for kind {target_kind}")
        print("Creating Schema........")
        schema_id = create_schema(target_kind, dag_name)
        print(f"Schema created with id = {schema_id}")
        logging.info(f"Schema created for {data_partition_id} with id = {schema_id}")
    else:
        print(f"Schema already exists with id = {schema_id}")
        logging.info(f"Schema already exists with id = {schema_id}")

    local_file_path = f".\\input_files\\{filename}"
    print("File used for ingestion = " + local_file_path)

    if target_kind.__contains__("Trajectory"):
        wellbore = create_wellbore() if not wellbore_id else wellbore_id
        if wellbore_id:
            print(f"Wellbore Id provided = {wellbore_id}")
            logging.info(f"Wellbore Id provided = {wellbore_id}")
        if definitive_trajectory:
            print(f"DefinitiveTrajectory:True, VerticalReferenceID:RT")
            logging.info(f"DefinitiveTrajectory:True, VerticalReferenceID:RT")
        filemetadata_id = create_file_metadata(wellbore)
    else:
        filemetadata_id = create_file_metadata()
    print(filemetadata_id)
    logging.info(f"File Generic Id (Metadata) = {filemetadata_id}")
    # workflow_payload = create_workflow_payload(filemetadata_id)
    sToken = encode_client_credentials(client_id, client_secret)
    workflow_payload = get_workflow_payload(dag_name,
                                            data_partition_id,
                                            adme_dns_host,
                                            osdu_token,
                                            happyme_subscription_key,
                                            filemetadata_id,
                                            filename,
                                            sToken)
    print(f"{workflow_payload=}")
    create_dag_ui_payload(workflow_payload, dag_name)

    validate_and_register(dag_name, data_partition_id)

    workflow_response = trigger_workflow(workflow_payload)
    if workflow_response:
        print(workflow_response)

        logging.info(f"Workflow run_id = {workflow_response.get('runId')}")
        logging.info(f"Workflow correlation_id = {workflow_response.get('correlation-id')}")

        success_records = []
        failed_records = []
        while True:
            try:
                global_status(workflow_response["correlation-id"], success_records, failed_records)
                time.sleep(5)
                workflow_status(workflow_response['runId'])
                print("=" * 100)
            except KeyboardInterrupt:
                print("Exiting loop...")
                exit(1)
    else:
        print(f"Error while submitting workflow run {workflow_payload.get('runId')}")
