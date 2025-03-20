import json
import logging
import os
import uuid

import requests
from retry import retry

from configuration import keyvault
from filemetadata_templates.filemetadata_template import get_filemetadata_record_template
from wellbore_templates.wellbore_template import get_wellbore_template


def configure_logging(dp):
    logging.basicConfig(
        filename=f'.\\logs\\logfile_{dp}.log',
        level=logging.INFO,  # This is minimum level above which all logs will be seen
        format=f'%(asctime)s:%(levelname)s:{uuid.uuid4()}:%(message)s',
        filemode='a')


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


@retry(exceptions=Exception, tries=2, delay=0)
def get_token(env_name):
    global platform
    if env_name in keyvault["envs"]:
        platform = "saas"
    elif env_name in keyvault["envs-ltops"]:
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
    # print(key_vault.get(platform).get("url"))
    # print(key_vault.get(platform).get("headers"))
    # print(key_vault.get(platform).get("payload"))
    response = requests.request(method="POST", url=key_vault.get(platform).get("url"),
                                headers=key_vault.get(platform).get("headers"),
                                data=key_vault.get(platform).get("payload"))

    # print(response.text)
    if response.status_code == 200:
        # print(f"********* Token Generated Successfully ************")
        response_dict = json.loads(response.text)
        return "Bearer " + response_dict["access_token"]
    else:
        print(f"Error occurred while creating token. {response.text}")
        exit(1)


def create_wellbore():
    # print(f"Creating Wellbore with kind {wellbore_kind}")
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
        # print(wellbore_id)
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
        'subscription-key': happyme_subscription_key
    }
    response = requests.request("GET", file_metadata_upload_url, headers=headers, data=payload, timeout=TIME_OUT)
    # print(response.text)
    if response.status_code == 401:
        print("Invalid or Expired Token")
        exit(1)

    elif response.status_code == 403:
        print("Access Denied")
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
        # print("\nFile Uploaded on Cloud successfully. Response Status Code = " + "201")
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
            # print(payload)
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

    else:
        print(f"\nFile Uploading Failed. Response Status Code = {response.status_code} reason = {response.text}")
        exit(1)


if __name__ == "__main__":
    TIME_OUT = 60
    results = {}
    # change key to envs or envs-ltops
    envs = keyvault["envs-ltops"]
    dags = keyvault["dags-ltops"]

    for env in envs[:]:
        results[env] = {}
        client_id = keyvault[env]["client_id"]
        client_secret = keyvault[env]["client_secret"]
        aad = "41ff26dc-250f-4b13-8981-739be8610c21"
        scope = keyvault[env]["scope"]
        osdu_token = get_token(env)

        adme_dns_host = keyvault[env]["adme_dns_host"]
        seds_dns_host = keyvault[env]["seds_dns_host"]

        data_partition_id = keyvault[env]["data_partition_id"]
        configure_logging(data_partition_id)
        # Pre-PAAS
        # acl_domain = "enterprisedata.cloud.slb-ds.com" if env == "evt" else "enterprisedata.slb.com"
        # SEDS
        acl_domain = "dataservices.energy"
        acl_user = "default"
        own_acl_role = "owners"
        view_acl_role = "viewers"

        ingestion_type = "Generic"
        definitive_trajectory = False
        wellbore_kind = "osdu:wks:master-data--Wellbore:1.3.0"
        wellbore_id = None

        legal_tag = f"{data_partition_id}-default-legal"
        happyme_subscription_key = keyvault[env]["happy_me_subscription_key"]

        authority = f"{data_partition_id}"
        for dag in dags[:]:
            target_kind = keyvault[env]["target_kind"][dag]
            filename = keyvault["file_name"][dag]
            local_file_path = f".\\input_files\\{filename}"
            file_type = keyvault["file_types"][dag]

            ################# CREATE FILE METADATA ######################
            if target_kind.__contains__("Trajectory"):
                wellbore = create_wellbore() if wellbore_id is None else wellbore_id
                if wellbore_id:
                    # print(f"Wellbore Id provided = {wellbore_id}")
                    logging.info(f"Wellbore Id provided = {wellbore_id}")
                if definitive_trajectory:
                    # print(f"DefinitiveTrajectory:True, VerticalReferenceID:RT")
                    logging.info(f"DefinitiveTrajectory:True, VerticalReferenceID:RT")
                filemetadata_id = create_file_metadata(wellbore)
            else:
                filemetadata_id = create_file_metadata()
            results[env][dag] = filemetadata_id
            print(f"{env},{dag},{results[env][dag]}")
            logging.info(f"Bulk Metadata Generator for dag {dag} on {env} = {filemetadata_id}")
        print("=" * 50, "\n")
    for env in envs[:]:
        for dag in dags[:]:
            print(f"{env},{dag},{results[env][dag]}")
