# schema used for document ingestion
def get_schema_template():
    return {
        "license": "Copyright 2017-2020, Schlumberger\n\nLicensed under the Apache License, Version 2.0 (the "
                   "\"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a "
                   "copy of the License at\n\nhttp://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by "
                   "applicable"
                   "law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\""
                   "BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License "
                   "for"
                   "the specific language governing permissions and\nlimitations under the License.\n",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "description": "shapefile schema",
        "title": "Shapefile Schema",
        "type": "object",
        "definitions": {
            "data": {
                "description": "The domain specific data container for a well.",
                "title": "Well Data",
                "type": "object",
                "properties": {
                    "SPUD_DATE": {
                        "format": "date",
                        "description": "Date of spudding",
                        "title": "Spud Date",
                        "type": "string",
                        "example": "1999-11-23T00:00:00"
                    },
                    "MEASURED_DEPTH": {
                        "description": "Md of the wellbore",
                        "title": "Measured Depth",
                        "type": "number",
                        "example": 14
                    },
                    "TVD": {
                        "description": "TVD of the well",
                        "title": "True Vertical Depth",
                        "type": "number",
                        "example": [
                            20711
                        ]
                    },
                    "DF_ELEV": {
                        "description": "TBD",
                        "title": "DF elevation",
                        "type": "number",
                        "example": [
                            3600
                        ]
                    },
                    "SpatialLocation": {
                        "description": "The spatial location information such as coordinates, CRS information (left empty when not appropriate).",
                        "$ref": "#/definitions/osdu:wks:AbstractSpatialLocation:1.1.0"
                    },
                    "NO2_BH_LONGITUDE": {
                        "description": "TBD",
                        "title": "BH Longitude",
                        "type": "number",
                        "example": [
                            -119.2
                        ]
                    },
                    "NOD_DATUM": {
                        "description": "Wellbore location CRS",
                        "title": "NOD datum",
                        "type": "string",
                        "example": "World Geodetic System 1984"
                    },
                    "WELLBORE_NAME": {
                        "description": "TBD",
                        "title": "WELLBORE_NAME",
                        "type": "string",
                        "example": "Andreas WELL1"
                    },
                    "WELLBORE_NUMBER": {
                        "description": "Internal id",
                        "title": "WELLBORE_NUMBER",
                        "type": "string",
                        "x-osdu-natural-key": 1,
                        "example": "A1234"
                    },
                    "STATE": {
                        "description": "The state, in which the wellbore is located.",
                        "title": "State",
                        "type": "string",
                        "example": [
                            "Texas"
                        ]
                    },
                    "HOLE_DIRECTION": {
                        "description": "The shape of the wellbore",
                        "title": "Wellbore Shape",
                        "type": "string",
                        "example": [
                            "D",
                            "V"
                        ]
                    },
                    "CLASS": {
                        "description": "The current class of the wellbore",
                        "title": "class",
                        "type": "string",
                        "example": "NEW FIELD WILDCAT"
                    },
                    "projectIds": {
                        "description": "The relationship tags associated with this entity.",
                        "title": "Project IDs",
                        "type": "object",
                        "x-osdu-indexing": {
                            "type": "nested"
                        }
                    },
                    "NOD_SURFACE_LONGITUDE": {
                        "description": "TBD",
                        "title": "Surface Longitude",
                        "type": "number",
                        "example": [
                            -119.2
                        ]
                    },
                    "WELL_NUMBER": {
                        "description": "TBD",
                        "title": "Well number",
                        "type": "string",
                        "example": "SMP 123456"
                    },
                    "NOD_SURFACE_X": {
                        "title": "Surface X location",
                        "type": "number",
                        "example": [
                            692123.4568789
                        ]
                    },
                    "NOD_SURFACE_LATITUDE": {
                        "title": "Surface Latitude",
                        "type": "number",
                        "example": [
                            60.2
                        ]
                    },
                    "NOD_SURFACE_Y": {
                        "title": "Surface Y location",
                        "type": "number",
                        "example": [
                            692123.4568789
                        ]
                    },
                    "COUNTRY": {
                        "description": "The country, in which the wellbore is located.",
                        "title": "Country",
                        "type": "string",
                        "example": [
                            "US"
                        ]
                    },
                    "FINAL_DRILL_DATE": {
                        "format": "date",
                        "description": "The date and time when activities to drill the borehole ends",
                        "title": "Final drill date",
                        "type": "string",
                        "example": "1988-10-23T00:00:00"
                    },
                    "RIG_RELEASE_DATE": {
                        "format": "date",
                        "description": "The date and time when drilling rig was released",
                        "title": "Rig release date",
                        "type": "string",
                        "example": "1988-10-23T00:00:00"
                    },
                    "PLOT_NAME": {
                        "description": "TBD",
                        "title": "WEL plot name",
                        "type": "string",
                        "example": "SMP G 0"
                    },
                    "COMPLETION_DATE": {
                        "format": "date",
                        "description": "The date and time when wellbore was completed",
                        "title": "Completion date",
                        "type": "string",
                        "example": "1988-10-23T00:00:00"
                    },
                    "NO2_BH_X": {
                        "description": "TBD",
                        "title": "BH X location",
                        "type": "number",
                        "example": [
                            692123.4568789
                        ]
                    },
                    "NO2_BH_Y": {
                        "description": "TBD",
                        "title": "BH Y location",
                        "type": "number",
                        "example": [
                            463456.7890123
                        ]
                    },
                    "FIELD_NAME": {
                        "description": "The field name, to which the wellbore belongs.",
                        "title": "Field",
                        "type": "string",
                        "example": "ATWATER VLLY B 8"
                    },
                    "OPERATOR_CODE": {
                        "description": "system code for the operator of the wellbore.",
                        "title": "Operator CODE",
                        "type": "string",
                        "example": "12456"
                    },
                    "LEASE_NAME": {
                        "description": "The lease name, to which the wellbore belongs.",
                        "title": "Lease",
                        "type": "string",
                        "example": "SMP G09995"
                    },
                    "COUNTY": {
                        "description": "The county, in which the wellbore is located.",
                        "title": "County",
                        "type": "string",
                        "example": [
                            "Yoakum County",
                            501
                        ]
                    },
                    "UWI": {
                        "title": "UWI",
                        "type": "string",
                        "description": "Unique Well Identifier"
                    },
                    "Kick_off_wellbore": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Wellbore",
                                "GroupType": "master-data"
                            }
                        ],
                        "type": "string",
                        "description": "This is a pointer to the parent wellbore. The wellbore that starts from top has no parent."
                    },
                    "Wellbore": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "Wellbore"
                            }
                        ],
                        "type": "string",
                        "description": "This is a pointer to the parent field."
                    },
                    "LEASE_NUMBER": {
                        "description": "The lease name, to which the wellbore belongs.",
                        "title": "Lease",
                        "type": "string",
                        "example": "SMP G09995"
                    },
                    "KB_ELEV": {
                        "description": "TBD",
                        "title": "KB elevation",
                        "type": "number",
                        "example": [
                            3654
                        ]
                    },
                    "GROUND_ELEV": {
                        "description": "TBD",
                        "title": "GL elevation",
                        "type": "number",
                        "example": [
                            3600
                        ]
                    },
                    "NO2_BH_LATITUDE": {
                        "description": "TBD",
                        "title": "BH Latitude",
                        "type": "number",
                        "example": [
                            60.2
                        ]
                    },
                    "OPERATOR": {
                        "description": "The current operator of the wellbore.",
                        "title": "Current Operator",
                        "type": "string",
                        "example": "ACME ENERGY PRODUCTION CO LP"
                    },
                    "WEL_REF_ELEV": {
                        "description": "TBD",
                        "title": "Elevation reference",
                        "type": "number",
                        "example": [
                            3654
                        ]
                    },
                    "CON_PK_SOURCE": {
                        "description": "The source of the record data",
                        "title": "Source",
                        "type": "string",
                        "example": [
                            "PI"
                        ]
                    },
                    "DRILL_TOTAL_DEPTH": {
                        "description": "TBD",
                        "title": "Drilling total depth",
                        "type": "number",
                        "example": [
                            9000
                        ]
                    },
                    "FLUID_NAME": {
                        "description": "Fluid used during drilling",
                        "title": "Fluid name",
                        "type": "string",
                        "example": [
                            "water",
                            "WBM"
                        ]
                    },
                    "ABANDON_DATE": {
                        "format": "date",
                        "description": "The date and time when wellbore was abandoned",
                        "title": "Abandonement date",
                        "type": "string",
                        "example": "1988-10-23T00:00:00"
                    },
                    "API": {
                        "description": "The unique wellbore identifier, aka. API number, US well number or UBHI. Codes can have 10, 12 or 14 digits depending on the availability of directional sidetrack (2 digits) and event sequence codes (2 digits).",
                        "title": "Government Number",
                        "type": "string",
                        "example": 3456789012
                    },
                    "ELEV_UOM": {
                        "description": "UPOM of the elevation reference used for the measurements",
                        "title": "Elevation reference Unit",
                        "type": "string",
                        "example": "m"
                    },
                    "OPERATOR_NAME": {
                        "description": "The operator of the wellbore.",
                        "title": "Operator name",
                        "type": "string",
                        "example": "LIBERTY OIL INC"
                    },
                    "ELEVATION_REF": {
                        "description": "Elevation reference used for the measurements",
                        "title": "Elevation reference",
                        "type": "string",
                        "example": "MSL"
                    }
                },
            },
            "accessControlList": {
                "description": "The access control tags associated with this entity.",
                "title": "Access Control List",
                "type": "object",
                "properties": {
                    "viewers": {
                        "description": "The data viewers group specification.",
                        "title": "Owners",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": [
                            "data.default.viewers@slb.p4d.cloud.slb-ds.com"
                        ]
                    },
                    "owners": {
                        "description": "The data owner group specification.",
                        "title": "Owners",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": [
                            "data.default.owners@slb.p4d.cloud.slb-ds.com"
                        ]
                    }
                }
            },
            "legal": {
                "description": "Legal meta data like legal tags, relevant other countries, legal status.",
                "title": "Legal Meta Data",
                "type": "object",
                "properties": {
                    "legaltags": {
                        "description": "The list of legal tags, see compliance API.",
                        "title": "Legal Tags",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "otherRelevantDataCountries": {
                        "description": "The list of other relevant data countries using the ISO 2-letter codes, see compliance API.",
                        "title": "Other Relevant Data Countries",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "status": {
                        "title": "Legal Status",
                        "type": "string",
                        "description": "The legal status."
                    }
                }
            },
            "metaItem": {
                "description": "A meta data item, which allows the association of named properties or property values to a Unit/Measurement/CRS/Azimuth/Time context.",
                "title": "Frame of Reference Meta Data Item",
                "type": "object",
                "properties": {
                    "name": {
                        "description": "The name of the CRS or the symbol/name of the unit",
                        "title": "Name or Symbol",
                        "type": "string",
                        "example": [
                            "ftUS",
                            "NAD27 * OGP-Usa Conus / North Dakota South [32021,15851]"
                        ]
                    },
                    "propertyValues": {
                        "description": "The list of property values, to which this meta data item provides Unit/CRS context to. Typically a unit symbol is a value to a data structure; this symbol is then registered in this propertyValues array and the persistableReference provides the absolute reference.",
                        "title": "Attribute Names",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": [
                            "Foot US",
                            "ftUS"
                        ]
                    },
                    "persistableReference": {
                        "description": "The persistable reference string uniquely identifying the CRS or Unit",
                        "title": "Persistable Reference",
                        "type": "string",
                        "example": "{\"scaleOffset\":{\"scale\":0.3048006096012192,\"offset\":0.0},\"symbol\":\"ftUS\",\"baseMeasurement\":{\"ancestry\":\"Length\",\"type\":\"UM\"},\"type\":\"USO\"}"
                    },
                    "uncertainty": {
                        "title": "Uncertainty",
                        "type": "number",
                        "description": "The uncertainty of the values measured given the unit or CRS unit."
                    },
                    "kind": {
                        "description": "The kind of reference, unit, measurement, CRS or azimuth reference.",
                        "title": "Reference Kind",
                        "type": "string",
                        "example": [
                            "Unit",
                            "CRS",
                            "Measurement",
                            "AzimuthReference"
                        ]
                    },
                    "propertyNames": {
                        "description": "The list of property names, to which this meta data item provides Unit/CRS context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like \"data.structureA.propertyB\" to define a unique context.",
                        "title": "Attribute Names",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": [
                            "elevationFromMsl",
                            "totalDepthMdDriller",
                            "wellHeadProjected"
                        ]
                    }
                },
                "required": [
                    "kind",
                    "persistableReference"
                ]
            },
            "osdu:wks:AbstractSpatialLocation:1.1.0": {
                "x-osdu-inheriting-from-kind": [],
                "x-osdu-license": "Copyright 2022, The Open Group \nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "x-osdu-schema-source": "osdu:wks:AbstractCommonResources:1.0.0",
                "description": "Common resources to be injected at root 'data' level for every entity, which is persistable in Storage. The insertion is performed by the OsduSchemaComposer script.",
                "x-osdu-review-status": "Accepted",
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
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-ResourceLifecycleStatus:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "Describes the current Resource Lifecycle status.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "ResourceLifecycleStatus",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string",
                        "title": "Resource Lifecycle Status"
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
                        "type": "string",
                        "title": "Resource Security Classification"
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
                        "type": "string",
                        "title": "Resource Curation Status"
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
                        "type": "string",
                        "title": "Existence Kind"
                    },
                    "TechnicalAssuranceID": {
                        "pattern": "^[\\w\\-\\.]+:reference-data\\-\\-TechnicalAssuranceType:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                        "description": "DEPRECATED: Describes a record's overall suitability for general business consumption based on data quality. Clarifications: Since Certified is the highest classification of suitable quality, any further change or versioning of a Certified record should be carefully considered and justified. If a Technical Assurance value is not populated then one can assume the data has not been evaluated or its quality is unknown (=Unevaluated). Technical Assurance values are not intended to be used for the identification of a single \"preferred\" or \"definitive\" record by comparison with other records.",
                        "x-osdu-relationship": [
                            {
                                "EntityType": "TechnicalAssuranceType",
                                "GroupType": "reference-data"
                            }
                        ],
                        "type": "string",
                        "title": "Technical Assurance ID"
                    },
                    "Source": {
                        "type": "string",
                        "title": "Data Source",
                        "description": "The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed."
                    }
                },
                "$id": "https://schema.osdu.opengroup.org/json/abstract/AbstractCommonResources.1.0.0.json"
            },
            "ancestryList": {
                "description": "A list of entity IDs in the data lake, which act as legal parents/sources to the current entity.",
                "title": "Parent List",
                "type": "object",
                "properties": {
                    "parents": {
                        "description": "An array of none, one or many entity references in the data lake, which identify the source of data in the legal sense. Example: the 'parents' will be queried when e.g. the subscription of source data services is terminated; access to the derivatives is also terminated.",
                        "title": "Parents",
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "example": []
                    }
                }
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
            }
        },
        "properties": {
            "ancestry": {
                "description": "The links to data, which constitute the inputs.",
                "title": "Ancestry",
                "$ref": "#/definitions/ancestryList"
            },
            "data": {
                "description": "Well data container",
                "title": "Well Data",
                "$ref": "#/definitions/data"
            },
            "kind": {
                "description": "OSDU demo well kind specification",
                "title": "Well Kind",
                "type": "string"
            },
            "meta": {
                "description": "The meta data section linking the 'unitKey', 'crsKey' to self-contained definitions (persistableReference)",
                "title": "Frame of Reference Meta Data",
                "type": "array",
                "items": {
                    "$ref": "#/definitions/metaItem"
                }
            },
            "legal": {
                "description": "The geological interpretation's legal tags",
                "title": "Legal Tags",
                "$ref": "#/definitions/legal"
            },
            "id": {
                "description": "The unique identifier of the well",
                "title": "Well ID",
                "type": "string"
            },
            "acl": {
                "description": "The access control tags associated with this entity.",
                "title": "Access Control List",
                "$ref": "#/definitions/accessControlList"
            },
            "type": {
                "description": "The reference entity type as declared in common:metadata:entity:*.",
                "title": "Entity Type",
                "type": "string"
            },
            "version": {
                "format": "int64",
                "description": "The version number of this well; set by the framework.",
                "title": "Entity Version Number",
                "type": "number",
                "example": "1040815391631285"
            },
            "tags": {
                "description": "A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.",
                "title": "Tag Dictionary",
                "type": "array",
                "items": {
                    "$ref": "#/definitions/tags"
                }
            }
        }
    }
