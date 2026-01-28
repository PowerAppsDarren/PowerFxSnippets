---
title: "Sample Data: Employee Info (5K)"
description: "5,000 basic employee information records for testing"
category: "data-management"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - employees
  - basic-info
difficulty: beginner
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
license: "MIT"
---

## Overview

A streamlined dataset of 5,000 employee records with essential information fields. This is a lighter version suitable for quick testing and simpler application scenarios.

## Columns

| Column     | Type   | Description                          |
|------------|--------|--------------------------------------|
| AutoNumber | Number | Sequential record identifier         |
| Name       | Text   | Full name combined                   |
| FirstName  | Text   | Employee first name                  |
| LastName   | Text   | Employee last name                   |
| Email      | Text   | Email address                        |
| Role       | Text   | Job title                            |
| Location   | Text   | Work location                        |
| Salary     | Text   | Salary amount with currency symbol   |
| Phone      | Text   | Phone number                         |

## Use Cases

- Quick employee directory prototypes
- Testing form inputs and validation
- Demonstrating collection operations
- Simple search and filter demos
- Testing data import scenarios

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: 5,000

## Sample Power Fx Usage

```powerfx
// Simple name search
Filter(colEmployeeInfo, txtSearch.Text in Name)

// Sort by salary (requires parsing)
SortByColumns(
    AddColumns(colEmployeeInfo, "SalaryNum", Value(Substitute(Mid(Salary, 2), ",", ""))),
    "SalaryNum",
    SortOrder.Descending
)

// Distinct roles
Distinct(colEmployeeInfo, Role)

// Count by location
GroupBy(colEmployeeInfo, "Location", "Employees")
```

## Comparison with employee-5k.csv

| Feature       | employee-5k.csv | employeeinfo-5k.csv |
|---------------|-----------------|---------------------|
| Columns       | 15              | 9                   |
| Department    | Yes             | No                  |
| Boolean Flags | Yes             | No                  |
| Notes Field   | Yes             | No                  |
| DOB           | Yes             | No                  |
| File Size     | Larger          | Smaller             |

Use this dataset when you need a lighter-weight option for testing.
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
