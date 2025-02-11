# Microsoft-Base-Themes

This is some YAML you can paste into your canvas Power Apps applciation.

## Add This to Your App.Formulas

Once declared in App.Formulas, you can use these themes in your app by simply referencing fxAllThemes. 
For example: 

Rect

```PowerFx
    fxAllThemes = {
        PowerApps:      PowerAppsTheme, 
        TeamsTheme:     TeamsTheme,
        SharePoint:     SharePointTheme, 
        Steel:          SteelTheme, 
        Red:            RedTheme, 
        Orange:         OrangeTheme, 
        Green:          GreenTheme, 
        Platinum:       PlatinumTheme
    };
```

Related Tagss:
    - #colors
    - #color-palettes
    - #color-functions
    - #app-formulas