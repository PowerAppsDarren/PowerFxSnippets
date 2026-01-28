---
title: "Sample Data: Employee Records (5K)"
description: "5,000 mock employee records with comprehensive HR data fields"
category: "data-management"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - employees
  - hr
  - human-resources
difficulty: beginner
products:
  - power-apps-canvas
  - power-automate
  - power-bi
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
license: "MIT"
---

## Overview

A comprehensive dataset of 5,000 mock employee records suitable for testing HR applications, demonstrating Power Apps capabilities, and building proof-of-concept solutions.

## Columns

| Column     | Type     | Description                                        |
|------------|----------|----------------------------------------------------|
| AutoNumber | Number   | Sequential record identifier                       |
| FullName   | Text     | Employee full name                                 |
| FirstName  | Text     | Employee first name                                |
| LastName   | Text     | Employee last name                                 |
| Email      | Text     | Work email address                                 |
| Role       | Text     | Job title/role                                     |
| Location   | Text     | Work location/city                                 |
| Salary     | Text     | Salary with currency code                          |
| Phone      | Text     | Phone number                                       |
| Department | Text     | Department name                                    |
| IsActive   | Boolean  | Active employee status                             |
| IsManager  | Boolean  | Manager status flag                                |
| IsAdmin    | Boolean  | Admin privileges flag                              |
| DOB        | DateTime | Date of birth                                      |
| Notes      | Text     | Additional notes (may contain special characters)  |

## Departments Included

- Product Management
- Research and Development
- Training
- Engineering
- Legal
- Marketing
- Sales
- Support
- Human Resources
- Accounting
- Services

## Use Cases

- Building employee directory apps
- Testing HR management solutions
- Demonstrating filtering and sorting
- Performance testing with medium datasets
- Building org chart visualizations
- Testing role-based access control

## File Details

- **Format**: CSV
- **Encoding**: UTF-8
- **Rows**: 5,000

## Sample Power Fx Usage

```powerfx
// Filter by department
Filter(colEmployees, Department = "Engineering")

// Find managers
Filter(colEmployees, IsManager = true)

// Search by name
Search(colEmployees, txtSearch.Text, "FullName", "Email")

// Group by department
GroupBy(colEmployees, "Department", "DeptEmployees")

// Calculate average salary (requires parsing)
Average(
    AddColumns(colEmployees, "SalaryNum", Value(Mid(Salary, 2)))
    .SalaryNum
)
```

## Special Characters Note

The Notes field intentionally contains various special characters including:
- Emojis
- Unicode characters
- SQL injection test strings
- Special punctuation
- Multi-language text

This is useful for testing input validation and display handling.
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
