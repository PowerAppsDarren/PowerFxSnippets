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
