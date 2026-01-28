# See All Icons in a Gallery

First of all, you need to implement the changes outlined in [all-icons-in-gallery.md](./all-icons-in-gallery.md) to your application. This will create a collection of all the icons in your application. Once you've done that, you can use the code below to create a gallery that displays all the icons.

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