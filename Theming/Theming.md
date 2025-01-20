# Theming

Be sure to check out these related topics: 
- [Colors](Colors.md)
- [Color Palettes](Color%20Palettes.md)
- [Color Resources](Color%20Resources.md)
- [Color Functions](Color%20Functions.md)


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
