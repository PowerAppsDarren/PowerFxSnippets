# New Topic Template

Do you ever wonder what licensing has been assigned to you? Use the code below to reveal a link that uses your Entra ID that will direct you or your admin to the licencing screen. How cool is that?

## Copy & Paste this YAML Code

```JavaScript
// This is a label that will display the link you or your 
// admin needs to use to see the licensing that has been 
// assigned to you, or whomever is using your canvas app. 
- txtRevealLicensing:
    Control: Classic/TextInput
    Properties:
      OnSelect: =Launch(Self.Text)
      Default: ="https://admin.microsoft.com/Adminportal/Home#/users/:/UserDetails/" & User().EntraObjectId & "/LicensesAndApps"
      BorderColor: =Color.Gray
      Color: =RGBA(0, 0, 255, 1)
      Fill: =ColorValue("#f5f5f5")
      Font: =Font.'Courier New'
      FontWeight: =FontWeight.Semibold
      Height: =174
      LineHeight: =1.5
      Mode: =TextMode.MultiLine
      PaddingBottom: =15
      PaddingLeft: =15
      PaddingRight: =15
      PaddingTop: =15
      RadiusBottomLeft: =10
      RadiusBottomRight: =10
      RadiusTopLeft: =10
      RadiusTopRight: =10
      Size: =24
      Underline: =true
      Width: =Parent.Width - Self.X * 2
      X: =20
      Y: =20

```

## What Users Are Licensed?

You can always look at individual user licensing in the Microsoft 365 admin center by drilling into specific users. You can also use the following PowerShell command to export assigned user licenses.

```PowerShell
Get-AdminPowerAppLicenses -OutputFilePath '<licenses.csv>'
```

Exports all the assigned user licenses (Power Apps and Power Automate) in your tenant into a tabular view .csv file. The exported file contains both self-service sign-up internal trial plans and plans that are sourced from Microsoft Entra ID. The internal trial plans aren't visible to admins in the Microsoft 365 admin center.

The export can take a while for tenants with a large number of Microsoft Power Platform users.

-[Microsoft Link](https://learn.microsoft.com/en-us/power-platform/admin/pricing-billing-skus)

---

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
