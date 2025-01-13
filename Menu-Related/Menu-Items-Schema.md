# Menu-Items-Schema

I've tried my best to come up with a standard schema for the menu items that you might use in your Power Apps applications. 

```PowerFx
    //
    // This is the collection used for any of the the menus used
    //
    fxMenuItems = Sort(
        AddColumns([
            {
                AsciiIcon: "🏠", 
                ScreenToGoTo: 'Home Screen',
                MenuText: Substitute(
                    Upper('Home Screen'.Name), 
                    " SCREEN", 
                    ""
                ),
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "🚗", 
                ScreenToGoTo: 'Request Screen',
                MenuText: "REQUEST",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "🗓️", 
                ScreenToGoTo: 'Reservations Screen',
                MenuText: "RESERVATIONS",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "✅", 
                ScreenToGoTo: 'Return Screen',
                MenuText: "RETURN",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            }
        ], 
        MenuTextWithEmoji, 
        AsciiIcon & " " & MenuText 
        ), 
        SortOrder
    );

```PowerFx
    //
    // This is the collection used for any of the the menus used
    //
    fxMenuItems = Sort(
        AddColumns([
            {
                AsciiIcon: "🏠", 
                ScreenToGoTo: 'Home Screen',
                MenuText: Substitute(
                    Upper('Home Screen'.Name), 
                    " SCREEN", 
                    ""
                ),
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "🚗", 
                ScreenToGoTo: 'Request Screen',
                MenuText: "REQUEST",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "🗓️", 
                ScreenToGoTo: 'Reservations Screen',
                MenuText: "RESERVATIONS",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            },
            {
                AsciiIcon: "✅", 
                ScreenToGoTo: 'Return Screen',
                MenuText: "RETURN",
                ParentScreenName: "",
                ImageOrIcon: "Icon",
                MenuImage: SampleImage,
                MenuIcon: Icon.Home,
                ShowForThisRole: "User;",
                Visible: true,
                LaunchLink: false,
                LaunchURL: ""
            }
        ], 
        MenuTextWithEmoji, 
        AsciiIcon & " " & MenuText 
        ), 
        SortOrder
    );
```