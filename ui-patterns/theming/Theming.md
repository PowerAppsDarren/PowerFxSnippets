# Theming

Be sure to check out these related topics:

- [Colors](./colors.md)
- [Color Palettes](./color%20palettes.md)
- [Color Resources](./color%20resources.md)
- [Color Functions](./color%20functions.md)


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
