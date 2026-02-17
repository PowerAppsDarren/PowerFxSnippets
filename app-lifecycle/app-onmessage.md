# App.OnMessage

## Table of Contents

- [Add This to Your Application](#add-this-to-your-application)

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
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
