---
title: Pad Numbers Inside String
description: Collection of user-defined functions for padding, extracting, and formatting numbers embedded within strings
category: string-manipulation/padding
tags:
  - padding
  - numbers
  - formatting
  - text-extraction
  - user-defined-function
related:
  - ../transformations/eliminate-string-within-string
  - ../parsing/find-string-exactly-within-table
---

# Pad Numbers Inside String


```PowerFx
    // =======================================================
    //
    // Darren added the following code to help with...
    //
    //      fxPadNumbers                    (StringValue:Text):Text
    //      fxGetNumericPosition            (StringValue:Text):Number
    //      fxGetBeforeDuringAfterNumeric   (StringValue:Text):fxNumericHandlingType
    //      fxGetEndingNumericPosition      (StringValue:Text):Number
    //      fxGetNumericEndingPosition      (StringValue:Text):Number
    //      fxMakeNumeric                   (StringValue:Text):Text
    //      fxNumericHandlingType           (user-defined type)
    //      fxFormatNumberAsText            (StringValue:Text):Text
    //
    // =======================================================

    fxPadNumbers(StringValue:Text):Text = (
        If(
            IsNumeric(
                StringValue
            ),
            StringValue,
            fxMakeNumeric(StringValue)
        )
    );

    //
    // EXAMPLE: fxGetNumericPosition("ABC123XYZ")
    //          LEN: 9
    //
    fxGetNumericPosition(StringValue:Text):Number = (
        Value(
            First(
                Split(
                    Trim( 
                        Concat(
                            ForAll(
                                Sequence(Len(StringValue)) As my,
                                With(
                                    { 
                                        myChar: Mid(StringValue, my.Value, 1)
                                    },
                                    If(
                                        IsNumeric(myChar),  // F, F, F, T, T, T, F, F, F
                                        " " & my.Value & " ",
                                        " "
                                    )
                                )
                            ), 
                            Value 
                        )                                   // "   123   " 

                                                                // " "
                                                                // " "
                                                                // " "
                                                                // " 4 "
                                                                // " 5 "
                                                                // " 6 "
                                                                // " "
                                                                // " "
                                                                // " "

                                                            // Trim gives us..
                                                            // "4 5 6"
                    ),  
                    " "
                )
            ).Value
        ) 
    );

    fxFormatNumberAsText(NumberString:Text):Text = Text(
        Value(NumberString), 
        "0000.00"
    );

    fxGetBeforeDuringAfterNumeric(StringValue:Text):fxNumericHandlingType = (
        With(
            {
                myBeginning:    fxGetNumericPosition(StringValue), 
                myEnding:       fxGetEndingNumericPosition(StringValue)
            },
            {
                BeforeNumber:
                    Mid(
                        StringValue,
                        1,
                        myBeginning - 1
                    ),
                NumberText:                         
                    Mid(
                        StringValue,
                        myBeginning,
                        myEnding - myBeginning + 1
                    ),
                AfterNumber:
                    Mid(
                        StringValue,
                        myEnding + 1
                    )
            }
        )
    );

    //
    // EXAMPLE: fxGetNumericPosition("ABC123XYZ")
    //          LEN: 9
    //
    fxGetEndingNumericPosition(StringValue:Text):Number = (
        Value(
            Index(
                Split(
                    Trim( 
                        Concat(
                            ForAll(
                                Sequence(Len(StringValue)) As my,
                                With(
                                    { 
                                        myChar: Mid(StringValue, my.Value, 1)
                                    },
                                    If(
                                        IsNumeric(myChar),  // F, F, F, T, T, T, F, F, F
                                        " " & my.Value & " ",
                                        " "
                                    )
                                )
                            ), 
                            Value 
                        )
                                        //"DRILLING SUPPORT -- DRILL SHIELD 30" -- DS10 - 8' -- EACH"
                                        //"                                 30            8         "
                                        //                                  ^34
                        
                                                        // "   123   " 

                                                                // " "
                                                                // " "
                                                                // " "
                                                                // " 4 "
                                                                // " 5 "
                                                                // " 6 "
                                                                // " "
                                                                // " "
                                                                // " "
                                                                
                                                            // Trim gives us..
                                                            // "4 5 6"
                    ),  
                    " "
                ), 
                2
            ).Value
        ) 
    );

    fxGetNumericEndingPosition__OLD(StringValue:Text):Number = (
        Value(
            First( 
                ForAll(
                    Sequence(Len(StringValue)) As my,
                    With(
                        { 
                            myChar: Mid(StringValue, my.Value, 1)
                        },
                        If(
                            IsNumeric(myChar),
                            myChar,
                            myChar & ","
                        )
                    )
                )
            ).Value   
        ) - 1
    );

    fxMakeNumeric(StringValue:Text):Text = (
        Concat(
            ForAll(
                Sequence(Len(StringValue)) As my,
                With(
                    { 
                        myChar:Mid(StringValue,my.Value,1)
                    },
                    If(
                        IsNumeric(myChar),
                        myChar,
                        If(
                            myChar = ".", 
                            myChar, 
                            ""
                        )
                    )
                )
            ),
            Value
        )
    );

    fxNumericHandlingType:= Type(
        {
            BeforeNumber:Text,
            NumberText:Text,
            AfterNumber:Text
        }
    );

    fxFindcharacter(StringValue:Text, LookForChar:Text):Number = (
        With(
            {
                myPosition: Find(LookForChar,StringValue)
            },
            If(IsBlank( myPosition), 0, myPosition)
        )
    );
```

---

# Parting Thoughts

### Free Community & Course Materials

🆓 Get access to our [free community and resources](https://tinyurl.com/DarrensStuffFree) ⬅️

### Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to message us from [Our Website](https://superpowerlabs.co) or check out our 
- [YouTube Channel](https://youtube.com/superpowerlabs).
- https://powerplatformlinks.com/

### Disclaimer

THIS CODE IS PROVIDED **AS IS WITHOUT WARRANTY OF ANY KIND**, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
