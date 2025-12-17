---
title: "Sample DrawSQL JSON Schema"
description: "Sample JSON schema for DrawSQL database diagrams, containing table structures and relationships for Power Apps data modeling"
category: "data-operations"
subcategory: "drawsql"
tags:
  - data
  - schema
  - json
  - database
  - diagram
difficulty: intermediate
products:
  - power-apps-canvas
dependencies: []
author: "PowerFxSnippets Community"
created: 2025-11-20
updated: 2025-11-20
license: "MIT"
related: []
---

# Sample DrawSQL JSON Schema

This snippet provides Power Fx code that creates a variable called fxSampleDrawSQLJSON containing a JSON string. This JSON represents a sample schema used to draw SQL database diagrams in Power Apps, which you can use as a starting point for your own database modeling.

## Add This to Your Application

```PowerFx
    fxSampleDrawSQLJSON = "{
		""parent_uuid"": ""d6388337-79f3-4856-83d5-ead97e47d5bf"",
		""driver"": ""sqlsrv"",
		""uuid"": ""7a55f1aa-abf6-4248-a6e8-e19988ea10ed"",
		""tables"": [
			{
				""uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
				""name"": ""ListItem"",
				""color"": ""#9561E2"",
				""order"": 2,
				""comment"": null,
				""width"": null,
				""left"": 10,
				""top"": -220,
				""columns"": [
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 66,
						""driver_data_type_name"": ""bigint"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": true,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""ID"",
						""order"": 1,
						""table_uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
						""uuid"": ""2742d655-0fe7-48df-b73e-7af0b2bd6b4a""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 66,
						""driver_data_type_name"": ""bigint"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""ListID"",
						""order"": 2,
						""table_uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
						""uuid"": ""bd7541a6-43ad-4882-950e-cbc15083d60c""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 134,
						""driver_data_type_name"": ""varchar"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""Title"",
						""order"": 3,
						""table_uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
						""uuid"": ""e61414b2-3e03-43fb-a149-7116df85d59b""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 134,
						""driver_data_type_name"": ""varchar"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""Description"",
						""order"": 4,
						""table_uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
						""uuid"": ""27a1dbc5-58bb-490d-8c54-f2c8c931b600""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 134,
						""driver_data_type_name"": ""varchar"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""Answer"",
						""order"": 5,
						""table_uuid"": ""d1e37730-ede0-4b71-84bb-be5ae56d5c8f"",
						""uuid"": ""de68e143-8c0c-45fa-8615-105f0b62d706""
					}
				],
				""indexes"": []
			},
			{
				""uuid"": ""fbd988e3-ca97-4a56-8004-7620e24163ea"",
				""name"": ""List"",
				""color"": ""#F66D9B"",
				""order"": 1,
				""comment"": null,
				""width"": null,
				""left"": -450,
				""top"": -190,
				""columns"": [
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 66,
						""driver_data_type_name"": ""bigint"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": true,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""ID"",
						""order"": 1,
						""table_uuid"": ""fbd988e3-ca97-4a56-8004-7620e24163ea"",
						""uuid"": ""046e4f37-0705-443b-8b45-c1dcbc498aae""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 134,
						""driver_data_type_name"": ""varchar"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""Title"",
						""order"": 2,
						""table_uuid"": ""fbd988e3-ca97-4a56-8004-7620e24163ea"",
						""uuid"": ""502f909b-59d2-4dfc-9730-558d5a3c425f""
					},
					{
						""comment"": null,
						""default"": null,
						""driver_data_type_id"": 134,
						""driver_data_type_name"": ""varchar"",
						""driver_data_type_params"": [],
						""duplicated_from_column_uuid"": null,
						""is_auto_increment"": false,
						""is_index"": false,
						""is_nullable"": false,
						""is_primary_key"": false,
						""is_unique_key"": false,
						""is_unsigned"": false,
						""name"": ""Description"",
						""order"": 3,
						""table_uuid"": ""fbd988e3-ca97-4a56-8004-7620e24163ea"",
						""uuid"": ""1bbbd706-f8e0-4196-b1b7-551d2aec1f08""
					}
				],
				""indexes"": []
			}
		],
		""relationships"": {
			""7d4a07e9-2c9a-40cc-9db6-f23c2ffcdbee"": {
				""uuid"": ""7d4a07e9-2c9a-40cc-9db6-f23c2ffcdbee"",
				""source_column_uuid"": ""bd7541a6-43ad-4882-950e-cbc15083d60c"",
				""target_column_uuid"": ""046e4f37-0705-443b-8b45-c1dcbc498aae"",
				""type"": ""many-to-one"",
				""name"": null
			}
		},
		""created_at"": ""2024-11-16T13:39:57+00:00"",
		""schema_version"": 2,
		""version"": 2
	}"
```

## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co)
* https://superpowerlabs.co 

---

## Disclaimer

**THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
