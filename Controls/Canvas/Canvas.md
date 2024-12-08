# Canvas Control

This is some YAML you can paste into your canvas Power Apps applciation.

## Canvas Control Only

```PowerFx
- canCanvas:
    Control: FluidGrid
    Variant: fluidGridWithBlankCard
    Properties:
      BorderThickness: =0
      Height: =Parent.Height - Self.Y
      Width: =Parent.Width
      Y: =Self.X
```

## Canvas with Data Cards

```PowerFx
- canCanvas:
    Control: FluidGrid
    Variant: fluidGridWithBlankCard
    Properties:
      BorderThickness: =0
      Height: =Parent.Height - Self.Y
      Width: =Parent.Width
      Y: =Self.X
    Children:
    - dcdDataCard01:
        Control: DataCard
        Properties:
          BorderColor: =If(StartsWith(Host.Version, "PowerApps-Studio"), RGBA(245, 245, 245, 1), Color.Transparent)
          BorderStyle: =BorderStyle.Dashed
          BorderThickness: =4
          Height: =180
          Width: =Parent.Width
        Children:
        - cntContainer01:
            Control: GroupContainer
            Variant: manualLayoutContainer
            Properties:
              BorderColor: =ColorValue("#dddddd")
              BorderThickness: =2
              DropShadow: =DropShadow.Semibold
              Fill: =ColorValue("#f5f5f5")
              Height: =Parent.Height - Self.Y * 2.3
              RadiusBottomLeft: =8
              RadiusBottomRight: =8
              RadiusTopLeft: =8
              RadiusTopRight: =8
              Width: =Parent.Width - Self.X * 2
              X: =25
              Y: =25
    - dcdDataCard02:
        Control: DataCard
        Properties:
          BorderColor: =If(StartsWith(Host.Version, "PowerApps-Studio"), RGBA(245, 245, 245, 1), Color.Transparent)
          BorderStyle: =BorderStyle.Dashed
          BorderThickness: =4
          Height: =180
          Width: =Parent.Width
        Children:
        - cntContainer02:
            Control: GroupContainer
            Variant: manualLayoutContainer
            Properties:
              BorderColor: =ColorValue("#dddddd")
              BorderThickness: =2
              DropShadow: =DropShadow.Semibold
              Fill: =ColorValue("#f5f5f5")
              Height: =Parent.Height - Self.Y * 2.3
              RadiusBottomLeft: =8
              RadiusBottomRight: =8
              RadiusTopLeft: =8
              RadiusTopRight: =8
              Width: =Parent.Width - Self.X * 2
              X: =25
              Y: =25
    - dcdDataCard03:
        Control: DataCard
        Properties:
          BorderColor: =If(StartsWith(Host.Version, "PowerApps-Studio"), RGBA(245, 245, 245, 1), Color.Transparent)
          BorderStyle: =BorderStyle.Dashed
          BorderThickness: =4
          Height: =180
          Width: =Parent.Width
        Children:
        - cntContainer03:
            Control: GroupContainer
            Variant: manualLayoutContainer
            Properties:
              BorderColor: =ColorValue("#dddddd")
              BorderThickness: =2
              DropShadow: =DropShadow.Semibold
              Fill: =ColorValue("#f5f5f5")
              Height: =Parent.Height - Self.Y * 2.3
              RadiusBottomLeft: =8
              RadiusBottomRight: =8
              RadiusTopLeft: =8
              RadiusTopRight: =8
              Width: =Parent.Width - Self.X * 2
              X: =25
              Y: =25
```


## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗