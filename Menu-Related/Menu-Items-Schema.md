# Menu-Items-Schema

I've tried my best to come up with a standard schema for the menu items that you might use in your Power Apps applications. If this is the format you'd like to use, then copy and paste this into your App.Formulas. 

```PowerFx
    fxMenuItem_Type:= Type( 
        {
            AsciiIcon:              Text,       // You may want an emoji to show along with the menu text
            SortOrder:              Number,     // You probably want the menu items displayed in a certian order
            ScreenToGoTo:           Text,           // Real Type: Screen
            MenuText:               Text,           // You may not want the menu text to be the same as the screen name (maybe exclude " Screen")
            ParentScreenName:       Text,           // Recursive relationship for parent/child relationships
            ImageOrIcon:            Text,           // "Icon", "Image", "Emoji"
            MenuImage:              Text,           // Real Type: Image
            MenuIcon:               Text,           // Real Type: Icon.___
            ShowForThisRole:        Text,           // Contains all the roles the menu shows for (delimited by ";"'s)
            Visible:                Boolean,        // You never know when you might want to hide a screen quickly
            LaunchLink:             Boolean,        // Does the menu need to use Launch instead of Navigate?
            LaunchURL:              Text            // If it is a link outside of the app, what's the URL?
        }
    );

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
            }
        ], 
        MenuTextWithEmoji, 
        AsciiIcon & " " & MenuText 
        ), 
        SortOrder
    );
```