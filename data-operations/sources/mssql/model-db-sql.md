---
title: "Model Database SQL Schema"
description: "SQL CREATE TABLE statements for a model database schema with main tables, details, and many-to-many relationships for Power Apps data sources"
category: "data-operations"
subcategory: "mssql"
tags:
  - data
  - sql
  - schema
  - database
  - relationships
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

# Model Database SQL Schema

## Table of Contents

- [Add This to Your Application](#add-this-to-your-application)

This snippet provides SQL CREATE TABLE statements for a model database schema, including main tables, detail tables, and many-to-many mapping tables suitable for Power Apps data sources.

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
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
