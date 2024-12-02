

```PowerFx
- icoChangePointerToHand:
    Control: Classic/Icon
    Variant: 3DPrinting
    Properties:
      OnSelect: =Select(Parent)
      Color: =Color.Transparent
      Height: =Parent.TemplateHeight
      Icon: =Icon.Printing3D
      Width: =Parent.TemplateWidth
```