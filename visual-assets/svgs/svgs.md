# SVGs

## Table of Contents

- [Resources](#resources)
- [Replace and Encode SVGs](#replace-and-encode-svgs)

## Resources

- [[Guide to SVGs]]
- [2,000 Free Power Apps Icons](https://www.matthewdevaney.com/2000-free-power-apps-icons/)

## Replace and Encode SVGs

These two formulas go well together.

```PowerFx
fxGetColoredSVGNoEncode(SVGText:Text, ColorToReplace:Text, DesiredColor:Text):Text =  
    Substitute(
        SVGText, 
        $"='{ColorToReplace}'", 
        $"='{DesiredColor}'"
    );

fxSVGEncode(svgCode:Text):Text = 
    "data:image/svg+xml; utf8, " & EncodeUrl(svgCode);
```

- A beginners guide to SVG: https://www.youtube.com/playlist?list=PL4-IK0AVhVjP0EeV513_b30lhGRTfMbYd
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
