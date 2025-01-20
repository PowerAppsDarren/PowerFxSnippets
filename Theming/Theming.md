# Theming

Pass in a color value and get the hex value back.

```PowerFx
fxGetHexFromColor(ColorValue:Color):Text = Left(
    Substitute(
        JSON(ColorValue, JSONFormat.Compact), 
        """",
        ""
    ), 
    7
);
```
