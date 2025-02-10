# Theming

Be sure to check out these related topics:

- [Colors](Colors.md)
- [Color Palettes](Color%20Palettes.md)
- [Color Resources](Color%20Resources.md)
- [Color Functions](Color%20Functions.md)


TODO: Add links to these other folders in this repo: 
 /Colors, /Color Palettes, /Color Resources, /Color Functions


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
