def get_wellbore_template(wellbore_kind, acl_domain, data_partition_id, acl_user,own_acl_role,view_acl_role, legal):
    return [{
        "kind": f"{wellbore_kind}",
        "version": 1669912978836291,
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
                f"{legal}"
                # "dp1-Test-Legal-Tag-7643990"
            ],
            "otherRelevantDataCountries": [
                "US"
            ],
            "status": "compliant"
        },
        "tags": {
            "QualityScore": "High",
            "QCCompleteness": "High"
        },
        "meta": [
            {
                "kind": "CRS",
                "name": "NZGD_2000_NZ_Continental_Shelf_2000",
                "persistableReference": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"3851\"},\"type\":\"LBC\",\"ver\":\"PE_10_7_1\",\"name\":\"NZGD_2000_NZ_Continental_Shelf_2000\",\"wkt\":\"PROJCS[\\\"NZGD_2000_NZ_Continental_Shelf_2000\\\",GEOGCS[\\\"GCS_NZGD_2000\\\",DATUM[\\\"D_NZGD_2000\\\",SPHEROID[\\\"GRS_1980\\\",6378137.0,298.257222101]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",3000000.0],PARAMETER[\\\"False_Northing\\\",7000000.0],PARAMETER[\\\"Central_Meridian\\\",173.0],PARAMETER[\\\"Standard_Parallel_1\\\",-37.5],PARAMETER[\\\"Standard_Parallel_2\\\",-44.5],PARAMETER[\\\"Latitude_Of_Origin\\\",-41.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",3851]]\"}",
                "propertyNames": [
                    "wellHeadProjected.x",
                    "wellHeadProjected.y",
                    "wellHeadGeographic.latitude",
                    "wellHeadGeographic.longitude"
                ]
            },
            {
                "kind": "Unit",
                "name": "m",
                "persistableReference": "{\"scaleOffset\":{\"scale\":1.0,\"offset\":0.0},\"symbol\":\"M\",\"baseMeasurement\":{\"ancestry\":\"Length\",\"type\":\"UM\"},\"type\":\"USO\"}",
                "propertyNames": [
                    "properties.unit"
                ]
            },
            {
                "kind": "Unit",
                "name": "M",
                "persistableReference": "{\"scaleOffset\":{\"scale\":1.0,\"offset\":0.0},\"symbol\":\"M\",\"baseMeasurement\":{\"ancestry\":\"Length\",\"type\":\"UM\"},\"type\":\"USO\"}",
                "propertyNames": [
                    "properties.unit"
                ]
            },
            {
                "kind": "Unit",
                "name": "ft",
                "persistableReference": "\"{\\\"scaleOffset\\\":{\\\"scale\\\":0.3048,\\\"offset\\\":0.0},\\\"symbol\\\":\\\"FT\\\",\\\"baseMeasurement\\\":{\\\"ancestry\\\":\\\"Length\\\",\\\"type\\\":\\\"UM\\\"},\\\"type\\\":\\\"USO\\\"}\"",
                "propertyNames": [
                    "properties.unit",
                    "wellHeadElevation.value",
                    "wellHeadGeographic.elevationFromMsl.value",
                    "wellHeadProjected.elevationFromMsl.value"
                ]
            },
            {
                "kind": "DateTime",
                "name": "datetime",
                "persistableReference": "{\"format\":\"yyyy-MM-ddTHH:mm:ss.SSS\",\"timeZone\":\"UTC\",\"type\":\"DTM\"}",
                "propertyNames": [
                    "dateModified"
                ]
            }
        ],
        "data": {
            "FacilityID": "100000732898",
            "FacilityTypeID": f"{data_partition_id}:reference-data--FacilityType:Wellbore:",
            "FacilityName": "TA-TA-YO-YO-2",
            "NameAliases": [
                {
                    "AliasName": "100000732898",
                    "AliasNameTypeID": f"{data_partition_id}:reference-data--AliasNameType:UniqueIdentifier:"
                }
            ],
            "SpatialLocation": {
                "AsIngestedCoordinates": {
                    "type": "AnyCrsFeatureCollection",
                    "CoordinateReferenceSystemID": f"{data_partition_id}:reference-data--CoordinateReferenceSystem:Projected:EPSG::3851:",
                    "persistableReferenceCrs": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"3851\"},\"type\":\"LBC\",\"ver\":\"PE_10_7_1\",\"name\":\"NZGD_2000_NZ_Continental_Shelf_2000\",\"wkt\":\"PROJCS[\\\"NZGD_2000_NZ_Continental_Shelf_2000\\\",GEOGCS[\\\"GCS_NZGD_2000\\\",DATUM[\\\"D_NZGD_2000\\\",SPHEROID[\\\"GRS_1980\\\",6378137.0,298.257222101]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",3000000.0],PARAMETER[\\\"False_Northing\\\",7000000.0],PARAMETER[\\\"Central_Meridian\\\",173.0],PARAMETER[\\\"Standard_Parallel_1\\\",-37.5],PARAMETER[\\\"Standard_Parallel_2\\\",-44.5],PARAMETER[\\\"Latitude_Of_Origin\\\",-41.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",3851]]\"}",
                    "persistableReferenceVerticalCrs": "{\"authCode\":{\"auth\":\"EPSG\",\"code\":\"3851\"},\"type\":\"LBC\",\"ver\":\"PE_10_7_1\",\"name\":\"NZGD_2000_NZ_Continental_Shelf_2000\",\"wkt\":\"PROJCS[\\\"NZGD_2000_NZ_Continental_Shelf_2000\\\",GEOGCS[\\\"GCS_NZGD_2000\\\",DATUM[\\\"D_NZGD_2000\\\",SPHEROID[\\\"GRS_1980\\\",6378137.0,298.257222101]],PRIMEM[\\\"Greenwich\\\",0.0],UNIT[\\\"Degree\\\",0.0174532925199433]],PROJECTION[\\\"Lambert_Conformal_Conic\\\"],PARAMETER[\\\"False_Easting\\\",3000000.0],PARAMETER[\\\"False_Northing\\\",7000000.0],PARAMETER[\\\"Central_Meridian\\\",173.0],PARAMETER[\\\"Standard_Parallel_1\\\",-37.5],PARAMETER[\\\"Standard_Parallel_2\\\",-44.5],PARAMETER[\\\"Latitude_Of_Origin\\\",-41.0],UNIT[\\\"Meter\\\",1.0],AUTHORITY[\\\"EPSG\\\",3851]]\"}",
                    "persistableReferenceUnitZ": "ft",
                    "features": [
                        {
                            "type": "AnyCrsFeature",
                            "properties": {},
                            "geometry": {
                                "type": "AnyCrsPoint",
                                "coordinates": [
                                    3112495.70065638,
                                    7179245.6647411,
                                    34.5
                                ]
                            }
                        }
                    ]
                }
            },
            "TechnicalAssuranceTypeID": f"{data_partition_id}:reference-data--TechnicalAssuranceType:Suitable:",
            "Source": "Techlog",
            "VerticalMeasurements": [
                {
                    "VerticalMeasurement": 34.5,
                    "VerticalMeasurementTypeID": f"{data_partition_id}:reference-data--VerticalMeasurementType:MSL:",
                    "VerticalMeasurementPathID": f"{data_partition_id}:reference-data--VerticalMeasurementPath:ELEV:",
                    "VerticalMeasurementUnitOfMeasureID": f"{data_partition_id}:reference-data--UnitOfMeasure:ft:",
                    # "VerticalMeasurementID": "Well Head Elevation",
                    "VerticalMeasurementID": "RT"
                }
            ],
            "DefaultVerticalMeasurementID": "Well Head Elevation",
            "ExtensionProperties": {
                "slb": {
                    "kind": "slb:wbddms:WellboreExtensions:1.0.0",
                    "externalIds": [
                        "techlog:wellbore-D5A5861C-077B-4CA9-9C0E-8F76819B9F34",
                        "techlog:project-CE3DE501-AFEC-47EA-99A2-E0FE30630E46"
                    ],
                    "propertyDictionary": [
                        {
                            "description": "COMPANY",
                            "name": "Company"
                        },
                        {
                            "name": "Y",
                            "unitKey": "m",
                            "value": "7179245.66474110"
                        },
                        {
                            "description": "LATITUDE",
                            "name": "Latitude",
                            "value": "-39.37534990"
                        },
                        {
                            "name": "X",
                            "unitKey": "m",
                            "value": "3112495.70065638"
                        },
                        {
                            "description": "SERVICE COMPANY",
                            "name": "SRVC",
                            "value": "TAG Oil (NZ) Ltd"
                        },
                        {
                            "description": "LOCATION",
                            "name": "LOC"
                        },
                        {
                            "description": "NULL VALUE",
                            "name": "NULL",
                            "value": "-999.25"
                        },
                        {
                            "name": "Elevation_datum",
                            "value": "MSL"
                        },
                        {
                            "description": "STATE",
                            "name": "State"
                        },
                        {
                            "description": "UNIQUE WELL ID",
                            "name": "UWI",
                            "value": "100000732898"
                        },
                        {
                            "name": "CRS_Data",
                            "value": "<?xml version=\"1.0\" encoding=\"utf-8\"?><!--INFO: This file accompanies a data file and contains the spatial context.--><!--INFO: It was made by serializing an Ocean spatial companion information record.--><!--INFO: The coordinate reference system (CRS) is verbosely defined as ESRI well-known-text (WKT).--><SpatialCompanion version=\"1.0\"><ILateBoundCoordinateReferenceSystem name=\"NZGD_2000_NZ_Continental_Shelf_2000\" crsType=\"Projected\" engine=\"ESRI\" engineVersion=\"PE_10_7_1\"><AuthorityCode>EPSG,3851</AuthorityCode><WKT>PROJCS[\"NZGD_2000_NZ_Continental_Shelf_2000\",GEOGCS[\"GCS_NZGD_2000\",DATUM[\"D_NZGD_2000\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Lambert_Conformal_Conic\"],PARAMETER[\"False_Easting\",3000000.0],PARAMETER[\"False_Northing\",7000000.0],PARAMETER[\"Central_Meridian\",173.0],PARAMETER[\"Standard_Parallel_1\",-37.5],PARAMETER[\"Standard_Parallel_2\",-44.5],PARAMETER[\"Latitude_Of_Origin\",-41.0],UNIT[\"Meter\",1.0],AUTHORITY[\"EPSG\",3851]]</WKT></ILateBoundCoordinateReferenceSystem><Info history=\"\" /></SpatialCompanion>"
                        },
                        {
                            "name": "Horizontal_coordinate_system_code",
                            "value": "3851"
                        },
                        {
                            "description": "WELL",
                            "name": "WELL",
                            "value": "Cheal-B-5"
                        },
                        {
                            "description": "START DEPTH",
                            "name": "STRT",
                            "unitKey": "M",
                            "value": "-11.12520"
                        },
                        {
                            "description": "API NUMBER",
                            "name": "API"
                        },
                        {
                            "name": "Horizontal_coordinate_system_authority",
                            "value": "EPSG"
                        },
                        {
                            "description": "STOP DEPTH",
                            "name": "STOP",
                            "unitKey": "M",
                            "value": "1843.27800"
                        },
                        {
                            "description": "FIELD",
                            "name": "Field"
                        },
                        {
                            "description": "COUNTRY",
                            "name": "Country"
                        },
                        {
                            "description": "DATE",
                            "name": "DATE"
                        },
                        {
                            "name": "Elevation",
                            "unitKey": "ft",
                            "value": "34.5"
                        },
                        {
                            "description": "ESRI,PE_10_7_1: <?xml version=\"1.0\" encoding=\"utf-16\"?><ILateBoundCoordinateReferenceSystem name=\"NZGD_2000_NZ_Continental_Shelf_2000\"><AuthorityCode>EPSG,3851</AuthorityCode></ILateBoundCoordinateReferenceSystem>",
                            "name": "Horizontal_coordinate_system",
                            "value": "NZGD_2000_NZ_Continental_Shelf_2000"
                        },
                        {
                            "description": "COUNTY",
                            "name": "CNTY"
                        },
                        {
                            "description": "LONGITUDE",
                            "name": "Longitude",
                            "value": "174.30749680"
                        },
                        {
                            "description": "STEP",
                            "name": "STEP",
                            "unitKey": "M",
                            "value": "0.15240"
                        },
                        {
                            "name": "TEST"
                        }
                    ],
                    "wellHeadGeographic": {
                        "crsKey": "NZGD_2000_NZ_Continental_Shelf_2000",
                        "elevationFromMsl": {
                            "unitKey": "ft",
                            "value": 34.5
                        },
                        "latitude": -39.3753499,
                        "longitude": 174.3074968
                    }
                },
                "techlog": {
                    "delfi_source_entity": {
                        "id": f"{data_partition_id}:wellbore:techlog-CE3DE501-AFEC-47EA-99A2-E0FE30630E46--D5A5861C-077B-4CA9-9C0E-8F76819B9F34",
                        "data": {
                            "relationships": {
                                "definitiveTrajectory": {
                                    "id": f"{data_partition_id}:trajectory:techlog-CE3DE501-AFEC-47EA-99A2-E0FE30630E46--1BD145ED-BDB9-4696-949A-6416810BADA4"
                                }
                            },
                            "wellHeadProjected": {
                                "crsKey": "NZGD_2000_NZ_Continental_Shelf_2000"
                            },
                            "wellHeadElevation": {
                                "unitKey": "ft"
                            }
                        }
                    }
                }
            }
        }
    }]
