---
title: Find String Exactly Within Table
description: User-defined function to check if a string exists exactly within a delimited list of strings
category: string-manipulation/parsing
tags:
  - string-search
  - exact-match
  - delimiter
  - table-lookup
  - user-defined-function
related:
  - ../transformations/eliminate-string-within-string
  - ../validation/string-is-empty
---

# Find String Exactly Within Table of Strings

Consider the following scenario where you want to check if a specific string exists exactly within a table of strings, using a specified delimiter. This function will return `true` if the string is found exactly as specified, and `false` otherwise.

```PowerFx
fxFun_ContainsExactString(
        TextToFind:Text, 
        TextToFindIn:Text, 
        DelimiterValue:Text):Boolean = (
    CountRows(
        Filter(
            ForAll(
                Split(TextToFindIn, DelimiterValue) As myRecord, 
                TextToFind = myRecord.Value
            ), 
            Value = true
        )
    ) > 0
);
```