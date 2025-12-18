# Data Schemas

Schema definitions used to generate sample datasets.

## Contents

| File                   | Description                       |
|------------------------|-----------------------------------|
| `car-data-schema.json` | Mockaroo schema for vehicle data  |
| `car-data-schema.md`   | Schema documentation              |

## About Mockaroo

[Mockaroo](https://mockaroo.com) is a powerful mock data generator that supports:
- 150+ data types
- Custom field definitions
- Multiple export formats
- Schema import/export

## Using Schema Files

1. Go to [Mockaroo.com](https://mockaroo.com)
2. Import the JSON schema
3. Customize row count and settings
4. Download generated data

## Creating Custom Schemas

To create your own schema:
```json
{
  "name": "My Dataset",
  "num_rows": 1000,
  "file_format": "csv",
  "columns": [
    {
      "name": "id",
      "type": "Row Number"
    },
    {
      "name": "name",
      "type": "Full Name"
    }
  ]
}
```

## Common Mockaroo Types

- `GUID` - Unique identifiers
- `Full Name` - Person names
- `Email Address` - Valid emails
- `Phone` - Phone numbers
- `Car Make`, `Car Model`, `Car VIN` - Vehicle data
- `Custom List` - Your own values
