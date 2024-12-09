
# Replace and Encode SVGs

These two formulas go well together.

## Add This to Your Application

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