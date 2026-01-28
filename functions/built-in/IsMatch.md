---
title: "IsMatch Function - Time Validation Pattern"
description: "Regular expression pattern for validating 12-hour time format with AM/PM using IsMatch function"
category: "business-logic"
subcategory: "built-in-functions"
tags:
  - ismatch
  - regex
  - validation
  - time-format
  - pattern-matching
difficulty: intermediate
products:
  - power-apps-canvas
author: "Unknown"
created: 2026-01-26
updated: 2026-01-26
license: "MIT"
---
# IsMatch

## Table of Contents

- [Add This to Your Application](#add-this-to-your-application)

This is some YAML you can paste into your canvas Power Apps applciation that will

## Add This to Your Application

```PowerFx
IsMatch(
    txtTime.Value,
    "^(0?[1-9]|1[0-2]):[0-5][0-9](./\s)?(AM|PM)$",
    MatchOptions.Complete
)
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
