---
title: "Sample Data: All Kinds of Data"
description: "Comprehensive sample dataset with diverse data types for testing Power Apps applications"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - comprehensive
  - testing
  - diverse-types
difficulty: beginner
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A large, comprehensive sample dataset containing various data types commonly encountered in enterprise applications. This dataset is ideal for testing data binding, filtering, sorting, and display scenarios in Power Apps.

## Columns

| Column           | Type     | Description                             |
|------------------|----------|-----------------------------------------|
| AutoId           | GUID     | Auto-generated unique identifier        |
| uuid             | GUID     | Universally unique identifier           |
| email            | Text     | Email address                           |
| ipAddress        | Text     | IP address (v4)                         |
| pw               | Text     | Sample password string                  |
| hash             | Text     | Bcrypt hash value                       |
| lipsum           | Text     | Lorem ipsum placeholder text            |
| buzzword         | Text     | Business buzzword                       |
| Latitude         | Number   | Geographic latitude coordinate          |
| longitude        | Number   | Geographic longitude coordinate         |
| ApplicationName  | Text     | Random application name                 |
| AnimalCommon     | Text     | Common animal name                      |
| AnimalScientific | Text     | Scientific animal name                  |
| City             | Text     | City name                               |
| Country          | Text     | Country name                            |
| Choices          | Text     | Sample choices field                    |
| NatoPhonetic     | Text     | NATO phonetic alphabet string           |
| ccNumbers        | Text     | Sample credit card numbers (test data)  |
| color            | Text     | Color name                              |
| sequence         | Text     | Sequence identifier                     |
| domain           | Text     | Domain name                             |
| dateTime         | DateTime | Date and time value                     |
| ip4              | Text     | IPv4 address                            |
| ip6              | Text     | IPv6 address                            |
| jsonArray        | Text     | JSON array string                       |
| scenario         | Text     | Test scenario description               |

## Use Cases

- Testing data type handling in Power Apps galleries and forms
- Demonstrating diverse column types in Power Fx formulas
- Performance testing with large datasets
- Training and educational scenarios
- Prototyping data-driven applications

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Size**: ~6.5 MB
- **Approximate Rows**: 40,000+

## Sample Power Fx Usage

```powerfx
// Filter by country
Filter(colAllKindsOfData, Country = "United States")

// Search across multiple text fields
Search(colAllKindsOfData, txtSearch.Text, "City", "Country", "email")

// Sort by date
SortByColumns(colAllKindsOfData, "dateTime", SortOrder.Descending)
```

## Notes

- Contains mock/synthetic data for testing purposes only
- Credit card numbers are generated test data, not real
- Passwords and hashes are sample data, not for production use
