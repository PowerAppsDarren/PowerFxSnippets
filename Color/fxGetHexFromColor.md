# fxGetHexFromColor() User-Defined Function

Paste this code into your App.Formulas and call it to convert a ColorValue to a hex string.

```PowerFx
    fxGetHexFromColor(ColorValue:Color, IncludeAlpha:Boolean):Text = (
        With( 
            {
                MyVal: Substitute(
                            JSON(ColorValue), 
                            """", 
                            ""
                        )
            },
            Left(MyVal, Len(MyVal) - 2)
        )
    );


    fxGetHexFromColor(ColorValue:Color):Text = Left(
        Substitute(
            JSON(ColorValue, JSONFormat.Compact), 
            """",
            ""
        ), 
        7
    );
```