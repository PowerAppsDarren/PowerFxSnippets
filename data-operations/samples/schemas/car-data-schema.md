---
title: "Schema: Car Data Generation Schema"
description: "Mockaroo schema definition for generating car/vehicle sample data"
category: "data-operations"
subcategory: "samples"
tags:
  - schema
  - json
  - mockaroo
  - data-generation
  - vehicles
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A Mockaroo schema definition file that describes how to generate realistic vehicle data. This JSON file can be imported into Mockaroo.com to create custom car datasets.

## Schema Fields

| Field Name         | Mockaroo Type  | Description                                       |
|--------------------|----------------|---------------------------------------------------|
| uuid               | GUID           | Unique identifier                                 |
| status_code        | Custom List    | Status values: active, inactive, pending, retired |
| created_at         | Datetime       | Record creation timestamp                         |
| updated_at         | Datetime       | Last update timestamp                             |
| user_assigned_uuid | GUID           | Assigned user reference                           |
| notes              | Paragraphs     | Text notes                                        |
| demand             | Custom List    | Demand level: high, medium, low                   |
| category           | Custom List    | Vehicle category                                  |
| year               | Car Model Year | Vehicle year                                      |
| make               | Car Make       | Manufacturer                                      |
| model              | Car Model      | Model name                                        |
| vin                | Car VIN        | Vehicle ID number                                 |

## Vehicle Categories

The schema includes these vehicle categories:
- Economical
- Sport
- Luxury
- Van
- Truck
- Extra Large

## Use Cases

- Generating custom test datasets
- Understanding data structure for imports
- Recreating or extending the sample data
- Learning Mockaroo schema format

## Using the Schema

1. Go to [Mockaroo.com](https://mockaroo.com)
2. Click "Upload" or import JSON
3. Load the `car-data-schema.json` file
4. Adjust row count and format
5. Download generated data

## Sample Generated Output

```csv
uuid,status_code,created_at,updated_at,category,year,make,model,vin
abc-123,active,1/15/2020,3/20/2021,Sport,2019,Toyota,Camry,1HGBH41JXMN109186
```

## Related Files

- `vehicles/car-data.csv` - Generated using this schema
