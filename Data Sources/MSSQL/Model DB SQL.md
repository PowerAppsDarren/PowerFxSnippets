# NEW_TOPIC_GOES_HERE

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```tsql
CREATE TABLE "MANY2MANY_MAP"(
    "ID" BIGINT NOT NULL,
    "LEFT_ID" BIGINT NOT NULL,
    "RIGHT_ID" BIGINT NOT NULL
);

ALTER TABLE
    "MANY2MANY_MAP" ADD CONSTRAINT "many2many_map_id_primary" PRIMARY KEY("ID");

CREATE TABLE "MAIN_DETAILS"(
    "ID" BIGINT NOT NULL,
    "GUID" uniqueidentifier NOT NULL,
    "MAIN_TABLE_ID" BIGINT NOT NULL,
    "IS_ACTIVE" BIT NOT NULL,
    "IS_DELETED" BIT NOT NULL,
    "NAME" NVARCHAR(255) NOT NULL,
    "TITLE" NVARCHAR(255) NOT NULL,
    "CREATED_WHEN" DATETIME NOT NULL,
    "CREATED_BY" uniqueidentifier NOT NULL,
    "UPDATED_WHEN" DATETIME NOT NULL,
    "UPDATED_BY" uniqueidentifier NOT NULL,
    "NOTES" NVARCHAR(4000) NOT NULL,
    "TENANT_ID" uniqueidentifier NOT NULL,
    "ENVIRONMENT_ID" uniqueidentifier NOT NULL,
    "APPLICATION_ID" uniqueidentifier NOT NULL,
    "RECORD_VERSION" NVARCHAR(100) NOT NULL,
    "JSON_HISTORY" TEXT NOT NULL,
    "CHECK_SUM" NVARCHAR(255) NOT NULL
);

ALTER TABLE
    "MAIN_DETAILS" ADD CONSTRAINT "main_details_id_primary" PRIMARY KEY("ID");

CREATE INDEX "main_details_guid_index" ON
    "MAIN_DETAILS"("GUID");
CREATE TABLE "MANY2MANY_RIGHT"("ID" BIGINT NOT NULL);

ALTER TABLE
    "MANY2MANY_RIGHT" ADD CONSTRAINT "many2many_right_id_primary" PRIMARY KEY("ID");

CREATE TABLE "MANY2MANY_LEFT"("ID" BIGINT NOT NULL);

ALTER TABLE
    "MANY2MANY_LEFT" ADD CONSTRAINT "many2many_left_id_primary" PRIMARY KEY("ID");

CREATE TABLE "MAIN_TABLE"(
    "ID" BIGINT NOT NULL,
    "GUID" uniqueidentifier NOT NULL,
    "IS_ACTIVE" BIT NOT NULL,
    "IS_DELETED" BIT NOT NULL,
    "NAME" NVARCHAR(255) NOT NULL,
    "TITLE" NVARCHAR(255) NOT NULL,
    "CREATED_WHEN" DATETIME NOT NULL,
    "CREATED_BY" uniqueidentifier NOT NULL,
    "UPDATED_WHEN" DATETIME NOT NULL,
    "UPDATED_BY" uniqueidentifier NOT NULL,
    "NOTES" NVARCHAR(4000) NOT NULL,
    "TENANT_ID" uniqueidentifier NOT NULL,
    "ENVIRONMENT_ID" uniqueidentifier NOT NULL,
    "APPLICATION_ID" uniqueidentifier NOT NULL,
    "RECORD_VERSION" NVARCHAR(100) NOT NULL,
    "JSON_HISTORY" TEXT NOT NULL,
    "CHECK_SUM" NVARCHAR(255) NOT NULL
);

ALTER TABLE
    "MAIN_TABLE" ADD CONSTRAINT "main_table_id_primary" PRIMARY KEY("ID");

CREATE INDEX "main_table_guid_index" ON
    "MAIN_TABLE"("GUID");

ALTER TABLE
    "MAIN_TABLE" ADD CONSTRAINT "main_table_id_foreign" FOREIGN KEY("ID") REFERENCES "MAIN_DETAILS"("ID");

ALTER TABLE
    "MANY2MANY_MAP" ADD CONSTRAINT "many2many_map_left_id_foreign" FOREIGN KEY("LEFT_ID") REFERENCES "MANY2MANY_LEFT"("ID");
    
ALTER TABLE
    "MANY2MANY_MAP" ADD CONSTRAINT "many2many_map_right_id_foreign" FOREIGN KEY("RIGHT_ID") REFERENCES "MANY2MANY_RIGHT"("ID");
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
