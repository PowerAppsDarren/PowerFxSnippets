# Replace Color in SVG

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