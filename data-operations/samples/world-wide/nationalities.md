---
title: "Sample Data: Nationalities List"
description: "List of nationality demonyms for international applications"
category: "data-management"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - nationalities
  - demonyms
  - international
difficulty: beginner
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
license: "MIT"
---

## Overview

A simple list of nationality demonyms (the terms used to describe people from specific countries). Useful for forms, profiles, and international applications.

## Columns

| Column      | Type | Description                                         |
|-------------|------|-----------------------------------------------------|
| Nationality | Text | Nationality demonym (e.g., "American", "British")   |

## Sample Entries

- Afghan
- Albanian
- American
- Australian
- British
- Canadian
- Chinese
- French
- German
- Indian
- Japanese
- Mexican
- And many more...

## Use Cases

- Profile form nationality dropdowns
- User registration forms
- HR applications
- Census or survey applications
- International user profiling

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: ~150 nationalities

## Sample Power Fx Usage

```powerfx
// Nationality dropdown
Items: Sort(colNationalities, Nationality)

// Search nationalities
Filter(colNationalities, StartsWith(Nationality, txtSearch.Text))

// Validate nationality input
If(
    txtNationality.Text in colNationalities.Nationality,
    "Valid",
    "Please select a valid nationality"
)
```

## Combining with Countries

Note: This file contains only nationality names. To map nationalities to countries, you may need to create a custom mapping table.

```powerfx
// Example mapping (manual)
Switch(
    selectedNationality,
    "American", "us",
    "British", "gb",
    "Canadian", "ca",
    // Add more mappings as needed
    ""
)
```
