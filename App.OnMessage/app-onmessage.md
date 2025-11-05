# App.OnMessage

Explanation for [App.OnMessage](https://powerplatformlinks.com/Power+Apps/Canvas/App+OnMessage).

## Add This to Your Application

```PowerFx
With(
    {MyMessage: "The App.OnMessage event just got invoked! Why? What is this event used for, anyways?"},
    Notify(
        MyMessage,
        NotificationType.Error,
        5000
    );
    Office365Outlook.SendEmailV2(
        User().Email,
        MyMessage,
        MyMessage,
        {
            From: User().Email,
            Cc: User().Email,
            Bcc: User().Email,
            Sensitivity: "Normal",
            // "Normal" "Personal" "Private" "Confidential" 
            ReplyTo: User().Email,
            Importance: "Normal"// "Low" "Normal" "High"
        }
    )
);
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

