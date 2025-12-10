# Super Input Control (cmp_Input)

A versatile, morphing Power Apps input component that adapts to different input types while maintaining consistent styling and validation behavior.

## Description

This component provides a unified interface for single line text, multiline text, dropdown, and date picker inputs. It features built-in required field validation with visual feedback, spell checking capabilities, and comprehensive theming options.

## Features

- **Morphing Input Types**: Single control that switches between text, multiline text, dropdown, and date picker
- **Required Field Validation**: Visual border color changes when required fields are empty
- **Spell Check Support**: Built-in spell checking for text inputs
- **Customizable Theming**: Comprehensive color, font, and border styling options
- **Display Modes**: Supports Edit, View, and Disabled states
- **Reset Capability**: Programmatically reset input values
- **Drop Shadow**: Optional shadow effect for visual depth
- **Hover States**: Interactive hover effects for better UX
- **Accessibility**: Includes accessible labels and tooltips
- **Output Property**: Single `aValue` property returns the current value regardless of input type

## Supported Input Types

Configure the component using the `InputType` property:

| Code | Type | Description |
|------|------|-------------|
| `txt` | Single Line Text | Standard text input for single line entries |
| `txtx` | Multi-line Text | Expandable text area for longer content |
| `drp` | Dropdown | Selection list with customizable items |
| `dte` | Date Picker | Calendar-based date selection |

## Custom Properties

### Core Configuration

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `InputType` | Text | `"txt"` | Input type: `txt`, `txtx`, `drp`, or `dte` |
| `FieldName` | Text | `"Field Name"` | Label text displayed above the input |
| `HintText` | Text | `""` | Placeholder text shown in empty text inputs |
| `Tooltip` | Text | `""` | Tooltip text for accessibility and guidance |
| `DisplayMode` | Text | `"Edit"` | Control mode: `"Edit"`, `"View"`, or `"Disabled"` |
| `Required` | Boolean | `true` | Shows validation border when field is empty |
| `Reset` | Boolean | `false` | Set to `true` to clear the input value |
| `SpellCheck` | Boolean | `true` | Enable spell checking for text inputs |
| `DropShadow` | Boolean | `true` | Show drop shadow effect on the input container |

### Default Values

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `TextFieldDefault` | Text | `""` | Default value for text inputs (`txt` and `txtx`) |
| `DropdownDefault` | Text | `"Red"` | Default selected value for dropdown |
| `DateDefault` | Text | `Today()` | Default date for date picker |
| `DropdownItems` | Table | `["", "Red", "Green", "Blue"]` | List of dropdown options |

### Border Styling

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `BorderColor` | Color | `#30006F` | Normal border color |
| `BorderColorRequired` | Color | `#EC008C` | Border color when required field is empty |
| `BorderWidth` | Number | `1` | Border thickness in pixels |
| `BorderRadius` | Number | `8` | Corner radius in pixels |

### Color Styling

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `FillColor` | Color | `Color.White` | Background fill color of input |
| `HoverFillColor` | Color | `ColorFade(cmp_Input.IconHoverColor, .95)` | Background color on hover |
| `InputColor` | Color | `RGBA(0, 0, 0, 1)` | Text color for input values |
| `FieldNameColor` | Color | `cmp_Input.IconColor` | Color of the field name label |
| `IconColor` | Color | `#30006F` | Color for icons (dropdown chevron, date picker) |
| `IconHoverColor` | Color | `#EC008C` | Icon color on hover |
| `IconBackgroundColor` | Color | `Color.White` | Background color for icons |
| `DropdownSelectionColor` | Color | `Color.White` | Text color for selected dropdown item |

### Font Styling

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `Font` | Text | `"Montserrat"` | Font family for all text |
| `InputFontSize` | Number | `13` | Font size for input values |
| `FieldNameFontSize` | Number | `11` | Font size for field name label |
| `FieldNameHeight` | Number | `28` | Height of the field name label area |

### Events

| Property | Type | Description |
|----------|------|-------------|
| `OnChange` | Event | Fires when the input value changes (dropdown only) |

### Output

| Property | Type | Description |
|----------|------|-------------|
| `aValue` | Text (Output) | Returns the current value of the active input control |

## Usage Examples

### Example 1: Single Line Text Input

```powerfx
// Add component to screen
cmp_Input_Name

// Configure properties
cmp_Input_Name.InputType = "txt"
cmp_Input_Name.FieldName = "Full Name"
cmp_Input_Name.HintText = "Enter your full name"
cmp_Input_Name.Required = true
cmp_Input_Name.SpellCheck = true

// Get the value
Set(varUserName, cmp_Input_Name.aValue)
```

### Example 2: Multi-line Text Input

```powerfx
// Add component to screen
cmp_Input_Description

// Configure properties
cmp_Input_Description.InputType = "txtx"
cmp_Input_Description.FieldName = "Description"
cmp_Input_Description.HintText = "Provide detailed description..."
cmp_Input_Description.Required = false
cmp_Input_Description.Height = 150

// Get the value
Set(varDescription, cmp_Input_Description.aValue)
```

### Example 3: Dropdown Selection

```powerfx
// Add component to screen
cmp_Input_Status

// Configure properties
cmp_Input_Status.InputType = "drp"
cmp_Input_Status.FieldName = "Status"
cmp_Input_Status.DropdownItems = ["", "Active", "Pending", "Completed", "Cancelled"]
cmp_Input_Status.DropdownDefault = "Active"
cmp_Input_Status.Required = true

// Handle change event
cmp_Input_Status.OnChange =
    If(
        cmp_Input_Status.aValue = "Completed",
        Notify("Task completed!", NotificationType.Success)
    )

// Get the value
Set(varStatus, cmp_Input_Status.aValue)
```

### Example 4: Date Picker

```powerfx
// Add component to screen
cmp_Input_DueDate

// Configure properties
cmp_Input_DueDate.InputType = "dte"
cmp_Input_DueDate.FieldName = "Due Date"
cmp_Input_DueDate.DateDefault = DateAdd(Today(), 7, Days)
cmp_Input_DueDate.Required = true

// Get the value
Set(varDueDate, cmp_Input_DueDate.aValue)
```

### Example 5: Custom Theming

```powerfx
// Corporate brand colors
cmp_Input_Custom.BorderColor = ColorValue("#0078D4")      // Microsoft Blue
cmp_Input_Custom.BorderColorRequired = ColorValue("#D13438")  // Red for errors
cmp_Input_Custom.IconColor = ColorValue("#0078D4")
cmp_Input_Custom.IconHoverColor = ColorValue("#106EBE")
cmp_Input_Custom.Font = "Segoe UI"
cmp_Input_Custom.BorderRadius = 4
cmp_Input_Custom.BorderWidth = 2
cmp_Input_Custom.DropShadow = false
```

### Example 6: Form Reset

```powerfx
// Reset button OnSelect
UpdateContext({varResetInputs: true});
UpdateContext({varResetInputs: false})

// Component Reset property
cmp_Input_Name.Reset = varResetInputs
cmp_Input_Email.Reset = varResetInputs
cmp_Input_Phone.Reset = varResetInputs
```

## The aValue Output Property

The `aValue` property is a **unified output** that automatically returns the correct value based on the current `InputType`:

```powerfx
// Internal formula (for reference)
Switch(
    cmp_Input.InputType,
    "txt", txt_Input.Text,           // Returns text from single-line input
    "txtx", txtx_Input.Text,         // Returns text from multi-line input
    "drp", drp_Input.SelectedText.Value,  // Returns selected dropdown text
    "dte", dte_Input.SelectedDate    // Returns selected date
)
```

This means you can use `cmp_Input.aValue` in your formulas without worrying about which input type is currently active.

### Using aValue in Collections

```powerfx
// Collect form data
Collect(
    colFormData,
    {
        Name: cmp_Input_Name.aValue,
        Email: cmp_Input_Email.aValue,
        Status: cmp_Input_Status.aValue,
        StartDate: cmp_Input_StartDate.aValue
    }
)
```

### Using aValue in Patch

```powerfx
// Save to data source
Patch(
    MyDataSource,
    Defaults(MyDataSource),
    {
        FullName: cmp_Input_Name.aValue,
        Notes: cmp_Input_Notes.aValue,
        Category: cmp_Input_Category.aValue,
        DueDate: cmp_Input_DueDate.aValue
    }
)
```

## Styling and Theming

### Color System

The component uses a coordinated color system:

- **Primary Color**: Default border and icon color (`BorderColor`, `IconColor`)
- **Accent Color**: Required field validation and hover states (`BorderColorRequired`, `IconHoverColor`)
- **Neutral Colors**: Fill and background colors (`FillColor`, `IconBackgroundColor`)

### Default Theme

The default theme uses a purple and magenta color scheme:

- Primary: `#30006F` (Deep Purple)
- Accent: `#EC008C` (Magenta)
- Font: Montserrat

### Creating Theme Variations

```powerfx
// Modern minimalist theme
Set(varTheme, {
    Primary: ColorValue("#333333"),
    Accent: ColorValue("#007ACC"),
    Background: ColorValue("#FFFFFF"),
    Font: "Segoe UI",
    Radius: 2,
    Shadow: false
})

// Apply theme to component
cmp_Input.BorderColor = varTheme.Primary
cmp_Input.BorderColorRequired = varTheme.Accent
cmp_Input.IconColor = varTheme.Primary
cmp_Input.IconHoverColor = varTheme.Accent
cmp_Input.FillColor = varTheme.Background
cmp_Input.Font = varTheme.Font
cmp_Input.BorderRadius = varTheme.Radius
cmp_Input.DropShadow = varTheme.Shadow
```

## Validation Behavior

The component provides visual validation feedback when `Required = true`:

1. **Empty Required Field**: Border color changes to `BorderColorRequired` (default: magenta)
2. **Filled Required Field**: Border color shows normal `BorderColor` (default: purple)

This works automatically for all input types:

- **Text fields** (`txt`, `txtx`): Validates using `IsBlank(text)`
- **Dropdown** (`drp`): Validates using `IsBlank(SelectedText.Value)`
- **Date picker** (`dte`): Validates using `IsBlank(SelectedDate)`

## Component Dimensions

- **Default Height**: 70 pixels (includes label + input area)
- **Default Width**: 300 pixels
- **Field Name Height**: 28 pixels (customizable)
- **Input Area Height**: Calculated as `Height - FieldNameHeight - 5`

Adjust the component height for multi-line text inputs to provide more space.

## Credits

Original component created by **Colin** and shared with the Power Apps community. This component demonstrates best practices for creating reusable, themeable input controls in Power Apps.

## Tips and Best Practices

1. **Consistent Naming**: Use a naming convention for instances (e.g., `cmp_Input_FieldName`)
2. **Theme Variables**: Store theme colors in global variables or a collection for consistency
3. **Required Fields**: Set `Required = false` for optional fields to avoid unnecessary validation indicators
4. **Dropdown Empty Option**: Include an empty string (`""`) as the first item in `DropdownItems` to allow clearing selections
5. **Date Defaults**: Use Power Fx date functions for intelligent defaults (e.g., `Today()`, `DateAdd(Today(), 7)`)
6. **Reset Patterns**: Use context variables with toggle pattern for reliable reset behavior
7. **Accessibility**: Always set meaningful `FieldName` and `Tooltip` values for screen readers
8. **Height for Multi-line**: Increase component height when using `txtx` input type for better UX

## Troubleshooting

### Border color not changing for required fields

- Verify `Required = true`
- Check that the field is actually empty
- Ensure `BorderColorRequired` is visually distinct from `BorderColor`

### Reset not working

- Use toggle pattern: Set to `true`, then immediately set to `false`
- Example: `UpdateContext({varReset: true}); UpdateContext({varReset: false})`

### Dropdown items not showing

- Verify `DropdownItems` is a valid table or array
- Check that items are text values
- Ensure `InputType = "drp"`

### Value not retrieving correctly

- Always use `aValue` output property
- Check that `InputType` is set correctly
- For dates, remember `aValue` returns a Date type when `InputType = "dte"`

## Related Resources

- [Power Apps Components Documentation](https://learn.microsoft.com/power-apps/maker/canvas-apps/create-component)
- [Power Fx Formula Reference](https://learn.microsoft.com/power-platform/power-fx/formula-reference)
- [Component Best Practices](https://learn.microsoft.com/power-apps/maker/canvas-apps/component-behavior)
