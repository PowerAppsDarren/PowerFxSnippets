# SVG Resources for Power Apps

## Table of Contents

- [Start Here](#start-here)
- [Quick Start](#quick-start)
  - [Display an SVG in Power Apps](#display-an-svg-in-power-apps)
  - [Use Theme Colors with SVGs](#use-theme-colors-with-svgs)
- [Contents](#contents)
- [External Resources](#external-resources)

This directory contains SVG icons, documentation, and code patterns for working with SVGs in Power Apps.

## Start Here

1. **[INDEX.md](../../ai-protocols/index.md)** - Complete searchable catalog of all SVG files
2. **[Best SVG Snippet](./best-svg-snippet.md)** - Comprehensive guide to SVG usage
3. **[SVG Files](./svg-files)** - Actual SVG icon files

## Quick Start

### Display an SVG in Power Apps

```powerfx
// In an Image control's Image property:
"data:image/svg+xml;utf8," & EncodeUrl("<svg>...</svg>")
```

### Use Theme Colors with SVGs

```powerfx
// Replace default color with app theme color
With(
    {
        svgCode: "<svg>...</svg>",
        themeColor: Left(Substitute(JSON(App.Theme.Colors.Primary), """", ""), 7)
    },
    "data:image/svg+xml;utf8," & EncodeUrl(
        Substitute(svgCode, "#000000", themeColor)
    )
)
```

## Contents

| Resource | Description |
|----------|-------------|
| [INDEX.md](../../ai-protocols/index.md) | Complete SVG catalog with paths and descriptions |
| [svg-files/](./svg-files) | Icon files organized by category |
| [best-svg-snippet.md](./best-svg-snippet.md) | Detailed SVG implementation guide |
| [basic-spinner.md](./basic-spinner.md) | Animated spinner implementation |
| [replace-color-in-svg.md](./replace-color-in-svg.md) | Color replacement function |
| [svgs.md](./svgs.md) | Additional resources and links |

## External Resources

- [2,000 Free Power Apps Icons](https://www.matthewdevaney.com/2000-free-power-apps-icons/)
- [SVG Video Playlist](https://www.youtube.com/playlist?list=PL4-IK0AVhVjP0EeV513_b30lhGRTfMbYd)
- [Microsoft Branding Guidelines](./microsoft-branding.md)
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
