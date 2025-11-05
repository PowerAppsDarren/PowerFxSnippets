# Code Editor

This is some YAML you can paste into your canvas Power Apps applciation that will serve well as a code editor. It's a multi-line text input that has a Courier New font and a grey background. It's also got some padding so it looks nice. You can use it to edit your Power Apps code, or to edit any other kind of code. It's a great way to get started with Power Apps development, or to learn about Power Apps development.

## Add This to Your Application

```PowerFx
- txtCodeEditor:
    Control: Classic/TextInput
    Properties:
      Default: |-
        ="- CONTROL_NAME_GOES_HERE:
            Control: Button"
      Clear: =true
      DisabledBorderColor: =Self.Fill
      Font: =Font.'Courier New'
      Height: =Parent.Height - Self.Y * 2
      HoverFill: =Self.Fill
      LineHeight: =1.4
      Mode: =TextMode.MultiLine
      PaddingBottom: =10
      PaddingLeft: =10
      PaddingRight: =10
      PaddingTop: =10
      Size: =18
      Width: =Parent.Width - Self.X * 2
      X: =20
      Y: =20
```

## Free Community & Course Materials
🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com 

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

