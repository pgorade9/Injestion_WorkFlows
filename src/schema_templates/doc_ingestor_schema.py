# schema used for document ingestion
def get_schema_template():
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Document",
        "description": "document schema",
        "type": "object",
        "definitions": {
            "legal": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "title": "legal",
                "type": "object"
            },
            "metaItem": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "title": "metaItem",
                "type": "object"
            },
            "tagDictionary": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "title": "tagDictionary",
                "type": "object"
            },
            "linkList": {
                "type": "object",
                "properties": {
                    "name": {
                        "link": "string"
                    }
                }
            },
            "documentData": {
                "description": "The domain specific data container for a document.",
                "title": "Document Data",
                "type": "object",
                "properties": {
                    "Relationships": {
                        "description": "The Non-Deterministic relationships block - Aliging with AbstractGenericRelationships structure",
                        "type": "array",
                        "title": "Relationships",
                        "x-osdu-indexing": {
                            "type": "flattened"
                        },
                        "items": {
                            "description": "The",
                            "type": "object",
                            "title": "Relationship",
                            "properties": {
                                "RelationshipName": {
                                    "type": "string",
                                    "title": "Relationship Name",
                                    "description": "The relationship name or role."
                                },
                                "TargetID": {
                                    "pattern": "^[\\w\\-\\.]+:[\\w\\-\\.]+:[\\w\\-\\.\\:\\%]+:[0-9]*$",
                                    "description": "The reference to a target record id. It may or may not refer to a specific version. This property is mandatory.",
                                    "x-osdu-relationship": [],
                                    "type": "string",
                                    "title": "Target ID"
                                },
                                "Description": {
                                    "type": "string",
                                    "title": "Description",
                                    "description": "An optional additional description."
                                }
                            },
                            "required": [
                                "TargetID"
                            ]
                        }
                    },
                    "FileType": {
                        "description": "TBD",
                        "title": "FileType",
                        "type": "string",
                        "example": "pdf"
                    },
                    "wellboreId": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "wellbore",
                                "GroupType": "master-data"
                            }
                        ],
                        "title": "The well-known i.e. deterministic relationship attribute defined for entity type - wellbore",
                        "type": "string"
                    },
                    "RockFormationId": {
                        "x-osdu-relationship": [
                            {
                                "EntityType": "RockFormation",
                                "GroupType": "master-data"
                            }
                        ],
                        "title": "The well-known i.e. deterministic relationship attribute defined for entity type - wellbore",
                        "type": "string"
                    },
                    "FileSource": {
                        "title": "FileSource",
                        "type": "string",
                        "description": "Source of the document"
                    },
                    "FileDateCreated": {
                        "title": "FileDateCreated",
                        "type": "datetime",
                        "description": "TBD"
                    },
                    "Name": {
                        "title": "Name",
                        "type": "string",
                        "description": "Name of the document"
                    },
                    "FileDateModified": {
                        "title": "FileDateModified",
                        "type": "datetime",
                        "description": "TBD"
                    },
                    "FileSize": {
                        "title": "FileSize",
                        "type": "string",
                        "description": "TBD"
                    }
                },
                "$id": "definitions/documentData"
            },
        },
        "properties": {
            "ancestry": {
                "description": "The links to data, which constitute the inputs.",
                "title": "Ancestry",
                "$ref": "#/definitions/linkList"
            },
            "data": {
                "description": "Document data container",
                "title": "Document Data",
                "$ref": "#/definitions/documentData"
            },
            "kind": {
                "default": "slb:pg:document:3.0.0",
                "description": "OSDU demo wellbore kind specification",
                "title": "Wellbore Kind",
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
            "acl": {
                "description": "The access control tags associated with this entity.",
                "title": "Access Control List",
                "$ref": "#/definitions/tagDictionary"
            },
            "id": {
                "description": "The unique identifier of the Document",
                "title": "Document ID",
                "type": "string"
            },
            "type": {
                "description": "The reference entity type as declared in common:metadata:entity:*.",
                "title": "Entity Type",
                "type": "string"
            },
            "version": {
                "format": "int64",
                "description": "The version number of this wellbore; set by the framework.",
                "title": "Entity Version Number",
                "type": "number",
                "example": "1040815391631285"
            }
        }
    }