# Sample DrawSQL Export JSON

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```JSON
{
    "parent_uuid": "48f874fd-2070-443a-ba4f-756223d7ebc5",
    "driver": "sqlsrv",
    "uuid": "1c4f6230-02d3-4c89-a1a3-ea71f8721f65",
    "tables": [
        {
            "uuid": "359d5bed-895e-4ed5-90ca-8f9319fd230d",
            "name": "MANY2MANY_MAP",
            "color": "#6574CD",
            "order": 4,
            "comment": null,
            "width": null,
            "left": 350,
            "top": -120,
            "columns": [
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": true,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ID",
                    "order": 1,
                    "table_uuid": "359d5bed-895e-4ed5-90ca-8f9319fd230d",
                    "uuid": "bda4b750-68fa-4514-a7b5-20e30c9cc175"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "LEFT_ID",
                    "order": 2,
                    "table_uuid": "359d5bed-895e-4ed5-90ca-8f9319fd230d",
                    "uuid": "d497f842-145f-41b3-90b8-d799732a007a"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "RIGHT_ID",
                    "order": 3,
                    "table_uuid": "359d5bed-895e-4ed5-90ca-8f9319fd230d",
                    "uuid": "769b9943-1d1c-484f-a753-4477f9fa92cf"
                }
            ],
            "indexes": []
        },
        {
            "uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
            "name": "MAIN_DETAILS",
            "color": "#F66D9B",
            "order": 2,
            "comment": "This is the main table in our application.",
            "width": null,
            "left": 20,
            "top": -300,
            "columns": [
                {
                    "comment": "An auto number or identity type of column",
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": true,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ID",
                    "order": 1,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "e3fbe39b-bb1b-45c8-a591-7004a9e5b370"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": true,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "GUID",
                    "order": 2,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "73cf4a30-f1d9-4c18-a96a-d511ca6e43d3"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "MAIN_TABLE_ID",
                    "order": 3,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "f8278b6c-ec44-4300-ad32-996adf9f2ded"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 70,
                    "driver_data_type_name": "bit",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "IS_ACTIVE",
                    "order": 4,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "5c80b1fc-734f-4d70-96cd-8d4522556fa7"
                },
                {
                    "comment": "This field is for logical deletions. We could also use this for automated processes that will delete when it runs.",
                    "default": null,
                    "driver_data_type_id": 70,
                    "driver_data_type_name": "bit",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "IS_DELETED",
                    "order": 5,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "9192aa98-3c22-4695-a4a2-da9fa960b27b"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "NAME",
                    "order": 6,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "e6d3a3ca-c0a8-42e8-8ac4-d9fde2e81bc7"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "TITLE",
                    "order": 7,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "e2db130e-3736-44d7-998b-bf21337d70d5"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 136,
                    "driver_data_type_name": "datetime",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CREATED_WHEN",
                    "order": 8,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "245d6648-ceac-4c9e-844f-b6c385f7382a"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CREATED_BY",
                    "order": 9,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "8377e969-2a40-48c4-926c-52aed463b159"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 136,
                    "driver_data_type_name": "datetime",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "UPDATED_WHEN",
                    "order": 10,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "04addcae-6847-42f2-8d2d-dc3399199eff"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "UPDATED_BY",
                    "order": 11,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "7ecdb274-3477-42a7-a3e2-238b05d700d1"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [
                        4000
                    ],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "NOTES",
                    "order": 12,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "81c0e3f9-4ad9-4766-9f56-c5277a5681ba"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "TENANT_ID",
                    "order": 13,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "c5cc8602-2047-4817-8263-eecf1aa127e1"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ENVIRONMENT_ID",
                    "order": 14,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "39fd9b3f-86ae-4969-837a-bb22a9d270ff"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "APPLICATION_ID",
                    "order": 15,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "9819e56c-38ef-45ca-a100-2087a89d105b"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [
                        100
                    ],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "RECORD_VERSION",
                    "order": 16,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "90801154-cf1b-423d-92c8-194846fc94ec"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 153,
                    "driver_data_type_name": "text",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "JSON_HISTORY",
                    "order": 17,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "f90873e7-26f2-45f5-9a7c-94f386a24b4e"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CHECK_SUM",
                    "order": 18,
                    "table_uuid": "5278ec5a-1162-4eeb-a090-768eb49077be",
                    "uuid": "29df2812-8d55-4f01-b595-2fb79210962c"
                }
            ],
            "indexes": []
        },
        {
            "uuid": "6924bff2-0420-48a6-ac2f-cede5550fe73",
            "name": "MANY2MANY_RIGHT",
            "color": "#6574CD",
            "order": 4,
            "comment": null,
            "width": null,
            "left": 710,
            "top": 50,
            "columns": [
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": true,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ID",
                    "order": 1,
                    "table_uuid": "6924bff2-0420-48a6-ac2f-cede5550fe73",
                    "uuid": "ba074119-657b-47ba-8c40-409b0ad8f0e0"
                }
            ],
            "indexes": []
        },
        {
            "uuid": "b15cdfec-70d0-4a09-999f-c8bdaa055195",
            "name": "MANY2MANY_LEFT",
            "color": "#6574CD",
            "order": 3,
            "comment": null,
            "width": null,
            "left": 700,
            "top": -150,
            "columns": [
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": true,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ID",
                    "order": 1,
                    "table_uuid": "b15cdfec-70d0-4a09-999f-c8bdaa055195",
                    "uuid": "5aecb150-8d27-4916-bdcb-4ea4bb4b3696"
                }
            ],
            "indexes": []
        },
        {
            "uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
            "name": "MAIN_TABLE",
            "color": "#F66D9B",
            "order": 1,
            "comment": "This is the main table in our application.",
            "width": null,
            "left": -360,
            "top": -300,
            "columns": [
                {
                    "comment": "An auto number or identity type of column",
                    "default": null,
                    "driver_data_type_id": 66,
                    "driver_data_type_name": "bigint",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": true,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ID",
                    "order": 1,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "7632c05e-42b6-424e-b94b-6bdc65d8f62c"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": true,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "GUID",
                    "order": 2,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "ad323652-67b5-4eb5-a152-0f5399609797"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 70,
                    "driver_data_type_name": "bit",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "IS_ACTIVE",
                    "order": 3,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "4d05d0e1-d690-4429-b519-27da0c1091e0"
                },
                {
                    "comment": "This field is for logical deletions. We could also use this for automated processes that will delete when it runs.",
                    "default": null,
                    "driver_data_type_id": 70,
                    "driver_data_type_name": "bit",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "IS_DELETED",
                    "order": 4,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "0636ac54-b81d-4775-9067-c56a0f78de77"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "NAME",
                    "order": 5,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "433e83cf-e78c-48af-b4d0-f0c1041d924d"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "TITLE",
                    "order": 6,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "6b17293e-4bce-43da-b70f-09ffb4fad4eb"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 136,
                    "driver_data_type_name": "datetime",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CREATED_WHEN",
                    "order": 7,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "9fc0f7f4-bd56-4dda-b33a-dfa495fc09ba"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CREATED_BY",
                    "order": 8,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "6912656c-6480-462f-aa05-3d63cc374415"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 136,
                    "driver_data_type_name": "datetime",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "UPDATED_WHEN",
                    "order": 9,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "479cc73d-5a3c-4bbd-9022-2f5d287495da"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "UPDATED_BY",
                    "order": 10,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "419e83f8-7cbd-4218-85f0-26bb76e33228"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [
                        4000
                    ],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "NOTES",
                    "order": 11,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "8982322e-8189-4f23-8f5f-6ec19e158ce3"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "TENANT_ID",
                    "order": 12,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "76702813-9b32-4eea-8ade-b082d19d99e0"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "ENVIRONMENT_ID",
                    "order": 13,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "e34761bc-63a7-404a-b695-169bbb5c8ffd"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 104,
                    "driver_data_type_name": "uniqueidentifier",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "APPLICATION_ID",
                    "order": 14,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "87a2ea20-1ec8-4497-83cc-7ffb426cb357"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [
                        100
                    ],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "RECORD_VERSION",
                    "order": 15,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "ec60b26d-5d18-4e6f-a3e4-0bf6dff67a22"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 153,
                    "driver_data_type_name": "text",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "JSON_HISTORY",
                    "order": 16,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "1eab9c7b-bc68-4052-97f4-47864adf07c2"
                },
                {
                    "comment": null,
                    "default": null,
                    "driver_data_type_id": 97,
                    "driver_data_type_name": "nvarchar",
                    "driver_data_type_params": [],
                    "duplicated_from_column_uuid": null,
                    "is_auto_increment": false,
                    "is_index": false,
                    "is_nullable": false,
                    "is_primary_key": false,
                    "is_unique_key": false,
                    "is_unsigned": false,
                    "name": "CHECK_SUM",
                    "order": 17,
                    "table_uuid": "e24f4949-a242-4236-b505-2a83a5de1f03",
                    "uuid": "b10a34a1-f836-433f-a90f-cc7a46c21fa8"
                }
            ],
            "indexes": []
        }
    ],
    "relationships": {
        "0f5aad39-dd0e-4fed-8b5e-d674e64eff78": {
            "uuid": "0f5aad39-dd0e-4fed-8b5e-d674e64eff78",
            "source_column_uuid": "e3fbe39b-bb1b-45c8-a591-7004a9e5b370",
            "target_column_uuid": "7632c05e-42b6-424e-b94b-6bdc65d8f62c",
            "type": "many-to-one",
            "name": null
        },
        "36fb419c-1c2a-4046-b9bc-04ba850acfcc": {
            "uuid": "36fb419c-1c2a-4046-b9bc-04ba850acfcc",
            "source_column_uuid": "d497f842-145f-41b3-90b8-d799732a007a",
            "target_column_uuid": "5aecb150-8d27-4916-bdcb-4ea4bb4b3696",
            "type": "many-to-one",
            "name": null
        },
        "98ff8eb8-ed76-42f1-bea8-b7d3e11c58e3": {
            "uuid": "98ff8eb8-ed76-42f1-bea8-b7d3e11c58e3",
            "source_column_uuid": "769b9943-1d1c-484f-a753-4477f9fa92cf",
            "target_column_uuid": "ba074119-657b-47ba-8c40-409b0ad8f0e0",
            "type": "many-to-one",
            "name": null
        }
    },
    "created_at": "2024-11-16T15:58:49+00:00",
    "schema_version": 2,
    "version": 2
}
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
