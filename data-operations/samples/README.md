# Sample Data Catalog

A comprehensive collection of sample datasets for Power Apps development, testing, and demonstrations.

## Directory Structure

```
samples/
├── 538-data/           # FiveThirtyEight political/statistical data
├── jokes/              # Family-friendly joke collections
├── lorem-ipsum/        # Placeholder text samples
├── people/             # Employee and person datasets
├── schemas/            # Data generation schemas
├── vehicles/           # Automotive and fleet data
├── world-wide/         # Geographic reference data
└── all-kinds-of-data.csv  # Comprehensive multi-type dataset
```

## Dataset Overview

### By Category

| Category | Datasets | Best For |
|----------|----------|----------|
| People | 3 files | HR apps, directories, profiles |
| Geographic | 4 files | Internationalization, dropdowns |
| Vehicles | 1 file | Fleet management, inventory |
| Reference | 2 files | Political analysis, statistics |
| Entertainment | 2 files | Fun apps, demos |
| Utility | 1 file | Comprehensive testing |

### By Size

| Size | Datasets | Use Case |
|------|----------|----------|
| Small (<100 rows) | jokes, nationalities | Quick demos |
| Medium (100-5K rows) | countries, employees | Standard apps |
| Large (5K-50K rows) | person, car-data | Performance testing |
| Extra Large (50K+) | all-kinds-of-data | Stress testing |

## Quick Start Guide

### Loading Data in Power Apps

```powerfx
// Import CSV from SharePoint or other data source
ClearCollect(colData, 'your-data-source')

// Or use static data in App.Formulas
fxCountries = Table(
    {alpha2: "us", name: "United States"},
    {alpha2: "gb", name: "United Kingdom"}
    // ...
)
```

### Common Operations

```powerfx
// Search
Filter(colData, txtSearch.Text in ColumnName)

// Sort
SortByColumns(colData, "ColumnName", SortOrder.Ascending)

// Group
GroupBy(colData, "Category", "Items")

// Distinct values
Distinct(colData, ColumnName)
```

## Detailed Dataset Catalog

### 538-data/
Political and statistical reference data from FiveThirtyEight.
- `index.csv` - Dataset index with URLs

### jokes/
Entertainment datasets for fun applications.
- `dadjoke.csv` - ~100 family-friendly dad jokes

### lorem-ipsum/
Placeholder text for UI mockups.
- `readme.md` - Various Lorem Ipsum text samples

### people/
Employee and person mock data.
- `employee-5k.csv` - 5,000 employees with departments, roles
- `employeeinfo-5k.csv` - 5,000 basic employee records
- `person.csv` - 50,000+ person records with images

### schemas/
Data generation schemas for Mockaroo.
- `car-data-schema.json` - Vehicle data generator schema

### vehicles/
Automotive sample data.
- `car-data.csv` - 50,000+ vehicle records

### world-wide/
Geographic reference data.
- `countries.csv` - ~200 sovereign nations with ISO codes
- `nationalities.csv` - ~150 nationality demonyms
- `world.csv` - ~250 countries and territories
- `world-cities.md` - 100 major world cities

### Root Files
- `all-kinds-of-data.csv` - Comprehensive multi-type dataset (~40K rows)
- `data-samples.md` - Original data source links

## Data Formats

All CSV files use:
- **Encoding**: UTF-8
- **Delimiter**: Comma (,)
- **Headers**: First row

## External Data Sources

Looking for more data? Check these resources:

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [World Bank Data Catalog](https://datacatalog.worldbank.org)
- [Data.gov](https://data.gov)
- [FiveThirtyEight Data](https://github.com/fivethirtyeight/data)

## Contributing

To add new sample datasets:
1. Add CSV file to appropriate subdirectory
2. Create companion .md file with documentation
3. Update subdirectory README.md
4. Update this catalog

## License

Sample data in this repository is provided for educational and testing purposes. Check individual datasets for specific licensing terms.

---

## Free Community & Course Materials

Get access to our free Power Apps crash course (and our community):
- https://tinyurl.com/DarrensStuffFree

## Support

If you need help with Power Platform:
- Email: support@superpowerlabs.co
- Links: https://powerplatformlinks.com

## Disclaimer

THIS DATA IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND. All data is mock/synthetic and should not be used for real-world decision making.
