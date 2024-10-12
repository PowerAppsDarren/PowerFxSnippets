# New Topic

Power Apps just can't handle raw SVG code. It needs to be encoded. Here's a simple function to do that for you. This function will take your SVG code and return it encoded so it can be used in a Power Apps image control.

## Applies to

![Power Apps](https://img.shields.io/badge/Power%20Apps-Yes-green "Yes")
![Power Automate](https://img.shields.io/badge/Power%20Automate-No-red "No")
![Power BI](https://img.shields.io/badge/Power%20BI-No-red "No")
![Power Pages](https://img.shields.io/badge/Power%20Pages-No-red "No")
![Power Virtual Agents](https://img.shields.io/badge/Power%20Virtual%20Agents-No-red "No")
![Dataverse](https://img.shields.io/badge/Dataverse-No-red "No")
![AI Builder](https://img.shields.io/badge/AI%20Builder-No-red "No")
![Custom Connectors](https://img.shields.io/badge/Custom%20Connectors-No-red "No")
![Power Fx](https://img.shields.io/badge/Power%20Fx-Yes-green "Yes")

## Add This to Your Application

```JavaScript
    //
    // Have SVG code formatted for Power Apps so it shows up properly?
    //
    fxSVGEncode(svgCode:Text):Text = 
        "data:image/svg+xml; utf8, " & EncodeUrl(svgCode);
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
