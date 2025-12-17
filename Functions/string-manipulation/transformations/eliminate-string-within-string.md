---
title: Eliminate String Within String
description: User-defined function to remove a substring from within another string (case-insensitive)
category: string-manipulation/transformations
tags:
  - string-removal
  - substring
  - text-transformation
  - user-defined-function
related:
  - ../parsing/find-string-exactly-within-table
  - ../validation/string-is-empty
---

# Eliminate String Within String

This user-defined function will eliminate a string within another string. The function will return the source string with the string to eliminate removed. If the string to eliminate is not found, the source string is returned as is.

```PowerFx
    fx_Strings_EliminateString(SourceString:Text, ToEliminate:Text):Text = (
        With( 
            {
                myLenString: Len(ToEliminate),
                myScreenFound: Not IsBlank(
                    Find(
                        Upper(ToEliminate), 
                        Upper(SourceString)
                    )
                ), 
                myScreenPosition: Find(
                    Upper(ToEliminate), 
                    Upper(SourceString)
                )
            }, 
            If( 
                myScreenFound, 
                Concatenate(
                    Left(SourceString, myScreenPosition - 1), 
                    Mid(SourceString, myScreenPosition + myLenString)
                ), 
                SourceString
            ) // & "--" & myScreenPosition
        )
    );
```