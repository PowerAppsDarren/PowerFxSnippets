# Colors

## Table of Contents

- [Categories](#categories)
  - [[Functions](../../functions)](#functionsfunctions)
  - [[Palettes](./palettes)](#palettespalettes)
  - [[Utilities](../../utilities)](#utilitiesutilities)
- [Quick Reference](#quick-reference)
  - [Color Conversions](#color-conversions)
  - [Web Colors Collection](#web-colors-collection)
  - [Theme Palette](#theme-palette)
- [Accessibility](#accessibility)
- [Related Resources](#related-resources)
- [Credits](#credits)

Power Fx color utilities, conversion functions, palettes, and resources for Power Apps development.

## Categories

### [Functions](../../functions)

Color conversion and manipulation functions.

| File | Description |
|------|-------------|
| [color-functions.md](functions/color-functions.md) | Canvas component with accessibility color functions (color blindness simulations, contrast checking) |
| [fxgethexfromcolor.md](functions/fxgethexfromcolor.md) | Convert Power Apps Color value to hex string |
| [hex-2-rgb.md](functions/hex-2-rgb.md) | Convert hexadecimal color codes to RGB values |
| [hsv-2-rgb.md](functions/hsv-2-rgb.md) | Convert HSV to RGB color values |
| [luminance.md](functions/luminance.md) | Calculate luminance for accessibility |
| [rgb-2-hsl.md](functions/rgb-2-hsl.md) | Convert RGB to HSL color values |
| [rgb-2-hsv.md](functions/rgb-2-hsv.md) | Convert RGB to HSV color values |
| [rgb-2-lin.md](functions/rgb-2-lin.md) | Convert sRGB to linearized values |

### [Palettes](./palettes)

Color collections, themes, and palette definitions.

| File | Description |
|------|-------------|
| [color-collection.md](palettes/color-collection.md) | All 140 web colors as a Power Apps collection |
| [color-palette-pa.md](palettes/color-palette-pa.md) | Power Apps branding theme with extended colors |
| [color-palettes.md](palettes/color-palettes.md) | Simple color palette configuration |
| [color-template.md](palettes/color-template.md) | Canvas component template for color functions |
| [microsoft-power-apps.md](palettes/microsoft-power-apps.md) | Microsoft branding and trademark guidelines |
| [web-colors.md](palettes/web-colors.md) | 140 web colors with categories and tags |

### [Utilities](../../utilities)

External resources and tools.

| File | Description |
|------|-------------|
| [color-resources.md](utilities/color-resources.md) | External color tools, Nord theme, gradient generators |

## Quick Reference

### Color Conversions

```powerfx
// HEX to RGB
With({...}, { Color: RGBA(R, G, B, 1), R: R, G: G, B: B })

// RGB to HSV
With({CMAX: Max(R,G,B), CMIN: Min(R,G,B)}, { H: ..., S: ..., V: ... })

// Color to Hex String
fxGetHexFromColor(ColorValue:Color):Text
```

### Web Colors Collection

```powerfx
fxWebColors = [
    { ID: 1, Name: "AliceBlue", HexCode: "#F0F8FF", Value: ColorValue("#F0F8FF"), ... },
    // ... 140 total colors
]
```

### Theme Palette

```powerfx
fxColorPalette = {
    Primary:    ColorValue("#742774"),
    Dark:       ColorValue("#BB35A4"),
    Light:      ColorValue("#D467B9"),
    Lighter:    ColorValue("#E48CC7"),
    Background: RGBA(255, 255, 255, 1),
    Text:       RGBA(0, 0, 0, 1)
}
```

## Accessibility

The color functions include simulations for various types of color blindness:
- **Achromatomaly** / **Achromatopsia** - Grayscale vision
- **Deuteranomaly** / **Deuteranopia** - Green-blind
- **Protanomaly** / **Protanopia** - Red-blind
- **Tritanomaly** / **Tritanopia** - Blue-blind

## Related Resources

- [Web Colors (Wikipedia)](https://en.wikipedia.org/wiki/Web_colors)
- [Nord Theme](https://www.nordtheme.com/docs/colors-and-palettes)
- [CSS Gradient Generator](https://cssgradient.io/)
- [AI Colors](https://aicolors.co/)

## Credits

- Color functions adapted from [P3N-101/color-functions](https://github.com/P3N-101/color-functions)
- Color conversions from [matthewdevaney/powerapps-custom-functions](https://github.com/matthewdevaney/powerapps-custom-functions)

---

*Merged from `color/`, `color-palettes/`, and `themes-color-palettes/` directories*
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
