# 538 Data Samples

Sample datasets and links from FiveThirtyEight, the statistical analysis and data journalism organization.

## Contents

| File | Description |
|------|-------------|
| `index.csv` | Index of available 538 datasets with URLs |
| `538-data.md` | Original overview documentation |
| `index.md` | Detailed dataset documentation |

## About FiveThirtyEight Data

FiveThirtyEight publishes open datasets related to:
- Political polling and elections
- Sports analytics
- Cultural and social trends
- Economic data

## Usage

The `index.csv` file provides links to datasets hosted on FiveThirtyEight's GitHub repository. Use it as a reference to download specific datasets for your Power Apps projects.

## Resources

- [FiveThirtyEight GitHub](https://github.com/fivethirtyeight/data)
- [ABC News 538](https://abcnews.go.com/538)

## Importing into Power Apps

```powerfx
// Load as a collection
ClearCollect(col538Index, '538-data-index')

// Launch dataset link
Launch(First(Filter(col538Index, subfolder_name = "pollster-ratings")).dataset_url)
```
