# Nested Galleries

This is a helpful canvas Power Apps code snippet.

[[nested-galleries.msapp]]

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/e7d61632ead649a096a4881d96ec96f0?sid=4e311220-82a9-4a07-9364-6d38475e4f3c" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Add This to Your Application

```PowerFx
- btnGenData:
    Control: Button
    Properties:
      OnSelect: |-
        =ClearCollect(
            colMasterData, 
            ForAll(
                Sequence(6) As My, 
                {
                    Title: "#" & My.Value & " - Master Data Table",
                    DetailTable: 
                        ForAll(
                            Sequence(RandBetween(1, 8)), 
                            {
                                Title: "#" & ThisRecord.Value & " - " & GUID()
                            }
                        )
                }
            )    
        )
      Text: ="Create Data"
      Height: =42
      Width: =132
      X: =24
      Y: =27
- galParent:
    Control: Gallery
    Variant: variableTemplateHeightGallery
    Properties:
      Items: =colMasterData
      BorderThickness: =4
      DelayItemLoading: =true
      Fill: =RGBA(106, 122, 127, 1)
      Height: =Parent.Height - Self.Y - 40
      Layout: =Layout.Vertical
      LoadingSpinner: =LoadingSpinner.Data
      TemplateFill: =Color.White
      TemplatePadding: =1
      TemplateSize: =300
      Width: =1314
      X: =24
      Y: =87
    Children:
    - Label1:
        Control: Label
        Properties:
          OnSelect: =Select(Parent)
          Text: =ThisItem.Title
          BorderThickness: =1
          Height: =50
          Width: =608
          X: =10
          Y: =10
    - galChild:
        Control: Gallery
        Variant: galleryVertical
        Properties:
          Items: |-
            =ThisItem.DetailTable
            //Filter(Table2, FK = ThisItem.ID)
          BorderStyle: =BorderStyle.Dotted
          BorderThickness: =4
          DelayItemLoading: =true
          Fill: =RGBA(253, 207, 180, 1)
          Height: =Self.AllItemsCount * 52 + 4
          Layout: =Layout.Vertical
          LoadingSpinner: =LoadingSpinner.Data
          TemplateFill: =Color.AliceBlue
          TemplatePadding: =2
          TemplateSize: =50
          Width: =638
          X: =80
          Y: =80
        Children:
        - TextCanvas4_1:
            Control: Text
            Properties:
              Text: =Upper(ThisItem.Title)
              Height: |
                =50
              Width: =448
              X: =40

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

