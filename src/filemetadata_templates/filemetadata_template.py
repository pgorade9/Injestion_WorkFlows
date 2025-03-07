"""

FILE GENERIC 1.0.0

OSDU Definitions:
https://community.opengroup.org/osdu/data/data-definitions/-/blob/master/E-R/dataset/File.Generic.1.0.0.md#3-table-of-filegeneric-data-properties-section-abstractdataset
Prashant Gorade please refer AbstractDataset in OSDU for the attributes inside data

"""
import logging


def get_filemetadata_record_template(file_source_path, wellbore_id, filename, target_kind, file_type, mime_type,
                                     file_size, authority, acl_user,own_acl_role,view_acl_role,
                                     ingestion_type, data_partition_id, acl_domain, legal_tag,
                                     definitive_trajectory=False):
    filemetadata = {
        "data": {
            "Name": filename,
            "Description": "This is a " + file_type + " file.",
            "TotalSize": file_size,
            "EncodingFormatTypeID": f"{authority}:reference-data--EncodingFormatType:{mime_type}",
            "SchemaFormatTypeID": "string",
            "Endian": "BIG",
            "DatasetProperties": {
                "FileSourceInfo": {
                    "FileSource": file_source_path,
                    "Name": filename,
                    "FileSize": file_size,
                    "EncodingFormatTypeID": f"{authority}:reference-data--EncodingFormatType:{mime_type}"
                }
            },
            "Checksum": "string",
            "ExtensionProperties": {
                "Classification": "Raw Generic File",
                "Description": "This is a " + file_type + " file.",
                "ExternalIds": [
                    "string"
                ],
                "FileDateCreated": {},
                "FileDateModified": {},
                "FileContentsDetails": {
                    "TargetKind": target_kind,
                    "nestedFieldDelimiter": ".",
                    "FileType": file_type,
                    "SpatialMapping": {
                        "type": "point",
                        "latitude": "LATITUDE",
                        "longitude": "LONGITUDE"
                    },
                    "FrameOfReference": [
                        {
                            "kind": "CRS",
                            "name": "GCS_WGS_1984",
                            "persistableReference": "{\"wkt\":\"GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433],AUTHORITY[\\\"EPSG\\\",4326]]\",\"ver\":\"PE_10_3_1\",\"name\":\"GCS_WGS_1984\",\"authCode\":{\"auth\":\"EPSG\",\"code\":\"4326\"},\"type\":\"LBC\"}",
                            "propertyNames": [
                                "LATITUDE",
                                "LONGITUDE"
                            ],
                            "propertyValues": [
                                "deg"
                            ],
                            "uncertainty": 0
                        },
                        {
                            "kind": "DateTime",
                            "persistableReference": "{\"type\": \"DAT\", \"format\": \"MM-dd-yyyy\"}",
                            "propertyNames": [
                                "PERMIT_DATE",
                                "INITIAL_COMPLETION_DATE",
                                "STATUS_DATE",
                                "SPUD_date"
                            ],
                            "propertyValues": [],
                            "uncertainty": 0
                        },
                        {
                            "kind": "Unit",
                            "name": "ft",
                            "persistableReference": "{\"scaleOffset\":{\"scale\":0.3048,\"offset\":0.0},\"symbol\":\"ft\",\"baseMeasurement\":{\"ancestry\":\"Length\",\"type\":\"UM\"},\"type\":\"USO\"}",
                            "propertyNames": [
                                "MD",
                                "TVD",
                                "ELEVATION"
                            ],
                            "propertyValues": [
                                "ft"
                            ],
                            "uncertainty": 0
                        }
                    ]
                }
            },  # No attributes for Extension Properties defined in osdu data definitions
        },
        "meta": [],
        "version": 1619610331101956,
        "kind": f"{authority}:wks:dataset--File.{ingestion_type}:1.0.0",
        "acl": {
            "viewers": [
                f"data.{acl_user}.{view_acl_role}@{data_partition_id}.{acl_domain}"
            ],
            "owners": [
                f"data.{acl_user}.{own_acl_role}@{data_partition_id}.{acl_domain}"
            ]
        },
        "legal": {
            "legaltags": [
                f"{legal_tag}"
            ],
            "otherRelevantDataCountries": [
                "US"
            ],
            "status": "compliant"
        }
    }
    if definitive_trajectory:
        definitive_trajectory_attributes = {"DefinitiveTrajectory": True,
                                            "VerticalReferenceID": "RT"
                                            }
        filemetadata['data']['ExtensionProperties']['FileContentsDetails'] = {**filemetadata['data']['ExtensionProperties']['FileContentsDetails'], **definitive_trajectory_attributes}
    if wellbore_id:
        filemetadata['data']['ExtensionProperties']['FileContentsDetails']["WellboreID"] = wellbore_id
        filemetadata['data']['ExtensionProperties']['FileContentsDetails']['Authority'] = 'osdu'

    if file_type in ["LAS", "DLIS"]:
        filemetadata['data']['ExtensionProperties']['FileContentsDetails'] = {}
        filemetadata['data']['ExtensionProperties']['FileContentsDetails']['Authority'] = 'osdu'
        filemetadata['data']['ExtensionProperties']['FileContentsDetails']['FrameOfReference'] = []
        filemetadata['data']['ExtensionProperties']['FileContentsDetails']['FileType'] = file_type
        filemetadata['kind'] = f"osdu:wks:dataset--File.{ingestion_type}:1.0.0"

    # logging.info(f"File metadata kind = {filemetadata['kind']}")
    # print(f"File metadata kind = {filemetadata['kind']}")
    return filemetadata
