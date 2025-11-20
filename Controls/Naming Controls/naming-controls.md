---
title: "Naming Controls Guidelines"
description: "Best practices and rules for naming controls in Power Apps."
category: "Controls"
tags: ["naming", "best-practices", "standards", "conventions"]
difficulty: beginner
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Naming Controls

- [A better reading experience](https://powerplatformlinks.com/Power+Apps/Canvas/Naming+Controls).

The names and scope of all control names in canvas Power Apps are global! This means that if you have a control named "txtFirstName" in one screen, you cannot have another control with the same name in another screen. The name "txtFirstName" is reserved for the first control you created with that name, and you cannot use it for another control. This rule applies to all control names, regardless of the control type or the screen it's on. It is for this reason, it's a good practice to use unique and descriptive names for your controls to avoid any confusion or errors in your app. This may mean including some of the screen name or the screen's purpose in the controls for that particular screen (minus any spaces or the word "Screen" - which developers are encouraged to use in screen names). For example, "txt_Customer_FirstName" or "btn_NewOrder_Submit". 

Control names also have specific rules regarding allowed and disallowed characters. Here's a breakdown of the naming conventions for control names in canvas Power Apps:

## Allowed Characters

1. Letters (A-Z, a-z)
2. Numbers (0-9)
3. Underscore (_)

## Naming Rules

1. Control names must start with a letter (A-Z, a-z).
2. After the first character, you can use letters, numbers, and underscores.
3. Names are case-sensitive. For example, "btnSubmit" and "BtnSubmit" are considered different names.
4. Names must be unique within the app.

## Not Allowed

1. Spaces
2. Special characters (e.g., @, #, $, %, &, *, -, +, =, /, \, etc.)
3. Reserved words (such as If, Then, Else, etc.)

## Best Practices

1. Use camel case for naming controls. For example: "txtFirstName", "btnSubmit", "galCustomers".
2. Start the name with a three-letter prefix indicating the control type. For example:
   - "txt" for text input
   - "btn" for button
   - "gal" for gallery
   - "lbl" for label[2][5]

3. Make names descriptive and meaningful. For example, "txtEmployeeName" is better than "txt1".

4. Avoid using numbers at the end of control names unless absolutely necessary. Instead, use more descriptive suffixes.

5. Keep names concise while still being clear about the control's purpose.

By following these rules and best practices, you'll create control names that are both valid and easily understandable, which will improve the readability and maintainability of your Power Apps[1][2][5].

Citations:
[1] https://www.linkedin.com/pulse/powerapps-best-practices-naming-conventions-samir-daoudi
[2] https://www.matthewdevaney.com/power-apps-coding-standards-for-canvas-apps/power-apps-standards-naming-conventions/
[3] https://www.c-sharpcorner.com/article/prevent-special-characters-in-powerapps-forms/
[4] https://www.microsoft.com/en-us/power-platform/blog/power-apps/powerapps-canvas-app-coding-standards-and-guidelines/
[5] https://learn.microsoft.com/en-us/power-apps/guidance/coding-guidelines/code-readability

## Free Community & Course Materials
🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com 

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

