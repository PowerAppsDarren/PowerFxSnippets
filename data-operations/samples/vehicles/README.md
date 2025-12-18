# Vehicle Sample Data

Automotive and fleet management sample datasets.

## Contents

| File           | Description                   | Rows    |
|----------------|-------------------------------|---------|
| `car-data.csv` | Comprehensive vehicle records | 50,000+ |
| `car-data.md`  | Dataset documentation         | -       |

## Dataset Features

The vehicle dataset includes:
- Make and model information
- VIN (Vehicle Identification Number)
- Model year (1957-2012 range)
- Color codes (hex format)
- Maintenance tracking
- Base64-encoded photos

## Car Makes Included

- American: Ford, Chevrolet, Chrysler, Buick, Dodge
- Japanese: Toyota, Honda, Nissan, Subaru, Lexus
- German: Mercedes-Benz, Audi, BMW
- Korean: Hyundai, Daewoo
- And many more...

## Use Cases

- Fleet management applications
- Car dealership inventory
- Vehicle maintenance tracking
- Automotive dashboards
- Color display demos

## Quick Start

```powerfx
// Load vehicle data
ClearCollect(colVehicles, 'car-data')

// Filter by make
Filter(colVehicles, CarMake = "Toyota")

// Show vehicles needing maintenance
Filter(colVehicles, NeedsMaintenance = true)

// Display body color
Rectangle.Fill: ColorValue(ThisItem.BodyColor)
```

## Related Schema

See `schemas/car-data-schema.json` for the Mockaroo schema used to generate this data.

## External Resources

- [Vehicle Make/Model Datasets](https://github.com/topics/make-model-year)
- [Kaggle Car Datasets](https://www.kaggle.com/datasets?search=cars)
