# Best-SVG-Snippet

Here is the best SVG snippet that I've found so far. It's a bit more complex than the other snippets, but it's worth it. 

## Get These Ready!

1. **SVG Code**: You can easily find SVG code on the net. SVG code will begin and end with a single double quote ("). There will be other double quotes inside the SVG code. You must double up on those! ...otherwise PowerFx will be confused and thinks that you're trying to end and start other strings inside. This is what is called an 'escape sequence' in the programming world.
2. **Color to Replace**: You will probably find something like this (fill="#000000"), which is black as you see in the above example. It could be some other Color, so adjust accordingly.
3. **Color to Replace With**: Hexadecimal, also known as "hex", is a numbering system that uses 16 symbols to represent numbers instead of the 10 symbols used in the decimal system. If you don't already have a color hex code you'd like to use, you may need to use the JSON function like you see below. If you use JSON, you will need to get rid of the double quotes using the Substitute function. ...And, to get rid of the extra hex code that defines the opacity Use the Left() function with the numeric value of 7. A hex code for a color is typically 6 characters (`00` through `ff` each). 0 or 00 is hex for zero. f or ff is hex for 255! #: this symbol is signifying that the rest is a hexidecimal value R: The first hex value after the `#` is for how much Red will be in the final color. G: The second hex value after the red is for how much Green will be in the final color. B: The subsequent hex value after the green is for how much Blue will be in the final color.
4. **SVG Prefix**: Directly from Google: "data:image/svg+xml;utf8," is a prefix used to embed an SVG image directly into a web page as a data URI, indicating that the following data is an SVG image encoded in UTF-8 format.
5. **SVG Code with New Color**: Here, we'll just put these two strings together after we do a URL encode on SVGCodeWithNewColor

## Put this code in your Image

```PowerFx
With( 
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
                                    cmpSpinner.PrimaryThemeColor,
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
```