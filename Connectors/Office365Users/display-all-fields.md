# Display All Profile Fields

This is a template to be used for new code snippets for this code repository.

## Add This to Your Application

```JavaScript
- Label8_93:
    Control: Label
    Properties:
      Text: ="officeLocation"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =600
- Label8_92:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().officeLocation
      Width: =400
      X: =299
      Y: =600
- Label8_91:
    Control: Label
    Properties:
      Text: ="preferredLanguage"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =680
- Label8_90:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().preferredLanguage
      Width: =400
      X: =299
      Y: =680
- Label8_89:
    Control: Label
    Properties:
      Text: ="postalCode"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =640
- Label8_88:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().postalCode
      Width: =400
      X: =299
      Y: =640
- Label8_87:
    Control: Label
    Properties:
      Text: ="mySite"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =560
- Label8_86:
    Control: Label
    Properties:
      OnSelect: =Launch(Self.Text)
      Text: =Office365Users.MyProfileV2().mySite
      Width: =400
      X: =299
      Y: =560
- Label8_85:
    Control: Label
    Properties:
      Text: ="mobilePhone"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =520
- Label8_84:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().mobilePhone
      Width: =400
      X: =299
      Y: =520
- Label8_83:
    Control: Label
    Properties:
      Text: ="mailNickname"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =480
- Label8_82:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().mailNickname
      Width: =400
      X: =299
      Y: =480
- Label8_81:
    Control: Label
    Properties:
      Text: ="mail"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =440
- Label8_80:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().mail
      Width: =400
      X: =299
      Y: =440
- Label8_79:
    Control: Label
    Properties:
      Text: ="jobTitle"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =400
- Label8_78:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().jobTitle
      Width: =400
      X: =299
      Y: =400
- Label8_77:
    Control: Label
    Properties:
      Text: ="displayName"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =280
- Label8_76:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().displayName
      Width: =400
      X: =299
      Y: =280
- Label8_75:
    Control: Label
    Properties:
      Text: ="id"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =360
- Label8_74:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().id
      Width: =400
      X: =299
      Y: =360
- Label8_73:
    Control: Label
    Properties:
      Text: ="givenName"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =320
- Label8_72:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().givenName
      Width: =400
      X: =299
      Y: =320
- Label8_71:
    Control: Label
    Properties:
      Text: ="department"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =240
- Label8_70:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().department
      Width: =400
      X: =299
      Y: =240
- Label8_69:
    Control: Label
    Properties:
      Text: ="country"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =200
- Label8_68:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().country
      Width: =400
      X: =299
      Y: =200
- Label8_67:
    Control: Label
    Properties:
      Text: ="companyName"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =160
- Label8_66:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().companyName
      Width: =400
      X: =299
      Y: =160
- Label8_65:
    Control: Label
    Properties:
      Text: ="city"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =120
- Label8_64:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().city
      Width: =400
      X: =299
      Y: =120
- Label8_63:
    Control: Label
    Properties:
      Text: ="aboutMe"
      Align: =Align.Right
      Fill: =RGBA(229, 229, 229, 1)
      Width: =200
      X: =99
      Y: =80
- Label8_62:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().aboutMe
      Width: =400
      X: =299
      Y: =80
- Label8_123:
    Control: Label
    Properties:
      Text: ="skills"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =564
- Label8_122:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().skills, Value & Char(10))
      Width: =400
      X: =921
      Y: =564
- Label8_121:
    Control: Label
    Properties:
      Text: ="pastProjects"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =524
- Label8_120:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().pastProjects, Value & Char(10))
      Width: =400
      X: =921
      Y: =524
- Label8_119:
    Control: Label
    Properties:
      Text: ="skills"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =484
- Label8_118:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().interests, Value & Char(10))
      Width: =400
      X: =921
      Y: =484
- Label8_117:
    Control: Label
    Properties:
      Text: ="birthday"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =362
- Label8_116:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().birthday
      Width: =400
      X: =921
      Y: =362
- Label8_115:
    Control: Label
    Properties:
      Text: ="accountEnabled"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =322
- Label8_114:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().accountEnabled
      Width: =400
      X: =921
      Y: =322
- Label8_113:
    Control: Label
    Properties:
      Text: ="hireDate"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =444
- Label8_112:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().hireDate
      Width: =400
      X: =921
      Y: =444
- Label8_111:
    Control: Label
    Properties:
      Text: ="businessPhones"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =404
- Label8_110:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().businessPhones, Value & Char(10))
      Width: =400
      X: =921
      Y: =404
- Label8_109:
    Control: Label
    Properties:
      Text: ="surname"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =200
- Label8_108:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().surname
      Width: =400
      X: =921
      Y: =200
- Label8_107:
    Control: Label
    Properties:
      Text: ="streetAddress"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =160
- Label8_106:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().streetAddress
      Width: =400
      X: =921
      Y: =160
- Label8_105:
    Control: Label
    Properties:
      Text: ="state"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =120
- Label8_104:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().state
      Width: =400
      X: =921
      Y: =120
- Label8_103:
    Control: Label
    Properties:
      Text: ="skills"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =644
- Label8_102:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().skills, Value & Char(10))
      Width: =400
      X: =921
      Y: =644
- Label8_101:
    Control: Label
    Properties:
      Text: ="responsibilities"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =604
- Label8_100:
    Control: Label
    Properties:
      Text: =Concat(Office365Users.MyProfileV2().responsibilities, Value & Char(10))
      Width: =400
      X: =921
      Y: =604
- Label8_99:
    Control: Label
    Properties:
      Text: ="userType"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =282
- Label8_98:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().userType
      Width: =400
      X: =921
      Y: =282
- Label8_97:
    Control: Label
    Properties:
      Text: ="userPrincipalName"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =242
- Label8_96:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().userPrincipalName
      Width: =400
      X: =921
      Y: =242
- Label8_95:
    Control: Label
    Properties:
      Text: ="preferredName"
      Align: =Align.Right
      Fill: =RGBA(213, 213, 213, 1)
      Width: =200
      X: =721
      Y: =80
- Label8_94:
    Control: Label
    Properties:
      Text: =Office365Users.MyProfileV2().preferredName
      Width: =400
      X: =921
      Y: =80
- Image1_1:
    Control: Image
    Properties:
      Image: =gblCurrentUser.PhotoBase64
      Height: =80
      Width: =80
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
