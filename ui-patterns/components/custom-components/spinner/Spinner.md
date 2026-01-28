---
title: "Spinner Component"
description: "A customizable loading spinner component for canvas apps with SVG animation and color replacement support"
category: "ui-patterns"
subcategory: "loading"
tags:
  - spinner
  - loading
  - component
  - svg
  - animation
difficulty: intermediate
products:
  - power-apps-canvas
dependencies: []
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
related: []
---

# Spinner Component

````yaml
ComponentDefinitions:
  compSpinner:
    DefinitionType: CanvasComponent
    CustomProperties:
      InnerFill:
        PropertyKind: Input
        DisplayName: Inner Fill
        Description: Inner Fill
        DataType: Color
        Default: =compSpinner.Fill
      InnerSpinnerHeight:
        PropertyKind: Input
        DisplayName: Inner Spinner Height
        Description: A custom property
        DataType: Number
        Default: =200
      InnerSpinnerWidth:
        PropertyKind: Input
        DisplayName: Inner Spinner Width
        Description: A custom property
        DataType: Number
        Default: =200
      OuterFill:
        PropertyKind: Input
        DisplayName: Outer Fill
        Description: A custom property
        DataType: Color
        Default: =RGBA(255, 255, 255, .80)
      ShowSpinner:
        PropertyKind: Input
        DisplayName: Show Spinner
        Description: A custom property
        RaiseOnReset: true
        DataType: Boolean
        Default: =true
      SpinnerImage:
        PropertyKind: Input
        DisplayName: Spinner Image
        Description: A custom property
        DataType: Image
        Default: |-
          =With( 
              {
                  //
                  // STEP 1️⃣       
                  //              You can easily find SVG code on the net.
                  //              SVG code will begin and end with a single double quote ("). 
                  //              There will be other double quotes inside the SVG code. 
                  //
                  //              You must double up on those! 
                  //              ...otherwise PowerFx will be confused and thinks that 
                  //              you're trying to end and start other strings inside. 🫤
                  //              This is what is called an 'escape sequence' in the 
                  //              programming world.
                  //
                  SVGCode:        
                                  "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 100 100"" preserveAspectRatio=""xMidYMid"" width=""200"" height=""200"" style=""shape-rendering: auto; display: block; background: transparent;"" xmlns:xlink=""http://www.w3.org/1999/xlink""><g><path stroke=""none"" fill=""#000000"" d=""M10 50A40 40 0 0 0 90 50A40 43.5 0 0 1 10 50""><animateTransform values=""0 50 51.75;360 50 51.75"" keyTimes=""0;1"" repeatCount=""indefinite"" dur=""1.1764705882352942s"" type=""rotate"" attributeName=""transform""></animateTransform></path><g></g></g></svg>", 
                  //
                  // STEP 2️⃣
                  //              You will probably find something like this (fill=""#000000""), which
                  //              is black as you see in the above example. It could be some other Color, 
                  //              so adjust accordingly. 
                  //
                  ReplacedColor:  "#000000",  
                  // 
                  // STEP 3️⃣
                  //              Hexadecimal, also known as "hex", is a numbering system that 
                  //              uses 16 symbols to represent numbers instead of the 10 symbols 
                  //              used in the decimal system
                  //
                  //              If you don't already have a color hex code you'd like to use, 
                  //              you may need to use the JSON function like you see below. 
                  //              If you use JSON, you will need to get rid of the double quotes
                  //              using the Substitute function. 
                  //
                  //              ...And, to get rid of the extra hex code that defines the opacity
                  //              Use the Left() function with the numeric value of 7. 
                  //              A hex code for a color is typically 6 characters 
                  //              (`00` through `ff` each). 0 or 00 is hex for zero. 
                  //              f or ff is hex for 255!
                  //              
                  //              #: this symbol is signifying that the rest is a hexidecimal value
                  //              R: The first hex value after the `#` is for how much Red will be in the final color.
                  //              G: The second hex value after the red is for how much Green will be in the final color.
                  //              B: The subsequent hex value after the green is for how much Blue will be in the final color.
                  //
                  ReplaceWith:    // Substitute to get rid of the double quotes
                                  // Left(stringValue, 7) will give us a good hex code to use to replace
                                  Left(
                                      Substitute(
                                          JSON(
                                              App.Theme.Colors.Primary,
                                              JSONFormat.Compact
                                          ),
                                          """",
                                          ""
                                      ),
                                      7
                                  ), // example: "#00ff00"
                  // 
                  // STEP 4️⃣
                  //              Directly from Google: 
                  //              "data:image/svg+xml;utf8," is a prefix used to embed 
                  //              an SVG image directly into a web page as a data URI, 
                  //              indicating that the following data is an SVG image 
                  //              encoded in UTF-8 format.
                  //
                  SVGPrefix:      "data:image/svg+xml; utf8, "
              },
              //
              // Nexting with Functions here because we need
              // the previous with values for this one!
              //
              With( 
                  { 
                      SVGCodeWithNewColor: Substitute(
                                              SVGCode, 
                                              ReplacedColor, 
                                              ReplaceWith
                                          )
                  },
                  //
                  // Here, we'll just put these two strings together
                  // after we do a URL encode on SVGCodeWithNewColor
                  //
                  Concatenate( 
                      SVGPrefix,
                      EncodeUrl(SVGCodeWithNewColor)
                  )
              ) 
          )
    Properties:
      Fill: =Color.Transparent
      Height: |-
        =If(
            compSpinner.Visible,
            App.Height,
            0
        )
      Width: |-
        =If(
            compSpinner.Visible,
            App.Width,
            0
        )
    Children:
      - cntSpinner:
          Control: GroupContainer@1.3.0
          Variant: ManualLayout
          Properties:
            BorderColor: =Self.Fill
            BorderThickness: =2
            DropShadow: =DropShadow.None
            Fill: =compSpinner.InnerFill
            Height: =Parent.Height
            RadiusBottomLeft: =0
            RadiusBottomRight: =0
            RadiusTopLeft: =0
            RadiusTopRight: =0
            Width: =Parent.Width
          Children:
            - imgSpinner:
                Control: Image@2.2.3
                Properties:
                  Height: =compSpinner.InnerSpinnerHeight
                  Image: =compSpinner.SpinnerImage
                  Width: =compSpinner.InnerSpinnerWidth
                  X: =Abs((App.Width - Self.Width) / 2)
                  Y: =Abs((App.Height - Self.Height) / 2)
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
