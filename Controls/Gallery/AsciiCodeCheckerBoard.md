# AsciiCodeCheckerBoard

This is some YAML you can paste into your canvas Power Apps applciation.
Once pasted into canvas Power Apps as YAML, you will get a gallery (vertical)
that displays the ASCII codes from 33 to 126 in a checkerboard pattern, and it 
will look like a black and white checkerboard.

## Add This to Your Application

```YAML
- galAsciiCodes:
    Control: Gallery
    Variant: galleryVertical
    Properties:
      Items: |-
        =ForAll(
            //
            // 33 is !
            // 126 is ~
            // These two numbers mark the beginning and end of the 
            // characters we're interested in!
            //
            // If you want more, add in the unicode chars: https://en.wikipedia.org/wiki/List_of_Unicode_characters
            //
            // ASCII Reference: https://en.wikipedia.org/wiki/ASCII
            //
            Sequence(126 - 33, 33, 1),
            {
                AsciiCode:  Value,
                Value:      Char(Value)
            }
        )
      WrapCount: =9
      DelayItemLoading: =true
      Fill: =RGBA(214, 221, 224, 1)
      Height: =Parent.Height
      Layout: =Layout.Vertical
      LoadingSpinner: =LoadingSpinner.Data
      TemplateFill: |-
        =If(
            Mod(
                ThisItem.AsciiCode,
                2
            ) = 1,
            Color.White,
            Color.Black
        )
      TemplateSize: =Self.Width / 9
      Transition: =Transition.Push
      Width: =Parent.Width
    Children:
    - Label13:
        Control: Label
        Properties:
          OnSelect: =Select(Parent)
          Text: =ThisItem.AsciiCode
          Color: |-
            =If(
                Mod(
                    ThisItem.AsciiCode,
                    2
                ) = 1,    
                Color.Black,
                Color.White
            )
          Width: =146.22222222222223
    - lblShowAsciiValue:
        Control: Label
        Properties:
          Text: =ThisItem.Value
          Align: =Align.Center
          Color: |-
            =If(
                Mod(
                    ThisItem.AsciiCode,
                    2
                ) = 1,    
                Color.Black,
                Color.White
            )
          Height: =Parent.TemplateHeight
          Size: =48
          Width: =Parent.TemplateWidth
```