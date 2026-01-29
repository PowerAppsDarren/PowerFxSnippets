# Power Fx Gotchas

## Table of Contents

- [Date & Time Formatting](#date-time-formatting)
  - [⚠️ CRITICAL: `m`/`mm` is Context-Sensitive!](#critical-mmm-is-context-sensitive)
  - [Month Formats](#month-formats)
  - [Day Formats](#day-formats)
  - [Time Formats](#time-formats)
  - [Year Formats](#year-formats)
  - [Working Examples](#working-examples)
  - [Inside String Interpolation](#inside-string-interpolation)
- [More Gotchas](#more-gotchas)

> **Purpose:** Document Power Fx behaviors that differ from common assumptions (Excel, JavaScript, .NET, etc.). This file helps AI assistants and developers avoid incorrect assumptions.

📚 **Official Documentation:** https://learn.microsoft.com/en-us/power-platform/power-fx/overview

🔍 **To verify syntax:** Use `ref_search_documentation` with query like "Power Fx Text function" then `ref_read_url` on the result.

---

## Date & Time Formatting

Power Fx date formatting is **NOT the same as .NET/C#**. Many uppercase formats that work in .NET **do not exist** in Power Fx.

### ⚠️ CRITICAL: `m`/`mm` is Context-Sensitive!

The `m` and `mm` placeholders mean **different things** depending on position:

| Position in Format String | Meaning | Example |
|---------------------------|---------|---------|
| After `h` or `hh` | **Minutes** | `"hh:mm"` → `"02:30"` |
| Before `ss` | **Minutes** | `"mm:ss"` → `"30:45"` |
| Anywhere else | **Month** | `"mm/dd"` → `"12/18"` |

```powerfx
// Same placeholder, different meaning!
Text(Now(), "mm/dd/yyyy")      // mm = MONTH  → "12/18/2025"
Text(Now(), "hh:mm AM/PM")     // mm = MINUTES → "02:30 PM"
Text(Now(), "hh:mm:ss")        // mm = MINUTES → "02:30:45"
```

This is VERY different from .NET where `M` = month and `m` = minutes (always).

### Month Formats

| Format   | Power Fx Result | Notes                          |
|----------|-----------------|--------------------------------|
| `m`      | `1` - `12`      | Month number (no leading zero) |
| `mm`     | `01` - `12`     | Month number (with leading zero) |
| `mmm`    | `Jan` - `Dec`   | Month abbreviation             |
| `mmmm`   | `January`...    | Full month name                |
| `MMM`    | **ERROR**       | Does NOT exist in Power Fx     |
| `MMMM`   | **ERROR**       | Does NOT exist in Power Fx     |

### Day Formats

| Format   | Power Fx Result | Notes                        |
|----------|-----------------|------------------------------|
| `d`      | `1` - `31`      | Day number (no leading zero) |
| `dd`     | `01` - `31`     | Day number (with leading zero) |
| `ddd`    | `Mon` - `Sun`   | Day abbreviation             |
| `dddd`   | `Monday`...     | Full day name                |

### Time Formats

| Format   | Power Fx Result | Notes                           |
|----------|-----------------|--------------------------------|
| `h`      | `1` - `12`      | Hour 12-hour (no leading zero) |
| `hh`     | `01` - `12`     | Hour 12-hour (with leading zero) |
| `H`      | `0` - `23`      | Hour 24-hour (no leading zero) |
| `HH`     | `00` - `23`     | Hour 24-hour (with leading zero) |
| `ss`     | `00` - `59`     | Seconds                        |
| `AM/PM`  | `AM` or `PM`    | Meridiem indicator             |

### Year Formats

| Format   | Power Fx Result | Notes            |
|----------|-----------------|------------------|
| `yy`     | `25`            | 2-digit year     |
| `yyyy`   | `2025`          | 4-digit year     |

### Working Examples

```powerfx
// ✅ CORRECT - These work in Power Fx
Text(Now(), "mm/dd/yyyy")              // "12/18/2025"
Text(Now(), "mmm dd, yyyy")            // "Dec 18, 2025"
Text(Now(), "mmmm d, yyyy")            // "December 18, 2025"
Text(Now(), "dddd, mmmm d, yyyy")      // "Wednesday, December 18, 2025"
Text(Now(), "hh:mm:ss AM/PM")          // "02:30:45 PM"
Text(Now(), "mm/dd/yyyy hh:mm AM/PM")  // "12/18/2025 02:30 PM"

// ❌ WRONG - These cause errors in Power Fx
Text(Now(), "MMM dd, yyyy")            // ERROR - MMM doesn't exist
Text(Now(), "MMMM d, yyyy")            // ERROR - MMMM doesn't exist
Text(Now(), "MM/DD/YYYY")              // ERROR - uppercase doesn't work
```

### Inside String Interpolation

When using `$"..."` syntax, escape quotes by doubling them:

```powerfx
// Inside $"..." - double the quotes
$"Date: {Text(Now(), ""mmm dd, yyyy"")}"

// Outside $"..." - single quotes work
"Date: " & Text(Now(), "mmm dd, yyyy")
```

---

## More Gotchas

*Add more Power Fx-specific behaviors here as they're discovered.*

---

## History

| Date       | Author          | Changes                                                        |
|------------|-----------------|----------------------------------------------------------------|
| 2026-01-29 | Darren          | Restored to public repo from private repo                      |
| 2025-12-18 | Claude Opus 4.5 | Added m/mm context-sensitivity rule, official docs link        |
| 2025-12-18 | Claude Opus 4.5 | Created with date formatting rules                             |
