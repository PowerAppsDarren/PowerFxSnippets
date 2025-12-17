---
title: "Sample Data: Person Records (Large)"
description: "Large dataset of person records with extensive identity and security fields"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - people
  - identity
  - large-dataset
difficulty: intermediate
products:
  - power-apps-canvas
  - power-bi
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A large-scale person dataset with extensive identity information including secure fields like passwords, hashes, and base64-encoded images. Ideal for testing with larger data volumes and complex data types.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| Identifier | Number | Sequential identifier |
| GUID | GUID | Unique identifier |
| FirstName | Text | Person's first name |
| LastName | Text | Person's last name |
| EmailAddress | Text | Primary email |
| AlternateEmail | Text | Secondary email |
| PhoneNumber | Text | Phone with country code |
| ImageURL | URL | Link to placeholder image |
| Base64ImageURL | Text | Base64-encoded image data |
| BirthDate | DateTime | Date of birth |
| IsManager | Boolean | Manager status |
| IsAdmin | Boolean | Admin status |
| Notes | Text | Additional notes |
| PassPhrase | Text | Sample passphrase hash |
| Password | Text | Sample password (mock data) |
| CountryCode | Text | Two-letter country code |

## Use Cases

- Performance testing with large datasets
- Testing image display from base64
- Building user profile applications
- Testing authentication UI components
- Demonstrating data pagination

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Size**: ~14 MB
- **Rows**: 50,000+

## Sample Power Fx Usage

```powerfx
// Display base64 image
Image(LookUp(colPersons, Identifier = 1).Base64ImageURL)

// Filter by country
Filter(colPersons, CountryCode = "US")

// Search by name
Search(colPersons, txtSearch.Text, "FirstName", "LastName")

// Get admins only
Filter(colPersons, IsAdmin = true)
```

## Performance Considerations

Due to the large size of this dataset:
- Consider using delegation with data sources
- Implement pagination for galleries
- Use local caching strategies
- Limit columns loaded when possible

## Security Note

All passwords, hashes, and security tokens in this dataset are mock data generated for testing purposes. Never use real credentials in sample data files.
