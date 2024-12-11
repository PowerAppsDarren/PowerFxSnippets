# Basic Spinner

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```PowerFx
// ======================================================================
// ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
// Be sure to turn on the features in the settings of the canvas 
// Power Apps application
//      🔴 1. User-defined Functions
//      🔴 2. User-defined Types
// ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
// ====================================================================== 

//
// fxGetColoredSVGNoEncode
//
fxGetColoredSVGNoEncode(SVGText:Text, ColorToReplace:Text, DesiredColor:Text):Text =  
    Substitute(
        SVGText, 
        $"{ColorToReplace}", 
        $"{DesiredColor}"
    );

//
// fxSVGEncode
//
fxSVGEncode(svgCode:Text):Text = 
    "data:image/svg+xml; utf8, " & EncodeUrl(svgCode);

//
// fxSpinnerSimple
//
fxSpinnerSimple():Text = fxSVGEncode(
    fxGetColoredSVGNoEncode(
        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 100 100"" preserveAspectRatio=""xMidYMid"" width=""200"" height=""200"" style=""shape-rendering: auto; display: block; background: transparent;"" xmlns:xlink=""http://www.w3.org/1999/xlink""><g><path stroke=""none"" fill=""#000000"" d=""M10 50A40 40 0 0 0 90 50A40 43.5 0 0 1 10 50""><animateTransform values=""0 50 51.75;360 50 51.75"" keyTimes=""0;1"" repeatCount=""indefinite"" dur=""1.1764705882352942s"" type=""rotate"" attributeName=""transform""></animateTransform></path><g></g></g></svg>", 
        "#000000",
        Substitute(JSON(App.Theme.Colors.Primary), """", "")
    )
);
```

## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co)
* https://superpowerlabs.co 

---

## Disclaimer

**THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**

```
- Image1:
    Control: Image
    Properties:
      Image: ="data:image/svg+xml; utf8, " & EncodeUrl("<svg  viewBox='0 0 2048 2048' xmlns='http://www.w3.org/2000/svg'><path d='M1754 1220l142 308-338 30-30 338-308-142-196 277-196-277-308 142-30-338-338-30 142-308-277-196 277-196-142-308 338-30 30-338 308 142 196-277 196 277 308-142 30 338 338 30-142 308 277 196-277 196zm-50 196l-111-240 216-152-216-152 111-240-264-24-24-264-240 111-152-216-152 216-240-111-24 264-264 24 111 240-216 152 216 152-111 240 264 24 24 264 240-111 152 216 152-216 240 111 24-264 264-24z' fill='#000000'></path></svg>")
      BorderThickness: =4
      Height: =414
      Width: =496
      X: =102
      Y: =84
```