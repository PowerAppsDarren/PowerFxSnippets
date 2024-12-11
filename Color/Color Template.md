# COLOR

Credit: https://github.com/P3N-101/color-functions

```PowerFx"
'color-functions' As CanvasComponent":
    AchromatomalyColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 61.8 / 100.0 + G * 32 / 100.0 + B * 6.2 / 100.0),
                      (R * 16.3 / 100.0 + G * 77.5 / 100.0 + B * 6.2 / 100.0),
                      (R * 16.3 / 100.0 + G * 32.0 / 100.0 + B * 51.6 / 100.0),1
                  )
                /*
                Achromatomaly:
                R:[61.8, 32,    6.2]
                G:[16.3, 77.5,  6.2]
                B:[16.3, 32.0, 51.6]
                */
    AchromatopsiaColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 29.9 / 100.0 + G * 58.7 / 100.0 + B * 11.4 / 100.0),
                      (R * 29.9 / 100.0 + G * 58.7 / 100.0 + B * 11.4 / 100.0),
                      (R * 29.9 / 100.0 + G * 58.7 / 100.0 + B * 11.4 / 100.0),1
                  )
                /*
                Achromatopsia:
                R:[29.9, 58.7, 11.4]
                G:[29.9, 58.7, 11.4]
                B:[29.9, 58.7, 11.4]
                */
    chkContrast(DarkColor As Number, LightColor As Number):
        DarkColor:
            Default: =100
        LightColor:
            Default: =100
        ThisProperty:
            Default: |-
                =If(
                    // Check which Value is higher, calculation then is (darkColor+0.05) / (lightColor+0.05)
                    LightColor >DarkColor,
                    Text(
                        Sum((LightColor + 0.05) / (DarkColor + 0.05)),
                        "[$-en-GB]#.000"
                    ),
                    Text(
                        Sum((DarkColor + 0.05) / (LightColor + 0.05)),
                        "[$-en-GB]#.000"
                    )
                )
    DeuteranomalyColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 80 / 100.0 + G * 20 / 100.0 + B * 0 / 100.0),
                      (R * 25.833 / 100.0 + G * 74.167 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 14.167 / 100.0 + B * 85.833 / 100.0),1
                  )
                
                /*
                Deuteranomaly:
                R:[80,     20,      0]
                G:[25.833, 74.167,  0]
                B: [0,     14.167, 85.833]
                */
    DeuteranopiaColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 62.5 / 100.0 + G * 37.5 / 100.0 + B * 0 / 100.0),
                      (R * 70 / 100.0 + G * 30 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 30 / 100.0 + B * 70 / 100.0),1
                  )
                
                /*
                
                 Deuteranopia: 
                    R:[62.5, 37.5,  0]
                    G:[70,   30,    0]
                    B: [0,   30,   70]
                    */
    getLuminance(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =Sum(
                    ('color-functions'.sRGBtoLIN(R) * 0.2126) + 
                    ('color-functions'.sRGBtoLIN(G) * 0.7152) + 
                    ('color-functions'.sRGBtoLIN(B) * 0.0722)
                )
    ProtanomalyColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =// Return Protanomaly RGB Color 
                RGBA(
                      (R * 81.667 / 100.0 + G * 18.333 / 100.0 + B * 0 / 100.0),
                      (R * 33.333 / 100.0 + G * 66.667 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 12.5 / 100.0 + B * 87.5 / 100.0),1
                  )
                
                /*
                Protanomaly:  
                R:[81.667, 18.333,    0]
                G:[33.333, 66.667,    0]
                B:[     0    12.5, 87.5]
                
                */
    ProtanopiaColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =// Return Protanopia RGB Color 
                RGBA(
                      (R * 56.667 / 100.0 + G * 43.333 / 100.0 + B * 0 / 100.0),
                      (R * 55.833 / 100.0 + G * 44.167 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 24.167 / 100.0 + B * 75.833 / 100.0),1
                  )
                /*
                Protanopia: 
                R:[56.667, 43.333,      0]
                G:[55.833, 44.167,      0]
                B:[     0, 24.167, 75.833]
                
                */
    sRGBtoLIN(colorChannel As Number):
        colorChannel:
            Default: =100
        ThisProperty:
            Default: |-
                =If(
                    Sum(colorChannel / 255) <= 0.03928,
                    Sum(colorChannel / 255) / 12.92,
                    Power(
                        ((Sum(colorChannel / 255) + 0.055) / 1.055),
                        2.4
                    )
                )
    TritanomalyColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 96.667 / 100.0 + G * 3.333 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 73.333 / 100.0 + B * 26.667 / 100.0),
                      (R * 0 / 100.0 + G * 18.333 / 100.0 + B * 81.667 / 100.0),1
                  )
                /*
                Tritanomaly:  {
                R:[96.667, 3.333,   0],
                G: [0,     73.333, 26.667],
                B: [0,     18.333, 81.667]
                */
    TritanopiaColor(R As Number, G As Number, B As Number):
        R:
            Default: =100
        G:
            Default: =100
        B:
            Default: =100
        ThisProperty:
            Default: |-
                =RGBA(
                      (R * 95 / 100.0 + G * 5 / 100.0 + B * 0 / 100.0),
                      (R * 0 / 100.0 + G * 43.333 / 100.0 + B * 56.667 / 100.0),
                      (R * 0 / 100.0 + G * 47.5 / 100.0 + B * 52.5 / 100.0),1
                  )
                
                /*
                
                Tritanopia:   {
                R:[95,  5,      0],
                G: [0, 43.333, 56.667],
                B: [0, 47.5,   52.5]
                    */
    Fill: =RGBA(0, 0, 0, 0)
    Height: |
        =App.Height
    HEXtoDEC: |-
        =Table({DEC:0,HEX:"00"},{DEC:1,HEX:"01"},{DEC:2,HEX:"02"},{DEC:3,HEX:"03"},{DEC:4,HEX:"04"},{DEC:5,HEX:"05"},{DEC:6,HEX:"06"},{DEC:7,HEX:"07"},{DEC:8,HEX:"08"},{DEC:9,HEX:"09"},{DEC:10,HEX:"0A"},{DEC:11,HEX:"0B"},{DEC:12,HEX:"0C"},{DEC:13,HEX:"0D"},{DEC:14,HEX:"0E"},{DEC:15,HEX:"0F"},{DEC:16,HEX:"10"},{DEC:17,HEX:"11"},{DEC:18,HEX:"12"},{DEC:19,HEX:"13"},{DEC:20,HEX:"14"},{DEC:21,HEX:"15"},{DEC:22,HEX:"16"},{DEC:23,HEX:"17"},{DEC:24,HEX:"18"},{DEC:25,HEX:"19"},{DEC:26,HEX:"1A"},{DEC:27,HEX:"1B"},{DEC:28,HEX:"1C"},{DEC:29,HEX:"1D"},{DEC:30,HEX:"1E"},{DEC:31,HEX:"1F"},{DEC:32,HEX:"20"},{DEC:33,HEX:"21"},{DEC:34,HEX:"22"},{DEC:35,HEX:"23"},{DEC:36,HEX:"24"},{DEC:37,HEX:"25"},{DEC:38,HEX:"26"},{DEC:39,HEX:"27"},{DEC:40,HEX:"28"},{DEC:41,HEX:"29"},{DEC:42,HEX:"2A"},{DEC:43,HEX:"2B"},{DEC:44,HEX:"2C"},{DEC:45,HEX:"2D"},{DEC:46,HEX:"2E"},{DEC:47,HEX:"2F"},{DEC:48,HEX:"30"},{DEC:49,HEX:"31"},{DEC:50,HEX:"32"},{DEC:51,HEX:"33"},{DEC:52,HEX:"34"},{DEC:53,HEX:"35"},{DEC:54,HEX:"36"},{DEC:55,HEX:"37"},{DEC:56,HEX:"38"},{DEC:57,HEX:"39"},{DEC:58,HEX:"3A"},{DEC:59,HEX:"3B"},{DEC:60,HEX:"3C"},{DEC:61,HEX:"3D"},{DEC:62,HEX:"3E"},{DEC:63,HEX:"3F"},{DEC:64,HEX:"40"},{DEC:65,HEX:"41"},{DEC:66,HEX:"42"},{DEC:67,HEX:"43"},{DEC:68,HEX:"44"},{DEC:69,HEX:"45"},{DEC:70,HEX:"46"},{DEC:71,HEX:"47"},{DEC:72,HEX:"48"},{DEC:73,HEX:"49"},{DEC:74,HEX:"4A"},{DEC:75,HEX:"4B"},{DEC:76,HEX:"4C"},{DEC:77,HEX:"4D"},{DEC:78,HEX:"4E"},{DEC:79,HEX:"4F"},{DEC:80,HEX:"50"},{DEC:81,HEX:"51"},{DEC:82,HEX:"52"},{DEC:83,HEX:"53"},{DEC:84,HEX:"54"},{DEC:85,HEX:"55"},{DEC:86,HEX:"56"},{DEC:87,HEX:"57"},{DEC:88,HEX:"58"},{DEC:89,HEX:"59"},{DEC:90,HEX:"5A"},{DEC:91,HEX:"5B"},{DEC:92,HEX:"5C"},{DEC:93,HEX:"5D"},{DEC:94,HEX:"5E"},{DEC:95,HEX:"5F"},{DEC:96,HEX:"60"},{DEC:97,HEX:"61"},{DEC:98,HEX:"62"},{DEC:99,HEX:"63"},{DEC:100,HEX:"64"},{DEC:101,HEX:"65"},{DEC:102,HEX:"66"},{DEC:103,HEX:"67"},{DEC:104,HEX:"68"},{DEC:105,HEX:"69"},{DEC:106,HEX:"6A"},{DEC:107,HEX:"6B"},{DEC:108,HEX:"6C"},{DEC:109,HEX:"6D"},{DEC:110,HEX:"6E"},{DEC:111,HEX:"6F"},{DEC:112,HEX:"70"},{DEC:113,HEX:"71"},{DEC:114,HEX:"72"},{DEC:115,HEX:"73"},{DEC:116,HEX:"74"},{DEC:117,HEX:"75"},{DEC:118,HEX:"76"},{DEC:119,HEX:"77"},{DEC:120,HEX:"78"},{DEC:121,HEX:"79"},{DEC:122,HEX:"7A"},{DEC:123,HEX:"7B"},{DEC:124,HEX:"7C"},{DEC:125,HEX:"7D"},{DEC:126,HEX:"7E"},{DEC:127,HEX:"7F"},{DEC:128,HEX:"80"},{DEC:129,HEX:"81"},{DEC:130,HEX:"82"},{DEC:131,HEX:"83"},{DEC:132,HEX:"84"},{DEC:133,HEX:"85"},{DEC:134,HEX:"86"},{DEC:135,HEX:"87"},{DEC:136,HEX:"88"},{DEC:137,HEX:"89"},{DEC:138,HEX:"8A"},{DEC:139,HEX:"8B"},{DEC:140,HEX:"8C"},{DEC:141,HEX:"8D"},{DEC:142,HEX:"8E"},{DEC:143,HEX:"8F"},{DEC:144,HEX:"90"},{DEC:145,HEX:"91"},{DEC:146,HEX:"92"},{DEC:147,HEX:"93"},{DEC:148,HEX:"94"},{DEC:149,HEX:"95"},{DEC:150,HEX:"96"},{DEC:151,HEX:"97"},{DEC:152,HEX:"98"},{DEC:153,HEX:"99"},{DEC:154,HEX:"9A"},{DEC:155,HEX:"9B"},{DEC:156,HEX:"9C"},{DEC:157,HEX:"9D"},{DEC:158,HEX:"9E"},{DEC:159,HEX:"9F"},{DEC:160,HEX:"A0"},{DEC:161,HEX:"A1"},{DEC:162,HEX:"A2"},{DEC:163,HEX:"A3"},{DEC:164,HEX:"A4"},{DEC:165,HEX:"A5"},{DEC:166,HEX:"A6"},{DEC:167,HEX:"A7"},{DEC:168,HEX:"A8"},{DEC:169,HEX:"A9"},{DEC:170,HEX:"AA"},{DEC:171,HEX:"AB"},{DEC:172,HEX:"AC"},{DEC:173,HEX:"AD"},{DEC:174,HEX:"AE"},{DEC:175,HEX:"AF"},{DEC:176,HEX:"B0"},{DEC:177,HEX:"B1"},{DEC:178,HEX:"B2"},{DEC:179,HEX:"B3"},{DEC:180,HEX:"B4"},{DEC:181,HEX:"B5"},{DEC:182,HEX:"B6"},{DEC:183,HEX:"B7"},{DEC:184,HEX:"B8"},{DEC:185,HEX:"B9"},{DEC:186,HEX:"BA"},{DEC:187,HEX:"BB"},{DEC:188,HEX:"BC"},{DEC:189,HEX:"BD"},{DEC:190,HEX:"BE"},{DEC:191,HEX:"BF"},{DEC:192,HEX:"C0"},{DEC:193,HEX:"C1"},{DEC:194,HEX:"C2"},{DEC:195,HEX:"C3"},{DEC:196,HEX:"C4"},{DEC:197,HEX:"C5"},{DEC:198,HEX:"C6"},{DEC:199,HEX:"C7"},{DEC:200,HEX:"C8"},{DEC:201,HEX:"C9"},{DEC:202,HEX:"CA"},{DEC:203,HEX:"CB"},{DEC:204,HEX:"CC"},{DEC:205,HEX:"CD"},{DEC:206,HEX:"CE"},{DEC:207,HEX:"CF"},{DEC:208,HEX:"D0"},{DEC:209,HEX:"D1"},{DEC:210,HEX:"D2"},{DEC:211,HEX:"D3"},{DEC:212,HEX:"D4"},{DEC:213,HEX:"D5"},{DEC:214,HEX:"D6"},{DEC:215,HEX:"D7"},{DEC:216,HEX:"D8"},{DEC:217,HEX:"D9"},{DEC:218,HEX:"DA"},{DEC:219,HEX:"DB"},{DEC:220,HEX:"DC"},{DEC:221,HEX:"DD"},{DEC:222,HEX:"DE"},{DEC:223,HEX:"DF"},{DEC:224,HEX:"E0"},{DEC:225,HEX:"E1"},{DEC:226,HEX:"E2"},{DEC:227,HEX:"E3"},{DEC:228,HEX:"E4"},{DEC:229,HEX:"E5"},{DEC:230,HEX:"E6"},{DEC:231,HEX:"E7"},{DEC:232,HEX:"E8"},{DEC:233,HEX:"E9"},{DEC:234,HEX:"EA"},{DEC:235,HEX:"EB"},{DEC:236,HEX:"EC"},{DEC:237,HEX:"ED"},{DEC:238,HEX:"EE"},{DEC:239,HEX:"EF"},{DEC:240,HEX:"F0"},{DEC:241,HEX:"F1"},{DEC:242,HEX:"F2"},{DEC:243,HEX:"F3"},{DEC:244,HEX:"F4"},{DEC:245,HEX:"F5"},{DEC:246,HEX:"F6"},{DEC:247,HEX:"F7"},{DEC:248,HEX:"F8"},{DEC:249,HEX:"F9"},{DEC:250,HEX:"FA"},{DEC:251,HEX:"FB"},{DEC:252,HEX:"FC"},{DEC:253,HEX:"FD"},{DEC:254,HEX:"FE"},{DEC:255,HEX:"FF"})
    Width: |
        =App.Width
    X: =0
    Y: =0
    ZIndex: =1
```