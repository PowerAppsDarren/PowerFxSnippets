
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
