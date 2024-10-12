# Random Screen Transition

This function will return one of the 5 screen transitions randomly.
It is a user defined function (UDF) and not a named formula
so that it will return a fresh value.

## Applies to

![Power Apps](https://img.shields.io/badge/Power%20Apps-Yes-green "Yes")
![Power Automate](https://img.shields.io/badge/Power%20Automate-No-red "No")
![Power BI](https://img.shields.io/badge/Power%20BI-No-red "No")
![Power Pages](https://img.shields.io/badge/Power%20Pages-No-red "No")
![Power Virtual Agents](https://img.shields.io/badge/Power%20Virtual%20Agents-No-red "No")
![Dataverse](https://img.shields.io/badge/Dataverse-No-red "No")
![AI Builder](https://img.shields.io/badge/AI%20Builder-No-red "No")
![Custom Connectors](https://img.shields.io/badge/Custom%20Connectors-No-red "No")
![Power Fx](https://img.shields.io/badge/Power%20Fx-Yes-green "Yes")

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
