# SVG Icon Index

A searchable catalog of all SVG icons and related resources in this repository.

**Total SVG Files**: 11
**Total Documentation Files**: 8
**Categories**: 2 (Skill Indicators, Power Platform)

---

## Quick Reference

### Power Platform Icons

Official Microsoft Power Platform service icons. Scalable vector graphics with gradient fills.

| Name | Path | Description |
|------|------|-------------|
| AI Builder | `svg-files/power-platform/aibuilder-scalable.svg` | AI Builder service - purple/blue gradient |
| Dataverse | `svg-files/power-platform/dataverse-scalable.svg` | Dataverse database - green gradient |
| Power Apps | `svg-files/power-platform/powerapps-scalable.svg` | Power Apps - purple/magenta gradient |
| Power Automate | `svg-files/power-platform/powerautomate-scalable.svg` | Power Automate flows - blue gradient |
| Power BI | `svg-files/power-platform/powerbi-scalable.svg` | Power BI analytics - yellow/orange gradient |
| Power Pages | `svg-files/power-platform/powerpages-scalable.svg` | Power Pages websites - blue/cyan gradient |
| Power Platform | `svg-files/power-platform/powerplatform-scalable.svg` | Main platform logo - combined gradient |
| Power Virtual Agents | `svg-files/power-platform/powervirtualagents-scalable.svg` | Copilot Studio - green gradient |

### Skill Level Indicators

Bar-chart style icons for indicating difficulty or skill levels.

| Name | Path | Description |
|------|------|-------------|
| Beginner | `svg-files/beginner.svg` | Single green filled bar (1/3) |
| Intermediate | `svg-files/intermediate.svg` | First bar filled (1/3, others outlined) |
| Advanced | `svg-files/advanced.svg` | First bar filled (1/3, others outlined) |

---

## Documentation Files

| File | Description |
|------|-------------|
| `basic-spinner.md` | Complete spinner implementation with color replacement |
| `basic-svg-spinner.md` | Simple named formula for spinner SVG |
| `best-svg-snippet.md` | Comprehensive guide to SVG usage in Power Apps |
| `guide-to-svgs.md` | Video resources for learning SVGs |
| `microsoft-branding.md` | Microsoft trademark and branding guidelines links |
| `replace-color-in-svg.md` | User-defined function for color replacement |
| `svgs.md` | Overview and resource links |
| `readme.md` | Original directory readme |

---

## Additional Resources (Non-SVG)

Located in `svg-files/power-platform/`:

| File | Type | Description |
|------|------|-------------|
| `copilot-icon.png` | PNG | Microsoft Copilot icon (raster) |
| `cela-licenses-public-use-icons.pdf` | PDF | Microsoft licensing guidelines |
| `power-platform-icons-faq.pdf` | PDF | Icon usage FAQ |

---

## Usage Patterns

### Basic SVG Encoding

```powerfx
// Named formula for SVG encoding
fxSVGEncode(svgCode:Text):Text =
    "data:image/svg+xml; utf8, " & EncodeUrl(svgCode);
```

### Color Replacement

```powerfx
// Replace color before encoding
fxGetColoredSVGNoEncode(SVGText:Text, ColorToReplace:Text, DesiredColor:Text):Text =
    Substitute(
        SVGText,
        $"{ColorToReplace}",
        $"{DesiredColor}"
    );
```

### Theme-Aware Colors

```powerfx
// Get hex color from theme
Left(
    Substitute(
        JSON(App.Theme.Colors.Primary, JSONFormat.Compact),
        """",
        ""
    ),
    7
)  // Returns: "#RRGGBB"
```

### Complete Spinner Example

```powerfx
fxSpinnerSimple():Text = fxSVGEncode(
    fxGetColoredSVGNoEncode(
        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 100 100"" ...>...</svg>",
        "#000000",
        Substitute(JSON(App.Theme.Colors.Primary), """", "")
    )
);
```

---

## File Statistics

| Category | Count | Location |
|----------|-------|----------|
| Power Platform SVGs | 8 | `svg-files/power-platform/` |
| Skill Level SVGs | 3 | `svg-files/` |
| Documentation | 8 | Root directory |
| Supporting Files | 3 | `svg-files/power-platform/` |

---

## Related Sections

- [Power Platform Icons README](svg-files/power-platform/README.md)
- [SVG Files README](svg-files/README.md)
- [Best SVG Snippet Guide](best-svg-snippet.md)
