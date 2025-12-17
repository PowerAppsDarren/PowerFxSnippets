---
title: "Sample Data: World Countries (Complete)"
description: "Extended world countries list including territories and special regions"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - countries
  - territories
  - geography
  - iso-codes
difficulty: beginner
products:
  - power-apps-canvas
  - power-bi
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

An extended world countries list that includes not just sovereign nations but also territories, special administrative regions, and other geographic entities with ISO codes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| id | Number | Numeric ISO code |
| alpha2 | Text | Two-letter code |
| alpha3 | Text | Three-letter code |
| name | Text | Full name |

## Difference from countries.csv

This file (`world.csv`) includes additional entries such as:
- Aland Islands
- American Samoa
- Anguilla
- Antarctica
- Aruba
- And other territories/dependencies

## Use Cases

- Comprehensive geographic selection
- Shipping destination lists
- Tax jurisdiction identification
- Complete ISO code reference
- Regulatory compliance applications

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: ~250 entries

## Sample Power Fx Usage

```powerfx
// All geographic entities
SortByColumns(colWorld, "name")

// Filter for specific regions
Filter(colWorld, id >= 1 And id <= 100)

// Search including territories
Search(colWorld, txtSearch.Text, "name")
```

## When to Use Which File

| Scenario | Recommended File |
|----------|------------------|
| Country of citizenship | countries.csv |
| Shipping destinations | world.csv |
| Political analysis | countries.csv |
| Complete ISO reference | world.csv |
| Simplified UI | countries.csv |
