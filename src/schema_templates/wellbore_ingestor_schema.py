def get_schema_template_trajectory():
    return {
        "x-osdu-inheriting-from-kind": [
            {
                "kind": "osdu:wks:AbstractWPCGroupType:1.0.0",
                "name": "WorkProductComponent"
            }
        ],
        "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the "
                          "\"License\"); you may not use this file except in compliance with the License. You may "
                          "obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless "
                          "required by applicable law or agreed to in writing, software distributed under the License "
                          "is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, "
                          "either express or implied. See the License for the specific language governing permissions "
                          "and limitations under the License.",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "x-osdu-schema-source": "osdu:wks:work-product-component--WellboreTrajectory:1.1.0",
        "description": "Work Product Component describing an individual instance of a wellbore trajectory data "
                       "object. Also called a deviation survey, wellbore trajectory is data that is used to calculate "
                       "the position and spatial uncertainty of a planned or actual wellbore in 2-dimensional and "
                       "3-dimensional space.",
        "title": "WellboreTrajectory",
        "type": "object",
        "x-osdu-review-status": "Accepted",
        "required": [
            "kind",
            "acl",
            "legal"
        ],
        "x-osdu-virtual-properties": {
            "data.VirtualProperties.DefaultLocation": {
                "type": "object",
                "priority": [
                    {
                        "path": "data.SpatialArea"
                    },
                    {
                        "path": "data.SpatialPoint"
                    }
                ]
            },
            "data.VirtualProperties.DefaultName": {
                "type": "string",
                "priority": [
                    {
                        "path": "data.Name"
                    }
                ]
            }
        },
        "additionalProperties": 'false',
        "x-osdu-supported-file-formats": [
            "WITSML",
            "P7/17",
            "P7/2000",
            "LAS2",
            "LAS3",
            "csv"
        ],
        "definitions": {
            "osdu:wks:AbstractWorkProductComponent:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractWorkProductComponent:1.0.0",
                "description": "Generic reference object containing the universal properties of a Work Product "
                               "Component for inclusion in data type specific Work Product Component objects",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractWorkProductComponent",
                "type": "object",
                "properties": {
                    "SpatialArea": {
                        "description": "A polygon boundary that reflects the locale of the content of the work product component (location of the subject matter).",
                        "$ref": "#/definitions/osdu:wks:AbstractSpatialLocation:1.0.0"
                    },
                    "Description": {
                        "description": "Description.  Summary of the work product component.  Not the same as Remark which captures thoughts of creator about the wpc.",
                        "type": "string"
                    },
                    "CreationDateTime": {
                        "format": "date-time",
                        "description": "Date that a resource (work  product component here) is formed outside of OSDU before loading (e.g. publication date).",
                        "type": "string"
                    },
                    "BusinessActivities": {
                        "description": "Array of business processes/workflows that the work product component has been through (ex. well planning, exploration).",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "SpatialPoint": {
                        "description": "A centroid point that reflects the locale of the content of the work product component (location of the subject matter).",
                        "$ref": "#/definitions/osdu:wks:AbstractSpatialLocation:1.0.0"
                    },
                    "GeoContexts": {
                        "x-osdu-indexing": {
                            "type": "nested"
                        },
                        "description": "List of geographic entities which provide context to the WPC.  This may include multiple types or multiple values of the same type.",
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractGeoContext:1.0.0"
                        }
                    },
                    "AuthorIDs": {
                        "description": "Array of Authors' names of the work product component.  Could be a person or company entity.",
                        "type": "array",
                        "title": "Author IDs",
                        "items": {
                            "type": "string"
                        }
                    },
                    "SubmitterName": {
                        "description": "Name of the person that first submitted the work product component to OSDU.",
                        "type": "string"
                    },
                    "LineageAssertions": {
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "Defines relationships with other objects (any kind of Resource) upon which this work product component depends.  The assertion is directed only from the asserting WPC to ancestor objects, not children.  It should not be used to refer to files or artefacts within the WPC -- the association within the WPC is sufficient and Artefacts are actually children of the main WPC file. They should be recorded in the data.Artefacts[] array.",
                        "type": "array",
                        "items": {
                            "description": "Defines relationships with other objects (any kind of Resource) upon which this work product component depends.  The assertion is directed only from the asserting WPC to ancestor objects, not children.  It should not be used to refer to files or artefacts within the WPC -- the association within the WPC is sufficient and Artefacts are actually children of the main WPC file. They should be recorded in the data.Artefacts[] array.",
                            "type": "object",
                            "title": "LineageAssertion",
                            "properties": {
                                "ID": {
                                    "x-osdu-relationship": [],
                                    "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
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
                                    "description": "Used by LineageAssertion to describe the nature of the line of descent of a work product component from a prior Resource, such as DIRECT, INDIRECT, REFERENCE.  It is not for proximity (number of nodes away), it is not to cover all the relationships in a full ontology or graph, and it is not to describe the type of activity that created the asserting WPC.  LineageAssertion does not encompass a full provenance, process history, or activity model.",
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
                    },
                    "Name": {
                        "description": "Name",
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractWorkProductComponent.1.0.0.json"
            },
            "osdu:wks:AbstractCommonResources:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractCommonResources:1.0.0",
                "description": "Common resources to be injected at root 'data' level for every entity, which is persistable in Storage. The insertion is performed by the OsduSchemaComposer script.",
                "x-osdu-review-status": "Accepted",
                "title": "OSDU Common Resources",
                "type": "object",
                "properties": {
                    "ResourceHomeRegionID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "OSDURegion",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-OSDURegion:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The name of the home [cloud environment] region for this OSDU resource object.",
                        "type": "string",
                        "title": "Resource Home Region ID"
                    },
                    "ResourceHostRegionIDs": {
                        "description": "The name of the host [cloud environment] region(s) for this OSDU resource object.",
                        "type": "array",
                        "title": "Resource Host Region ID",
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
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceLifecycleStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceLifecycleStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Resource Lifecycle status.",
                        "type": "string",
                        "title": "Resource Lifecycle Status"
                    },
                    "ResourceSecurityClassification": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceSecurityClassification",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceSecurityClassification:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Classifies the security level of the resource.",
                        "type": "string",
                        "title": "Resource Security Classification"
                    },
                    "ResourceCurationStatus": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceCurationStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceCurationStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Curation status.",
                        "type": "string",
                        "title": "Resource Curation Status"
                    },
                    "ExistenceKind": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ExistenceKind",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ExistenceKind:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Where does this data resource sit in the cradle-to-grave span of its existence?",
                        "type": "string",
                        "title": "Existence Kind"
                    },
                    "TechnicalAssuranceID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "TechnicalAssuranceType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TechnicalAssuranceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "DEPRECATED: Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "string",
                        "title": "Technical Assurance ID"
                    },
                    "Source": {
                        "description": "The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed.",
                        "type": "string",
                        "title": "Data Source"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractCommonResources.1.0.0.json"
            },
            "osdu:wks:AbstractMetaItem:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "oneOf": [
                    {
                        "title": "FrameOfReferenceUOM",
                        "type": "object",
                        "properties": {
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the Unit.",
                                "title": "UOM Persistable Reference",
                                "type": "string",
                                "example": "{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}"
                            },
                            "kind": {
                                "const": "Unit",
                                "description": "The kind of reference, 'Unit' for FrameOfReferenceUOM.",
                                "title": "UOM Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides Unit context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "UOM Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "HorizontalDeflection.EastWest",
                                    "HorizontalDeflection.NorthSouth"
                                ]
                            },
                            "name": {
                                "description": "The unit symbol or name of the unit.",
                                "title": "UOM Unit Symbol",
                                "type": "string",
                                "example": "ft[US]"
                            },
                            "unitOfMeasureID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "UnitOfMeasure",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to unit of measure reference.",
                                "type": "string",
                                "example": "namespace:reference-data--UnitOfMeasure:ftUS:"
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
                            "coordinateReferenceSystemID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CoordinateReferenceSystem",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to CRS reference.",
                                "type": "string",
                                "example": "namespace:reference-data--CoordinateReferenceSystem:Projected:EPSG::32615:"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the CRS.",
                                "title": "CRS Persistable Reference",
                                "type": "string",
                                "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32615\"},\"name\":\"WGS_1984_UTM_Zone_15N\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"PROJCS[\\\"WGS_1984_UTM_Zone_15N\\\",GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Transverse_Mercator\\\"],PARAMETER[\\\"False_Easting\\\",500000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-93.0],PARAMETER[\\\"Scale_Factor\\\",0.9996],PARAMETER[\\\"Latitude_Of_Origin\\\",0.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",32615]]\"}"
                            },
                            "kind": {
                                "const": "CRS",
                                "description": "The kind of reference, constant 'CRS' for FrameOfReferenceCRS.",
                                "title": "CRS Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides CRS context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "CRS Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "KickOffPosition.X",
                                    "KickOffPosition.Y"
                                ]
                            },
                            "name": {
                                "description": "The name of the CRS.",
                                "title": "CRS Name",
                                "type": "string",
                                "example": "WGS 84 / UTM zone 15N"
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
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying DateTime reference.",
                                "title": "DateTime Persistable Reference",
                                "type": "string",
                                "example": "{\"format\":\"yyyy-MM-ddTHH:mm:ssZ\",\"timeZone\":\"UTC\",\"type\":\"DTM\"}"
                            },
                            "kind": {
                                "const": "DateTime",
                                "description": "The kind of reference, constant 'DateTime', for FrameOfReferenceDateTime.",
                                "title": "DateTime Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides DateTime context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "DateTime Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Acquisition.StartTime",
                                    "Acquisition.EndTime"
                                ]
                            },
                            "name": {
                                "description": "The name of the DateTime format and reference.",
                                "title": "DateTime Name",
                                "type": "string",
                                "example": "UTC"
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
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying AzimuthReference.",
                                "title": "AzimuthReference Persistable Reference",
                                "type": "string",
                                "example": "{\"code\":\"TrueNorth\",\"type\":\"AZR\"}"
                            },
                            "kind": {
                                "const": "AzimuthReference",
                                "description": "The kind of reference, constant 'AzimuthReference', for FrameOfReferenceAzimuthReference.",
                                "title": "AzimuthReference Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides AzimuthReference context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "AzimuthReference Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Bearing"
                                ]
                            },
                            "name": {
                                "description": "The name of the CRS or the symbol/name of the unit.",
                                "title": "AzimuthReference Name",
                                "type": "string",
                                "example": "TrueNorth"
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    }
                ],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractMetaItem:1.0.0",
                "description": "A meta data item, which allows the association of named properties or property values to a Unit/Measurement/CRS/Azimuth/Time context.",
                "title": "Frame of Reference Meta Data Item",
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractMetaItem.1.0.0.json"
            },
            "osdu:wks:AbstractLegalParentList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractLegalParentList:1.0.0",
                "description": "A list of entity id:version references to record instances recorded in the data "
                               "platform, from which the current record is derived and from which the legal tags must "
                               "be derived. This structure is included by the SystemProperties \"ancestry\", "
                               "which is part of all OSDU records. Not extensible.",
                "additionalProperties": 'false',
                "title": "Parent List",
                "type": "object",
                "properties": {
                    "parents": {
                        "description": "An array of none, one or many entity references of 'direct parents' in the data platform, which mark the current record as a derivative. In contrast to other relationships, the source record version is required. During record creation or update the ancestry.parents[] relationships are used to collect the legal tags from the sources and aggregate them in the legal.legaltags[] array. As a consequence, should e.g., one or more of the legal tags of the source data expire, the access to the derivatives is also terminated. For details, see ComplianceService tutorial, 'Creating derivative Records'.",
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
            },
            "osdu:wks:AbstractGeoContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "oneOf": [
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoPoliticalContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoBasinContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoFieldContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoPlayContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoProspectContext:1.0.0"
                    }
                ],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoContext:1.0.0",
                "description": "A geographic context to an entity. It can be either a reference to a GeoPoliticalEntity, Basin, Field, Play or Prospect.",
                "title": "AbstractGeoContext",
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoContext.1.0.0.json"
            },
            "osdu:wks:AbstractFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
            "osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
                        "example": "namespace:reference-data--CoordinateReferenceSystem:BoundProjected:EPSG::32021_EPSG::15851:"
                    },
                    "persistableReferenceCrs": {
                        "description": "The CRS reference as persistableReference string. If populated, the CoordinateReferenceSystemID takes precedence.",
                        "type": "string",
                        "title": "CRS Reference",
                        "example": "{\"authCode\":{\"auth\":\"OSDU\",\"code\":\"32021079\"},\"lateBoundCRS\":{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32021\"},\"name\":\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"PROJCS[\\\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",2000000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-100.5],PARAMETER[\\\"Standard_Parallel_1\\\",46.18333333333333],PARAMETER[\\\"Standard_Parallel_2\\\",47.48333333333333],PARAMETER[\\\"Latitude_Of_Origin\\\",45.66666666666666],UNIT[\\\"Foot_US\\\",0.3048006096012192],AUTHORITY[\\\"EPSG\\\",32021]]\"},\"name\":\"NAD27 * OGP-Usa Conus / North Dakota CS27 South zone [32021,15851]\",\"singleCT\":{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"15851\"},\"name\":\"NAD_1927_To_WGS_1984_79_CONUS\",\"type\":\"ST\",\"ver\":\"PE_10_9_1\",\"wkt\":\"GEOGTRAN[\\\"NAD_1927_To_WGS_1984_79_CONUS\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],METHOD[\\\"NADCON\\\"],PARAMETER[\\\"Dataset_conus\\\",0.0],OPERATIONACCURACY[5.0],AUTHORITY[\\\"EPSG\\\",15851]]\"},\"type\":\"EBC\",\"ver\":\"PE_10_9_1\"}"
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
                        "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"5714\"},\"name\":\"MSL_Height\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"VERTCS[\\\"MSL_Height\\\",VDATUM[\\\"Mean_Sea_Level\\\"],PARAMETER[\\\"Vertical_Shift\\\",0.0],PARAMETER[\\\"Direction\\\",1.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",5714]]\"}"
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
                        "example": "namespace:reference-data--CoordinateReferenceSystem:Vertical:EPSG::5714:"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractAnyCrsFeatureCollection.1.0.0.json"
            },
            "osdu:wks:AbstractGeoFieldContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoFieldContext:1.0.0",
                "description": "A single, typed field entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "title": "AbstractGeoFieldContext",
                "type": "object",
                "properties": {
                    "FieldID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Field:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to Field.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Field",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "const": "Field",
                        "type": "string",
                        "description": "The fixed type 'Field' for this AbstractGeoFieldContext."
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoFieldContext.1.0.0.json"
            },
            "osdu:wks:AbstractGeoProspectContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoProspectContext:1.0.0",
                "description": "A single, typed Prospect entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoProspectContext",
                "type": "object",
                "properties": {
                    "ProspectID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Prospect:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the prospect.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Prospect",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "ProspectID",
                            "TargetPropertyName": "ProspectTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ProspectType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The ProspectType reference of the Prospect (via ProspectID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ProspectType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoProspectContext.1.0.0.json"
            },
            "osdu:wks:AbstractGeoBasinContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoBasinContext:1.0.0",
                "description": "A single, typed basin entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoBasinContext",
                "type": "object",
                "properties": {
                    "BasinID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Basin:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to Basin.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Basin",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "BasinID",
                            "TargetPropertyName": "BasinTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-BasinType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The BasinType reference of the Basin (via BasinID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "BasinType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoBasinContext.1.0.0.json"
            },
            "osdu:wks:AbstractSpatialLocation:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractSpatialLocation:1.0.0",
                "description": "A geographic object which can be described by a set of points.",
                "title": "AbstractSpatialLocation",
                "type": "object",
                "properties": {
                    "AsIngestedCoordinates": {
                        "description": "The original or 'as ingested' coordinates (Point, MultiPoint, LineString, MultiLineString, Polygon or MultiPolygon). The name 'AsIngestedCoordinates' was chosen to contrast it to 'OriginalCoordinates', which carries the uncertainty whether any coordinate operations took place before ingestion. In cases where the original CRS is different from the as-ingested CRS, the AppliedOperations can also contain the list of operations applied to the coordinate prior to ingestion. The data structure is similar to GeoJSON FeatureCollection, however in a CRS context explicitly defined within the AbstractAnyCrsFeatureCollection. The coordinate sequence follows GeoJSON standard, i.e. 'eastward/longitude', 'northward/latitude' {, 'upward/height' unless overridden by an explicit direction in the AsIngestedCoordinates.VerticalCoordinateReferenceSystemID}.",
                        "x-osdu-frame-of-reference": "CRS:",
                        "title": "As Ingested Coordinates",
                        "$ref": "#/definitions/osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0"
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
                        "$ref": "#/definitions/osdu:wks:AbstractFeatureCollection:1.0.0"
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
            "osdu:wks:AbstractLegalTags:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
            "osdu:wks:AbstractTechnicalAssurance:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractTechnicalAssurance:1.0.0",
                "description": "Describes a record's overall suitability for general business consumption based on level of trust.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractTechnicalAssurance",
                "type": "object",
                "required": [
                    "TechnicalAssuranceTypeID"
                ],
                "properties": {
                    "Comment": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Any additional context to support the determination of technical assurance",
                        "type": "string",
                        "title": "Comment",
                        "example": "This is free form text from reviewer, e.g. restrictions on use"
                    },
                    "Reviewers": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "The individuals, or roles, that reviewed and determined the technical assurance value",
                        "type": "array",
                        "title": "Reviewers",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractContact:1.0.0"
                        },
                        "example": [
                            {
                                "RoleTypeID": "namespace:reference-data--ContactRoleType:AccountOwner:",
                                "OrganisationID": "namespace:master-data--Organisation:SomeUniqueOrganisationID:",
                                "Name": "Example Name"
                            }
                        ]
                    },
                    "UnacceptableUsage": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "List of workflows and/or personas that the technical assurance value is not valid for (e.g., This data is not trusted for seismic interpretation)",
                        "type": "array",
                        "title": "Unacceptable Usage",
                        "items": {
                            "description": "Describes the workflows and/or personas that the technical assurance value is not valid for (e.g., This data has a technical assurance property of \"trusted\", but it is not suitable for Seismic Interpretation).",
                            "type": "object",
                            "title": "UnacceptableUsage",
                            "properties": {
                                "WorkflowUsage": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowUsageType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowUsageType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the business activities, processes, and/or workflows that the record is technical assurance value is not valid for.",
                                    "type": "string",
                                    "title": "Workflow Usage",
                                    "example": "namespace:reference-data--WorkflowUsageType:SeismicInterpretation:"
                                },
                                "WorkflowPersona": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowPersonaType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowPersonaType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the role or personas that the record is technical assurance value is not valid for.",
                                    "type": "string",
                                    "title": "Workflow Persona",
                                    "example": "namespace:reference-data--WorkflowPersonaType:SeismicInterpreter:"
                                }
                            }
                        },
                        "example": [
                            {
                                "WorkflowUsage": "namespace:reference-data--WorkflowUsageType:SeismicInterpretation:",
                                "WorkflowPersona": "namespace:reference-data--WorkflowPersonaType:SeismicInterpreter:"
                            }
                        ]
                    },
                    "AcceptableUsage": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "List of workflows and/or personas that the technical assurance value is valid for (e.g., This data is trusted for Seismic Processing)",
                        "type": "array",
                        "title": "Acceptable Usage",
                        "items": {
                            "description": "Describes the workflows and/or personas that the technical assurance value is valid for (e.g., This data has a technical assurance property of \"trusted\" and it is suitable for Seismic Interpretation).",
                            "type": "object",
                            "title": "AcceptableUsage",
                            "properties": {
                                "WorkflowUsage": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowUsageType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowUsageType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the business activities, processes, and/or workflows that the record is technical assurance value is valid for.",
                                    "type": "string",
                                    "title": "Workflow Usage",
                                    "example": "namespace:reference-data--WorkflowUsageType:SeismicProcessing:"
                                },
                                "WorkflowPersona": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowPersonaType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowPersonaType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the role or personas that the record is technical assurance value is valid for.",
                                    "type": "string",
                                    "title": "Workflow Persona",
                                    "example": "namespace:reference-data--WorkflowPersonaType:SeismicProcessor:"
                                }
                            }
                        },
                        "example": [
                            {
                                "WorkflowUsage": "namespace:reference-data--WorkflowUsageType:SeismicProcessing:",
                                "WorkflowPersona": "namespace:reference-data--WorkflowPersonaType:SeismicProcessor:"
                            }
                        ]
                    },
                    "TechnicalAssuranceTypeID": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "TechnicalAssuranceType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TechnicalAssuranceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "string",
                        "title": "Technical Assurance Type ID",
                        "example": "namespace:reference-data--TechnicalAssuranceType:Trusted:"
                    },
                    "EffectiveDate": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "format": "date",
                        "description": "Date when the technical assurance determination for this record has taken place",
                        "type": "string",
                        "title": "Effective Date",
                        "example": "2020-02-13"
                    }
                },
                "x-osdu-governance-authorities": [
                    "OSDU"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractTechnicalAssurance.1.0.0.json"
            },
            "osdu:wks:AbstractGeoPlayContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoPlayContext:1.0.0",
                "description": "A single, typed Play entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoPlayContext",
                "type": "object",
                "properties": {
                    "PlayID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Play:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the play.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Play",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "PlayID",
                            "TargetPropertyName": "PlayTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-PlayType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The PlayType reference of the Play (via PlayID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "PlayType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoPlayContext.1.0.0.json"
            },
            "osdu:wks:AbstractFacilityVerticalMeasurement:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractFacilityVerticalMeasurement:1.0.0",
                "description": "A location along a wellbore, _usually_ associated with some aspect of the drilling of the wellbore, but not with any intersecting _subsurface_ natural surfaces.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractFacilityVerticalMeasurement",
                "type": "object",
                "properties": {
                    "WellboreTVDTrajectoryID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "WellboreTrajectory",
                                "GroupType": "work-product-component"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:work-product-component\\-\\-WellboreTrajectory:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies what directional survey or wellpath was used to calculate the TVD.",
                        "type": "string"
                    },
                    "VerticalCRSID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "CoordinateReferenceSystem",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "A vertical coordinate reference system defines the origin for height or depth values. It is expected that either VerticalCRSID or VerticalReferenceID reference is provided in a given vertical measurement array object, but not both.",
                        "type": "string"
                    },
                    "VerticalMeasurementSourceID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementSource",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementSource:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies Driller vs Logger.",
                        "type": "string"
                    },
                    "VerticalReferenceID": {
                        "description": "The reference point from which the relative vertical measurement is made. This is only populated if the measurement has no VerticalCRSID specified. The value entered must match the VerticalMeasurementID for another vertical measurement array element in Wellbore or Well or in a related parent facility. The relationship should be  declared explicitly in VerticalReferenceEntityID. Any chain of measurements must ultimately resolve to a Vertical CRS. It is expected that a VerticalCRSID or a VerticalReferenceID is provided in a given vertical measurement array object, but not both.",
                        "type": "string"
                    },
                    "TerminationDateTime": {
                        "format": "date-time",
                        "description": "The date and time at which a vertical measurement instance is no longer in effect.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "VerticalMeasurementPathID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementPath",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementPath:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies Measured Depth, True Vertical Depth, or Elevation.",
                        "type": "string"
                    },
                    "EffectiveDateTime": {
                        "format": "date-time",
                        "description": "The date and time at which a vertical measurement instance becomes effective.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "VerticalMeasurement": {
                        "description": "The value of the elevation or depth. Depth is positive downwards from a vertical reference or geodetic datum along a path, which can be vertical; elevation is positive upwards from a geodetic datum along a vertical path. Either can be negative.",
                        "x-osdu-frame-of-reference": "UOM_via_property:VerticalMeasurementUnitOfMeasureID",
                        "type": "number"
                    },
                    "VerticalMeasurementTypeID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies the type of vertical measurement (TD, Plugback, Kickoff, Drill Floor, Rotary Table...).",
                        "type": "string"
                    },
                    "VerticalMeasurementDescription": {
                        "description": "Text which describes a vertical measurement in detail.",
                        "type": "string"
                    },
                    "VerticalMeasurementUnitOfMeasureID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "UnitOfMeasure",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The unit of measure for the vertical measurement. If a unit of measure and a vertical CRS are provided, the unit of measure provided is taken over the unit of measure from the CRS.",
                        "type": "string"
                    },
                    "VerticalReferenceEntityID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Wellbore",
                                "GroupType": "master-data"
                            },
                            {
                                "EntityType": "Well",
                                "GroupType": "master-data"
                            },
                            {
                                "EntityType": "Rig",
                                "GroupType": "master-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:(master-data\\-\\-Wellbore|master-data\\-\\-Well|master-data\\-\\-Rig):[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "This relationship identifies the entity (aka record) in which the VerticalReferenceID is found; It could be a different OSDU entity or a self-reference. For example, a Wellbore VerticalMeasurement may reference a member of a VerticalMeasurements[] array in its parent Well record. Alternatively, VerticalReferenceEntityID may be populated with the ID of its own Wellbore record to make explicit that VerticalReferenceID is intended to be found in this record, not another.",
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractFacilityVerticalMeasurement.1.0.0.json"
            },
            "osdu:wks:AbstractGeoPoliticalContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoPoliticalContext:1.0.0",
                "description": "A single, typed geo-political entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoPoliticalContext",
                "type": "object",
                "properties": {
                    "GeoPoliticalEntityID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-GeoPoliticalEntity:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to GeoPoliticalEntity.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "GeoPoliticalEntity",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "GeoPoliticalEntityID",
                            "TargetPropertyName": "GeoPoliticalEntityTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-GeoPoliticalEntityType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The GeoPoliticalEntityType reference of the GeoPoliticalEntity (via GeoPoliticalEntityID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "GeoPoliticalEntityType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoPoliticalContext.1.0.0.json"
            },
            "osdu:wks:AbstractWPCGroupType:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractWPCGroupType:1.0.0",
                "description": "Generic reference object containing the universal group-type properties of a Work Product Component for inclusion in data type specific Work Product Component objects",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractWPCGroupType",
                "type": "object",
                "properties": {
                    "Datasets": {
                        "description": "The record id, which identifies this OSDU File or dataset resource.",
                        "type": "array",
                        "items": {
                            "x-osdu-relationship": [
                                {
                                    "GroupType": "dataset"
                                }
                            ],
                            "pattern": "^[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                            "type": "string"
                        }
                    },
                    "IsDiscoverable": {
                        "description": "A flag that indicates if the work product component is searchable, which means covered in the search index.",
                        "type": "boolean"
                    },
                    "TechnicalAssurances": {
                        "x-osdu-indexing": {
                            "type": "nested"
                        },
                        "description": "Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "array",
                        "title": "Technical Assurances",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractTechnicalAssurance:1.0.0"
                        }
                    },
                    "Artefacts": {
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "An array of Artefacts - each artefact has a Role, Resource tuple. An artefact is distinct from the file, in the sense certain valuable information is generated during loading process (Artefact generation process). Examples include retrieving location data, performing an OCR which may result in the generation of artefacts which need to be preserved distinctly",
                        "type": "array",
                        "items": {
                            "description": "An array of Artefacts - each artefact has a Role, Resource tuple. An artefact is distinct from the file, in the sense certain valuable information is generated during loading process (Artefact generation process). Examples include retrieving location data, performing an OCR which may result in the generation of artefacts which need to be preserved distinctly",
                            "type": "object",
                            "title": "Artefacts",
                            "properties": {
                                "ResourceID": {
                                    "x-osdu-relationship": [
                                        {
                                            "GroupType": "dataset"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
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
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractWPCGroupType.1.0.0.json"
            },
            "osdu:wks:AbstractAccessControlList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractAccessControlList:1.0.0",
                "description": "The access control tags associated with this entity. This structure is included by "
                               "the SystemProperties \"acl\", which is part of all OSDU records. Not extensible.",
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
            "osdu:wks:AbstractContact:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractContact:1.0.0",
                "description": "An object with properties that describe a specific person or other point-of-contact (like an email distribution list) that is relevant in this context (like a given data set or business project). The contact specified may be either internal or external to the organisation (something denoted via the Organisation object that is referenced). Note that some properties contain personally identifiable information, so it might not be appropriate to populate all properties in all scenarios.",
                "x-osdu-review-status": "Accepted",
                "title": "Abstract Contact",
                "type": "object",
                "properties": {
                    "RoleTypeID": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ContactRoleType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ContactRoleType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The identifier of a reference value for the role of the contact within the associated organisation, such as Account owner, Sales Representative, Technical Support, Project Manager, Party Chief, Client Representative, Senior Observer.",
                        "type": "string",
                        "title": "Role Type ID"
                    },
                    "OrganisationID": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Organisation",
                                "GroupType": "master-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the company the contact is associated with.",
                        "type": "string",
                        "title": "Organisation ID"
                    },
                    "Comment": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "description": "Additional information about the contact",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "type": "string",
                        "title": "Comment"
                    },
                    "PhoneNumber": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Contact phone number. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "type": "string",
                        "title": "Phone Number",
                        "example": "1-555-281-5555"
                    },
                    "EmailAddress": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Contact email address. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "type": "string",
                        "title": "Email Address",
                        "example": "support@company.com"
                    },
                    "Name": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "description": "Name of the individual contact. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "type": "string",
                        "title": "Name"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractContact.1.0.0.json"
            }
        },
        "properties": {
            "ancestry": {
                "description": "The links to data, which constitute the inputs, from which this record instance is derived.",
                "title": "Ancestry",
                "$ref": "#/definitions/osdu:wks:AbstractLegalParentList:1.0.0"
            },
            "data": {
                "allOf": [
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractCommonResources:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractWPCGroupType:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractWorkProductComponent:1.0.0"
                    },
                    {
                        "type": "object",
                        "title": "IndividualProperties",
                        "properties": {
                            "SurveyToolTypeID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "SurveyToolType",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-SurveyToolType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "The type of tool or equipment used to acquire this Directional Survey.  For example, gyroscopic, magnetic, MWD, TOTCO, acid bottle, etc. Follow OWSG reference data and support the ISCWSA survey tool definitions.",
                                "type": "string",
                                "title": "Type of the Survey Tool"
                            },
                            "CompanyID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "Organisation",
                                        "GroupType": "master-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "The relationship to company who engaged the service company (ServiceCompanyID) to perform the surveying.",
                                "type": "string",
                                "title": "Company ID"
                            },
                            "GeographicCRSID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CoordinateReferenceSystem",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "Coordinate Reference System defining the Geodetic Datum of the station LATITUDE and LONGITUDE values. If LATITUDE and LONGITUDE attributes are stored, clearly identifying their Datum is required.",
                                "type": "string",
                                "title": "Geographic Coordinate Reference System",
                                "example": "namespace:reference-data--CoordinateReferenceSystem:Geographic2D:EPSG::4326:"
                            },
                            "SurveyVersion": {
                                "description": "The version of the wellbore survey deliverable received from the service provider - as given by this provider",
                                "type": "string",
                                "title": "Survey Version"
                            },
                            "AvailableTrajectoryStationProperties": {
                                "x-osdu-indexing": {
                                    "type": "flattened"
                                },
                                "description": "The array of TrajectoryStationProperty definitions describing the available properties for this instance of WellboreTrajectory.",
                                "type": "array",
                                "title": "Available Trajectory Station Properties",
                                "items": {
                                    "description": "A set of properties describing a trajectory station property which is available for this instance of a WellboreTrajectory.",
                                    "type": "object",
                                    "title": "Curve",
                                    "properties": {
                                        "TrajectoryStationPropertyTypeID": {
                                            "x-osdu-relationship": [
                                                {
                                                    "EntityType": "TrajectoryStationPropertyType",
                                                    "GroupType": "reference-data"
                                                }
                                            ],
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TrajectoryStationPropertyType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "description": "The reference to a trajectory station property type - or if interpreted as channels, the curve or channel name type, identifying e.g. MD, Inclination, Azimuth. This is a relationship to a reference-data--TrajectoryStationPropertyType record id.",
                                            "type": "string",
                                            "title": "Trajectory Station Property Type ID",
                                            "example": "partition-id:reference-data--TrajectoryStationPropertyType:AzimuthTN:"
                                        },
                                        "StationPropertyUnitID": {
                                            "x-osdu-relationship": [
                                                {
                                                    "EntityType": "UnitOfMeasure",
                                                    "GroupType": "reference-data"
                                                }
                                            ],
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "description": "Unit of Measure for the station properties of type TrajectoryStationPropertyType.",
                                            "type": "string",
                                            "title": "Station Property Unit ID",
                                            "example": "partition-id:reference-data--UnitOfMeasure:dega:"
                                        },
                                        "Name": {
                                            "description": "The name of the curve (e.g. column in a CSV document) as originally found. If absent The name of the TrajectoryStationPropertyType is intended to be used.",
                                            "type": "string",
                                            "title": "Name",
                                            "example": "AzimuthTN"
                                        }
                                    }
                                }
                            },
                            "WellboreID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "Wellbore",
                                        "GroupType": "master-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Wellbore:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "A unique name, code or number designated to the Wellbore.",
                                "type": "string",
                                "title": "Wellbore"
                            },
                            "ServiceCompanyID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "Organisation",
                                        "GroupType": "master-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "Name of the Survey Company.",
                                "type": "string",
                                "title": "Service Company"
                            },
                            "ProjectedCRSID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CoordinateReferenceSystem",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "Coordinate Reference System defining the Projection of the station EASTING and NORTHING values. If  type is \"Grid North\" and EASTING and NORTHING attributes are stored, clearly identifying their projection is required.",
                                "type": "string",
                                "title": "Projected Coordinate Reference System ID",
                                "example": "namespace:reference-data--CoordinateReferenceSystem:Projected:EPSG::32615:"
                            },
                            "SurveyReferenceIdentifier": {
                                "description": "Unique or Distinctive Survey Reference Number, Job Number, File Number, Identifier, Label, Name, etc. as indicated on a directional survey report, file, etc.  Use this attribute to allow correlation of the data in this Directional Survey back to the original source document, file, etc.",
                                "type": "string",
                                "title": "Survey Reference Identifier"
                            },
                            "SurveyType": {
                                "description": "The type of this directional survey.  For example a \"Directional Survey\" where MD, Inclination and Azimuth are all measured or a \"Position Log\" where Inclination and Azimuth are both null and only MD, TVD and X/Y Offsets are available) - or \"Full Survey\" where everything is fully filled-up, depth-inclination-azimuth.",
                                "type": "string",
                                "title": "Directional Survey Type"
                            },
                            "TopDepthMeasuredDepth": {
                                "description": "Measured depth in wellbore where the directional survey starts. This should equal the minimum station measured depth for this directional survey, regardless of whether the surveyed station represents an actual surveyed MD or not.",
                                "x-osdu-frame-of-reference": "UOM:length",
                                "type": "number",
                                "title": "Survey Top Measured Depth"
                            },
                            "AppliedOperations": {
                                "description": "The audit trail of operations applied to the station coordinates from the original state to the current state. The list may contain operations applied prior to ingestion as well as the operations applied to produce the Wgs84Coordinates. The text elements refer to ESRI style CRS and Transformation names, which may have to be translated to EPSG standard names.",
                                "type": "array",
                                "title": "Applied Operations",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "ActiveIndicator": {
                                "description": "A flag indicating if the survey is currently active or valid within his lifecycle stage, not necessarily the definitive survey.",
                                "type": "boolean",
                                "title": "Active Survey Indicator"
                            },
                            "AzimuthReferenceType": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "AzimuthReferenceType",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-AzimuthReferenceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "The North reference of the trajectory used to define the azimuth angular measurement values. For example, True North, Grid North, Magnetic North.",
                                "type": "string",
                                "title": "Azimuth Reference Type"
                            },
                            "AcquisitionDate": {
                                "format": "date-time",
                                "description": "The date that the survey data was acquired on the field.",
                                "type": "string",
                                "title": "Effective Date"
                            },
                            "TieMeasuredDepth": {
                                "description": "Tie-point depth measured along the wellbore from the measurement reference datum to the survey station - where tie point is the place on the originating survey where the current survey intersect it.",
                                "x-osdu-frame-of-reference": "UOM:length",
                                "type": "number",
                                "title": "Tie Measured Depth"
                            },
                            "ExtrapolatedMeasuredDepth": {
                                "description": "The measured depth to which the survey segment was extrapolated.",
                                "x-osdu-frame-of-reference": "UOM:length",
                                "type": "number",
                                "title": "Extrapolated Measured Depth"
                            },
                            "VerticalMeasurement": {
                                "description": "References an entry in the Vertical Measurement array for the Wellbore identified by WellboreID, which defines the vertical reference datum for all survey station measured depths.",
                                "$ref": "#/definitions/osdu:wks:AbstractFacilityVerticalMeasurement:1.0.0"
                            },
                            "BaseDepthMeasuredDepth": {
                                "description": "Measured depth within the wellbore of the LAST surveyed station with recorded data.  If a stored survey has been extrapolated to a deeper depth than the last surveyed station then that is the extrapolated measured depth and not the survey base depth.",
                                "x-osdu-frame-of-reference": "UOM:length",
                                "type": "number",
                                "title": "Survey Base Measured Depth"
                            },
                            "CalculationMethodType": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CalculationMethodType",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CalculationMethodType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "Calculation Method Type used to compute the TVD, X OFFSET, Y OFFSET and DOG LEG SEVERITY values for this Directional Survey. For example, Radius of Curvature, Minimum Curvature, Balanced Tangential, etc.",
                                "type": "string",
                                "title": "Calculation Method Type"
                            },
                            "AcquisitionRemark": {
                                "description": "Remarks related to acquisition context which is not the same as Description which is a summary of the work-product-component.",
                                "type": "string",
                                "title": "Survey Remark"
                            }
                        },
                        "required": [
                            "WellboreID",
                            "TopDepthMeasuredDepth",
                            "BaseDepthMeasuredDepth",
                            "VerticalMeasurement"
                        ]
                    },
                    {
                        "type": "object",
                        "title": "ExtensionProperties",
                        "properties": {
                            "ExtensionProperties": {
                                "type": "object"
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
                "example": "osdu:wks:work-product-component--WellboreTrajectory:1.1.0"
            },
            "acl": {
                "description": "The access control tags associated with this entity.",
                "title": "Access Control List",
                "$ref": "#/definitions/osdu:wks:AbstractAccessControlList:1.0.0"
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
                    "$ref": "#/definitions/osdu:wks:AbstractMetaItem:1.0.0"
                }
            },
            "legal": {
                "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                "title": "Legal Tags",
                "$ref": "#/definitions/osdu:wks:AbstractLegalTags:1.0.0"
            },
            "createUser": {
                "description": "The user reference, which created the first version of this resource object. Set by the System.",
                "title": "Resource Object Creation User Reference",
                "type": "string",
                "example": "some-user@some-company-cloud.com"
            },
            "id": {
                "pattern": "^[\\w\\-\\.]+:work-product-component\\-\\-WellboreTrajectory:[\\w\\-\\.\\:\\%]+$",
                "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                "title": "Entity ID",
                "type": "string",
                "example": "namespace:work-product-component--WellboreTrajectory:606f224a-ef1f-5690-9843-d26cd7e33e10"
            }
        },
        "$id": "https://schema.osdu.opengroup.org/json/work-product-component/WellboreTrajectory.1.1.0.json"
    }


def get_schema_template_well_log():
    return {
        "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
        "$id": "https://schema.osdu.opengroup.org/json/work-product-component/WellLog.1.2.0.json",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "x-osdu-schema-source": "osdu:wks:work-product-component--WellLog:1.2.0",
        "title": "WellLog",
        "description": "A well log is a data type that correlates a particular measurement or multiple measurements in a wellbore against depth and/or time within that wellbore. When plotted visually, well logs are typically long line graphs (called \"curves\") but may sometimes be discrete points or intervals. This schema object is intended for digital well logs, not raster log files or raster calibration files, but may be used for the latter in the absence of a defined OSDU schema for these use cases.",
        "type": "object",
        "definitions": {
            "osdu:wks:AbstractWorkProductComponent:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractWorkProductComponent:1.0.0",
                "description": "Generic reference object containing the universal properties of a Work Product "
                               "Component for inclusion in data type specific Work Product Component objects",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractWorkProductComponent",
                "type": "object",
                "properties": {
                    "SpatialArea": {
                        "description": "A polygon boundary that reflects the locale of the content of the work product component (location of the subject matter).",
                        "$ref": "#/definitions/osdu:wks:AbstractSpatialLocation:1.0.0"
                    },
                    "Description": {
                        "description": "Description.  Summary of the work product component.  Not the same as Remark which captures thoughts of creator about the wpc.",
                        "type": "string"
                    },
                    "CreationDateTime": {
                        "format": "date-time",
                        "description": "Date that a resource (work  product component here) is formed outside of OSDU before loading (e.g. publication date).",
                        "type": "string"
                    },
                    "BusinessActivities": {
                        "description": "Array of business processes/workflows that the work product component has been through (ex. well planning, exploration).",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "SpatialPoint": {
                        "description": "A centroid point that reflects the locale of the content of the work product component (location of the subject matter).",
                        "$ref": "#/definitions/osdu:wks:AbstractSpatialLocation:1.0.0"
                    },
                    "GeoContexts": {
                        "x-osdu-indexing": {
                            "type": "nested"
                        },
                        "description": "List of geographic entities which provide context to the WPC.  This may include multiple types or multiple values of the same type.",
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractGeoContext:1.0.0"
                        }
                    },
                    "AuthorIDs": {
                        "description": "Array of Authors' names of the work product component.  Could be a person or company entity.",
                        "type": "array",
                        "title": "Author IDs",
                        "items": {
                            "type": "string"
                        }
                    },
                    "SubmitterName": {
                        "description": "Name of the person that first submitted the work product component to OSDU.",
                        "type": "string"
                    },
                    "LineageAssertions": {
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "Defines relationships with other objects (any kind of Resource) upon which this work product component depends.  The assertion is directed only from the asserting WPC to ancestor objects, not children.  It should not be used to refer to files or artefacts within the WPC -- the association within the WPC is sufficient and Artefacts are actually children of the main WPC file. They should be recorded in the data.Artefacts[] array.",
                        "type": "array",
                        "items": {
                            "description": "Defines relationships with other objects (any kind of Resource) upon which this work product component depends.  The assertion is directed only from the asserting WPC to ancestor objects, not children.  It should not be used to refer to files or artefacts within the WPC -- the association within the WPC is sufficient and Artefacts are actually children of the main WPC file. They should be recorded in the data.Artefacts[] array.",
                            "type": "object",
                            "title": "LineageAssertion",
                            "properties": {
                                "ID": {
                                    "x-osdu-relationship": [],
                                    "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
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
                                    "description": "Used by LineageAssertion to describe the nature of the line of descent of a work product component from a prior Resource, such as DIRECT, INDIRECT, REFERENCE.  It is not for proximity (number of nodes away), it is not to cover all the relationships in a full ontology or graph, and it is not to describe the type of activity that created the asserting WPC.  LineageAssertion does not encompass a full provenance, process history, or activity model.",
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
                    },
                    "Name": {
                        "description": "Name",
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractWorkProductComponent.1.0.0.json"
            },
            "osdu:wks:AbstractCommonResources:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractCommonResources:1.0.0",
                "description": "Common resources to be injected at root 'data' level for every entity, which is persistable in Storage. The insertion is performed by the OsduSchemaComposer script.",
                "x-osdu-review-status": "Accepted",
                "title": "OSDU Common Resources",
                "type": "object",
                "properties": {
                    "ResourceHomeRegionID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "OSDURegion",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-OSDURegion:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The name of the home [cloud environment] region for this OSDU resource object.",
                        "type": "string",
                        "title": "Resource Home Region ID"
                    },
                    "ResourceHostRegionIDs": {
                        "description": "The name of the host [cloud environment] region(s) for this OSDU resource object.",
                        "type": "array",
                        "title": "Resource Host Region ID",
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
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceLifecycleStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceLifecycleStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Resource Lifecycle status.",
                        "type": "string",
                        "title": "Resource Lifecycle Status"
                    },
                    "ResourceSecurityClassification": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceSecurityClassification",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceSecurityClassification:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Classifies the security level of the resource.",
                        "type": "string",
                        "title": "Resource Security Classification"
                    },
                    "ResourceCurationStatus": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceCurationStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceCurationStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Curation status.",
                        "type": "string",
                        "title": "Resource Curation Status"
                    },
                    "ExistenceKind": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ExistenceKind",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ExistenceKind:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Where does this data resource sit in the cradle-to-grave span of its existence?",
                        "type": "string",
                        "title": "Existence Kind"
                    },
                    "TechnicalAssuranceID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "TechnicalAssuranceType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TechnicalAssuranceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "DEPRECATED: Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "string",
                        "title": "Technical Assurance ID"
                    },
                    "Source": {
                        "description": "The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed.",
                        "type": "string",
                        "title": "Data Source"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractCommonResources.1.0.0.json"
            },
            "osdu:wks:AbstractMetaItem:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "oneOf": [
                    {
                        "title": "FrameOfReferenceUOM",
                        "type": "object",
                        "properties": {
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the Unit.",
                                "title": "UOM Persistable Reference",
                                "type": "string",
                                "example": "{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}"
                            },
                            "kind": {
                                "const": "Unit",
                                "description": "The kind of reference, 'Unit' for FrameOfReferenceUOM.",
                                "title": "UOM Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides Unit context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "UOM Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "HorizontalDeflection.EastWest",
                                    "HorizontalDeflection.NorthSouth"
                                ]
                            },
                            "name": {
                                "description": "The unit symbol or name of the unit.",
                                "title": "UOM Unit Symbol",
                                "type": "string",
                                "example": "ft[US]"
                            },
                            "unitOfMeasureID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "UnitOfMeasure",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to unit of measure reference.",
                                "type": "string",
                                "example": "namespace:reference-data--UnitOfMeasure:ftUS:"
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
                            "coordinateReferenceSystemID": {
                                "x-osdu-relationship": [
                                    {
                                        "EntityType": "CoordinateReferenceSystem",
                                        "GroupType": "reference-data"
                                    }
                                ],
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "description": "SRN to CRS reference.",
                                "type": "string",
                                "example": "namespace:reference-data--CoordinateReferenceSystem:Projected:EPSG::32615:"
                            },
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying the CRS.",
                                "title": "CRS Persistable Reference",
                                "type": "string",
                                "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32615\"},\"name\":\"WGS_1984_UTM_Zone_15N\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"PROJCS[\\\"WGS_1984_UTM_Zone_15N\\\",GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Transverse_Mercator\\\"],PARAMETER[\\\"False_Easting\\\",500000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-93.0],PARAMETER[\\\"Scale_Factor\\\",0.9996],PARAMETER[\\\"Latitude_Of_Origin\\\",0.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",32615]]\"}"
                            },
                            "kind": {
                                "const": "CRS",
                                "description": "The kind of reference, constant 'CRS' for FrameOfReferenceCRS.",
                                "title": "CRS Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides CRS context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "CRS Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "KickOffPosition.X",
                                    "KickOffPosition.Y"
                                ]
                            },
                            "name": {
                                "description": "The name of the CRS.",
                                "title": "CRS Name",
                                "type": "string",
                                "example": "WGS 84 / UTM zone 15N"
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
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying DateTime reference.",
                                "title": "DateTime Persistable Reference",
                                "type": "string",
                                "example": "{\"format\":\"yyyy-MM-ddTHH:mm:ssZ\",\"timeZone\":\"UTC\",\"type\":\"DTM\"}"
                            },
                            "kind": {
                                "const": "DateTime",
                                "description": "The kind of reference, constant 'DateTime', for FrameOfReferenceDateTime.",
                                "title": "DateTime Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides DateTime context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "DateTime Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Acquisition.StartTime",
                                    "Acquisition.EndTime"
                                ]
                            },
                            "name": {
                                "description": "The name of the DateTime format and reference.",
                                "title": "DateTime Name",
                                "type": "string",
                                "example": "UTC"
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
                            "persistableReference": {
                                "description": "The self-contained, persistable reference string uniquely identifying AzimuthReference.",
                                "title": "AzimuthReference Persistable Reference",
                                "type": "string",
                                "example": "{\"code\":\"TrueNorth\",\"type\":\"AZR\"}"
                            },
                            "kind": {
                                "const": "AzimuthReference",
                                "description": "The kind of reference, constant 'AzimuthReference', for FrameOfReferenceAzimuthReference.",
                                "title": "AzimuthReference Reference Kind",
                                "type": "string"
                            },
                            "propertyNames": {
                                "description": "The list of property names, to which this meta data item provides AzimuthReference context to. A full path like \"StructureA.PropertyB\" is required to define a unique context; \"data\" is omitted since frame-of reference normalization only applies to the data block.",
                                "title": "AzimuthReference Property Names",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "example": [
                                    "Bearing"
                                ]
                            },
                            "name": {
                                "description": "The name of the CRS or the symbol/name of the unit.",
                                "title": "AzimuthReference Name",
                                "type": "string",
                                "example": "TrueNorth"
                            }
                        },
                        "required": [
                            "kind",
                            "persistableReference"
                        ]
                    }
                ],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractMetaItem:1.0.0",
                "description": "A meta data item, which allows the association of named properties or property values to a Unit/Measurement/CRS/Azimuth/Time context.",
                "title": "Frame of Reference Meta Data Item",
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractMetaItem.1.0.0.json"
            },
            "osdu:wks:AbstractLegalParentList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractLegalParentList:1.0.0",
                "description": "A list of entity id:version references to record instances recorded in the data "
                               "platform, from which the current record is derived and from which the legal tags must "
                               "be derived. This structure is included by the SystemProperties \"ancestry\", "
                               "which is part of all OSDU records. Not extensible.",
                "additionalProperties": 'false',
                "title": "Parent List",
                "type": "object",
                "properties": {
                    "parents": {
                        "description": "An array of none, one or many entity references of 'direct parents' in the data platform, which mark the current record as a derivative. In contrast to other relationships, the source record version is required. During record creation or update the ancestry.parents[] relationships are used to collect the legal tags from the sources and aggregate them in the legal.legaltags[] array. As a consequence, should e.g., one or more of the legal tags of the source data expire, the access to the derivatives is also terminated. For details, see ComplianceService tutorial, 'Creating derivative Records'.",
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
            },
            "osdu:wks:AbstractGeoContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "oneOf": [
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoPoliticalContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoBasinContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoFieldContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoPlayContext:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractGeoProspectContext:1.0.0"
                    }
                ],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoContext:1.0.0",
                "description": "A geographic context to an entity. It can be either a reference to a GeoPoliticalEntity, Basin, Field, Play or Prospect.",
                "title": "AbstractGeoContext",
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoContext.1.0.0.json"
            },
            "osdu:wks:AbstractFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
            "osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
                        "example": "namespace:reference-data--CoordinateReferenceSystem:BoundProjected:EPSG::32021_EPSG::15851:"
                    },
                    "persistableReferenceCrs": {
                        "description": "The CRS reference as persistableReference string. If populated, the CoordinateReferenceSystemID takes precedence.",
                        "type": "string",
                        "title": "CRS Reference",
                        "example": "{\"authCode\":{\"auth\":\"OSDU\",\"code\":\"32021079\"},\"lateBoundCRS\":{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"32021\"},\"name\":\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"PROJCS[\\\"NAD_1927_StatePlane_North_Dakota_South_FIPS_3302\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",2000000.0],PARAMETER[\\\"False_Northing\\\",0.0],PARAMETER[\\\"Central_Meridian\\\",-100.5],PARAMETER[\\\"Standard_Parallel_1\\\",46.18333333333333],PARAMETER[\\\"Standard_Parallel_2\\\",47.48333333333333],PARAMETER[\\\"Latitude_Of_Origin\\\",45.66666666666666],UNIT[\\\"Foot_US\\\",0.3048006096012192],AUTHORITY[\\\"EPSG\\\",32021]]\"},\"name\":\"NAD27 * OGP-Usa Conus / North Dakota CS27 South zone [32021,15851]\",\"singleCT\":{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"15851\"},\"name\":\"NAD_1927_To_WGS_1984_79_CONUS\",\"type\":\"ST\",\"ver\":\"PE_10_9_1\",\"wkt\":\"GEOGTRAN[\\\"NAD_1927_To_WGS_1984_79_CONUS\\\",GEOGCS[\\\"GCS_North_American_1927\\\",DATUM[\\\"D_North_American_1927\\\",SPHEROID[\\\"Clarke_1866\\\",6378206.4,294.9786982]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],GEOGCS[\\\"GCS_WGS_1984\\\",DATUM[\\\"D_WGS_1984\\\",SPHEROID[\\\"WGS_1984\\\",6378137.0,298.257223563]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],METHOD[\\\"NADCON\\\"],PARAMETER[\\\"Dataset_conus\\\",0.0],OPERATIONACCURACY[5.0],AUTHORITY[\\\"EPSG\\\",15851]]\"},\"type\":\"EBC\",\"ver\":\"PE_10_9_1\"}"
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
                        "example": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"5714\"},\"name\":\"MSL_Height\",\"type\":\"LBC\",\"ver\":\"PE_10_9_1\",\"wkt\":\"VERTCS[\\\"MSL_Height\\\",VDATUM[\\\"Mean_Sea_Level\\\"],PARAMETER[\\\"Vertical_Shift\\\",0.0],PARAMETER[\\\"Direction\\\",1.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",5714]]\"}"
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
                        "example": "namespace:reference-data--CoordinateReferenceSystem:Vertical:EPSG::5714:"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractAnyCrsFeatureCollection.1.0.0.json"
            },
            "osdu:wks:AbstractGeoFieldContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoFieldContext:1.0.0",
                "description": "A single, typed field entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "title": "AbstractGeoFieldContext",
                "type": "object",
                "properties": {
                    "FieldID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Field:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to Field.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Field",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "const": "Field",
                        "type": "string",
                        "description": "The fixed type 'Field' for this AbstractGeoFieldContext."
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoFieldContext.1.0.0.json"
            },
            "osdu:wks:AbstractGeoProspectContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoProspectContext:1.0.0",
                "description": "A single, typed Prospect entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoProspectContext",
                "type": "object",
                "properties": {
                    "ProspectID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Prospect:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the prospect.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Prospect",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "ProspectID",
                            "TargetPropertyName": "ProspectTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ProspectType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The ProspectType reference of the Prospect (via ProspectID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ProspectType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoProspectContext.1.0.0.json"
            },
            "osdu:wks:AbstractGeoBasinContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoBasinContext:1.0.0",
                "description": "A single, typed basin entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoBasinContext",
                "type": "object",
                "properties": {
                    "BasinID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Basin:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to Basin.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Basin",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "BasinID",
                            "TargetPropertyName": "BasinTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-BasinType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The BasinType reference of the Basin (via BasinID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "BasinType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoBasinContext.1.0.0.json"
            },
            "osdu:wks:AbstractSpatialLocation:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractSpatialLocation:1.0.0",
                "description": "A geographic object which can be described by a set of points.",
                "title": "AbstractSpatialLocation",
                "type": "object",
                "properties": {
                    "AsIngestedCoordinates": {
                        "description": "The original or 'as ingested' coordinates (Point, MultiPoint, LineString, MultiLineString, Polygon or MultiPolygon). The name 'AsIngestedCoordinates' was chosen to contrast it to 'OriginalCoordinates', which carries the uncertainty whether any coordinate operations took place before ingestion. In cases where the original CRS is different from the as-ingested CRS, the AppliedOperations can also contain the list of operations applied to the coordinate prior to ingestion. The data structure is similar to GeoJSON FeatureCollection, however in a CRS context explicitly defined within the AbstractAnyCrsFeatureCollection. The coordinate sequence follows GeoJSON standard, i.e. 'eastward/longitude', 'northward/latitude' {, 'upward/height' unless overridden by an explicit direction in the AsIngestedCoordinates.VerticalCoordinateReferenceSystemID}.",
                        "x-osdu-frame-of-reference": "CRS:",
                        "title": "As Ingested Coordinates",
                        "$ref": "#/definitions/osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0"
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
                        "$ref": "#/definitions/osdu:wks:AbstractFeatureCollection:1.0.0"
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
            "osdu:wks:AbstractLegalTags:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
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
            "osdu:wks:AbstractTechnicalAssurance:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractTechnicalAssurance:1.0.0",
                "description": "Describes a record's overall suitability for general business consumption based on level of trust.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractTechnicalAssurance",
                "type": "object",
                "required": [
                    "TechnicalAssuranceTypeID"
                ],
                "properties": {
                    "Comment": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Any additional context to support the determination of technical assurance",
                        "type": "string",
                        "title": "Comment",
                        "example": "This is free form text from reviewer, e.g. restrictions on use"
                    },
                    "Reviewers": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "The individuals, or roles, that reviewed and determined the technical assurance value",
                        "type": "array",
                        "title": "Reviewers",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractContact:1.0.0"
                        },
                        "example": [
                            {
                                "RoleTypeID": "namespace:reference-data--ContactRoleType:AccountOwner:",
                                "OrganisationID": "namespace:master-data--Organisation:SomeUniqueOrganisationID:",
                                "Name": "Example Name"
                            }
                        ]
                    },
                    "UnacceptableUsage": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "List of workflows and/or personas that the technical assurance value is not valid for (e.g., This data is not trusted for seismic interpretation)",
                        "type": "array",
                        "title": "Unacceptable Usage",
                        "items": {
                            "description": "Describes the workflows and/or personas that the technical assurance value is not valid for (e.g., This data has a technical assurance property of \"trusted\", but it is not suitable for Seismic Interpretation).",
                            "type": "object",
                            "title": "UnacceptableUsage",
                            "properties": {
                                "WorkflowUsage": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowUsageType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowUsageType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the business activities, processes, and/or workflows that the record is technical assurance value is not valid for.",
                                    "type": "string",
                                    "title": "Workflow Usage",
                                    "example": "namespace:reference-data--WorkflowUsageType:SeismicInterpretation:"
                                },
                                "WorkflowPersona": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowPersonaType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowPersonaType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the role or personas that the record is technical assurance value is not valid for.",
                                    "type": "string",
                                    "title": "Workflow Persona",
                                    "example": "namespace:reference-data--WorkflowPersonaType:SeismicInterpreter:"
                                }
                            }
                        },
                        "example": [
                            {
                                "WorkflowUsage": "namespace:reference-data--WorkflowUsageType:SeismicInterpretation:",
                                "WorkflowPersona": "namespace:reference-data--WorkflowPersonaType:SeismicInterpreter:"
                            }
                        ]
                    },
                    "AcceptableUsage": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "List of workflows and/or personas that the technical assurance value is valid for (e.g., This data is trusted for Seismic Processing)",
                        "type": "array",
                        "title": "Acceptable Usage",
                        "items": {
                            "description": "Describes the workflows and/or personas that the technical assurance value is valid for (e.g., This data has a technical assurance property of \"trusted\" and it is suitable for Seismic Interpretation).",
                            "type": "object",
                            "title": "AcceptableUsage",
                            "properties": {
                                "WorkflowUsage": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowUsageType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowUsageType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the business activities, processes, and/or workflows that the record is technical assurance value is valid for.",
                                    "type": "string",
                                    "title": "Workflow Usage",
                                    "example": "namespace:reference-data--WorkflowUsageType:SeismicProcessing:"
                                },
                                "WorkflowPersona": {
                                    "x-osdu-attribution-publication": "OSDU Data Platform",
                                    "x-osdu-attribution-revision": "1.0.0",
                                    "x-osdu-attribution-authority": "The Open Group",
                                    "x-osdu-relationship": [
                                        {
                                            "EntityType": "WorkflowPersonaType",
                                            "GroupType": "reference-data"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WorkflowPersonaType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "Name of the role or personas that the record is technical assurance value is valid for.",
                                    "type": "string",
                                    "title": "Workflow Persona",
                                    "example": "namespace:reference-data--WorkflowPersonaType:SeismicProcessor:"
                                }
                            }
                        },
                        "example": [
                            {
                                "WorkflowUsage": "namespace:reference-data--WorkflowUsageType:SeismicProcessing:",
                                "WorkflowPersona": "namespace:reference-data--WorkflowPersonaType:SeismicProcessor:"
                            }
                        ]
                    },
                    "TechnicalAssuranceTypeID": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "TechnicalAssuranceType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TechnicalAssuranceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "string",
                        "title": "Technical Assurance Type ID",
                        "example": "namespace:reference-data--TechnicalAssuranceType:Trusted:"
                    },
                    "EffectiveDate": {
                        "x-osdu-attribution-publication": "OSDU Data Platform",
                        "x-osdu-attribution-revision": "1.0.0",
                        "x-osdu-attribution-authority": "The Open Group",
                        "format": "date",
                        "description": "Date when the technical assurance determination for this record has taken place",
                        "type": "string",
                        "title": "Effective Date",
                        "example": "2020-02-13"
                    }
                },
                "x-osdu-governance-authorities": [
                    "OSDU"
                ],
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractTechnicalAssurance.1.0.0.json"
            },
            "osdu:wks:AbstractGeoPlayContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoPlayContext:1.0.0",
                "description": "A single, typed Play entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoPlayContext",
                "type": "object",
                "properties": {
                    "PlayID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Play:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the play.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Play",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "PlayID",
                            "TargetPropertyName": "PlayTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-PlayType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The PlayType reference of the Play (via PlayID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "PlayType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoPlayContext.1.0.0.json"
            },
            "osdu:wks:AbstractFacilityVerticalMeasurement:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractFacilityVerticalMeasurement:1.0.0",
                "description": "A location along a wellbore, _usually_ associated with some aspect of the drilling of the wellbore, but not with any intersecting _subsurface_ natural surfaces.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractFacilityVerticalMeasurement",
                "type": "object",
                "properties": {
                    "WellboreTVDTrajectoryID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "WellboreTrajectory",
                                "GroupType": "work-product-component"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:work-product-component\\-\\-WellboreTrajectory:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies what directional survey or wellpath was used to calculate the TVD.",
                        "type": "string"
                    },
                    "VerticalCRSID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "CoordinateReferenceSystem",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CoordinateReferenceSystem:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "A vertical coordinate reference system defines the origin for height or depth values. It is expected that either VerticalCRSID or VerticalReferenceID reference is provided in a given vertical measurement array object, but not both.",
                        "type": "string"
                    },
                    "VerticalMeasurementSourceID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementSource",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementSource:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies Driller vs Logger.",
                        "type": "string"
                    },
                    "VerticalReferenceID": {
                        "description": "The reference point from which the relative vertical measurement is made. This is only populated if the measurement has no VerticalCRSID specified. The value entered must match the VerticalMeasurementID for another vertical measurement array element in Wellbore or Well or in a related parent facility. The relationship should be  declared explicitly in VerticalReferenceEntityID. Any chain of measurements must ultimately resolve to a Vertical CRS. It is expected that a VerticalCRSID or a VerticalReferenceID is provided in a given vertical measurement array object, but not both.",
                        "type": "string"
                    },
                    "TerminationDateTime": {
                        "format": "date-time",
                        "description": "The date and time at which a vertical measurement instance is no longer in effect.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "VerticalMeasurementPathID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementPath",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementPath:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies Measured Depth, True Vertical Depth, or Elevation.",
                        "type": "string"
                    },
                    "EffectiveDateTime": {
                        "format": "date-time",
                        "description": "The date and time at which a vertical measurement instance becomes effective.",
                        "x-osdu-frame-of-reference": "DateTime",
                        "type": "string"
                    },
                    "VerticalMeasurement": {
                        "description": "The value of the elevation or depth. Depth is positive downwards from a vertical reference or geodetic datum along a path, which can be vertical; elevation is positive upwards from a geodetic datum along a vertical path. Either can be negative.",
                        "x-osdu-frame-of-reference": "UOM_via_property:VerticalMeasurementUnitOfMeasureID",
                        "type": "number"
                    },
                    "VerticalMeasurementTypeID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "VerticalMeasurementType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-VerticalMeasurementType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Specifies the type of vertical measurement (TD, Plugback, Kickoff, Drill Floor, Rotary Table...).",
                        "type": "string"
                    },
                    "VerticalMeasurementDescription": {
                        "description": "Text which describes a vertical measurement in detail.",
                        "type": "string"
                    },
                    "VerticalMeasurementUnitOfMeasureID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "UnitOfMeasure",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The unit of measure for the vertical measurement. If a unit of measure and a vertical CRS are provided, the unit of measure provided is taken over the unit of measure from the CRS.",
                        "type": "string"
                    },
                    "VerticalReferenceEntityID": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Wellbore",
                                "GroupType": "master-data"
                            },
                            {
                                "EntityType": "Well",
                                "GroupType": "master-data"
                            },
                            {
                                "EntityType": "Rig",
                                "GroupType": "master-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:(master-data\\-\\-Wellbore|master-data\\-\\-Well|master-data\\-\\-Rig):[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "This relationship identifies the entity (aka record) in which the VerticalReferenceID is found; It could be a different OSDU entity or a self-reference. For example, a Wellbore VerticalMeasurement may reference a member of a VerticalMeasurements[] array in its parent Well record. Alternatively, VerticalReferenceEntityID may be populated with the ID of its own Wellbore record to make explicit that VerticalReferenceID is intended to be found in this record, not another.",
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractFacilityVerticalMeasurement.1.0.0.json"
            },
            "osdu:wks:AbstractGeoPoliticalContext:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractGeoPoliticalContext:1.0.0",
                "description": "A single, typed geo-political entity reference, which is 'abstracted' to AbstractGeoContext and then aggregated by GeoContexts properties.",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractGeoPoliticalContext",
                "type": "object",
                "properties": {
                    "GeoPoliticalEntityID": {
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-GeoPoliticalEntity:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to GeoPoliticalEntity.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "GeoPoliticalEntity",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string"
                    },
                    "GeoTypeID": {
                        "x-osdu-is-derived": {
                            "RelationshipPropertyName": "GeoPoliticalEntityID",
                            "TargetPropertyName": "GeoPoliticalEntityTypeID"
                        },
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-GeoPoliticalEntityType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The GeoPoliticalEntityType reference of the GeoPoliticalEntity (via GeoPoliticalEntityID) for application convenience.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "GeoPoliticalEntityType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractGeoPoliticalContext.1.0.0.json"
            },
            "osdu:wks:AbstractWPCGroupType:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractWPCGroupType:1.0.0",
                "description": "Generic reference object containing the universal group-type properties of a Work Product Component for inclusion in data type specific Work Product Component objects",
                "x-osdu-review-status": "Accepted",
                "title": "AbstractWPCGroupType",
                "type": "object",
                "properties": {
                    "Datasets": {
                        "description": "The record id, which identifies this OSDU File or dataset resource.",
                        "type": "array",
                        "items": {
                            "x-osdu-relationship": [
                                {
                                    "GroupType": "dataset"
                                }
                            ],
                            "pattern": "^[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                            "type": "string"
                        }
                    },
                    "IsDiscoverable": {
                        "description": "A flag that indicates if the work product component is searchable, which means covered in the search index.",
                        "type": "boolean"
                    },
                    "TechnicalAssurances": {
                        "x-osdu-indexing": {
                            "type": "nested"
                        },
                        "description": "Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "type": "array",
                        "title": "Technical Assurances",
                        "items": {
                            "$ref": "#/definitions/osdu:wks:AbstractTechnicalAssurance:1.0.0"
                        }
                    },
                    "Artefacts": {
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "description": "An array of Artefacts - each artefact has a Role, Resource tuple. An artefact is distinct from the file, in the sense certain valuable information is generated during loading process (Artefact generation process). Examples include retrieving location data, performing an OCR which may result in the generation of artefacts which need to be preserved distinctly",
                        "type": "array",
                        "items": {
                            "description": "An array of Artefacts - each artefact has a Role, Resource tuple. An artefact is distinct from the file, in the sense certain valuable information is generated during loading process (Artefact generation process). Examples include retrieving location data, performing an OCR which may result in the generation of artefacts which need to be preserved distinctly",
                            "type": "object",
                            "title": "Artefacts",
                            "properties": {
                                "ResourceID": {
                                    "x-osdu-relationship": [
                                        {
                                            "GroupType": "dataset"
                                        }
                                    ],
                                    "pattern": "^[\\w\\-\\.]+:dataset\\-\\-[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
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
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractWPCGroupType.1.0.0.json"
            },
            "osdu:wks:AbstractAccessControlList:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 ("
                                  "the \"License\"); you may not use this file except in compliance with the License. "
                                  "You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 "
                                  ". Unless required by applicable law or agreed to in writing, software distributed "
                                  "under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR "
                                  "CONDITIONS OF ANY KIND, either express or implied. See the License for the "
                                  "specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractAccessControlList:1.0.0",
                "description": "The access control tags associated with this entity. This structure is included by "
                               "the SystemProperties \"acl\", which is part of all OSDU records. Not extensible.",
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
            "osdu:wks:AbstractContact:1.0.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractContact:1.0.0",
                "description": "An object with properties that describe a specific person or other point-of-contact (like an email distribution list) that is relevant in this context (like a given data set or business project). The contact specified may be either internal or external to the organisation (something denoted via the Organisation object that is referenced). Note that some properties contain personally identifiable information, so it might not be appropriate to populate all properties in all scenarios.",
                "x-osdu-review-status": "Accepted",
                "title": "Abstract Contact",
                "type": "object",
                "properties": {
                    "RoleTypeID": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ContactRoleType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ContactRoleType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "The identifier of a reference value for the role of the contact within the associated organisation, such as Account owner, Sales Representative, Technical Support, Project Manager, Party Chief, Client Representative, Senior Observer.",
                        "type": "string",
                        "title": "Role Type ID"
                    },
                    "OrganisationID": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Organisation",
                                "GroupType": "master-data"
                            }
                        ],
                        "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Reference to the company the contact is associated with.",
                        "type": "string",
                        "title": "Organisation ID"
                    },
                    "Comment": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "description": "Additional information about the contact",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "type": "string",
                        "title": "Comment"
                    },
                    "PhoneNumber": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Contact phone number. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "type": "string",
                        "title": "Phone Number",
                        "example": "1-555-281-5555"
                    },
                    "EmailAddress": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "description": "Contact email address. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "type": "string",
                        "title": "Email Address",
                        "example": "support@company.com"
                    },
                    "Name": {
                        "x-osdu-attribution-publication": "The OSDU Data Platform",
                        "description": "Name of the individual contact. Property may be left empty where it is inappropriate to provide personally identifiable information.",
                        "x-osdu-attribution-revision": "Evergreen",
                        "x-osdu-attribution-authority": "The Open Group",
                        "type": "string",
                        "title": "Name"
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractContact.1.0.0.json"
            }
        },
        "properties": {
            "id": {
                "description": "Previously called ResourceID or SRN which identifies this OSDU resource object without version.",
                "title": "Entity ID",
                "type": "string",
                "pattern": "^[\\w\\-\\.]+:work-product-component\\-\\-WellLog:[\\w\\-\\.\\:\\%]+$",
                "example": "namespace:work-product-component--WellLog:c2c79f1c-90ca-5c92-b8df-04dbe438f414"
            },
            "kind": {
                "description": "The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.",
                "title": "Entity Kind",
                "type": "string",
                "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.]+:[0-9]+.[0-9]+.[0-9]+$",
                "example": "osdu:wks:work-product-component--WellLog:1.2.0"
            },
            "version": {
                "description": "The version number of this OSDU resource; set by the framework.",
                "title": "Version Number",
                "type": "integer",
                "format": "int64",
                "example": 1562066009929332
            },
            "acl": {
                "description": "The access control tags associated with this entity.",
                "title": "Access Control List",
                "$ref": "{{schema-authority}}:wks:AbstractAccessControlList:1.0.0"
            },
            "legal": {
                "description": "The entity's legal tags and compliance status. The actual contents associated with the legal tags is managed by the Compliance Service.",
                "title": "Legal Tags",
                "$ref": "{{schema-authority}}:wks:AbstractLegalTags:1.0.0"
            },
            "tags": {
                "title": "Tag Dictionary",
                "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                "type": "object",
                "additionalProperties": {
                    "type": "string"
                },
                "example": {
                    "NameOfKey": "String value"
                }
            },
            "createTime": {
                "description": "Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                "title": "Resource Object Creation DateTime",
                "type": "string",
                "format": "date-time",
                "example": "2020-12-16T11:46:20.163Z"
            },
            "createUser": {
                "title": "Resource Object Creation User Reference",
                "description": "The user reference, which created the first version of this resource object. Set by the System.",
                "type": "string",
                "example": "some-user@some-company-cloud.com"
            },
            "modifyTime": {
                "description": "Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
                "title": "Resource Object Version Creation DateTime",
                "type": "string",
                "format": "date-time",
                "example": "2020-12-16T11:52:24.477Z"
            },
            "modifyUser": {
                "title": "Resource Object Version Creation User Reference",
                "description": "The user reference, which created this version of this resource object. Set by the System.",
                "type": "string",
                "example": "some-user@some-company-cloud.com"
            },
            "ancestry": {
                "description": "The links to data, which constitute the inputs, from which this record instance is derived.",
                "title": "Ancestry",
                "$ref": "{{schema-authority}}:wks:AbstractLegalParentList:1.0.0"
            },
            "meta": {
                "description": "The Frame of Reference meta data section linking the named properties to self-contained definitions.",
                "title": "Frame of Reference Meta Data",
                "type": "array",
                "items": {
                    "$ref": "{{schema-authority}}:wks:AbstractMetaItem:1.0.0"
                }
            },
            "data": {
                "allOf": [
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractCommonResources:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractWPCGroupType:1.0.0"
                    },
                    {
                        "$ref": "#/definitions/osdu:wks:AbstractWorkProductComponent:1.0.0"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "WellboreID": {
                                "type": "string",
                                "description": "The Wellbore where the Well Log Work Product Component was recorded",
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Wellbore:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "x-osdu-relationship": [
                                    {
                                        "GroupType": "master-data",
                                        "EntityType": "Wellbore"
                                    }
                                ]
                            },
                            "WellLogTypeID": {
                                "type": "string",
                                "description": "Well Log Type short Description such as Raw; Evaluated; Composite;....",
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LogType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "x-osdu-relationship": [
                                    {
                                        "GroupType": "reference-data",
                                        "EntityType": "LogType"
                                    }
                                ]
                            },
                            "TopMeasuredDepth": {
                                "type": "number",
                                "title": "Top Measured Depth",
                                "description": "Informational Top Measured Depth of the Well Log. Always populate SamplingStart and SamplingStop, which represents the real sampling of the WellLog, including  non-depth sampling.",
                                "x-osdu-frame-of-reference": "UOM:length"
                            },
                            "BottomMeasuredDepth": {
                                "type": "number",
                                "title": "Bottom Measured Depth",
                                "description": "Informational Bottom Measured Depth of the Well Log. Always populate SamplingStart and SamplingStop, which represents the real sampling of the WellLog, including  non-depth sampling.",
                                "x-osdu-frame-of-reference": "UOM:length"
                            },
                            "ServiceCompanyID": {
                                "type": "string",
                                "description": "The relationship to a Service Company, typically the producer or logging contractor.",
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "x-osdu-relationship": [
                                    {
                                        "GroupType": "master-data",
                                        "EntityType": "Organisation"
                                    }
                                ]
                            },
                            "LogSource": {
                                "type": "string",
                                "description": "OSDU Native Log Source - will be updated for later releases - not to be used yet"
                            },
                            "LogActivity": {
                                "type": "string",
                                "description": "Log Activity, used to describe the type of pass such as Calibration Pass - Main Pass - Repeated Pass"
                            },
                            "LogRun": {
                                "type": "string",
                                "description": "Log Run - describe the run of the log - can be a number, but may be also a alphanumeric description such as a version name"
                            },
                            "LogVersion": {
                                "type": "string",
                                "description": "Log Version"
                            },
                            "LoggingService": {
                                "type": "string",
                                "description": "Logging Service - mainly a short concatenation of the names of the tools"
                            },
                            "LogServiceDateInterval": {
                                "type": "object",
                                "description": "An interval built from two nested values : StartDate and EndDate. It applies to the whole log services and may apply to composite logs as [start of the first run job] and [end of the last run job]Log Service Date",
                                "title": "LogServiceDateInterval",
                                "properties": {
                                    "StartDate": {
                                        "type": "string",
                                        "format": "date-time"
                                    },
                                    "EndDate": {
                                        "type": "string",
                                        "format": "date-time"
                                    }
                                }
                            },
                            "ToolStringDescription": {
                                "type": "string",
                                "description": "Tool String Description - a long concatenation of the tools used for logging services such as GammaRay+NeutronPorosity"
                            },
                            "LoggingDirection": {
                                "type": "string",
                                "description": "Specifies whether curves were collected downward or upward"
                            },
                            "PassNumber": {
                                "type": "integer",
                                "description": "Indicates if the Pass is the Main one (1) or a repeated one - and it's level repetition"
                            },
                            "ActivityType": {
                                "type": "string",
                                "description": "General method or circumstance of logging - MWD, completion, ..."
                            },
                            "DrillingFluidProperty": {
                                "type": "string",
                                "description": "Type of mud at time of logging (oil, water based,...)"
                            },
                            "HoleTypeLogging": {
                                "type": "string",
                                "description": "Description of the hole related type of logging - POSSIBLE VALUE : OpenHole / CasedHole / CementedHole",
                                "pattern": "^OPENHOLE|CASEDHOLE|CEMENTEDHOLE$"
                            },
                            "VerticalMeasurementID": {
                                "type": "string",
                                "description": "DEPRECATED: Use data.VerticalMeasurement.VerticalReferenceID instead. References an entry in the Vertical Measurement array for the Wellbore identified by WellboreID, which defines the vertical reference datum for all curve measured depths. Either VerticalMeasurementID or VerticalMeasurement are populated."
                            },
                            "VerticalMeasurement": {
                                "$ref": "{{schema-authority}}:wks:AbstractFacilityVerticalMeasurement:1.0.0",
                                "description": "The vertical measurement reference for the log curves, which defines the vertical reference datum for the logged depths. Either VerticalMeasurement or VerticalMeasurementID are populated."
                            },
                            "Curves": {
                                "type": "array",
                                "x-osdu-indexing": {
                                    "type": "nested"
                                },
                                "items": {
                                    "type": "object",
                                    "title": "Curves",
                                    "properties": {
                                        "CurveID": {
                                            "type": "string",
                                            "description": "The ID of the Well Log Curve"
                                        },
                                        "DateStamp": {
                                            "type": "string",
                                            "description": "Date curve was created in the database",
                                            "format": "date-time",
                                            "x-osdu-frame-of-reference": "DateTime"
                                        },
                                        "CurveVersion": {
                                            "type": "string",
                                            "description": "The Version of the Log Curve."
                                        },
                                        "CurveQuality": {
                                            "type": "string",
                                            "description": "The Quality of the Log Curve."
                                        },
                                        "InterpreterName": {
                                            "type": "string",
                                            "description": "The name of person who interpreted this Log Curve."
                                        },
                                        "IsProcessed": {
                                            "type": "boolean",
                                            "description": "Indicates if the curve has been (pre)processed or if it is a raw recording"
                                        },
                                        "NullValue": {
                                            "type": "boolean",
                                            "description": "Indicates that there is no measurement within the curve"
                                        },
                                        "DepthCoding": {
                                            "type": "string",
                                            "description": "DEPRECATED: Replaced by boolean data.IsRegular. The Coding of the depth.",
                                            "pattern": "^REGULAR|DISCRETE$"
                                        },
                                        "Interpolate": {
                                            "type": "boolean",
                                            "description": "Whether curve can be interpolated or not"
                                        },
                                        "TopDepth": {
                                            "type": "number",
                                            "description": "The curve's minimum 'depth', i.e., the reference value at which the curve has its first non-absent value. The curve may contain further absent values in between TopDepth and BaseDepth. Note that the SamplingDomainType may not be a depth as the property name indicates.",
                                            "x-osdu-frame-of-reference": "UOM_via_property:DepthUnit"
                                        },
                                        "BaseDepth": {
                                            "type": "number",
                                            "description": "The curve's maximum 'depth' i.e., the reference value at which the curve has its last non-absent value. The curve may contain further absent values in between TopDepth and BaseDepth. Note that the SamplingDomainType may not be a depth as the property name indicates.",
                                            "x-osdu-frame-of-reference": "UOM_via_property:DepthUnit"
                                        },
                                        "DepthUnit": {
                                            "type": "string",
                                            "description": "Unit of Measure for TopDepth and BaseDepth.",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "UnitOfMeasure"
                                                }
                                            ]
                                        },
                                        "CurveUnit": {
                                            "type": "string",
                                            "description": "Unit of Measure for the Log Curve",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-UnitOfMeasure:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "UnitOfMeasure"
                                                }
                                            ]
                                        },
                                        "Mnemonic": {
                                            "type": "string",
                                            "description": "The Mnemonic of the Log Curve is the value as received either from Raw Providers or from Internal Processing team",
                                            "example": "PRES_HDRB.BAR"
                                        },
                                        "LogCurveTypeID": {
                                            "type": "string",
                                            "description": "The related record id of the Log Curve Type - which is the standard mnemonic chosen by the company - OSDU provides an initial list",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LogCurveType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "LogCurveType"
                                                }
                                            ]
                                        },
                                        "LogCurveBusinessValueID": {
                                            "type": "string",
                                            "description": "The related record id of the Log Curve Business Value Type.",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LogCurveBusinessValue:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "LogCurveBusinessValue"
                                                }
                                            ]
                                        },
                                        "LogCurveMainFamilyID": {
                                            "type": "string",
                                            "description": "The related record id of the Log Curve Main Family Type - which is the Geological Physical Quantity measured - such as porosity.",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LogCurveMainFamily:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "LogCurveMainFamily"
                                                }
                                            ]
                                        },
                                        "LogCurveFamilyID": {
                                            "type": "string",
                                            "description": "The related record id of the Log Curve Family - which is the detailed Geological Physical Quantity Measured - such as neutron porosity",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-LogCurveFamily:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "LogCurveFamily"
                                                }
                                            ]
                                        },
                                        "NumberOfColumns": {
                                            "type": "integer",
                                            "title": "Number Of Columns",
                                            "description": "The number of columns present in this Curve for a single reference value. For simple logs this is typically 1; for image logs this holds the number of image traces or property series. Further information about the columns can be obtained via the respective log or curve APIs of the Domain Data Management Service.",
                                            "example": 192
                                        },
                                        "CurveSampleTypeID": {
                                            "type": "string",
                                            "title": "Curve Sample Type ID",
                                            "description": "The value type to be expected as curve sample values.",
                                            "example": "namespace:reference-data--CurveSampleType:float:",
                                            "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-CurveSampleType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                            "x-osdu-relationship": [
                                                {
                                                    "GroupType": "reference-data",
                                                    "EntityType": "CurveSampleType"
                                                }
                                            ]
                                        },
                                        "CurveDescription": {
                                            "type": "string",
                                            "title": "Curve Description",
                                            "description": "Mnemonic-level curve description is used during parsing or reading and ingesting LAS or DLIS files, to explain the type of measurement being looked at, specifically for that moment. Curve description is specific to that single (log) mnemonic and for the entire log (acquisition run) interval. In essence, curve description defines the internal factors such as what the \"curve\" or measurement ideally is representing, how is it calculated, what are the assumptions and the \"constants\".",
                                            "example": "CBL Adjustment Factor, Resistivity Inversion Selection, Detector 1 Barite Constant"
                                        }
                                    }
                                }
                            },
                            "FrameIdentifier": {
                                "type": "string",
                                "title": "Frame Identifier",
                                "description": "For multi-frame or multi-section files, this identifier defines the source frame in the file. If the identifier is an index number the index starts with zero and is converted to a string for this property.",
                                "example": 0
                            },
                            "SamplingInterval": {
                                "type": "number",
                                "title": "Sampling Interval",
                                "description": "For regularly sampled curves this property holds the sampling interval. For non regular sampling rate this property is not set. The IsRegular flag indicates whether SamplingInterval is required.",
                                "example": 0.0254,
                                "x-osdu-frame-of-reference": "UOM"
                            },
                            "ReferenceCurveID": {
                                "type": "string",
                                "title": "Reference Curve ID",
                                "description": "The data.Curves[].CurveID, which holds the primary index (reference) values.",
                                "example": "MD"
                            },
                            "SamplingStart": {
                                "type": "number",
                                "title": "Sampling Start",
                                "description": "The start value/first value of the ReferenceCurveID, typically the start depth of the logging.",
                                "example": 2500,
                                "x-osdu-frame-of-reference": "UOM"
                            },
                            "SamplingStop": {
                                "type": "number",
                                "title": "Sampling Stop",
                                "description": "The stop value/last value of the ReferenceCurveID, typically the end depth of the logging.",
                                "example": 7500,
                                "x-osdu-frame-of-reference": "UOM"
                            },
                            "SamplingDomainTypeID": {
                                "type": "string",
                                "title": "Sampling Domain Type ID",
                                "description": "The sampling domain, e.g. measured depth, true vertical, travel-time, calendar-time.",
                                "example": "namespace:reference-data--WellLogSamplingDomainType:Depth:",
                                "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-WellLogSamplingDomainType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "x-osdu-relationship": [
                                    {
                                        "GroupType": "reference-data",
                                        "EntityType": "WellLogSamplingDomainType"
                                    }
                                ]
                            },
                            "CompanyID": {
                                "type": "string",
                                "title": "Company ID",
                                "description": "The relationship to company who engaged the service company (ServiceCompanyID) to perform the logging.",
                                "pattern": "^[\\w\\-\\.]+:master-data\\-\\-Organisation:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                "x-osdu-relationship": [
                                    {
                                        "GroupType": "master-data",
                                        "EntityType": "Organisation"
                                    }
                                ]
                            },
                            "CandidateReferenceCurveIDs": {
                                "type": "array",
                                "description": "Secondary index curves, which are alternative candidates to act as ReferenceCurveID. Generally not populated, except in the cases where multiple reference curves are present, e.g. measured depth and time.",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "ZeroTime": {
                                "type": "string",
                                "description": "Optional time reference for (calender) time logs. The ISO date time string representing zero time. Not to be confused with seismic travel time zero. The latter is defined by SeismicReferenceDatum.",
                                "format": "date-time",
                                "x-osdu-frame-of-reference": "DateTime"
                            },
                            "SeismicReferenceElevation": {
                                "$ref": "{{schema-authority}}:wks:AbstractFacilityVerticalMeasurement:1.0.0",
                                "description": "Populated only if the WellLog represents time-depth relationships or checkshots. It is expressed via the standard AbstractFacilityVerticalMeasurement. The following properties are expected to be present: VerticalMeasurementPathID (typically elevation), VerticalMeasurementTypeID as SeismicReferenceDatum, VerticalMeasurement holding the offset to either the VerticalCRSID or the chained VerticalReferenceID in the parent Wellbore."
                            },
                            "IsRegular": {
                                "type": "boolean",
                                "title": "Is Regular Flag",
                                "description": "Boolean property indicating the sampling mode of the ReferenceCurveID. True means all reference curve values are regularly spaced (see SamplingInterval); false means irregular or discrete sample spacing."
                            },
                            "LogRemark": {
                                "type": "string",
                                "title": "Log Remark",
                                "description": "Log remark provides contextual information during the actual log object acquisition. Explains how the measurement in the wellbore is taken on a point in time or depth. Additional information may be included such as bad weather, tool failure, etc. Usually a part of the log header, log remark contains info specific for an acquisition run, specific for a given logging tool (multiple measurements) and/or a specific interval. In essence, log remark represents the external factors and operational environment, directly or indirectly affecting the measurement quality/uncertainty (dynamically over time/depth) - adding both noise and bias to the measurements.",
                                "example": "tool failure, bad weather"
                            }
                        },
                        "title": "IndividualProperties"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "ExtensionProperties": {
                                "type": "object"
                            }
                        },
                        "title": "ExtensionProperties"
                    }
                ]
            }
        },
        "required": [
            "kind",
            "acl",
            "legal"
        ],
        "additionalProperties": 'false',
        "x-osdu-review-status": "Accepted",
        "x-osdu-supported-file-formats": [
            "WITSML",
            "DLIS",
            "LIS",
            "LAS2",
            "LAS3",
            "csv"
        ],
        "x-osdu-virtual-properties": {
            "data.VirtualProperties.DefaultLocation": {
                "type": "object",
                "priority": [
                    {
                        "path": "data.SpatialArea"
                    },
                    {
                        "path": "data.SpatialPoint"
                    }
                ]
            },
            "data.VirtualProperties.DefaultName": {
                "type": "string",
                "priority": [
                    {
                        "path": "data.Name"
                    }
                ]
            }
        },
        "x-osdu-inheriting-from-kind": [
            {
                "name": "WorkProductComponent",
                "kind": "osdu:wks:AbstractWPCGroupType:1.0.0"
            }
        ]
    }
