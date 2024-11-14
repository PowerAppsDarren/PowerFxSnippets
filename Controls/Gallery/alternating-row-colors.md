# Alternating Row Colors

In order to do alternating row colors in a Power Apps gallery control, you can use the following code to produce a great example on how to do this. This formula will alternate between two colors based on the index of the gallery item. You can replace the colors with your own as needed. 

How do we determine if a row should be 1 color or another? We use the [Mod](https://powerplatformlinks.com/Power+Apps/Canvas/Functions/Mod) function to determine if the index of the gallery item is even or odd. If it's even, we use one color, if it's odd, we use another. 

Here's the YAML code to paste into a screen in Power Apps Studio:

## Add This to Your Application

```PowerFx
- cntGalleryGrouping_1:
    Control: GroupContainer
    Variant: manualLayoutContainer
    Properties:
      BorderColor: =App.Theme.Colors.Primary
      BorderThickness: =4
      DropShadow: =DropShadow.Semibold
      Height: =Parent.Height - Self.Y * 2
      RadiusBottomLeft: =Self.RadiusTopLeft
      RadiusBottomRight: =Self.RadiusTopLeft
      RadiusTopLeft: =8
      RadiusTopRight: =Self.RadiusTopLeft
      Width: =Parent.Width - Self.X * 2
      X: =40
      Y: =40
    Children:
    - cntGalleryHeader_1:
        Control: GroupContainer
        Variant: manualLayoutContainer
        Properties:
          BorderColor: =Self.Fill
          BorderThickness: =4
          Fill: =App.Theme.Colors.Primary
          Height: =50
          RadiusBottomLeft: =0
          RadiusBottomRight: =0
          RadiusTopLeft: =0
          RadiusTopRight: =0
          Width: =Parent.Width
        Children:
        - lblHeading01_1:
            Control: Label
            Properties:
              Text: ="ORDINAL NUMBER"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
              Width: =210
        - lblHeading02_1:
            Control: Label
            Properties:
              Text: ="TITLE"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
              Width: =200
              X: =lblHeading01_1.X + lblHeading01_1.Width
        - lblHeading03_1:
            Control: Label
            Properties:
              Text: ="DESCRIPTION"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
              Width: =Parent.Width - Self.X - fxConstants.Control.Height
              X: =lblHeading02_1.X + lblHeading02_1.Width
    - galListing_1:
        Control: Gallery
        Variant: galleryVertical
        Properties:
          Items: |-
            =With(
                {
                    Data: CustomGallerySample,
                    RecordCount: CountRows(CustomGallerySample)
                }, 
                ForAll(
                    Sequence(RecordCount * 2) As OrdinalPosition, 
                    AddColumns(
                        Index(
                            Data, 
                            If(
                                OrdinalPosition.Value > RecordCount, 
                                OrdinalPosition.Value - RecordCount, 
                                OrdinalPosition.Value
                            )
                        ), 
                        OrderNumber, OrdinalPosition.Value,
                        TemplateFill,   If(
                                            Mod(OrdinalPosition.Value, 2) = 0, 
                                            Color.White, 
                                            ColorFade(App.Theme.Colors.Lighter80, 50%)
                                        )
                    )
                )
            )
          BorderColor: =App.Theme.Colors.Primary
          BorderThickness: =4
          DelayItemLoading: =true
          Fill: =ColorValue("#dddddd")
          Height: =Parent.Height - Self.Y
          Layout: =Layout.Vertical
          LoadingSpinner: =LoadingSpinner.Data
          TemplateFill: =ThisItem.TemplateFill
          TemplatePadding: =3
          TemplateSize: =60
          Width: =Parent.Width - Self.X
          Y: =cntGalleryHeader_1.Height + cntGalleryHeader_1.Y
        Children:
        - Icon1:
            Control: Classic/Icon
            Variant: NextArrow
            Properties:
              OnSelect: =Select(Parent)
              Height: =60
              Icon: =Icon.NextArrow
              PaddingBottom: =10
              PaddingLeft: =10
              PaddingRight: =10
              PaddingTop: =10
              Visible: =ThisItem.IsSelected
              X: =1212
        - lblField03_1:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: =ThisItem.SampleText
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              Width: =lblHeading03_1.Width
              X: =lblHeading03_1.X
        - lblField02_1:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: |-
                =Concat( 
                    FirstN(
                        Split(
                            ThisItem.SampleHeading, 
                            " " 
                        ),
                        2
                    ) As MyRecord, 
                    MyRecord.Value & " "
                ) & ThisItem.OrderNumber
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              Width: =lblHeading02_1.Width
              X: =lblHeading02_1.X
        - lblField01_1:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: =ThisItem.OrderNumber
              Align: =Align.Right
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              PaddingRight: =40
              Width: =lblHeading01_1.Width
              X: =lblHeading01_1.X

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

