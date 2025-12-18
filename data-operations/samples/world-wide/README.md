# World-Wide Sample Data

Geographic reference data including countries, nationalities, and cities.

## Contents

| File                | Description                                | Rows       |
|---------------------|--------------------------------------------|------------|
| `countries.csv`     | ISO country codes (sovereign nations)      | ~200       |
| `nationalities.csv` | Nationality demonyms                       | ~150       |
| `world.csv`         | Extended countries (including territories) | ~250       |
| `world-cities.md`   | World cities in Power Fx format            | 100 cities |

## Dataset Comparison

| Feature           | countries.csv | world.csv  |
|-------------------|---------------|------------|
| Sovereign Nations | Yes           | Yes        |
| Territories       | No            | Yes        |
| Dependencies      | No            | Yes        |
| Use Case          | Citizenship   | Shipping   |

## Data Fields

### Countries/World
- `id` - Numeric ISO code
- `alpha2` - Two-letter code (us, gb, fr)
- `alpha3` - Three-letter code (usa, gbr, fra)
- `name` - Full country name

### Nationalities
- `Nationality` - Demonym (American, British, French)

### World Cities
- Power Fx formatted data
- Includes: City, Country, Continent, Area, Density, Population

## Quick Start

```powerfx
// Country dropdown
Items: Sort(colCountries, name)

// Get country from code
LookUp(colCountries, alpha2 = "us").name

// Nationality picker
Items: Sort(colNationalities, Nationality)
```

## External Sources

- [ISO 3166 Standard](https://www.iso.org/iso-3166-country-codes.html)
- [World Countries GitHub](https://github.com/stefangabos/world_countries)
- [World Bank Data Catalog](https://datacatalog.worldbank.org)
