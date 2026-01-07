# String Manipulation Functions

Power Fx user-defined functions for string manipulation, parsing, validation, and formatting.

## Categories

### [Padding](./padding)

Functions for padding and formatting numbers within strings.

| File | Description |
|------|-------------|
| [padd-numbers-inside-string.md](padding/padd-numbers-inside-string.md) | Collection of functions for extracting, padding, and formatting numbers embedded in strings |

### [Transformations](./transformations)

Functions for modifying and transforming string content.

| File | Description |
|------|-------------|
| [eliminate-string-within-string.md](transformations/eliminate-string-within-string.md) | Remove a substring from within another string (case-insensitive) |

### [Parsing](./parsing)

Functions for parsing, splitting, and searching within strings.

| File | Description |
|------|-------------|
| [find-string-exactly-within-table.md](parsing/find-string-exactly-within-table.md) | Check if a string exists exactly within a delimited list |

### [Validation](./validation)

Functions for validating string content and format.

| File | Description |
|------|-------------|
| [string-is-empty.md](validation/string-is-empty.md) | Check if a string is empty or whitespace-only |

## Quick Reference

### Padding Functions

```powerfx
// Pad numbers in string
fxPadNumbers(StringValue:Text):Text

// Get position of first numeric character
fxGetNumericPosition(StringValue:Text):Number

// Extract before, number, and after portions
fxGetBeforeDuringAfterNumeric(StringValue:Text):fxNumericHandlingType

// Format number as text with pattern
fxFormatNumberAsText(NumberString:Text):Text
```

### Transformation Functions

```powerfx
// Remove substring from string (case-insensitive)
fx_Strings_EliminateString(SourceString:Text, ToEliminate:Text):Text
```

### Parsing Functions

```powerfx
// Check exact string match in delimited list
fxFun_ContainsExactString(TextToFind:Text, TextToFindIn:Text, DelimiterValue:Text):Boolean
```

### Validation Functions

```powerfx
// Check if string is empty or whitespace
fxFun_StringIsEmpty(TextValue:Text):Boolean
```

## Related Resources

- [Power Fx Functions Reference](https://learn.microsoft.com/power-platform/power-fx/reference/function-reference)
- [Text Functions in Power Fx](https://learn.microsoft.com/power-platform/power-fx/reference/function-text)

---

*Merged from `string-manipulation/` and `text-manipulation/` directories*
