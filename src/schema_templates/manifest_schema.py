def get_schema_template(data_partition_id):
    return {
        "x-osdu-inheriting-from-kind": [],
        "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "x-osdu-schema-source": "osdu:wks:Manifest:1.0.0",
        "description": "Load manifest applicable for all types defined as 'kind', i.e. registered as schemas with the "
                       "Schema Service. It supports loading of individual 'records' of any group-type or "
                       "combinations. The load sequence follows a well-defined sequence. The 'ReferenceData' array is "
                       "processed first (if populated). The 'MasterData' array is processed second (if populated) "
                       "second. The 'Data' structure is processed last (if populated). Inside the 'Data' property the "
                       "'Datasets' array is processed first, followed by the 'WorkProductComponents' array, "
                       "the 'WorkProduct' is processed last. Any arrays are ordered. should there be "
                       "interdependencies, the dependent items must be placed behind their relationship targets, "
                       "e.g. a master-data Well record must placed in the 'MasterData' array before its Wellbores.",
        "title": "Load Manifest Schema",
        "type": "object",
        "definitions": {
            f"{data_partition_id}:wks:AbstractCommonResources:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractCommonResources:1.0.0",
                "description": "Common resources to be injected at root 'data' level for every entity, which is "
                               "persistable in Storage. The insertion is performed by the OsduSchemaComposer script.",
                "title": "OSDU Common Resources",
                "type": "object",
                "properties": {
                    "ResourceHomeRegionID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-OSDURegion:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The name of the home [cloud environment] region for this OSDU resource object.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "OSDURegion",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Resource Home Region ID",
                        "type": "string"
                    },
                    "ResourceHostRegionIDs": {
                        "description": "The name of the host [cloud environment] region(s) for this OSDU resource object.",
                        "title": "Resource Host Region ID",
                        "type": "array",
                        "items": {
                            "x-osdu-relationship": [
                                {
                                    "EntityType": "OSDURegion",
                                    "GroupType": "reference-data"
                                }
                            ],
                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-OSDURegion:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                            "type": "string"
                        }
                    },
                    "ResourceLifecycleStatus": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceLifecycleStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Resource Lifecycle status.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceLifecycleStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Resource Lifecycle Status",
                        "type": "string"
                    },
                    "ResourceSecurityClassification": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceSecurityClassification:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Classifies the security level of the resource.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceSecurityClassification",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Resource Security Classification",
                        "type": "string"
                    },
                    "ResourceCurationStatus": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceCurationStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Curation status.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceCurationStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Resource Curation Status",
                        "type": "string"
                    },
                    "ExistenceKind": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ExistenceKind:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Where does this data resource sit in the cradle-to-grave span of its existence?",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ExistenceKind",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Existence Kind",
                        "type": "string"
                    },
                    "Source": {
                        "title": "Data Source",
                        "type": "string",
                        "description": "The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed."
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractCommonResources.1.0.0.json"
            },
            f"{data_partition_id}:wks:work-product-component--GenericWorkProductComponent:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:work-product-component--GenericWorkProductComponent:1.0.0",
                "description": "An auto-generated placeholder schema representing work-product-component group-type records in data loading/ingestion/creation manifests. Do not use this kind for actual records.",
                "title": "GenericWorkProductComponent",
                "type": "object",
                "properties": {
                    "ancestry": {
                        "description": "The links to data, which constitute the inputs.",
                        "title": "Ancestry",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalParentList:1.0.0"
                    },
                    "data": {
                        "allOf": [
                            {
                                "$ref": f"#/definitions/{data_partition_id}:wks:AbstractCommonResources:1.0.0"
                            },
                            {
                                "description": "Generic reference object containing the universal group-type properties of a Work Product Component for inclusion in data type specific Work Product Component objects",
                                "title": "AbstractWPCGroupType",
                                "type": "object",
                                "properties": {
                                    "Datasets": {
                                        "type": "array",
                                        "items": {
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "dataset"
                                                }
                                            ],
                                            "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*)$",
                                            "description": "The SRN which identifies this OSDU File resource.",
                                            "type": "string"
                                        }
                                    },
                                    "IsDiscoverable": {
                                        "description": "A flag that indicates if the work product component is searchable, which means covered in the search index.",
                                        "type": "boolean"
                                    },
                                    "Artefacts": {
                                        "description": "An array of Artefacts - each artefact has a Role, Resource tuple. An artefact is distinct from the file, in the sense certain valuable information is generated during loading process (Artefact generation process). Examples include retrieving location data, performing an OCR which may result in the generation of artefacts which need to be preserved distinctly",
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "ResourceID": {
                                                    "x-osdu-relationship": [
                                                        {
                                                            "GroupType": "dataset"
                                                        }
                                                    ],
                                                    "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*)$",
                                                    "description": "The SRN which identifies this OSDU Artefact resource.",
                                                    "type": "string"
                                                },
                                                "ResourceKind": {
                                                    "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                                                    "description": "The kind or schema ID of the artefact. Resolvable with the Schema Service.",
                                                    "type": "string"
                                                },
                                                "RoleID": {
                                                    "x-osdu-relationship": [
                                                        {
                                                            "EntityType": "ArtefactRole",
                                                            "GroupType": "reference-data"
                                                        }
                                                    ],
                                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ArtefactRole:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                                    "description": "The SRN of this artefact's role.",
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "IsExtendedLoad": {
                                        "description": "A flag that indicates if the work product component is undergoing an extended load.  It reflects the fact that the work product component is in an early stage and may be updated before finalization.",
                                        "type": "boolean"
                                    }
                                }
                            }
                        ]
                    },
                    "kind": {
                        "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                        "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                        "title": "Entity Kind",
                        "type": "string",
                        "example": "osdu:wks:work-product-component--GenericWorkProductComponent:1.0.0"
                    },
                    "acl": {
                        "description": "The access control tags associated with this entity.",
                        "title": "Access Control List",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAccessControlList:1.0.0"
                    },
                    "version": {
                        "format": "int64",
                        "description": "The version number of this OSDU resource; set by the framework.",
                        "title": "Version Number",
                        "type": "integer",
                        "example": 1562066009929332
                    },
                    "tags": {
                        "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                        "additionalProperties": {
                            "type": "string"
                        },
                        "title": "Tag Dictionary",
                        "type": "object",
                        "example": {
                            "NameOfKey": "String value"
                        }
                    },
                    "modifyUser": {
                        "description": "The user reference, which created this version of this resource object. Set by the System.",
                        "title": "Resource Object Version Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "modifyTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Version Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:52:24.477Z"
                    },
                    "createTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:46:20.163Z"
                    },
                    "meta": {
                        "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                        "title": "Frame of Reference Meta Data",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:AbstractMetaItem:1.0.0"
                        }
                    },
                    "legal": {
                        "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                        "title": "Legal Tags",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalTags:1.0.0"
                    },
                    "createUser": {
                        "description": "The user reference, which created the first version of this resource object. Set by the System.",
                        "title": "Resource Object Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "id": {
                        "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:work-product-component\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+)$",
                        "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                        "title": "Entity ID",
                        "type": "string",
                        "example": "namespace:work-product-component--GenericWorkProductComponent:80575f9c-fc7b-516b-b44f-996874b9f775"
                    }
                },
                "required": [
                    "kind",
                    "acl",
                    "legal"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/work-product-component/GenericWorkProductComponent.1.0.0.json"
            },
            f"{data_partition_id}:wks:dataset--GenericDataset:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:dataset--GenericDataset:1.0.0",
                "description": "An auto-generated placeholder schema representing dataset group-type records in data loading/ingestion/creation manifests. Do not use this kind for actual records.",
                "title": "GenericDataset",
                "type": "object",
                "properties": {
                    "ancestry": {
                        "description": "The links to data, which constitute the inputs.",
                        "title": "Ancestry",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalParentList:1.0.0"
                    },
                    "data": {
                        "allOf": [
                            {
                                "$ref": f"#/definitions/{data_partition_id}:wks:AbstractCommonResources:1.0.0"
                            },
                            {
                                "description": "Schema fragment holding properties common for all datasets.",
                                "title": "AbstractDataset",
                                "type": "object",
                                "properties": {
                                    "Endian": {
                                        "description": "Endianness of binary value.  Enumeration: \"BIG\", \"LITTLE\".  If absent, applications will need to interpret from context indicators.",
                                        "type": "string",
                                        "enum": [
                                            "BIG",
                                            "LITTLE"
                                        ]
                                    },
                                    "Description": {
                                        "description": "An optional, textual description of the dataset.",
                                        "type": "string",
                                        "title": "Description",
                                        "example": "As originally delivered by ACME.com."
                                    },
                                    "DatasetProperties": {
                                        "description": "Placeholder for a specialization.",
                                        "type": "object",
                                        "title": "Dataset Properties",
                                        "example": {}
                                    },
                                    "TotalSize": {
                                        "format": "integer",
                                        "pattern": "^[0-9]+$",
                                        "description": "Total size of the dataset in bytes; for files it is the same as declared in FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
                                        "type": "string",
                                        "title": "Total Size",
                                        "example": 13245217273
                                    },
                                    "EncodingFormatTypeID": {
                                        "x-osdu-relationship": [
                                            {
                                                "EntityType": "EncodingFormatType",
                                                "GroupType": "reference-data"
                                            }
                                        ],
                                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-EncodingFormatType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                        "description": "EncodingFormatType ID reference value relationship. It can me a mime-type or media-type.",
                                        "type": "string",
                                        "title": "Encoding Format Type ID",
                                        "example": "namespace:reference-data--EncodingFormatType:text%2Fcsv:"
                                    },
                                    "Name": {
                                        "description": "An optional name of the dataset, e.g. a user friendly file or file collection name.",
                                        "type": "string",
                                        "title": "Name",
                                        "example": "Dataset X221/15"
                                    },
                                    "SchemaFormatTypeID": {
                                        "x-osdu-relationship": [
                                            {
                                                "EntityType": "SchemaFormatType",
                                                "GroupType": "reference-data"
                                            }
                                        ],
                                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-SchemaFormatType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                        "description": "Relationship to the SchemaFormatType reference value.",
                                        "type": "string",
                                        "title": "Schema Format Type ID",
                                        "example": "namespace:reference-data--SchemaFormatType:CWLS%20LAS3:"
                                    }
                                }
                            }
                        ]
                    },
                    "kind": {
                        "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                        "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                        "title": "Entity Kind",
                        "type": "string",
                        "example": "osdu:wks:dataset--GenericDataset:1.0.0"
                    },
                    "acl": {
                        "description": "The access control tags associated with this entity.",
                        "title": "Access Control List",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAccessControlList:1.0.0"
                    },
                    "version": {
                        "format": "int64",
                        "description": "The version number of this OSDU resource; set by the framework.",
                        "title": "Version Number",
                        "type": "integer",
                        "example": 1562066009929332
                    },
                    "tags": {
                        "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                        "additionalProperties": {
                            "type": "string"
                        },
                        "title": "Tag Dictionary",
                        "type": "object",
                        "example": {
                            "NameOfKey": "String value"
                        }
                    },
                    "modifyUser": {
                        "description": "The user reference, which created this version of this resource object. Set by the System.",
                        "title": "Resource Object Version Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "modifyTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Version Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:52:24.477Z"
                    },
                    "createTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:46:20.163Z"
                    },
                    "meta": {
                        "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                        "title": "Frame of Reference Meta Data",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:AbstractMetaItem:1.0.0"
                        }
                    },
                    "legal": {
                        "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                        "title": "Legal Tags",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalTags:1.0.0"
                    },
                    "createUser": {
                        "description": "The user reference, which created the first version of this resource object. Set by the System.",
                        "title": "Resource Object Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "id": {
                        "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+)$",
                        "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                        "title": "Entity ID",
                        "type": "string",
                        "example": "namespace:dataset--GenericDataset:b792625f-5cb1-56c5-9699-eb35259e1f9f"
                    }
                },
                "required": [
                    "kind",
                    "acl",
                    "legal"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/dataset/GenericDataset.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractAnyCrsFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0",
                "description": "A schema like GeoJSON FeatureCollection with a non-WGS 84 CRS context; based on https://geojson.org/schema/FeatureCollection.json. Attention: the coordinate order is fixed: Longitude/Easting/Westing/X first, followed by Latitude/Northing/Southing/Y, optionally height as third coordinate.",
                "title": "AbstractAnyCrsFeatureCollection",
                "type": "object",
                "required": [
                    "type",
                    "persistableReferenceCrs",
                    "features"
                ],
                "properties": {
                    "CoordinateReferenceSystemID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The CRS reference into the CoordinateReferenceSystem catalog.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "CoordinateReferenceSystem",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Coordinate Reference System ID",
                        "type": "string",
                        "example": "namespace:reference-data--CoordinateReferenceSystem:BoundCRS.SLB.32021.15851:"
                    },
                    "persistableReferenceCrs": {
                        "description": "The CRS reference as persistableReference string. If populated, the CoordinateReferenceSystemID takes precedence.",
                        "type": "string",
                        "title": "CRS Reference",
                        "example": "{\"lateBoundCRS\":{\"wkt\":\"PROJCS[\\\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",2000000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-100.5],PARAMETER[\\\"Standard_Parallel_1\\\",46.1833333333333],PARAMETER[\\\"Standard_Parallel_2\\\",47.4833333333333],PARAMETER[\\\"Latitude_Of_Origin\\\",45.6666666666667],UNIT[\\\"Foot_US\\\",0.304800609601219],AUTHORITY[\\\"EPSG\\\",32021]]\",\"ver\":\"PE_10_3_1\",\"name\":\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\",\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32021\"},\"type\":\"LBC\"},\"singleCT\":{\"wkt\":\"GEOGTRAN[\\\"NAD_1927_To_WGS_1984_79_CONUS\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],METHOD[\\\"NADCON\\\"],PARAMETER[\\\"Dataset_conus\\\",0.0],AUTHORITY[\\\"EPSG\\\",15851]]\",\"ver\":\"PE_10_3_1\",\"name\":\"NAD_1927_To_WGS_1984_79_CONUS\",\"authCode\":{\"auth\":\"EPSG\",\"code\":\"15851\"},\"type\":\"ST\"},\"ver\":\"PE_10_3_1\",\"name\":\"NAD27 * OGP-Usa Conus / North Dakota South [32021,15851]\",\"authCode\":{\"auth\":\"SLB\",\"code\":\"32021079\"},\"type\":\"EBC\"}"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "title": "AnyCrsGeoJSON Feature",
                            "type": "object",
                            "required": [
                                "type",
                                "properties",
                                "geometry"
                            ],
                            "properties": {
                                "geometry": {
                                    "oneOf": [
                                        {
                                            "type": "null"
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON Point",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsPoint"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON LineString",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "type": "number"
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsLineString"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON Polygon",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 4,
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 2,
                                                            "type": "array",
                                                            "items": {
                                                                "type": "number"
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsPolygon"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON MultiPoint",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "type": "number"
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsMultiPoint"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON MultiLineString",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 2,
                                                            "type": "array",
                                                            "items": {
                                                                "type": "number"
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsMultiLineString"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON MultiPolygon",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 4,
                                                            "type": "array",
                                                            "items": {
                                                                "minItems": 2,
                                                                "type": "array",
                                                                "items": {
                                                                    "type": "number"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsMultiPolygon"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "AnyCrsGeoJSON GeometryCollection",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "geometries"
                                            ],
                                            "properties": {
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "AnyCrsGeometryCollection"
                                                    ]
                                                },
                                                "geometries": {
                                                    "type": "array",
                                                    "items": {
                                                        "oneOf": [
                                                            {
                                                                "title": "AnyCrsGeoJSON Point",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "minItems": 2,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsPoint"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "AnyCrsGeoJSON LineString",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "minItems": 2,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "type": "number"
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsLineString"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "AnyCrsGeoJSON Polygon",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 4,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 2,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "type": "number"
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsPolygon"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "AnyCrsGeoJSON MultiPoint",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "type": "number"
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsMultiPoint"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "AnyCrsGeoJSON MultiLineString",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 2,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "type": "number"
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsMultiLineString"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "AnyCrsGeoJSON MultiPolygon",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 4,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "minItems": 2,
                                                                                    "type": "array",
                                                                                    "items": {
                                                                                        "type": "number"
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "AnyCrsMultiPolygon"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        ]
                                                    }
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        }
                                    ]
                                },
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "AnyCrsFeature"
                                    ]
                                },
                                "properties": {
                                    "oneOf": [
                                        {
                                            "type": "null"
                                        },
                                        {
                                            "type": "object"
                                        }
                                    ]
                                },
                                "bbox": {
                                    "minItems": 4,
                                    "type": "array",
                                    "items": {
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    },
                    "persistableReferenceUnitZ": {
                        "description": "The unit of measure for the Z-axis (only for 3-dimensional coordinates, where the CRS does not describe the vertical unit). Note that the direction is upwards positive, i.e. Z means height.",
                        "type": "string",
                        "title": "Z-Unit Reference",
                        "example": "{\"scaleOffset\":{\"scale\":1.0,\"offset\":0.0},\"symbol\":\"m\",\"baseMeasurement\":{\"ancestry\":\"Length\",\"type\":\"UM\"},\"type\":\"USO\"}"
                    },
                    "bbox": {
                        "minItems": 4,
                        "type": "array",
                        "items": {
                            "type": "number"
                        }
                    },
                    "persistableReferenceVerticalCrs": {
                        "description": "The VerticalCRS reference as persistableReference string. If populated, the VerticalCoordinateReferenceSystemID takes precedence. The property is null or empty for 2D geometries. For 3D geometries and absent or null persistableReferenceVerticalCrs the vertical CRS is either provided via persistableReferenceCrs's CompoundCRS or it is implicitly defined as EPSG:5714 MSL height.",
                        "type": "string",
                        "title": "Vertical CRS Reference",
                        "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"5773\"},\"type\":\"LBC\",\"ver\":\"PE_10_3_1\",\"name\":\"EGM96_Geoid\",\"wkt\":\"VERTCS[\\\"EGM96_Geoid\\\",VDATUM[\\\"EGM96_Geoid\\\"],PARAMETER[\\\"Vertical_Shift\\\",0.0],PARAMETER[\\\"Direction\\\",1.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",5773]]\"}"
                    },
                    "type": {
                        "type": "string",
                        "enum": [
                            "AnyCrsFeatureCollection"
                        ]
                    },
                    "VerticalCoordinateReferenceSystemID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The explicit VerticalCRS reference into the CoordinateReferenceSystem catalog. This property stays empty for 2D geometries. Absent or empty values for 3D geometries mean the context may be provided by a CompoundCRS in 'CoordinateReferenceSystemID' or implicitly EPSG:5714 MSL height",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "CoordinateReferenceSystem",
                                "GroupType": "reference-data"
                            }
                        ],
                        "title": "Vertical Coordinate Reference System ID",
                        "type": "string",
                        "example": "namespace:reference-data--CoordinateReferenceSystem:VerticalCRS.EPSG.5773:"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractAnyCrsFeatureCollection.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractMetaItem:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "oneOf": [
                    {
                        "title": "FrameOfReferenceUOM",
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "The unit symbol or name of the unit.",
                                "title": "UOM Unit Symbol",
                                "type": "string",
                                "example": "ft[US]"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the Unit.",
                                "title": "UOM Persistable Reference",
                                "type": "string",
                                "example": "{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}"
                            },
                            "unitOfMeasureID": {
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to unit of measure reference.",
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "UnitOfMeasure",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "type": "string",
                                "example": "namespace:reference-data--UnitOfMeasure:ftUS:"
                            },
                            "kind": {
                                "const": "Unit",
                                "title": "UOM Reference Kind",
                                "description": "The kind of reference, 'Unit' for FrameOfReferenceUOM."
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides Unit context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like \"Data.StructureA.PropertyB\" to define a unique context.",
                                "title": "UOM Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "HorizontalDeflection.EastWest",
                                    "HorizontalDeflection.NorthSouth"
                                ]
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    },
                    {
                        "title": "FrameOfReferenceCRS",
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "The name of the CRS.",
                                "title": "CRS Name",
                                "type": "string",
                                "example": "NAD27 * OGP-Usa Conus / North Dakota South [32021,15851]"
                            },
                            "coordinateReferenceSystemID": {
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to CRS reference.",
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CoordinateReferenceSystem",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "type": "string",
                                "example": "namespace:reference-data--CoordinateReferenceSystem:EPSG.32615:"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the CRS.",
                                "title": "CRS Persistable Reference",
                                "type": "string",
                                "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32615\"},\"type\":\"LBC\",\"ver\":\"PE_10_3_1\",\"name\":\"WGS_1984_UTM_Zone_15N\",\"wkt\":\"PROJCS[\\\"WGS_1984_UTM_Zone_15N\\\",GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Transverse_Mercator\\\"],PARAMETER[\\\"False_Easting\\\",500000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-93.0],PARAMETER[\\\"Scale_Factor\\\",0.9996],PARAMETER[\\\"Latitude_Of_Origin\\\",0.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",32615]]\"}"
                            },
                            "kind": {
                                "const": "CRS",
                                "title": "CRS Reference Kind",
                                "description": "The kind of reference, constant 'CRS' for FrameOfReferenceCRS."
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides CRS context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like \"Data.StructureA.PropertyB\" to define a unique context.",
                                "title": "CRS Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "KickOffPosition.X",
                                    "KickOffPosition.Y"
                                ]
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    },
                    {
                        "title": "FrameOfReferenceDateTime",
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "The name of the DateTime format and reference.",
                                "title": "DateTime Name",
                                "type": "string",
                                "example": "UTC"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying DateTime reference.",
                                "title": "DateTime Persistable Reference",
                                "type": "string",
                                "example": "{\"format\":\"yyyy-MM-ddTHH:mm:ssZ\",\"timeZone\":\"UTC\",\"type\":\"DTM\"}"
                            },
                            "kind": {
                                "const": "DateTime",
                                "title": "DateTime Reference Kind",
                                "description": "The kind of reference, constant 'DateTime', for FrameOfReferenceDateTime."
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides DateTime context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like \"Data.StructureA.PropertyB\" to define a unique context.",
                                "title": "DateTime Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Acquisition.StartTime",
                                    "Acquisition.EndTime"
                                ]
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    },
                    {
                        "title": "FrameOfReferenceAzimuthReference",
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "The name of the CRS or the symbol/name of the unit.",
                                "title": "AzimuthReference Name",
                                "type": "string",
                                "example": "TrueNorth"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying AzimuthReference.",
                                "title": "AzimuthReference Persistable Reference",
                                "type": "string",
                                "example": "{\"code\":\"TrueNorth\",\"type\":\"AZR\"}"
                            },
                            "kind": {
                                "const": "AzimuthReference",
                                "title": "AzimuthReference Reference Kind",
                                "description": "The kind of reference, constant 'AzimuthReference', for FrameOfReferenceAzimuthReference."
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides AzimuthReference context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like \"Data.StructureA.PropertyB\" to define a unique context.",
                                "title": "AzimuthReference Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Bearing"
                                ]
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    }
                ],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractMetaItem:1.0.0",
                "description": "A meta data item, which allows the association of named properties or property values to a Unit/Measurement/CRS/Azimuth/Time context.",
                "title": "Frame of Reference Meta Data Item",
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractMetaItem.1.0.0.json"
            },
            f"{data_partition_id}:wks:work-product--GenericWorkProduct:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:work-product--GenericWorkProduct:1.0.0",
                "description": "An auto-generated placeholder schema representing work-product group-type records in data loading/ingestion/creation manifests. Do not use this kind for actual records.",
                "title": "GenericWorkProduct",
                "type": "object",
                "properties": {
                    "ancestry": {
                        "description": "The links to data, which constitute the inputs.",
                        "title": "Ancestry",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalParentList:1.0.0"
                    },
                    "data": {
                        "allOf": [
                            {
                                "$ref": f"#/definitions/{data_partition_id}:wks:AbstractCommonResources:1.0.0"
                            },
                            {
                                "description": "A collection of work product components such as might be produced by a business activity and which is delivered to the data platform for loading.",
                                "title": "WorkProduct",
                                "type": "object",
                                "properties": {
                                    "Description": {
                                        "description": "Description of the purpose of the work product.",
                                        "type": "string"
                                    },
                                    "AuthorIDs": {
                                        "description": "Array of Authors' names of the work product.  Could be a person or company entity.",
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "IsExtendedLoad": {
                                        "description": "A flag that indicates if the work product is undergoing an extended load.  It reflects the fact that the work product is in an early stage and may be updated before finalization.",
                                        "type": "boolean"
                                    },
                                    "Name": {
                                        "description": "Name of the instance of Work Product - could be a shipment number.",
                                        "type": "string"
                                    },
                                    "Components": {
                                        "type": "array",
                                        "items": {
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "work-product-component"
                                                }
                                            ],
                                            "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:work-product-component\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*)$",
                                            "description": "The SRN which identifies this OSDU Work Product Component resource.",
                                            "type": "string"
                                        }
                                    },
                                    "SpatialArea": {
                                        "description": "A polygon boundary that reflects the locale of the content of the work product (location of the subject matter).",
                                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractSpatialLocation:1.0.0"
                                    },
                                    "CreationDateTime": {
                                        "format": "date-time",
                                        "description": "Date that a resource (work  product here) is formed outside of OSDU before loading (e.g. publication date, work product delivery package assembly date).",
                                        "type": "string"
                                    },
                                    "Annotations": {
                                        "description": "Array of Annotations",
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "BusinessActivities": {
                                        "description": "Array of business processes/workflows that the work product has been through (ex. well planning, exploration).",
                                        "type": "array",
                                        "items": {
                                            "description": "Business Activity",
                                            "type": "string"
                                        }
                                    },
                                    "IsDiscoverable": {
                                        "description": "A flag that indicates if the work product is searchable, which means covered in the search index.",
                                        "type": "boolean"
                                    },
                                    "SpatialPoint": {
                                        "description": "A centroid point that reflects the locale of the content of the work product (location of the subject matter).",
                                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractSpatialLocation:1.0.0"
                                    },
                                    "SubmitterName": {
                                        "description": "Name of the person that first submitted the work product package to OSDU.",
                                        "type": "string"
                                    },
                                    "LineageAssertions": {
                                        "description": "Defines relationships with other objects (any kind of Resource) upon which this work product depends.  The assertion is directed only from the asserting WP to ancestor objects, not children.  It should not be used to refer to files or artefacts within the WP -- the association within the WP is sufficient and Artefacts are actually children of the main WP file. They should be recorded in the Data.Artefacts[] array.",
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "title": "LineageAssertion",
                                            "properties": {
                                                "ID": {
                                                    "x-osdu-relationship": [],
                                                    "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                                    "description": "The object reference identifying the DIRECT, INDIRECT, REFERENCE dependency.",
                                                    "type": "string"
                                                },
                                                "LineageRelationshipType": {
                                                    "x-osdu-relationship": [
                                                        {
                                                            "EntityType": "LineageRelationshipType",
                                                            "GroupType": "reference-data"
                                                        }
                                                    ],
                                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LineageRelationshipType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                                    "description": "Used by LineageAssertion to describe the nature of the line of descent of a work product from a prior Resource, such as DIRECT, INDIRECT, REFERENCE.  It is not for proximity (number of nodes away), it is not to cover all the relationships in a full ontology or graph, and it is not to describe the type of activity that created the asserting WP.  LineageAssertion does not encompass a full provenance, process history, or activity model.",
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "Tags": {
                                        "description": "Array of key words to identify the work product, especially to help in search.",
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "kind": {
                        "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                        "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                        "title": "Entity Kind",
                        "type": "string",
                        "example": "osdu:wks:work-product--GenericWorkProduct:1.0.0"
                    },
                    "acl": {
                        "description": "The access control tags associated with this entity.",
                        "title": "Access Control List",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAccessControlList:1.0.0"
                    },
                    "version": {
                        "format": "int64",
                        "description": "The version number of this OSDU resource; set by the framework.",
                        "title": "Version Number",
                        "type": "integer",
                        "example": 1562066009929332
                    },
                    "tags": {
                        "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                        "additionalProperties": {
                            "type": "string"
                        },
                        "title": "Tag Dictionary",
                        "type": "object",
                        "example": {
                            "NameOfKey": "String value"
                        }
                    },
                    "modifyUser": {
                        "description": "The user reference, which created this version of this resource object. Set by the System.",
                        "title": "Resource Object Version Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "modifyTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Version Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:52:24.477Z"
                    },
                    "createTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:46:20.163Z"
                    },
                    "meta": {
                        "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                        "title": "Frame of Reference Meta Data",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:AbstractMetaItem:1.0.0"
                        }
                    },
                    "legal": {
                        "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                        "title": "Legal Tags",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalTags:1.0.0"
                    },
                    "createUser": {
                        "description": "The user reference, which created the first version of this resource object. Set by the System.",
                        "title": "Resource Object Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "id": {
                        "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:work-product\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+)$",
                        "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                        "title": "Entity ID",
                        "type": "string",
                        "example": "namespace:work-product--GenericWorkProduct:955930ee-e6bd-5ae0-a6ee-67ba902e1635"
                    }
                },
                "required": [
                    "kind",
                    "acl",
                    "legal"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/work-product/GenericWorkProduct.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractLegalTags:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractLegalTags:1.0.0",
                "description": "Legal meta data like legal tags, relevant other countries, legal status. This structure is included by the SystemProperties \"legal\", which is part of all OSDU records. Not extensible.",
                "additionalProperties": 'false',
                "title": "Legal Meta Data",
                "type": "object",
                "properties": {
                    "legaltags": {
                        "description": "The list of legal tags, which resolve to legal properties (like country of origin, export classification code, etc.) and rules with the help of the Compliance Service.",
                        "title": "Legal Tags",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "otherRelevantDataCountries": {
                        "description": "The list of other relevant data countries as an array of two-letter country codes, see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.",
                        "title": "Other Relevant Data Countries",
                        "type": "array",
                        "items": {
                            "pattern": "^[A-Z]{2}$",
                            "type": "string"
                        }
                    },
                    "status": {
                        "pattern": "^(compliant|uncompliant)$",
                        "description": "The legal status. Set by the system after evaluation against the compliance rules associated with the \"legaltags\" using the Compliance Service.",
                        "title": "Legal Status",
                        "type": "string"
                    }
                },
                "required": [
                    "legaltags",
                    "otherRelevantDataCountries"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractLegalTags.1.0.0.json"
            },
            f"{data_partition_id}:wks:reference-data--GenericReferenceData:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:reference-data--GenericReferenceData:1.0.0",
                "description": "An auto-generated placeholder schema representing reference-data group-type records in data loading/ingestion/creation manifests. Do not use this kind for actual records.",
                "title": "GenericReferenceData",
                "type": "object",
                "properties": {
                    "ancestry": {
                        "description": "The links to data, which constitute the inputs.",
                        "title": "Ancestry",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalParentList:1.0.0"
                    },
                    "data": {
                        "allOf": [
                            {
                                "$ref": f"#/definitions/{data_partition_id}:wks:AbstractCommonResources:1.0.0"
                            }
                        ]
                    },
                    "kind": {
                        "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                        "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                        "title": "Entity Kind",
                        "type": "string",
                        "example": "osdu:wks:reference-data--GenericReferenceData:1.0.0"
                    },
                    "acl": {
                        "description": "The access control tags associated with this entity.",
                        "title": "Access Control List",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAccessControlList:1.0.0"
                    },
                    "version": {
                        "format": "int64",
                        "description": "The version number of this OSDU resource; set by the framework.",
                        "title": "Version Number",
                        "type": "integer",
                        "example": 1562066009929332
                    },
                    "tags": {
                        "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                        "additionalProperties": {
                            "type": "string"
                        },
                        "title": "Tag Dictionary",
                        "type": "object",
                        "example": {
                            "NameOfKey": "String value"
                        }
                    },
                    "modifyUser": {
                        "description": "The user reference, which created this version of this resource object. Set by the System.",
                        "title": "Resource Object Version Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "modifyTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Version Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:52:24.477Z"
                    },
                    "createTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:46:20.163Z"
                    },
                    "meta": {
                        "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                        "title": "Frame of Reference Meta Data",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:AbstractMetaItem:1.0.0"
                        }
                    },
                    "legal": {
                        "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                        "title": "Legal Tags",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalTags:1.0.0"
                    },
                    "createUser": {
                        "description": "The user reference, which created the first version of this resource object. Set by the System.",
                        "title": "Resource Object Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "id": {
                        "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:reference-data\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+)$",
                        "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                        "title": "Entity ID",
                        "type": "string",
                        "example": "namespace:reference-data--GenericReferenceData:63ca0ed3-d6fb-53f0-8549-0916ef144266"
                    }
                },
                "required": [
                    "id",
                    "kind",
                    "acl",
                    "legal"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/reference-data/GenericReferenceData.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractSpatialLocation:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractSpatialLocation:1.0.0",
                "description": "A geographic object which can be described by a set of points.",
                "title": "AbstractSpatialLocation",
                "type": "object",
                "properties": {
                    "AsIngestedCoordinates": {
                        "description": "The original or 'as ingested' coordinates (Point, MultiPoint, LineString, MultiLineString, Polygon or MultiPolygon). The name 'AsIngestedCoordinates' was chosen to contrast it to 'OriginalCoordinates', which carries the uncertainty whether any coordinate operations took place before ingestion. In cases where the original CRS is different from the as-ingested CRS, the OperationsApplied can also contain the list of operations applied to the coordinate prior to ingestion. The data structure is similar to GeoJSON FeatureCollection, however in a CRS context explicitly defined within the AbstractAnyCrsFeatureCollection. The coordinate sequence follows GeoJSON standard, i.e. 'eastward/longitude', 'northward/latitude' {, 'upward/height' unless overridden by an explicit direction in the AsIngestedCoordinates.VerticalCoordinateReferenceSystemID}.",
                        "x-osdu-frame-of-reference": "CRS:",
                        "title": "As Ingested Coordinates",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAnyCrsFeatureCollection:1.0.0"
                    },
                    "SpatialParameterTypeID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-SpatialParameterType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "A type of spatial representation of an object, often general (e.g. an Outline, which could be applied to Field, Reservoir, Facility, etc.) or sometimes specific (e.g. Onshore Outline, State Offshore Outline, Federal Offshore Outline, 3 spatial representations that may be used by Countries).",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "SpatialParameterType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    },
                    "QuantitativeAccuracyBandID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-QuantitativeAccuracyBand:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "An approximate quantitative assessment of the quality of a location (accurate to > 500 m (i.e. not very accurate)), to < 1 m, etc.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "QuantitativeAccuracyBand",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    },
                    "CoordinateQualityCheckRemarks": {
                        "type": "array",
                        "description": "Freetext remarks on Quality Check.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "AppliedOperations": {
                        "description": "The audit trail of operations applied to the coordinates from the original state to the current state. The list may contain operations applied prior to ingestion as well as the operations applied to produce the Wgs84Coordinates. The text elements refer to ESRI style CRS and Transformation names, which may have to be translated to EPSG standard names.",
                        "title": "Operations Applied",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": [
                            "conversion from ED_1950_UTM_Zone_31N to GCS_European_1950; 1 points converted",
                            "transformation GCS_European_1950 to GCS_WGS_1984 using ED_1950_To_WGS_1984_24; 1 points successfully transformed"
                        ]
                    },
                    "QualitativeSpatialAccuracyTypeID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-QualitativeSpatialAccuracyType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "A qualitative description of the quality of a spatial location, e.g. unverifiable, not verified, basic validation.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "QualitativeSpatialAccuracyType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    },
                    "CoordinateQualityCheckPerformedBy": {
                        "type": "string",
                        "description": "The user who performed the Quality Check."
                    },
                    "SpatialLocationCoordinatesDate": {
                        "format": "date-time",
                        "description": "Date when coordinates were measured or retrieved.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "CoordinateQualityCheckDateTime": {
                        "format": "date-time",
                        "description": "The date of the Quality Check.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "Wgs84Coordinates": {
                        "title": "WGS 84 Coordinates",
                        "description": "The normalized coordinates (Point, MultiPoint, LineString, MultiLineString, Polygon or MultiPolygon) based on WGS 84 (EPSG:4326 for 2-dimensional coordinates, EPSG:4326 + EPSG:5714 (MSL) for 3-dimensional coordinates). This derived coordinate representation is intended for global discoverability only. The schema of this substructure is identical to the GeoJSON FeatureCollection https://geojson.org/schema/FeatureCollection.json. The coordinate sequence follows GeoJSON standard, i.e. longitude, latitude {, height}",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractFeatureCollection:1.0.0"
                    },
                    "SpatialGeometryTypeID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-SpatialGeometryType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Indicates the expected look of the SpatialParameterType, e.g. Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon. The value constrains the type of geometries in the GeoJSON Wgs84Coordinates and AsIngestedCoordinates.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "SpatialGeometryType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractSpatialLocation.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractFeatureCollection:1.0.0",
                "description": "GeoJSON feature collection as originally published in https://geojson.org/schema/FeatureCollection.json. Attention: the coordinate order is fixed: Longitude first, followed by Latitude, optionally height above MSL (EPSG:5714) as third coordinate.",
                "title": "GeoJSON FeatureCollection",
                "type": "object",
                "required": [
                    "type",
                    "features"
                ],
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "FeatureCollection"
                        ]
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "title": "GeoJSON Feature",
                            "type": "object",
                            "required": [
                                "type",
                                "properties",
                                "geometry"
                            ],
                            "properties": {
                                "geometry": {
                                    "oneOf": [
                                        {
                                            "type": "null"
                                        },
                                        {
                                            "title": "GeoJSON Point",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "Point"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON LineString",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "type": "number"
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "LineString"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON Polygon",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 4,
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 2,
                                                            "type": "array",
                                                            "items": {
                                                                "type": "number"
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "Polygon"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON MultiPoint",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "type": "number"
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "MultiPoint"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON MultiLineString",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 2,
                                                            "type": "array",
                                                            "items": {
                                                                "type": "number"
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "MultiLineString"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON MultiPolygon",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "coordinates"
                                            ],
                                            "properties": {
                                                "coordinates": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "array",
                                                        "items": {
                                                            "minItems": 4,
                                                            "type": "array",
                                                            "items": {
                                                                "minItems": 2,
                                                                "type": "array",
                                                                "items": {
                                                                    "type": "number"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "MultiPolygon"
                                                    ]
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "title": "GeoJSON GeometryCollection",
                                            "type": "object",
                                            "required": [
                                                "type",
                                                "geometries"
                                            ],
                                            "properties": {
                                                "type": {
                                                    "type": "string",
                                                    "enum": [
                                                        "GeometryCollection"
                                                    ]
                                                },
                                                "geometries": {
                                                    "type": "array",
                                                    "items": {
                                                        "oneOf": [
                                                            {
                                                                "title": "GeoJSON Point",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "minItems": 2,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "Point"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "GeoJSON LineString",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "minItems": 2,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "type": "number"
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "LineString"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "GeoJSON Polygon",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 4,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 2,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "type": "number"
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "Polygon"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "GeoJSON MultiPoint",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "type": "number"
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "MultiPoint"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "GeoJSON MultiLineString",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "minItems": 2,
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 2,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "type": "number"
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "MultiLineString"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            {
                                                                "title": "GeoJSON MultiPolygon",
                                                                "type": "object",
                                                                "required": [
                                                                    "type",
                                                                    "coordinates"
                                                                ],
                                                                "properties": {
                                                                    "coordinates": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "array",
                                                                            "items": {
                                                                                "minItems": 4,
                                                                                "type": "array",
                                                                                "items": {
                                                                                    "minItems": 2,
                                                                                    "type": "array",
                                                                                    "items": {
                                                                                        "type": "number"
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                            "MultiPolygon"
                                                                        ]
                                                                    },
                                                                    "bbox": {
                                                                        "minItems": 4,
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "number"
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        ]
                                                    }
                                                },
                                                "bbox": {
                                                    "minItems": 4,
                                                    "type": "array",
                                                    "items": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        }
                                    ]
                                },
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "Feature"
                                    ]
                                },
                                "properties": {
                                    "oneOf": [
                                        {
                                            "type": "null"
                                        },
                                        {
                                            "type": "object"
                                        }
                                    ]
                                },
                                "bbox": {
                                    "minItems": 4,
                                    "type": "array",
                                    "items": {
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    },
                    "bbox": {
                        "minItems": 4,
                        "type": "array",
                        "items": {
                            "type": "number"
                        }
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractFeatureCollection.1.0.0.json"
            },
            f"{data_partition_id}:wks:master-data--GenericMasterData:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:master-data--GenericMasterData:1.0.0",
                "description": "An auto-generated placeholder schema representing master-data group-type records in data loading/ingestion/creation manifests. Do not use this kind for actual records.",
                "title": "GenericMasterData",
                "type": "object",
                "properties": {
                    "ancestry": {
                        "description": "The links to data, which constitute the inputs.",
                        "title": "Ancestry",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalParentList:1.0.0"
                    },
                    "data": {
                        "allOf": [
                            {
                                "$ref": f"#/definitions/{data_partition_id}:wks:AbstractCommonResources:1.0.0"
                            }
                        ]
                    },
                    "kind": {
                        "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                        "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                        "title": "Entity Kind",
                        "type": "string",
                        "example": "osdu:wks:master-data--GenericMasterData:1.0.0"
                    },
                    "acl": {
                        "description": "The access control tags associated with this entity.",
                        "title": "Access Control List",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractAccessControlList:1.0.0"
                    },
                    "version": {
                        "format": "int64",
                        "description": "The version number of this OSDU resource; set by the framework.",
                        "title": "Version Number",
                        "type": "integer",
                        "example": 1562066009929332
                    },
                    "tags": {
                        "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                        "additionalProperties": {
                            "type": "string"
                        },
                        "title": "Tag Dictionary",
                        "type": "object",
                        "example": {
                            "NameOfKey": "String value"
                        }
                    },
                    "modifyUser": {
                        "description": "The user reference, which created this version of this resource object. Set by the System.",
                        "title": "Resource Object Version Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "modifyTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Version Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:52:24.477Z"
                    },
                    "createTime": {
                        "format": "date-time",
                        "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                        "title": "Resource Object Creation DateTime",
                        "type": "string",
                        "example": "2020-12-16T11:46:20.163Z"
                    },
                    "meta": {
                        "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                        "title": "Frame of Reference Meta Data",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:AbstractMetaItem:1.0.0"
                        }
                    },
                    "legal": {
                        "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                        "title": "Legal Tags",
                        "$ref": f"#/definitions/{data_partition_id}:wks:AbstractLegalTags:1.0.0"
                    },
                    "createUser": {
                        "description": "The user reference, which created the first version of this resource object. Set by the System.",
                        "title": "Resource Object Creation User Reference",
                        "type": "string",
                        "example": "some-user@some-company-cloud.com"
                    },
                    "id": {
                        "pattern": "^(surrogate-key:.+|[\\w\\-\\.]+:master-data\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+)$",
                        "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                        "title": "Entity ID",
                        "type": "string",
                        "example": "namespace:master-data--GenericMasterData:9ca8054c-bce6-5a3a-b51d-f216fb1085a5"
                    }
                },
                "required": [
                    "id",
                    "kind",
                    "acl",
                    "legal"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/master-data/GenericMasterData.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractAccessControlList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractAccessControlList:1.0.0",
                "description": "The access control tags associated with this entity. This structure is included by the SystemProperties \"acl\", which is part of all OSDU records. Not extensible.",
                "additionalProperties": 'false',
                "title": "Access Control List",
                "type": "object",
                "properties": {
                    "viewers": {
                        "description": "The list of viewers to which this data record is accessible/visible/discoverable formatted as an email (core.common.model.storage.validation.ValidationDoc.EMAIL_REGEX).",
                        "title": "List of Viewers",
                        "type": "array",
                        "items": {
                            "pattern": "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                            "type": "string"
                        }
                    },
                    "owners": {
                        "description": "The list of owners of this data record formatted as an email (core.common.model.storage.validation.ValidationDoc.EMAIL_REGEX).",
                        "title": "List of Owners",
                        "type": "array",
                        "items": {
                            "pattern": "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "owners",
                    "viewers"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractAccessControlList.1.0.0.json"
            },
            f"{data_partition_id}:wks:AbstractLegalParentList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2021, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractLegalParentList:1.0.0",
                "description": "A list of entity IDs in the data ecosystem, which act as legal parents to the current entity. This structure is included by the SystemProperties \"ancestry\", which is part of all OSDU records. Not extensible.",
                "additionalProperties": 'false',
                "title": "Parent List",
                "type": "object",
                "properties": {
                    "parents": {
                        "description": "An array of none, one or many entity references in the data ecosystem, which identify the source of data in the legal sense. In contract to other relationships, the source record version is required. Example: the 'parents' will be queried when e.g. the subscription of source data services is terminated; access to the derivatives is also terminated.",
                        "title": "Parents",
                        "type": "array",
                        "items": {
                            "x-osdu-relationship": [],
                            "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]+$",
                            "type": "string"
                        },
                        "example": []
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractLegalParentList.1.0.0.json"
            }
        },
        "properties": {
            "ReferenceData": {
                "description": "Reference-data are submitted as an array of records.",
                "type": "array",
                "items": {
                    "$ref": f"#/definitions/{data_partition_id}:wks:reference-data--GenericReferenceData:1.0.0"
                }
            },
            "MasterData": {
                "description": "Master-data are submitted as an array of records.",
                "type": "array",
                "items": {
                    "$ref": f"#/definitions/{data_partition_id}:wks:master-data--GenericMasterData:1.0.0"
                }
            },
            "kind": {
                "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                "description": "The schema identification for the manifest record following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                "title": "Manifest  Kind",
                "type": "string",
                "example": "osdu:wks:Manifest:1.0.0"
            },
            "Data": {
                "description": "Manifest schema for work-product, work-product-component, dataset ensembles. The items in 'Datasets' are processed first since they are referenced by 'WorkProductComponents' ('data.DatasetIDs[]' and 'data.Artefacts[].ResourceID'). The WorkProduct is processed last collecting the WorkProductComponents.",
                "type": "object",
                "properties": {
                    "WorkProduct": {
                        "description": "The work-product component capturing the work-product-component records belonging to this loading/ingestion transaction.",
                        "$ref": f"#/definitions/{data_partition_id}:wks:work-product--GenericWorkProduct:1.0.0"
                    },
                    "Datasets": {
                        "description": "The list of 'Datasets' or data containers holding the actual data. The record ids are usually internal surrogate keys enabling the association of dataset records with work-product-component records, namely via 'DatasetIDs' and 'Artefacts.ResourceID' (both referring to 'dataset' group-type entity types).",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:dataset--GenericDataset:1.0.0"
                        }
                    },
                    "WorkProductComponents": {
                        "description": "The list of work-product-components records. The record ids are internal surrogate keys enabling the association of work-product-component records with the work-product records.",
                        "type": "array",
                        "items": {
                            "$ref": f"#/definitions/{data_partition_id}:wks:work-product-component--GenericWorkProductComponent:1.0.0"
                        }
                    }
                }
            }
        },
        "$id": "https://schema.osdu.opengroup.org/json/manifest/Manifest.1.0.0.json"
    }
