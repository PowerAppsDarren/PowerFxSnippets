# People Sample Data

## Table of Contents

- [Contents](#contents)
- [Dataset Comparison](#dataset-comparison)
- [Common Fields](#common-fields)
- [Use Cases](#use-cases)
- [Quick Start](#quick-start)
- [Special Characters](#special-characters)
- [Performance Notes](#performance-notes)

Mock employee and person datasets for HR applications, directories, and testing.

## Contents

| File                  | Description                        | Rows    | Size    |
|-----------------------|------------------------------------|---------|---------|
| `employee-5k.csv`     | Comprehensive employee records     | 5,000   | ~1 MB   |
| `employeeinfo-5k.csv` | Basic employee information         | 5,000   | ~500 KB |
| `person.csv`          | Large person dataset with images   | 50,000+ | ~14 MB  |

## Dataset Comparison

| Feature       | employee-5k | employeeinfo-5k | person       |
|---------------|-------------|-----------------|--------------|
| Basic Info    | Yes         | Yes             | Yes          |
| Department    | Yes         | No              | No           |
| Boolean Flags | Yes         | No              | Yes          |
| Images        | No          | No              | Yes (Base64) |
| Notes         | Yes         | No              | Yes          |
| Size          | Medium      | Small           | Large        |

## Common Fields

All datasets include:
- Names (first, last, full)
- Email addresses
- Phone numbers

## Use Cases

- Employee directory applications
- HR management systems
- User profile displays
- Performance testing
- Form validation testing

## Quick Start

```powerfx
// Load employee data
ClearCollect(colEmployees, 'employee-5k')

// Filter by department
Filter(colEmployees, Department = "Engineering")

// Search by name
Search(colEmployees, txtSearch.Text, "FullName")
```

## Special Characters

The `employee-5k.csv` Notes field intentionally contains special characters for testing:
- Unicode characters
- Emojis
- Multi-language text
- Test strings

## Performance Notes

For the large `person.csv` dataset:
- Consider pagination
- Use local caching
- Implement search delegation
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
