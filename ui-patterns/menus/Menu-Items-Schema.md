# Menu-Items-Schema

## Table of Contents

I've tried my best to come up with a standard schema for the menu items that you might use in your Power Apps applications. If this is the format you'd like to use, then copy and paste this into your App.Formulas. 

```PowerFx
    //
    // This type would be great to use to enforce the type of all menu items, 
    // but unfortunately, we can't enforce types that aren't accessible in App.Formulas
    // like Screen, Image, etc.
    //
    fxMenuItem_Type:= Type( 
        {
            AsciiIcon:              Text,       // You may want an emoji to show along with the menu text
            SortOrder:              Number,     // You probably want the menu items displayed in a certian order
            ScreenToGoTo:           Text,       // 🚨 Real Type: Screen 🚨 **why don't we have this type defined in PowerFx?**
            MenuText:               Text,       // You may not want the menu text to be the same as the screen name (maybe exclude " Screen")
            ParentScreenName:       Text,       // Recursive relationship for parent/child relationships
            ImageOrIcon:            Text,       // One of these three values: "Icon", "Image", "Emoji"
            MenuImage:              Text,       // 🚨 Real Type: Image 🚨 **why don't we have this type defined in PowerFx?** 
            MenuIcon:               Text,       // Real Type: Icon.___
            ShowForThisRole:        Text,       // Contains all the roles the menu shows for (delimited by ";"'s)
                                                //      Pass into a component's property (hopefully it has a property for this)
                                                //      with all the roles the current user is in, so that the menu 
                                                //      can filter all those out!
            Visible:                Boolean,    // You never know when you might want to hide a screen quickly
            LaunchLink:             Boolean,    // Does the menu need to use Launch instead of Navigate?
            LaunchURL:              Text        // If it is a link outside of the app, what's the URL?
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
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
