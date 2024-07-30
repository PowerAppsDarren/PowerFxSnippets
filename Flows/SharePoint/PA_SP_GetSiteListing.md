FLOW: PA_SP_GetSiteListing

TRIGGER: Power Apps (V2)
    - Inputs:
        - RootSharePointSiteURL

ACTION: Send an HTTP request to SharePoint
    - Site Address: RootSharePointSiteURL (from trigger)
    - Method: GET
    - Uri: _api/search/query?querytext='contentclass:STS_Site'&trimduplicates=false&selectproperties='Title,Path,SiteId,WebId,Description,Created,LastModifiedTime'
    - Headers: {"Accept": "application/json;odata=verbose"}
    - Body: (blank - should be for any GET)

ACTION: Parse JSON
    - Content: Body (from previous action)
    - Schema: 
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "properties": {
                            "type": "object",
                            "properties": {
                                "d": {
                                    "type": "object",
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        },
                                        "properties": {
                                            "type": "object",
                                            "properties": {
                                                "query": {
                                                    "type": "object",
                                                    "properties": {
                                                        "type": {
                                                            "type": "string"
                                                        },
                                                        "properties": {
                                                            "type": "object",
                                                            "properties": {
                                                                "PrimaryQueryResult": {
                                                                    "type": "object",
                                                                    "properties": {
                                                                        "type": {
                                                                            "type": "string"
                                                                        },
                                                                        "properties": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                                "RelevantResults": {
                                                                                    "type": "object",
                                                                                    "properties": {
                                                                                        "type": {
                                                                                            "type": "string"
                                                                                        },
                                                                                        "properties": {
                                                                                            "type": "object",
                                                                                            "properties": {
                                                                                                "Table": {
                                                                                                    "type": "object",
                                                                                                    "properties": {
                                                                                                        "type": {
                                                                                                            "type": "string"
                                                                                                        },
                                                                                                        "properties": {
                                                                                                            "type": "object",
                                                                                                            "properties": {
                                                                                                                "Rows": {
                                                                                                                    "type": "object",
                                                                                                                    "properties": {
                                                                                                                        "type": {
                                                                                                                            "type": "string"
                                                                                                                        },
                                                                                                                        "items": {
                                                                                                                            "type": "object",
                                                                                                                            "properties": {
                                                                                                                                "type": {
                                                                                                                                    "type": "string"
                                                                                                                                },
                                                                                                                                "properties": {
                                                                                                                                    "type": "object",
                                                                                                                                    "properties": {
                                                                                                                                        "Cells": {
                                                                                                                                            "type": "object",
                                                                                                                                            "properties": {
                                                                                                                                                "type": {
                                                                                                                                                    "type": "string"
                                                                                                                                                },
                                                                                                                                                "items": {
                                                                                                                                                    "type": "object",
                                                                                                                                                    "properties": {
                                                                                                                                                        "type": {
                                                                                                                                                            "type": "string"
                                                                                                                                                        },
                                                                                                                                                        "properties": {
                                                                                                                                                            "type": "object",
                                                                                                                                                            "properties": {
                                                                                                                                                                "Key": {
                                                                                                                                                                    "type": "object",
                                                                                                                                                                    "properties": {
                                                                                                                                                                        "type": {
                                                                                                                                                                            "type": "string"
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                },
                                                                                                                                                                "Value": {
                                                                                                                                                                    "type": "object",
                                                                                                                                                                    "properties": {
                                                                                                                                                                        "type": {
                                                                                                                                                                            "type": "string"
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                    }
                                                                                                                                                }
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

Action: Select
    - From: body('Parse_JSON')?['d']?['query']?['PrimaryQueryResult']?['RelevantResults']?['Table']?['Rows']?['results']
    - Map: 
            {
            "Title": @{item()?['Cells']['results'][0]?['Value']},
            "URL": @{item()?['Cells']['results'][1]?['Value']},
            "SiteId": @{item()?['Cells']['results'][2]?['Value']},
            "WebId": @{item()?['Cells']['results'][3]?['Value']},
            "Description": @{item()?['Cells']['results'][4]?['Value']},
            "Created": @{item()?['Cells']['results'][5]?['Value']},
            "LastModifiedTime": @{item()?['Cells']['results'][6]?['Value']}
            }

Action: Respond to a Power App or flow
    - Response: body('Select')