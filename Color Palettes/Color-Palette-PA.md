# Color Palette: Power Apps

```PowerFx

    #742774         // Primary
    #932d89         // Secondary
    #bb35a4         // Accent 
    #d467b9         // Neutral
    #e9a1cb         // Foreground
    #f1d4e6         // Background


    fxExtendedTheme = {
        //
        //
        //
        ThemeName:              "Power Apps Branding", // Should be unique by a particular theme author
        ThemeKey:               "POWER-APPS-BRANDING", // Should be unique by a particular theme author
        ThemeUUID:              "3e2bdee6-fc50-4d0f-8743-7e08a5d0ef5e", // A unique identifier value from the author
        ThemeAuthor:            "Darren Neese (support@superpowerlabs.co)",
        //
        // Three base properties so we never have to reference `App.Theme.___`
        //
        BaseFont:               App.Theme.Font, 
        BaseName:               App.Theme.Name,
        BaseColors:             App.Theme.Colors,
        //
        // Fonts (modern fonts need 3 more points/pixels)
        //
        DefaultFontName:        Font.'Open Sans', 
        DefaultFontSizeClassic: 12,
        //
        // Properties having to deal with light/dark mode feature
        //
        ThemeType:              "Light", 
        PairedThemeGUID:        "",
        //
        // Colors
        //
        Colors: {
            Primary: {
                Value:                  ColorValue("#742774"), 
                Name:                   "Primary", 
                HexCode:                "#742774", 
                OppositeColorName:      "PrimaryOpposite"
            },
            PrimaryOpposite: {
                Value:ColorValue("#ffffff"), 
                Name:"PrimaryOpposite", 
                HexCode:"#ffffff", 
                OppositeColorName:"Primary"
            },
            Secondary: {
                Value:ColorValue("#932d89"), 
                Name:"Secondary", 
                HexCode:"#932d89", 
                OppositeColorName:"SecondaryOpposite"
            },
            SecondaryOpposite: {
                Value:ColorValue("#000000"), 
                Name:"SecondaryOpposite", 
                HexCode:"#000000", 
                OppositeColorName:"Secondary"
            },
            Accent: {
                Value:ColorValue("#bb35a4"), 
                Name:"Accent", 
                HexCode:"#bb35a4", 
                OppositeColorName:"AccentOpposite"
            },
            AccentOpposite: {
                Value:ColorValue("#000000"), 
                Name:"AccentOpposite", 
                HexCode:"#000000", 
                OppositeColorName:"Accent"
            },
            Background: {
                Value:ColorValue("#f1d4e6"), 
                Name:"Background", 
                HexCode:"#f1d4e6", 
                OppositeColorName:"BackgroundOpposite"
            },
            BackgroundOpposite: {
                Value:ColorValue("#0a2e4a"),            // Primary's Darker50 Shade
                Name:"BackgroundOpposite", 
                HexCode:"#0a2e4a", 
                OppositeColorName:"Background"
            },
            Neutral: {
                Value:ColorValue("#d467b9"),          // Primary's Lighter60
                Name:"Neutral", 
                HexCode:"#d467b9", 
                OppositeColorName:"NeutralOpposite"
            },
            NeutralOpposite: {
                Value:ColorValue("#0a2e4a"),            // Primary's Darker50 Shade
                Name:"NeutralOpposite", 
                HexCode:"#0a2e4a", 
                OppositeColorName:"Neutral"
            },
            Menu: {
                Value:ColorValue("#742774"),          // Primary's Lighter60
                Name:"Menu", 
                HexCode:"#742774", 
                OppositeColorName:"MenuOpposite"
            },
            MenuOpposite: {
                Value:ColorValue("#ffffff"),            // Primary's Darker40 Shade
                Name:"MenuOpposite", 
                HexCode:"#ffffff", 
                OppositeColorName:"Menu"
            }
        }
    };

```
