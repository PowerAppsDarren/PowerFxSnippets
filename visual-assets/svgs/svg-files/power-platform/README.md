# Power Platform SVG Icons

This directory contains official scalable SVG icons for Microsoft Power Platform services and components.

## Contents

| Icon | File | Description |
|------|------|-------------|
| AI Builder | `aibuilder-scalable.svg` | AI Builder service icon - gradient purple/blue design |
| Dataverse | `dataverse-scalable.svg` | Dataverse database service icon - gradient green design |
| Power Apps | `powerapps-scalable.svg` | Power Apps service icon - gradient purple/magenta design |
| Power Automate | `powerautomate-scalable.svg` | Power Automate (Flow) service icon - gradient blue design |
| Power BI | `powerbi-scalable.svg` | Power BI analytics service icon - gradient yellow/orange design |
| Power Pages | `powerpages-scalable.svg` | Power Pages website builder icon - gradient blue/cyan design |
| Power Platform | `powerplatform-scalable.svg` | Main Power Platform logo - combined gradient design |
| Power Virtual Agents | `powervirtualagents-scalable.svg` | Copilot Studio (formerly PVA) icon - gradient green design |

## Additional Resources

| File | Type | Description |
|------|------|-------------|
| `copilot-icon.png` | PNG | Microsoft Copilot icon (raster format) |
| `cela-licenses-public-use-icons.pdf` | PDF | Microsoft CELA licensing guidelines for public use icons |
| `power-platform-icons-faq.pdf` | PDF | FAQ document for Power Platform icon usage |

## Usage in Power Apps

### Basic SVG Display

```powerfx
// Display an SVG in an Image control
Image.Image = "data:image/svg+xml," & EncodeUrl(svgContent)
```

### With Color Replacement

```powerfx
// Replace a color in the SVG before encoding
With(
    {
        svgContent: "<svg>...</svg>",
        originalColor: "#000000",
        newColor: Left(Substitute(JSON(App.Theme.Colors.Primary), """", ""), 7)
    },
    "data:image/svg+xml," & EncodeUrl(
        Substitute(svgContent, originalColor, newColor)
    )
)
```

## Icon Specifications

- **Format**: SVG (Scalable Vector Graphics)
- **Size**: 96x96 viewBox (scalable to any size)
- **Style**: Gradient fills with modern flat design
- **Color Space**: sRGB with linear gradients

## Licensing

These icons are provided by Microsoft for use with Power Platform applications. Please refer to the included PDF documents for licensing terms and usage guidelines:

- `cela-licenses-public-use-icons.pdf` - General licensing terms
- `power-platform-icons-faq.pdf` - Frequently asked questions about icon usage

## Related Resources

- [Microsoft Power Platform Icons](https://docs.microsoft.com/power-platform/)
- [Power Apps Icon Guidelines](https://docs.microsoft.com/powerapps/)
