# App.Formulas - Power Fx Named Formulas and Functions

This directory contains reusable Power Fx formulas, functions, and type definitions for use in canvas Power Apps `App.Formulas` property.

## Directory Structure

```
formulas/
├── collections/           # Inline table collections and data arrays
├── expressions/           # Named formulas, constants, and simple expressions
├── user-defined-functions/ # User-Defined Functions (UDFs)
├── user-defined-types/    # User-Defined Types (UDTs)
└── assets/               # Images and supporting files
```

## Quick Reference

### Collections

Data collections that can be copied directly into App.Formulas for reference data.

| File                                                                                      | Title                           | Description                                                                                 | Difficulty |
|-------------------------------------------------------------------------------------------|---------------------------------|---------------------------------------------------------------------------------------------|------------|
| [color-enum-in-named-formula.md](collections/color-enum-in-named-formula.md)             | Color Enum in Named Formula     | A collection of all 140 web colors for use in App.Formulas                                 | beginner   |
| [icons-as-collection.md](collections/icons-as-collection.md)                             | Icon Enumeration to Collection  | Converts the standard Icon enumeration into a searchable, filterable collection with metadata | beginner   |
| [error-kinds.md](collections/error-kinds.md)                                              | Error Kinds Collection          | A collection of all standard Power Apps error kinds for reference and handling              | beginner   |
| [fxmenuitems.yaml](collections/fxmenuitems.yaml)                                          | Menu Items Collection           | A template collection for building custom navigation menus with role-based visibility       | beginner   |

### Expressions

Named formulas, constants, and simple expressions for common tasks.

| File                                                                          | Title                           | Description                                                                               | Difficulty   |
|-------------------------------------------------------------------------------|---------------------------------|-------------------------------------------------------------------------------------------|--------------|
| [boolean-is-in-studio-mode.md](expressions/boolean-is-in-studio-mode.md)     | Are We in Studio Mode?          | Determine if the app is running in Studio Mode (editing mode) to show/hide elements      | beginner     |
| [code-comments.md](expressions/code-comments.md)                              | Consistent Code Comment Decor   | Standardized code comment decorations for consistent documentation                        | beginner     |
| [control-constants.md](expressions/control-constants.md)                      | Helpful Constants               | A set of standard constants for spacing, screen defaults, and control properties          | beginner     |
| [doc-type-icons.md](expressions/doc-type-icons.md)                            | File Type Icons                 | Generate URLs for file type icons based on file extensions                                | beginner     |
| [fxexp-allcontrols.md](expressions/fxexp-allcontrols.md)                      | All Controls Expression         | A comprehensive table of all Power Apps controls with metadata                            | intermediate |
| [fxrootsharepointurl.yaml](expressions/fxrootsharepointurl.yaml)             | Root SharePoint URL Expression  | Expression to extract the root SharePoint URL from the current user's profile             | intermediate |
| [top-of-app-formulas.md](expressions/top-of-app-formulas.md)                  | Top of App Formulas             | Table of contents and naming guidelines for App.Formulas                                  | beginner     |

### User-Defined Functions (UDFs)

Reusable functions with parameters that can be called from anywhere in your app.

| File                                                                                  | Title                          | Description                                                                    | Difficulty   |
|---------------------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------|--------------|
| [fxfindproportionalvalue.md](user-defined-functions/fxfindproportionalvalue.md)      | Find Proportional Value        | Calculates a proportional value based on two related fractions                 | intermediate |
| [screen-transition-random.md](user-defined-functions/screen-transition-random.md)    | Random Screen Transition       | A function to return a random screen transition effect                         | beginner     |
| [regular-expressions.md](user-defined-functions/regular-expressions.md)              | Regular Expressions Collection | A collection of common regular expressions with a UDF lookup function          | intermediate |

### User-Defined Types (UDTs)

Custom type definitions for structured data in Power Fx.

| File                                                                            | Title                        | Description                                                               | Difficulty   |
|---------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------------------|--------------|
| [user-defined-types-syntax.md](user-defined-types/user-defined-types-syntax.md) | User Defined Types Syntax    | Examples of defining custom types (records and collections) in Power Fx  | intermediate |
| [user-defined-types.md](user-defined-types/user-defined-types.md)              | User-Defined Types Examples  | Comprehensive examples of UDT, Named Formulas, and UDF                    | advanced     |

## Usage

### How to Use These Snippets

1. Open your canvas Power App in Power Apps Studio
2. Select **App** in the Tree view
3. In the formula bar, find the **Formulas** property (or use `App.Formulas`)
4. Copy the relevant formula code from these files into your App.Formulas

### Naming Conventions

We recommend the following prefixes for organization:

| Type                  | Prefix                | Example                                          |
|-----------------------|-----------------------|--------------------------------------------------|
| Named Expression      | `fx`                  | `fxWebColors`                                    |
| User-Defined Function | `fxFun_` or `fx...()` | `fxFun_Calculate()` or `fxRandomScreenTransition()` |
| User-Defined Type     | `fxTyp_`              | `fxTyp_Customer`                                 |

### Prerequisites

- For UDFs and UDTs, ensure **User-defined functions** is enabled in Settings > Updates > Experimental
- Some expressions may require specific connectors (e.g., Office365Users)

## Related Resources

- [Power Fx Reference](https://learn.microsoft.com/en-us/power-platform/power-fx/overview)
- [User-Defined Types Documentation](https://powerplatformlinks.com/CanvasUserDefined)
