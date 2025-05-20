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