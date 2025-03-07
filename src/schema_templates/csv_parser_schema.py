def get_schema_template():
    return {
        "license": "Copyright 2017-2020, Schlumberger\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\nhttp://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "description": "csv-parser schema",
        "title": "Wellbore",
        "type": "object",
        "definitions": {
            "osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0": {
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
            "osdu:wks:valueWithUnit:1.0.0": {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "description": "Number value associated with unit context. The 'unitKey' can be looked up in the root property meta[] array.",
                "x-osdu-schema-source": "osdu:wks:valueWithUnit:1.0.0",
                "title": "Value with unitKey",
                "type": "object",
                "properties": {
                    "unitKey": {
                        "description": "Unit for the value of the corresponding attribute for the domain object in question. The key can be looked up in the meta[] array under the root. It will be an array item with meta[i].kind == 'Unit' and meta[i].name == valueWithUnit.unitKey. The meta[i].propertyNames[] array will have to contain the name of the property including valueWithUnit to enable the normalizer to act on it.",
                        "title": "Unit Key",
                        "type": "string",
                        "x-osdu-natural-key": 2,
                        "example": "ft"
                    },
                    "value": {
                        "description": "Value of the corresponding attribute for the domain object in question.",
                        "title": "Value",
                        "type": "number",
                        "example": 30.2
                    }
                },
                "required": []
            },
            "linkList": {
                "type": "object",
                "properties": {
                    "name": {
                        "link": "string"
                    }
                }
            },
            "projectedPosition": {
                "description": "A position in the native CRS in Cartesian coordinates combined with an elevation from mean seal level (MSL)",
                "title": "Projected Position",
                "type": "object",
                "properties": {
                    "elevationFromMsl": {
                        "description": "Elevation from Mean Seal Level, downwards negative. The unit definition is found via 'elevationFromMsl.unitKey' in 'frameOfReference.units' dictionary.",
                        "type": "object",
                        "title": "Elevation from MSL",
                        "$ref": "#/definitions/osdu:wks:valueWithUnit:1.0.0"
                    },
                    "name": {
                        "title": "name",
                        "type": "string",
                        "example": "KB"
                    }
                },
                "required": []
            },
            "osdu:wks:AbstractFeatureCollection:1.0.0": {
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
            "osdu:wks:AbstractSpatialLocation:1.0.0": {
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
                        "$ref": f"#/definitions/osdu:wks:AbstractAnyCrsFeatureCollection:1.0.0"
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
                        "$ref": f"#/definitions/osdu:wks:AbstractFeatureCollection:1.0.0"
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
            "wellboreData": {
                "description": "The domain specific data container for a wellbore.",
                "title": "Wellbore Data",
                "type": "object",
                "properties": {
                    "SPUD_DATE": {
                        "format": "date",
                        "description": "The date and time when activities to drill the borehole begin to create a hole in the earth. For a sidetrack, this is the date kickoff operations began. The format follows ISO 8601 YYYY-MM-DD extended format",
                        "x-slb-aliasProperties": [
                            "witsml:DTimKickoff",
                            "ocean:SPUD_DATE",
                            "drillplan:spud_date"
                        ],
                        "title": "Spud Date",
                        "type": "string",
                        "example": "2013-03-22"
                    },
                    "SpatialLocation": {
                        "type": "object",
                        "description": "The spatial location information such as coordinates, CRS information.",
                        "$ref": f"#/definitions/osdu:wks:AbstractSpatialLocation:1.0.0"
                    },
                    "TVD": {
                        "x-slb-measurement": "True Vertical Depth",
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "True Vertical Depth",
                        "type": "string",
                        "example": [
                            20711,
                            "TBD"
                        ]
                    },
                    "PERMIT_NUMBER": {
                        "description": "Ther permit number for the wellbore",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Permit Number",
                        "type": "string",
                        "example": "SMP-09995"
                    },
                    "WELLBORE_NAME": {
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Wellbore Name",
                        "type": "string",
                        "example": "SMP G09995 001S0B1"
                    },
                    "CRS": {
                        "description": "Wellbore location CRS",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "CRS",
                        "type": "string",
                        "example": "World Geodetic System 1984"
                    },
                    "LONGUITUDE": {
                        "x-slb-measurement": "Longuitude",
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Longuitude",
                        "type": "string",
                        "example": [
                            -119.2,
                            "TBD"
                        ]
                    },
                    "STATE": {
                        "description": "The state, in which the wellbore is located.",
                        "x-slb-aliasProperties": [
                            "witsml:State"
                        ],
                        "title": "State",
                        "type": "string",
                        "example": [
                            "Texas"
                        ]
                    },
                    "CLASS": {
                        "description": "The current class of the wellbore",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "class",
                        "type": "string",
                        "example": "NEW FIELD WILDCAT"
                    },
                    "WELLBORE_SHAPE": {
                        "description": "The shape of the wellbore",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Wellbore Shape",
                        "type": "string",
                        "example": [
                            "DIRECTIONAL",
                            "VERTICAL"
                        ]
                    },
                    "FORMATION_AT_TD": {
                        "description": "The formation name at the wellbore total depth",
                        "x-slb-aliasProperties": [
                            "witsml:FORMATION_AT_TD"
                        ],
                        "title": "Formation at TD",
                        "type": "string",
                        "example": "MIOCENE LOWER"
                    },
                    "PERMIT_DATE": {
                        "format": "date",
                        "description": "The date and time when the wellbore permit was issued. The format follows ISO 8601 YYYY-MM-DD extended format",
                        "x-slb-aliasProperties": [
                            "witsml:DTimKickoff",
                            "ocean:PERMIT_DATE",
                            "drillplan:PERMIT_DATE"
                        ],
                        "title": "Permit Date",
                        "type": "string",
                        "example": "2013-03-22"
                    },
                    "STATUS": {
                        "description": "The current status of the wellbore",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Status",
                        "type": "string",
                        "example": "DRY & ABANDONED"
                    },
                    "COUNTRY": {
                        "description": "The country, in which the wellbore is located. The country name follows the convention in ISO 3166-1 'English short country name', see https://en.wikipedia.org/wiki/ISO_3166-1",
                        "x-slb-aliasProperties": [
                            "witsml:Country"
                        ],
                        "title": "Country",
                        "type": "string",
                        "example": [
                            "United States of America"
                        ]
                    },
                    "WB_NUMBER": {
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Wellbore Number",
                        "type": "string",
                        "example": "001S0B1"
                    },
                    "MD": {
                        "x-slb-measurement": "Measured Depth",
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Measured Depth",
                        "type": "number",
                        "example": 12.2
                    },
                    "ORIGINAL_OPERATOR": {
                        "description": "The original operator of the wellbore.",
                        "x-slb-aliasProperties": [
                            "ocean:Operator",
                            "witsml:Operator"
                        ],
                        "title": "Original Operator",
                        "type": "string",
                        "example": "Anadarko Petroleum"
                    },
                    "BASIN": {
                        "description": "The basin name, to which the wellbore belongs.",
                        "x-slb-aliasProperties": [
                            "witsml:BASIN"
                        ],
                        "title": "Basin",
                        "type": "string",
                        "example": "ATWATER"
                    },
                    "EPSG_CODE": {
                        "description": "EPSG code of the CRS",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "EPSG Code",
                        "type": "number",
                        "example": "4326"
                    },
                    "elevationReference": {
                        "x-slb-measurement": "Standard_Depth_Index",
                        "description": "The total depth along the wellbore as reported by the drilling contractor from 'elevationReference'. The unit definition is found via the property's unitKey' in 'frameOfReference.units' dictionary..",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "type": "object",
                        "title": "elevationReference",
                        "$ref": "#/definitions/projectedPosition"
                    },
                    "COUNTY": {
                        "description": "The county, in which the wellbore is located.",
                        "x-slb-aliasProperties": [
                            "witsml:County"
                        ],
                        "title": "County",
                        "type": "string",
                        "example": [
                            "ATWATER VALLEY"
                        ]
                    },
                    "UNIT_SYSTEM": {
                        "description": "Unit system used for the wellbore measurements",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Unit Sustem",
                        "type": "string",
                        "example": "English"
                    },
                    "UWI": {
                        "description": "The unique wellbore identifier, aka. API number, US well number or UBHI. Codes can have 10, 12 or 14 digits depending on the availability of directional sidetrack (2 digits) and event sequence codes (2 digits).",
                        "x-slb-aliasProperties": [
                            "ocean:UWI",
                            "witsml:SuffixAPI",
                            "drillplan:uwi"
                        ],
                        "title": "Unique Wellbore Identifier",
                        "type": "string",
                        "x-osdu-natural-key": 1,
                        "example": [
                            "SP435844921288",
                            "42-501-20130-01-02"
                        ]
                    },
                    "FIELD": {
                        "description": "The field name, to which the wellbore belongs.",
                        "x-slb-aliasProperties": [
                            "witsml:Field"
                        ],
                        "title": "Field",
                        "type": "string",
                        "example": "ATWATER VLLY B 8"
                    },
                    "INITIAL_COMPLETION_DATE": {
                        "format": "date",
                        "description": "The date and time of the initial completion of the wellbore. The format follows ISO 8601 YYYY-MM-DD extended format",
                        "x-slb-aliasProperties": [
                            "witsml:DTimKickoff",
                            "ocean:INITIAL_COMPLETION_DATE",
                            "drillplan:INITIAL_COMPLETION_DATE"
                        ],
                        "title": "Initial Completion Date",
                        "type": "string",
                        "example": "2013-03-22"
                    },
                    "ELEVATION": {
                        "x-slb-measurement": "Elevation",
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Elevation",
                        "type": "integer",
                        "example": [
                            84,
                            "TBD"
                        ]
                    },
                    "STATUS_DATE": {
                        "format": "date",
                        "description": "The date and time of the current status of the wellbore. The format follows ISO 8601 YYYY-MM-DD extended format",
                        "x-slb-aliasProperties": [
                            "witsml:DTimKickoff",
                            "ocean:STATUS_DATE",
                            "drillplan:STATUS_DATE"
                        ],
                        "title": "Status Date",
                        "type": "string",
                        "example": "2013-03-22"
                    },
                    "OPERATOR": {
                        "description": "The operator of the wellbore.",
                        "x-slb-aliasProperties": [
                            "ocean:Operator",
                            "witsml:Operator"
                        ],
                        "title": "Operator",
                        "type": "string",
                        "example": "Anadarko Petroleum"
                    },
                    "LEASE": {
                        "description": "The lease name, to which the wellbore belongs.",
                        "x-slb-aliasProperties": [
                            "witsml:LEASE"
                        ],
                        "title": "LEASE",
                        "type": "string",
                        "example": "SMP G09995"
                    },
                    "LATITUDE": {
                        "x-slb-measurement": "Latitude",
                        "description": "TBD",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Latitude",
                        "type": "string",
                        "example": [
                            60.2,
                            "TBD"
                        ]
                    },
                    "ELEVATION_REF": {
                        "description": "Elevation reference used for the measurements",
                        "x-slb-aliasProperties": [
                            "TBD:TBD"
                        ],
                        "title": "Elevation reference",
                        "type": "string",
                        "example": "MSL"
                    }
                },
                "$id": "definitions/wellboreData"
            }
        },
        "properties": {
            "ancestry": {
                "description": "The links to data, which constitute the inputs.",
                "title": "Ancestry",
                "$ref": "#/definitions/linkList"
            },
            "data": {
                "description": "Wellbore data container",
                "title": "Wellbore Data",
                "$ref": "#/definitions/wellboreData"
            },
            "kind": {
                "default": "osdu:wks:wellbore:1.0.0",
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
                "description": "The unique identifier of the wellbore",
                "title": "Wellbore ID",
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