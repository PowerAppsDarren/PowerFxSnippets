# Sample Fonts Screen

To make this reusable and more efficient, paste in the code from [this code snippet](Add-to-App-Formulas.md), then replace the `Items` property with `fxExp_Fonts` once you have done so. No need to have duplicate code. This code is shared as is so that if you didn't use App.Formulas, you can still use this code snippet to create a gallery that shows the available fonts in Power Apps.

![Sample Fonts Screen](fonts-screen.png)

```yaml
Screens:
  Fonts Screen:
    Properties:
      Fill: =App.Theme.Colors.Lighter70
    Children:
      - galFonts:
          Control: Gallery@2.15.0
          Variant: Vertical
          Properties:
            BorderColor: =Self.Fill
            BorderThickness: =2
            Fill: =RGBA(237, 237, 237, 1)
            Height: =Parent.Height - Self.Y * 2
            Items: |-
              =Sort(
                  [
                      {
                          ID: 1,
                          SortOrder: 100,
                          FontName: "Agency FB",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Agency FB, Arial, Helvetica, Verdana"
                      },
                      {
                          ID: 2,
                          SortOrder: 110,
                          FontName: "Algerian",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Algerian, Impact, Arial, Verdana"
                      },
                      {
                          ID: 3,
                          SortOrder: 120,
                          FontName: "Arial",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Arial, Helvetica, Verdana, Tahoma"
                      },
                      {
                          ID: 4,
                          SortOrder: 130,
                          FontName: "Arial Rounded MT",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Arial Rounded MT, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 5,
                          SortOrder: 140,
                          FontName: "Bahnschrift",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Bahnschrift, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 6,
                          SortOrder: 150,
                          FontName: "Baskerville Old Face",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Baskerville Old Face, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 7,
                          SortOrder: 160,
                          FontName: "Bauhaus 93",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Bauhaus 93, Impact, Arial, Verdana"
                      },
                      {
                          ID: 8,
                          SortOrder: 170,
                          FontName: "Bell MT",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Bell MT, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 9,
                          SortOrder: 180,
                          FontName: "Berlin Sans FB",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Berlin Sans FB, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 10,
                          SortOrder: 190,
                          FontName: "Bernard MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Bernard MT, Impact, Arial, Verdana"
                      },
                      {
                          ID: 11,
                          SortOrder: 200,
                          FontName: "Blackadder ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Blackadder ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 12,
                          SortOrder: 210,
                          FontName: "Bodoni MT",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Bodoni MT, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 13,
                          SortOrder: 220,
                          FontName: "Bodoni MT Poster",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Bodoni MT Poster, Impact, Georgia, Times New Roman"
                      },
                      {
                          ID: 14,
                          SortOrder: 230,
                          FontName: "Book Antiqua",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Book Antiqua, Palatino Linotype, Georgia, Times New Roman"
                      },
                      {
                          ID: 15,
                          SortOrder: 240,
                          FontName: "Bookman Old Style",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Bookman Old Style, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 16,
                          SortOrder: 250,
                          FontName: "Bookshelf Symbol 7",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Bookshelf Symbol 7, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 17,
                          SortOrder: 260,
                          FontName: "Bradley Hand ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Bradley Hand ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 18,
                          SortOrder: 270,
                          FontName: "Britannic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Britannic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 19,
                          SortOrder: 280,
                          FontName: "Broadway",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Broadway, Impact, Arial, Verdana"
                      },
                      {
                          ID: 20,
                          SortOrder: 290,
                          FontName: "Brush Script MT",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Brush Script MT, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 21,
                          SortOrder: 300,
                          FontName: "Calibri",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Calibri, Candara, Segoe UI, Arial"
                      },
                      {
                          ID: 22,
                          SortOrder: 310,
                          FontName: "Californian FB",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Californian FB, Georgia, Palatino Linotype, Times New Roman"
                      },
                      {
                          ID: 23,
                          SortOrder: 320,
                          FontName: "Calisto MT",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Calisto MT, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 24,
                          SortOrder: 330,
                          FontName: "Cambria",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Cambria, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 25,
                          SortOrder: 340,
                          FontName: "Cambria Math",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Cambria Math, Cambria, Georgia, Times New Roman"
                      },
                      {
                          ID: 26,
                          SortOrder: 350,
                          FontName: "Candara",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Candara, Calibri, Segoe UI, Arial"
                      },
                      {
                          ID: 27,
                          SortOrder: 360,
                          FontName: "Castellar",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Castellar, Impact, Arial, Verdana"
                      },
                      {
                          ID: 28,
                          SortOrder: 370,
                          FontName: "Centaur",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Centaur, Palatino Linotype, Georgia, Times New Roman"
                      },
                      {
                          ID: 29,
                          SortOrder: 380,
                          FontName: "Century",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Century, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 30,
                          SortOrder: 390,
                          FontName: "Century Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Century Gothic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 31,
                          SortOrder: 400,
                          FontName: "Century Schoolbook",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Century Schoolbook, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 32,
                          SortOrder: 410,
                          FontName: "Chiller",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Chiller, Impact, Arial, Verdana"
                      },
                      {
                          ID: 33,
                          SortOrder: 420,
                          FontName: "Colonna MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Colonna MT, Impact, Georgia, Times New Roman"
                      },
                      {
                          ID: 34,
                          SortOrder: 430,
                          FontName: "Comic Sans MS",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Comic Sans MS, Verdana, Arial, Tahoma"
                      },
                      {
                          ID: 35,
                          SortOrder: 440,
                          FontName: "Consolas",
                          IsPowerAppsFont: false,
                          Category: "Monospace",
                          IsWebSafe: true,
                          BestUse: "Body",
                          Family: "Consolas, Courier New, Lucida Console, monospace"
                      },
                      {
                          ID: 36,
                          SortOrder: 450,
                          FontName: "Constantia",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Constantia, Georgia, Cambria, Times New Roman"
                      },
                      {
                          ID: 37,
                          SortOrder: 460,
                          FontName: "Cooper",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Cooper, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 38,
                          SortOrder: 470,
                          FontName: "Copperplate Gothic",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Copperplate Gothic, Impact, Arial, Verdana"
                      },
                      {
                          ID: 39,
                          SortOrder: 480,
                          FontName: "Corbel",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Corbel, Candara, Calibri, Arial"
                      },
                      {
                          ID: 40,
                          SortOrder: 490,
                          FontName: "Courier New",
                          IsPowerAppsFont: true,
                          Category: "Monospace",
                          IsWebSafe: true,
                          BestUse: "Body",
                          Family: "Courier New, Consolas, Lucida Console, monospace"
                      },
                      {
                          ID: 41,
                          SortOrder: 500,
                          FontName: "Curlz MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Curlz MT, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 42,
                          SortOrder: 510,
                          FontName: "Dancing Script",
                          IsPowerAppsFont: true,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Dancing Script, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 43,
                          SortOrder: 520,
                          FontName: "Dubai",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Dubai, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 44,
                          SortOrder: 530,
                          FontName: "Ebrima",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Ebrima, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 45,
                          SortOrder: 540,
                          FontName: "Edwardian Script ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Edwardian Script ITC, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 46,
                          SortOrder: 550,
                          FontName: "Elephant",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Elephant, Georgia, Times New Roman, Impact"
                      },
                      {
                          ID: 47,
                          SortOrder: 560,
                          FontName: "Engravers MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Engravers MT, Impact, Arial, Verdana"
                      },
                      {
                          ID: 48,
                          SortOrder: 570,
                          FontName: "Eras ITC",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Eras ITC, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 49,
                          SortOrder: 580,
                          FontName: "Felix Titling",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Felix Titling, Impact, Georgia, Times New Roman"
                      },
                      {
                          ID: 50,
                          SortOrder: 590,
                          FontName: "Footlight MT",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Footlight MT, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 51,
                          SortOrder: 600,
                          FontName: "Forte",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Forte, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 52,
                          SortOrder: 610,
                          FontName: "Franklin Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Franklin Gothic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 53,
                          SortOrder: 620,
                          FontName: "Franklin Gothic Book",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Franklin Gothic Book, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 54,
                          SortOrder: 630,
                          FontName: "Freestyle Script",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Freestyle Script, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 55,
                          SortOrder: 640,
                          FontName: "French Script MT",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "French Script MT, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 56,
                          SortOrder: 650,
                          FontName: "Gabriola",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Gabriola, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 57,
                          SortOrder: 660,
                          FontName: "Gadugi",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Gadugi, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 58,
                          SortOrder: 670,
                          FontName: "Garamond",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Garamond, Georgia, Palatino Linotype, Times New Roman"
                      },
                      {
                          ID: 59,
                          SortOrder: 680,
                          FontName: "Georgia",
                          IsPowerAppsFont: true,
                          Category: "Serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Georgia, Times New Roman, Palatino Linotype, Cambria"
                      },
                      {
                          ID: 60,
                          SortOrder: 690,
                          FontName: "Gigi",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Gigi, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 61,
                          SortOrder: 700,
                          FontName: "Gill Sans",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Gill Sans, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 62,
                          SortOrder: 710,
                          FontName: "Gill Sans MT",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Gill Sans MT, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 63,
                          SortOrder: 720,
                          FontName: "Gloucester MT",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Gloucester MT, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 64,
                          SortOrder: 730,
                          FontName: "Goudy Old Style",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Goudy Old Style, Georgia, Palatino Linotype, Times New Roman"
                      },
                      {
                          ID: 65,
                          SortOrder: 740,
                          FontName: "Goudy Stout",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Goudy Stout, Impact, Arial, Verdana"
                      },
                      {
                          ID: 66,
                          SortOrder: 750,
                          FontName: "Great Vibes",
                          IsPowerAppsFont: true,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Great Vibes, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 67,
                          SortOrder: 760,
                          FontName: "Haettenschweiler",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Haettenschweiler, Impact, Arial, Verdana"
                      },
                      {
                          ID: 68,
                          SortOrder: 770,
                          FontName: "Harlow Solid",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Harlow Solid, Impact, Arial, Verdana"
                      },
                      {
                          ID: 69,
                          SortOrder: 780,
                          FontName: "Harrington",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Harrington, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 70,
                          SortOrder: 790,
                          FontName: "Helvetica",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Helvetica, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 71,
                          SortOrder: 800,
                          FontName: "High Tower Text",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "High Tower Text, Georgia, Palatino Linotype, Times New Roman"
                      },
                      {
                          ID: 72,
                          SortOrder: 810,
                          FontName: "HoloLens MDL2 Assets",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "HoloLens MDL2 Assets, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 73,
                          SortOrder: 820,
                          FontName: "Impact",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Impact, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 74,
                          SortOrder: 830,
                          FontName: "Imprint MT Shadow",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Imprint MT Shadow, Georgia, Times New Roman, Impact"
                      },
                      {
                          ID: 75,
                          SortOrder: 840,
                          FontName: "Informal Roman",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Informal Roman, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 76,
                          SortOrder: 850,
                          FontName: "Ink Free",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Ink Free, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 77,
                          SortOrder: 860,
                          FontName: "Javanese Text",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Javanese Text, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 78,
                          SortOrder: 870,
                          FontName: "Jokerman",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Jokerman, Comic Sans MS, Impact, Arial"
                      },
                      {
                          ID: 79,
                          SortOrder: 880,
                          FontName: "Juice ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Juice ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 80,
                          SortOrder: 890,
                          FontName: "Kristen ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Kristen ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 81,
                          SortOrder: 900,
                          FontName: "Kunstler Script",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Kunstler Script, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 82,
                          SortOrder: 910,
                          FontName: "Lato",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Lato, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 83,
                          SortOrder: 920,
                          FontName: "Lato Black",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Lato Black, Arial, Verdana, Impact"
                      },
                      {
                          ID: 84,
                          SortOrder: 930,
                          FontName: "Lato Hairline",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Lato Hairline, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 85,
                          SortOrder: 940,
                          FontName: "Lato Light",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Lato Light, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 86,
                          SortOrder: 950,
                          FontName: "Leelawadee",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Leelawadee, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 87,
                          SortOrder: 960,
                          FontName: "Leelawadee UI",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Leelawadee UI, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 88,
                          SortOrder: 970,
                          FontName: "Lucida Bright",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Lucida Bright, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 89,
                          SortOrder: 980,
                          FontName: "Lucida Calligraphy",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Lucida Calligraphy, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 90,
                          SortOrder: 990,
                          FontName: "Lucida Console",
                          IsPowerAppsFont: false,
                          Category: "Monospace",
                          IsWebSafe: true,
                          BestUse: "Body",
                          Family: "Lucida Console, Consolas, Courier New, monospace"
                      },
                      {
                          ID: 91,
                          SortOrder: 1000,
                          FontName: "Lucida Fax",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Lucida Fax, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 92,
                          SortOrder: 1010,
                          FontName: "Lucida Handwriting",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Lucida Handwriting, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 93,
                          SortOrder: 1020,
                          FontName: "Lucida Sans",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Lucida Sans, Lucida Sans Unicode, Arial, Verdana"
                      },
                      {
                          ID: 94,
                          SortOrder: 1030,
                          FontName: "Lucida Sans Typewriter",
                          IsPowerAppsFont: false,
                          Category: "Monospace",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Lucida Sans Typewriter, Consolas, Courier New, Lucida Console"
                      },
                      {
                          ID: 95,
                          SortOrder: 1040,
                          FontName: "Lucida Sans Unicode",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Lucida Sans Unicode, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 96,
                          SortOrder: 1050,
                          FontName: "Magneto",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Magneto, Comic Sans MS, Impact, Arial"
                      },
                      {
                          ID: 97,
                          SortOrder: 1060,
                          FontName: "Maiandra GD",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Maiandra GD, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 98,
                          SortOrder: 1070,
                          FontName: "Malgun Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Malgun Gothic, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 99,
                          SortOrder: 1080,
                          FontName: "Marlett",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Marlett, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 100,
                          SortOrder: 1090,
                          FontName: "Matura MT Script Capitals",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Matura MT Script Capitals, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 101,
                          SortOrder: 1100,
                          FontName: "Microsoft Himalaya",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft Himalaya, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 102,
                          SortOrder: 1110,
                          FontName: "Microsoft JhengHei",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Microsoft JhengHei, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 103,
                          SortOrder: 1120,
                          FontName: "Microsoft JhengHei UI",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Microsoft JhengHei UI, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 104,
                          SortOrder: 1130,
                          FontName: "Microsoft New Tai Lue",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft New Tai Lue, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 105,
                          SortOrder: 1140,
                          FontName: "Microsoft PhagsPa",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft PhagsPa, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 106,
                          SortOrder: 1150,
                          FontName: "Microsoft Sans Serif",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Microsoft Sans Serif, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 107,
                          SortOrder: 1160,
                          FontName: "Microsoft Tai Le",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft Tai Le, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 108,
                          SortOrder: 1170,
                          FontName: "Microsoft Uighur",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft Uighur, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 109,
                          SortOrder: 1180,
                          FontName: "Microsoft YaHei",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Microsoft YaHei, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 110,
                          SortOrder: 1190,
                          FontName: "Microsoft YaHei UI",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Microsoft YaHei UI, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 111,
                          SortOrder: 1200,
                          FontName: "Microsoft Yi Baiti",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Microsoft Yi Baiti, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 112,
                          SortOrder: 1210,
                          FontName: "MingLiU-ExtB",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "MingLiU-ExtB, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 113,
                          SortOrder: 1220,
                          FontName: "MingLiU_HKSCS-ExtB",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "MingLiU_HKSCS-ExtB, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 114,
                          SortOrder: 1230,
                          FontName: "Mistral",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Mistral, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 115,
                          SortOrder: 1240,
                          FontName: "Modern No. 20",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Modern No. 20, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 116,
                          SortOrder: 1250,
                          FontName: "Mongolian Baiti",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Mongolian Baiti, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 117,
                          SortOrder: 1260,
                          FontName: "Monotype Corsiva",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Monotype Corsiva, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 118,
                          SortOrder: 1270,
                          FontName: "MS Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "MS Gothic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 119,
                          SortOrder: 1280,
                          FontName: "MS Outlook",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "MS Outlook, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 120,
                          SortOrder: 1290,
                          FontName: "MS PGothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "MS PGothic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 121,
                          SortOrder: 1300,
                          FontName: "MS Reference Sans Serif",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "MS Reference Sans Serif, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 122,
                          SortOrder: 1310,
                          FontName: "MS Reference Specialty",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "MS Reference Specialty, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 123,
                          SortOrder: 1320,
                          FontName: "MS UI Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "MS UI Gothic, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 124,
                          SortOrder: 1330,
                          FontName: "MT Extra",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "MT Extra, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 125,
                          SortOrder: 1340,
                          FontName: "MV Boli",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "MV Boli, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 126,
                          SortOrder: 1350,
                          FontName: "Myanmar Text",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Myanmar Text, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 127,
                          SortOrder: 1360,
                          FontName: "Niagara Engraved",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Niagara Engraved, Impact, Arial, Verdana"
                      },
                      {
                          ID: 128,
                          SortOrder: 1370,
                          FontName: "Niagara Solid",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Niagara Solid, Impact, Arial, Verdana"
                      },
                      {
                          ID: 129,
                          SortOrder: 1380,
                          FontName: "Nirmala UI",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Nirmala UI, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 130,
                          SortOrder: 1390,
                          FontName: "NSimSun",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "NSimSun, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 131,
                          SortOrder: 1400,
                          FontName: "OCR A",
                          IsPowerAppsFont: false,
                          Category: "Monospace",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "OCR A, Courier New, Consolas, Lucida Console"
                      },
                      {
                          ID: 132,
                          SortOrder: 1410,
                          FontName: "Old English Text MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Old English Text MT, Georgia, Times New Roman, Impact"
                      },
                      {
                          ID: 133,
                          SortOrder: 1420,
                          FontName: "Onyx",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Onyx, Impact, Arial, Verdana"
                      },
                      {
                          ID: 134,
                          SortOrder: 1430,
                          FontName: "Open Sans",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Open Sans, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 135,
                          SortOrder: 1440,
                          FontName: "Open Sans Condensed",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Open Sans Condensed, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 136,
                          SortOrder: 1450,
                          FontName: "Palace Script MT",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Palace Script MT, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 137,
                          SortOrder: 1460,
                          FontName: "Palatino Linotype",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Palatino Linotype, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 138,
                          SortOrder: 1470,
                          FontName: "Papyrus",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Papyrus, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 139,
                          SortOrder: 1480,
                          FontName: "Parchment",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Parchment, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 140,
                          SortOrder: 1490,
                          FontName: "Patrick Hand",
                          IsPowerAppsFont: true,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Patrick Hand, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 141,
                          SortOrder: 1500,
                          FontName: "Perpetua",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Perpetua, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 142,
                          SortOrder: 1510,
                          FontName: "Perpetua Titling MT",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Perpetua Titling MT, Georgia, Impact, Times New Roman"
                      },
                      {
                          ID: 143,
                          SortOrder: 1520,
                          FontName: "Playbill",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Playbill, Impact, Arial, Verdana"
                      },
                      {
                          ID: 144,
                          SortOrder: 1530,
                          FontName: "PMingLiU-ExtB",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "PMingLiU-ExtB, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 145,
                          SortOrder: 1540,
                          FontName: "Poor Richard",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Poor Richard, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 146,
                          SortOrder: 1550,
                          FontName: "Pristina",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Pristina, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 147,
                          SortOrder: 1560,
                          FontName: "Rage",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Rage, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 148,
                          SortOrder: 1570,
                          FontName: "Ravie",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Ravie, Comic Sans MS, Impact, Arial"
                      },
                      {
                          ID: 149,
                          SortOrder: 1580,
                          FontName: "Rockwell",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Rockwell, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 150,
                          SortOrder: 1590,
                          FontName: "Script MT",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Script MT, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 151,
                          SortOrder: 1600,
                          FontName: "Segoe MDL2 Assets",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Segoe MDL2 Assets, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 152,
                          SortOrder: 1610,
                          FontName: "Segoe Print",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Segoe Print, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 153,
                          SortOrder: 1620,
                          FontName: "Segoe Script",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Segoe Script, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 154,
                          SortOrder: 1630,
                          FontName: "Segoe UI",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Segoe UI, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 155,
                          SortOrder: 1640,
                          FontName: "Segoe UI Emoji",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Segoe UI Emoji, Symbol, Arial, Verdana"
                      },
                      {
                          ID: 156,
                          SortOrder: 1650,
                          FontName: "Segoe UI Historic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Segoe UI Historic, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 157,
                          SortOrder: 1660,
                          FontName: "Segoe UI Symbol",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Segoe UI Symbol, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 158,
                          SortOrder: 1670,
                          FontName: "Showcard Gothic",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Showcard Gothic, Impact, Arial, Verdana"
                      },
                      {
                          ID: 159,
                          SortOrder: 1680,
                          FontName: "SimSun",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "SimSun, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 160,
                          SortOrder: 1690,
                          FontName: "SimSun-ExtB",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "SimSun-ExtB, Times New Roman, Georgia, Cambria"
                      },
                      {
                          ID: 161,
                          SortOrder: 1700,
                          FontName: "Sitka Banner",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Sitka Banner, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 162,
                          SortOrder: 1710,
                          FontName: "Sitka Display",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Sitka Display, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 163,
                          SortOrder: 1720,
                          FontName: "Sitka Heading",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Sitka Heading, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 164,
                          SortOrder: 1730,
                          FontName: "Sitka Small",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Sitka Small, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 165,
                          SortOrder: 1740,
                          FontName: "Sitka Subheading",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Sitka Subheading, Georgia, Times New Roman, Palatino Linotype"
                      },
                      {
                          ID: 166,
                          SortOrder: 1750,
                          FontName: "Sitka Text",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Sitka Text, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 167,
                          SortOrder: 1760,
                          FontName: "Snap ITC",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Snap ITC, Impact, Arial, Verdana"
                      },
                      {
                          ID: 168,
                          SortOrder: 1770,
                          FontName: "Stencil",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Stencil, Impact, Arial, Verdana"
                      },
                      {
                          ID: 169,
                          SortOrder: 1780,
                          FontName: "Sylfaen",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: false,
                          BestUse: "Body",
                          Family: "Sylfaen, Georgia, Times New Roman, Cambria"
                      },
                      {
                          ID: 170,
                          SortOrder: 1790,
                          FontName: "Symbol",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Symbol, Webdings, Wingdings, serif"
                      },
                      {
                          ID: 171,
                          SortOrder: 1800,
                          FontName: "Tahoma",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Tahoma, Verdana, Arial, Segoe UI"
                      },
                      {
                          ID: 172,
                          SortOrder: 1810,
                          FontName: "Tempus Sans ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Tempus Sans ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 173,
                          SortOrder: 1820,
                          FontName: "Times New Roman",
                          IsPowerAppsFont: false,
                          Category: "Serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Times New Roman, Georgia, Palatino Linotype, Cambria"
                      },
                      {
                          ID: 174,
                          SortOrder: 1830,
                          FontName: "Trebuchet MS",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Trebuchet MS, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 175,
                          SortOrder: 1840,
                          FontName: "Tw Cen MT",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Tw Cen MT, Arial, Verdana, Tahoma"
                      },
                      {
                          ID: 176,
                          SortOrder: 1850,
                          FontName: "Verdana",
                          IsPowerAppsFont: true,
                          Category: "Sans-serif",
                          IsWebSafe: true,
                          BestUse: "Both",
                          Family: "Verdana, Arial, Tahoma, Segoe UI"
                      },
                      {
                          ID: 177,
                          SortOrder: 1860,
                          FontName: "Viner Hand ITC",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Viner Hand ITC, Comic Sans MS, Verdana, Arial"
                      },
                      {
                          ID: 178,
                          SortOrder: 1870,
                          FontName: "Vivaldi",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Vivaldi, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 179,
                          SortOrder: 1880,
                          FontName: "Vladimir Script",
                          IsPowerAppsFont: false,
                          Category: "Script",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Vladimir Script, Comic Sans MS, Georgia, Times New Roman"
                      },
                      {
                          ID: 180,
                          SortOrder: 1890,
                          FontName: "Webdings",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Webdings, Symbol, Wingdings, serif"
                      },
                      {
                          ID: 181,
                          SortOrder: 1900,
                          FontName: "Wide Latin",
                          IsPowerAppsFont: false,
                          Category: "Display",
                          IsWebSafe: false,
                          BestUse: "Header",
                          Family: "Wide Latin, Impact, Arial, Verdana"
                      },
                      {
                          ID: 182,
                          SortOrder: 1910,
                          FontName: "Wingdings",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Wingdings, Symbol, Webdings, serif"
                      },
                      {
                          ID: 183,
                          SortOrder: 1920,
                          FontName: "Wingdings 2",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Wingdings 2, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 184,
                          SortOrder: 1930,
                          FontName: "Wingdings 3",
                          IsPowerAppsFont: false,
                          Category: "Symbol",
                          IsWebSafe: true,
                          BestUse: "Header",
                          Family: "Wingdings 3, Symbol, Webdings, Wingdings"
                      },
                      {
                          ID: 185,
                          SortOrder: 1940,
                          FontName: "Yu Gothic",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Yu Gothic, Segoe UI, Arial, Verdana"
                      },
                      {
                          ID: 186,
                          SortOrder: 1950,
                          FontName: "Yu Gothic UI",
                          IsPowerAppsFont: false,
                          Category: "Sans-serif",
                          IsWebSafe: false,
                          BestUse: "Both",
                          Family: "Yu Gothic UI, Segoe UI, Arial, Verdana"
                      }
                  ],
                  SortOrder,
                  SortOrder.Ascending
              )
            TemplateFill: =If(ThisItem.IsSelected, Color.LightYellow, Color.White)
            TemplatePadding: =3
            TemplateSize: =60
            Width: =Parent.Width * 60%
            X: =20
            Y: =20
          Children:
            - lblFontName:
                Control: Label@2.5.1
                Properties:
                  Font: =ThisItem.FontName
                  Height: =Parent.TemplateHeight
                  OnSelect: =Select(Parent)
                  PaddingLeft: =15
                  Size: =24
                  Text: =$"{ThisItem.FontName}"
                  Width: =Parent.TemplateWidth * 60%
            - lblCategory:
                Control: Label@2.5.1
                Properties:
                  Font: =ThisItem.FontName
                  Height: =Parent.TemplateHeight
                  OnSelect: =Select(Parent)
                  Size: =24
                  Text: =$"{ThisItem.Category}"
                  Width: =Parent.TemplateWidth - lblFontName.Width
                  X: =lblFontName.Width
            - icoWebSafe:
                Control: Classic/Icon@2.5.0
                Properties:
                  Color: =RGBA(167, 182, 203, 1)
                  Height: =Parent.TemplateHeight
                  Icon: =Icon.ThumbsUpFilled
                  OnSelect: =Select(Parent)
                  PaddingBottom: =10
                  PaddingLeft: =10
                  PaddingRight: =10
                  PaddingTop: =10
                  Tooltip: ="Web Safe Fonts"
                  Visible: =ThisItem.IsWebSafe
                  Width: =Self.Height
                  X: =417
      - lblParagraphSample:
          Control: Label@2.5.1
          Properties:
            Fill: =RGBA(255, 255, 255, 1)
            Font: =galFonts.Selected.FontName
            Height: =Parent.Height - Self.Y - 20
            PaddingBottom: =15
            PaddingLeft: =15
            PaddingRight: =15
            PaddingTop: =15
            Size: =17
            Text: ="The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. Sphinx of black quartz, judge my vow. How vexingly quick daft zebras jump!"
            VerticalAlign: =VerticalAlign.Top
            Width: =Parent.Width - galFonts.X * 3 - galFonts.Width
            X: =galFonts.X * 2 + galFonts.Width
            Y: =252
      - lblHeadingSample:
          Control: Label@2.5.1
          Properties:
            BorderColor: =RGBA(237, 237, 237, 1)
            BorderThickness: =2
            Fill: =RGBA(255, 255, 255, 1)
            Font: =galFonts.Selected.FontName
            Height: =210
            PaddingBottom: =15
            PaddingLeft: =15
            PaddingRight: =15
            PaddingTop: =15
            Size: =28
            Text: ="The quick brown fox jumps over the lazy dog."
            VerticalAlign: =VerticalAlign.Top
            Width: =Parent.Width - galFonts.X * 3 - galFonts.Width
            X: =galFonts.X * 2 + galFonts.Width
            Y: =20
```