---
title: "Sample Data: FiveThirtyEight Data Index"
description: "Index of FiveThirtyEight (538) open datasets for political and statistical analysis"
category: "data-operations"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - politics
  - statistics
  - fivethirtyeight
  - 538
difficulty: intermediate
products:
  - power-apps-canvas
  - power-bi
author: "PowerAppsDarren"
source: "https://github.com/fivethirtyeight/data"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

An index file cataloging available datasets from FiveThirtyEight (538), the statistical analysis and data journalism organization. This index provides links to various political, sports, and cultural datasets available in their GitHub repository.

## Columns

| Column         | Type | Description                                         |
|----------------|------|-----------------------------------------------------|
| subfolder_name | Text | Name of the dataset subfolder in the 538 GitHub repo|
| dataset_url    | URL  | Direct link to the dataset on GitHub                |
| article_url    | URL  | Link to the associated 538 article                  |

## Available Datasets

The index includes links to datasets covering:
- **Pollster Ratings**: Quality assessments of political pollsters
- **Election Data**: Primary results, delegate counts, and more
- **Congress Demographics**: Congressional voting patterns and member data
- **World Cup 2022**: Soccer predictions and results
- **District Urbanization**: Urban/rural classification of congressional districts
- **Cabinet Turnover**: Presidential cabinet appointment data

## Use Cases

- Building political analysis dashboards
- Creating data journalism projects
- Educational demonstrations of statistical concepts
- Combining multiple 538 datasets for deeper analysis
- Teaching polling methodology and accuracy

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: ~100 dataset references

## Sample Power Fx Usage

```powerfx
// Launch dataset in browser
Launch(First(Filter(col538Index, subfolder_name = "pollster-ratings")).dataset_url)

// Filter for election-related datasets
Filter(col538Index, "election" in LowerCase(subfolder_name))
```

## External Resources

- [FiveThirtyEight GitHub Repository](https://github.com/fivethirtyeight/data)
- [ABC News 538 Section](https://abcnews.go.com/538)

## Notes

- Data is sourced from FiveThirtyEight's open data initiative
- Some datasets may require additional context from associated articles
- URLs may change; verify links before production use
