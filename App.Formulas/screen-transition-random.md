# Random Screen Transition

This function will return one of the 5 screen transitions randomly.
It is a user defined function (UDF) and not a named formula
so that it will return a fresh value.

## Add This to Your Application

```JavaScript
    //
    // This function will return one of the 5 screen transitions randomly.    
    // It is a user defined function (UDF) and not a named formula
    // so that it will return a fresh value. 
    //
    fxRandomScreenTransition():Text = 
        With(
            {
                RandomNumber: RandBetween(1, 5)
            }, 
            Switch(
                RandomNumber, 
                1, ScreenTransition.Cover,
                2, ScreenTransition.CoverRight,
                3, ScreenTransition.Fade,
                4, ScreenTransition.UnCover,
                5, ScreenTransition.UnCoverRight,
                ScreenTransition.None
            )    
        );
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
