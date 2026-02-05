---
title: "Basic SVG Spinner"
description: "Simple named formula for basic SVG spinner animation"
category: "visual-assets"
subcategory: "svgs"
tags: [svg, spinner, animation, named-formula]
difficulty: "beginner"
products: ["power-apps-canvas"]
author: "PowerAppsDarren"
created: "2024-01-01"
updated: "2026-01-22"
license: "MIT"
related: [basic-spinner]
---

# Basic-SVG-Spinner

## Table of Contents

Here's a basic SVG spinner that you can use in your Power Apps. 

```PowerFx
//
// App.Formulas...
//
fxBasicSVGSpinner = (
    "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 100 100"" preserveAspectRatio=""xMidYMid"" width=""200"" height=""200"" style=""shape-rendering: auto; display: block; background: transparent;"" xmlns:xlink=""http://www.w3.org/1999/xlink""><g><path stroke=""none"" fill=""#000000"" d=""M10 50A40 40 0 0 0 90 50A40 43.5 0 0 1 10 50""><animateTransform values=""0 50 51.75;360 50 51.75"" keyTimes=""0;1"" repeatCount=""indefinite"" dur=""1.1764705882352942s"" type=""rotate"" attributeName=""transform""></animateTransform></path><g></g></g></svg>"
);
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
