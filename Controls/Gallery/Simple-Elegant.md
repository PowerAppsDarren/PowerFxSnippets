# Simple, Yet Elegant

![Images/gallery-elegant.png](Images/gallery-elegant.png)

- This gallery is a simple yet elegant way to display a list of items. 
- The gallery is contained within a GroupContainer that has a semibold drop shadow and a dotted border style. 
- The gallery itself has a light gray fill and a thin primary color border. 
- Each item in the gallery has a light gray fill and a white fill when selected. 
- The gallery items are displayed in a vertical layout and have a transition effect of push. 
- Each item in the gallery displays the first and last name of the user and their title. 
- The gallery items have a padding of 2 and a height of 50. 
- The gallery items have a badge that displays the first initial of the first and last name of the user. The badge has a rounded shape and a brand theme color. The badge is vertically aligned in the middle of the gallery item. The gallery has a header that displays the text "APP USERS" in white with a semibold font weight. The header has a primary color fill and a height of 50. The header has a border on the bottom that matches the primary color of the header fill. The header has a padding of 10 on the left side. The header has a width that matches the width of the parent container. The header has a radius of 0 on the top left, top right, bottom left, and bottom right corners. The header is positioned at the top of the parent container. The gallery is contained within a GroupContainer that has a primary color fill and a semibold drop shadow. The container has a border that matches the primary color of the fill and a thickness of 2. The container has a radius of 12 on the top left, top right, bottom left, and bottom right corners. The container has a width that matches the width of the parent container. The container has a height that matches the height of the parent container minus the padding on the top and bottom. The container is positioned 40 pixels from the left and top edges of the parent container. The gallery is positioned 40 pixels from the left and top edges of the container. The gallery has a width that matches the width of the parent container minus the padding on the left and right. The gallery has a height that matches the height of the parent container minus the padding on the top. The gallery is positioned below the header and has a height that matches the height of the parent container minus the height of the header and the padding on the top. The gallery has a width that matches the

```PowerFx- ctrGalleryContainingShadow:
    Control: GroupContainer@1.3.0
    Variant: AutoLayout
    Properties:
      BorderStyle: =BorderStyle.Dotted
      DropShadow: =DropShadow.None
      Height: =348
      LayoutDirection: =LayoutDirection.Vertical
      PaddingBottom: =30
      PaddingLeft: =20
      PaddingRight: =20
      PaddingTop: =20
      Width: =350
      X: =222
      Y: =225
    Children:
      - cntGalleryGrouping:
          Control: GroupContainer@1.3.0
          Variant: ManualLayout
          Properties:
            BorderColor: =App.Theme.Colors.Primary
            BorderThickness: =2
            DropShadow: =DropShadow.Semibold
            Height: =Parent.Height - Self.Y * 2
            RadiusBottomLeft: =12
            RadiusBottomRight: =12
            RadiusTopLeft: =12
            RadiusTopRight: =12
            Width: =612
            X: =40
            Y: =40
          Children:
            - galListing:
                Control: Gallery@2.15.0
                Variant: Vertical
                Properties:
                  BorderColor: =App.Theme.Colors.Primary
                  BorderThickness: =2
                  Fill: =ColorValue("#f5f5f5")
                  Height: =Parent.Height - Self.Y
                  Items: |-
                    =[
                        {
                            FirstName: "Darren", 
                            LastName: "Reese", 
                            Title: "Darren Reese"
                        },
                        {
                            FirstName: "John", 
                            LastName: "Smith", 
                            Title: "Jonny Smithers"
                        },
                        {
                            FirstName: "Jane", 
                            LastName: "Doe", 
                            Title: "Janie Doe"
                        },
                        {
                            FirstName: "Brian", 
                            LastName: "Powell", 
                            Title: "Brian Powell, the 3rd"
                        }
                    ]
                  TemplateFill: =If(ThisItem.IsSelected, App.Theme.Colors.Lighter80, Color.White)
                  TemplatePadding: =2
                  TemplateSize: =50
                  Transition: =Transition.Push
                  Width: =Parent.Width - Self.X
                  Y: =cntGalleryHeader.Height + cntGalleryHeader.Y
                Children:
                  - lblField02:
                      Control: Label@2.5.1
                      Properties:
                        Color: =fxFontTextColor
                        Height: =Parent.TemplateHeight
                        OnSelect: =Select(Parent)
                        PaddingLeft: =10
                        Text: =ThisItem.Title
                        Width: =lblHeading02.Width
                        X: =lblHeading02.X
                  - BadgeCanvas1:
                      Control: Badge@0.0.24
                      Properties:
                        Appearance: =If(ThisItem.IsSelected, 'BadgeCanvas.Appearance'.Filled, 'BadgeCanvas.Appearance'.Tint)
                        Content: =Left(ThisItem.FirstName, 1) & Left(ThisItem.LastName, 1)
                        Shape: ='BadgeCanvas.Shape'.Rounded
                        ThemeColor: ='BadgeCanvas.ThemeColor'.Brand
                        VerticalAlign: =VerticalAlign.Middle
                        X: =fxConstants.Controls.Margin
                        Y: '=fxGetCenteredDimension(Parent.TemplateHeight, Self.Height) '
            - cntGalleryHeader:
                Control: GroupContainer@1.3.0
                Variant: ManualLayout
                Properties:
                  Fill: =App.Theme.Colors.Primary
                  Height: =50
                  RadiusBottomLeft: =0
                  RadiusBottomRight: =0
                  RadiusTopLeft: =0
                  RadiusTopRight: =0
                  Width: =Parent.Width
                Children:
                  - lblHeading01:
                      Control: Label@2.5.1
                      Properties:
                        Color: =RGBA(255, 255, 255, 1)
                        FontWeight: =FontWeight.Semibold
                        Height: =Parent.Height
                        PaddingLeft: =10
                        Size: =15
                        Text: =
                        Width: =50
                  - lblHeading02:
                      Control: Label@2.5.1
                      Properties:
                        Color: =RGBA(255, 255, 255, 1)
                        FontWeight: =FontWeight.Semibold
                        Height: =Parent.Height
                        PaddingLeft: =10
                        Size: =15
                        Text: ="APP USERS"
                        Width: =Parent.Width - Self.X
                        X: =lblHeading01.X + lblHeading01.Width
```
