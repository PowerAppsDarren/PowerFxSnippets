# Spacer Medium Rectangle

This is a helpful canvas Power Apps code snippet.

## Add This to Your Application

```PowerFx
- retSpacerGuide:
    Control: Rectangle
    Properties:
      AccessibleLabel: ="This is just a spacer guide control."
      Tooltip: ="This is just a spacer guide control."
      BorderColor: =Color.Red // An annoying color that stands out
      BorderThickness: =1
      Fill: =RGBA(0, 255, 0, 1) // An annoying color that stands out
      Height: =fxConstants.Spacing.SpacingMd // 20
      Visible: =fxIsStudioMode // StartsWith(Host.Version, "PowerApps-Studio")
      Width: =fxConstants.Spacing.SpacingMd // 20
      X: =Parent.Width - Self.Width
      Y: =Parent.Height - Self.Height
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

