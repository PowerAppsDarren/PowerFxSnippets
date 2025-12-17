---
title: "Sample Data: Countries List"
description: "Complete list of world countries with ISO codes"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - countries
  - geography
  - iso-codes
difficulty: beginner
products:
  - power-apps-canvas
  - power-bi
author: "PowerAppsDarren"
source: "https://github.com/stefangabos/world_countries"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A comprehensive list of world countries with their ISO alpha-2 and alpha-3 codes. Essential for building internationalized applications, dropdowns, and data validation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| id | Number | Numeric country code (ISO 3166-1) |
| alpha2 | Text | Two-letter country code (e.g., "us") |
| alpha3 | Text | Three-letter country code (e.g., "usa") |
| name | Text | Full country name |

## Use Cases

- Country selection dropdowns
- Data validation for country fields
- Internationalization (i18n) implementations
- Geographic filtering and grouping
- Address form components

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: ~200 countries

## Sample Power Fx Usage

```powerfx
// Country dropdown
Items: SortByColumns(colCountries, "name", SortOrder.Ascending)

// Get country name from code
LookUp(colCountries, alpha2 = "us").name  // Returns "United States"

// Search countries
Filter(colCountries, txtSearch.Text in name)

// Get alpha2 from alpha3
LookUp(colCountries, alpha3 = "usa").alpha2  // Returns "us"
```

## Building a Country Picker

```powerfx
// ComboBox Items
SortByColumns(colCountries, "name")

// Display Template
ThisItem.name & " (" & Upper(ThisItem.alpha2) & ")"

// Selected Value
cbCountry.Selected.alpha2
```

## Combining with Other Data

```powerfx
// Join with other datasets
AddColumns(
    colEmployees,
    "CountryName",
    LookUp(colCountries, Upper(alpha2) = ThisRecord.CountryCode).name
)
```

## External Resources

- [ISO 3166-1 Standard](https://www.iso.org/iso-3166-country-codes.html)
- [World Countries GitHub](https://github.com/stefangabos/world_countries)
