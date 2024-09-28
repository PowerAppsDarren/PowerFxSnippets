# See All Icons in a Gallery

[After you add this code into your App.Formulas](all-icons-in-gallery.md), then you can use the code below to see them all in a gallery!

## Add This to Your Application

```JavaScript
- galIcons:
    Control: Gallery
    Variant: galleryVertical
    Properties:
      OnSelect: =
      Items: =fxIcons
      WrapCount: =4
      BorderColor: =Self.Fill
      BorderThickness: =4
      Fill: =RGBA(245, 245, 245, 1)
      Height: =685
      Layout: =Layout.Vertical
      TemplateFill: =Color.White
      TemplatePadding: =4
      TemplateSize: =80
      Width: =1261
      X: =45
      Y: =36
    Children:
    - lblIconName:
        Control: Label
        Properties:
          OnSelect: =Select(Parent)
          Text: =ThisItem.Category
          Color: =ColorValue("#555555")
          Height: =Parent.TemplateHeight
          Width: =Parent.TemplateWidth - Self.X
          X: =icoIcon.Width
    - icoIcon:
        Control: Classic/Icon
        Variant: 3DPrinting
        Properties:
          AccessibleLabel: =ThisItem.Name
          Tooltip: ="ThisItem.Name"
          Color: =ColorValue("#555555")
          Height: =Parent.TemplateHeight
          Icon: =ThisItem.Icon
          PaddingBottom: =Self.Height * 15%
          PaddingLeft: =Self.Height * 15%
          PaddingRight: =Self.Height * 15%
          PaddingTop: =Self.Height * 15%
          Width: =Self.Height
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
