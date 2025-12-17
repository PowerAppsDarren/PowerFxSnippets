---
title: "Sample Data: Vehicle/Car Records"
description: "Comprehensive vehicle dataset with make, model, VIN, and maintenance data"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - vehicles
  - cars
  - automotive
  - fleet-management
difficulty: beginner
products:
  - power-apps-canvas
  - power-bi
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A comprehensive vehicle dataset containing car records with make, model, year, VIN, colors, and maintenance tracking information. Perfect for building fleet management, inventory, or automotive applications.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| UUID | GUID | Unique vehicle identifier |
| CarModelYear | Number | Model year (1957-2012 range) |
| CarMake | Text | Manufacturer (Audi, Toyota, Ford, etc.) |
| CarModel | Text | Model name |
| CarVIN | Text | Vehicle Identification Number |
| BodyColor | Text | Exterior color (hex code) |
| InteriorColor | Text | Interior color (hex code) |
| NeedsMaintenance | Boolean | Maintenance required flag |
| LastMaintenance | Date | Date of last maintenance |
| PhotoBase64 | Text | Base64-encoded vehicle photo |

## Car Makes Included

- Audi, Toyota, Scion, Dodge, Chrysler
- Hyundai, Daewoo, Acura, Ford, Chevrolet
- Mercedes-Benz, Infiniti, Nissan, Subaru
- Buick, Lexus, and many more

## Use Cases

- Fleet management applications
- Car dealership inventory systems
- Vehicle maintenance tracking
- Automotive data visualization
- Color picker demonstrations (using hex codes)
- Image display from base64 encoding

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Size**: ~10 MB
- **Rows**: 50,000+

## Sample Power Fx Usage

```powerfx
// Filter cars needing maintenance
Filter(colCarData, NeedsMaintenance = true)

// Find by make
Filter(colCarData, CarMake = "Toyota")

// Display body color
Rectangle.Fill: ColorValue(ThisItem.BodyColor)

// Cars by year
Filter(colCarData, CarModelYear >= 2010)

// Sort by last maintenance
SortByColumns(colCarData, "LastMaintenance", SortOrder.Ascending)

// Search by VIN
Filter(colCarData, txtSearch.Text in CarVIN)
```

## Building a Fleet Dashboard

```powerfx
// Count by maintenance status
CountIf(colCarData, NeedsMaintenance = true) & " vehicles need service"

// Group by make
GroupBy(colCarData, "CarMake", "Vehicles")

// Calculate fleet age
Average(
    AddColumns(colCarData, "Age", Year(Today()) - CarModelYear)
    .Age
)
```

## Related Schema

See `schemas/car-data-schema.json` for the Mockaroo schema used to generate this data.
