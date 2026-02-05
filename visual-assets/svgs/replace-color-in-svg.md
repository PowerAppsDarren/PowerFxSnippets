---
title: "Replace Color in SVG"
description: "User-defined function to replace colors in SVG strings for dynamic theming"
category: "visual-assets"
subcategory: "svgs"
tags: [svg, colors, user-defined-function, theming]
difficulty: "intermediate"
products: ["power-apps-canvas"]
author: "PowerAppsDarren"
created: "2024-01-01"
updated: "2026-01-22"
license: "MIT"
related: [basic-spinner, svgs]
---

# Replace Color in SVG

## Table of Contents

```PowerFx
//
// fxGetColoredSVGNoEncode
//
fxGetColoredSVGNoEncode(SVGText:Text, 
                        ColorToReplace:Text, 
                        DesiredColor:Text):Text =  
    Substitute(
        SVGText, 
        $"{ColorToReplace}", 
        $"{DesiredColor}"
    );
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
