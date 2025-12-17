---
title: String Is Empty
description: User-defined function to check if a string is empty or contains only whitespace
category: string-manipulation/validation
tags:
  - validation
  - empty-check
  - whitespace
  - IsBlank
  - user-defined-function
related:
  - ../transformations/eliminate-string-within-string
  - ../parsing/find-string-exactly-within-table
---

# String Is Empty

## Description

This function checks if a given string is empty or contains only whitespace characters. It returns `true` if the string is empty or consists solely of whitespace, and `false` otherwise.

```PowerFx
fxFun_StringIsEmpty(TextValue:Text):Boolean = (
    Len(Trim(TextValue)) = 0
    Or 
    IsBlank(TextValue)
);
```