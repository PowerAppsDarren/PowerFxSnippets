# SVG Icon Files

This directory contains SVG icon files organized by category for use in Power Apps.

## Directory Structure

```
svg-files/
├── advanced.svg         # Skill level indicator - advanced
├── beginner.svg         # Skill level indicator - beginner
├── intermediate.svg     # Skill level indicator - intermediate
└── power-platform/      # Official Microsoft Power Platform icons
    ├── aibuilder-scalable.svg
    ├── dataverse-scalable.svg
    ├── powerapps-scalable.svg
    ├── powerautomate-scalable.svg
    ├── powerbi-scalable.svg
    ├── powerpages-scalable.svg
    ├── powerplatform-scalable.svg
    └── powervirtualagents-scalable.svg
```

## Skill Level Indicator Icons

| Icon | File | Description |
|------|------|-------------|
| Beginner | `beginner.svg` | Single filled bar (green) - indicates beginner difficulty |
| Intermediate | `intermediate.svg` | Two bars (first filled) - indicates intermediate difficulty |
| Advanced | `advanced.svg` | Three bars (first filled) - indicates advanced difficulty |

These icons use a bar-chart style to indicate difficulty levels, similar to signal strength indicators.

## Usage

### In Power Apps Image Control

```powerfx
// Load SVG directly
Image.Image = "data:image/svg+xml;utf8," & EncodeUrl(svgContent)
```

### With Theme Colors

```powerfx
// Replace default color with theme color
With(
    {
        themeColor: Left(Substitute(JSON(App.Theme.Colors.Primary), """", ""), 7)
    },
    "data:image/svg+xml;utf8," & EncodeUrl(
        Substitute(svgContent, "#00ff00", themeColor)
    )
)
```

## Subdirectories

- **[power-platform/](../../../README.md)** - Official Microsoft Power Platform service icons
