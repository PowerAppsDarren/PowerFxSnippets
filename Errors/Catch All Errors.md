# Catching All Errors

If you'd like to literally catch all errors in your canvas Power Apps, simply copy and paste the code shown below.

Related content: https://youtu.be/8qcPq4peows 📺

## Prerequisites

- ➡️ 🔴 **Add the Office365Outlook connector!** 🔴 ⬅️

## Documentation Links

- [Error, IfError, IsError, IsBlankOrError functions](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-iferror)
- [Errors function](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-errors)
- [Power Fx Error handling](https://learn.microsoft.com/en-us/power-platform/power-fx/error-handling)

---

## Step 1: Add Named Formulas to `App.Formulas`

Copy this code block to your **App.Formulas** property. Update the values as needed for your application.

```PowerFx
// ============================================================================
// ERROR HANDLER CONFIGURATION - Add to App.Formulas
// ============================================================================

// 1️⃣ Email address(es) to receive error notifications
//    For multiple recipients, separate with semicolons: "jon@domain.com;lisa@domain.com"
fxErrorHandlerEmail = "YOUR_EMAIL_HERE";

// 2️⃣ Application name (appears in email subject and body)
fxApplicationName = "The Power Apps Application";

// 3️⃣ Application URL - Choose one option:
//    OPTION A: Player URL (for users to open the app)
//              Find at make.powerapps.com > Your App > ... > Details > Web link
//              Example: https://apps.powerapps.com/play/e/12345.../a/12345...
//    OPTION B: Studio URL (for developers to edit the app)
//              Copy from browser address bar while editing
//              Example: https://make.powerapps.com/e/12345.../canvas?...
fxApplicationURL = "https://apps.powerapps.com/";

// 4️⃣ Table header background color (CSS hex format)
fxLightGrayColor = "#e5e5e5";
```

---

## Step 2: Add Error Handler to `App.OnError`

Copy this code block to your **App.OnError** property. This code can remain unmodified.

```PowerFx
// ============================================================================
// ERROR HANDLER - Add to App.OnError
// ============================================================================
With(
    {
        SubjectLine:            Concatenate(
                                    "Error(s) occurred in the ",
                                    fxApplicationName,
                                    " application for ",
                                    User().FullName
                                ),
        HowManyErrors:          CountRows(AllErrors) + CountRows(colAppErrors),
        LightGrayColorHexBG:    "background-color:" & fxLightGrayColor & ";",
        ScreenName:             App.ActiveScreen.Name,
        MyUsersName:            User().FullName,
        MyUsersEmail:           User().Email
    },
    // Collect all errors into the colAppErrors collection
    Collect(
        colAppErrors,
        ForAll(
            AllErrors As My,
            {
                Kind:           My.Kind,
                Message:        Text(My.Message),
                Source:         Text(My.Source),
                Observed:       Text(My.Observed),
                HttpResponse:   Text(My.Details.HttpResponse),
                HttpStatusCode: Text(My.Details.HttpStatusCode),
                TimeStamp:      Text(Now(), "MM/dd/yyyy hh:mm:ss:ffff AM/PM"),
                Screen:         ScreenName,
                UserEmail:      MyUsersEmail,
                UsersName:      MyUsersName
            }
        )
    );
    // Send email notification to developer(s)
    Office365Outlook.SendEmailV2(
        fxErrorHandlerEmail,
        SubjectLine,
        $"<html><body>
            <h3>Error Report for {MyUsersName} ({MyUsersEmail})</h3>
            <table style='width:100%;' border='1' cellpadding='10' cellspacing='0'>
                <tr style='{LightGrayColorHexBG} width:100%;'>
                    <th>Time Stamp</th>
                    <th>Screen Name</th>
                    <th>Kind</th>
                    <th>Source</th>
                    <th>Message</th>
                    <th>Observed</th>
                    <th>Http Response</th>
                    <th>Http Status Code</th>
                </tr>" &
                Concat(
                    colAppErrors,
                    $"<tr>
                        <td>{TimeStamp}</td>
                        <td>{Screen}</td>
                        <td>{Kind}</td>
                        <td>{Source}</td>
                        <td>{Message}</td>
                        <td>{Observed}</td>
                        <td>{HttpResponse}</td>
                        <td>{HttpStatusCode}</td>
                    </tr>"
                ) & $"
                <tr>
                    <td colspan='8' style='{LightGrayColorHexBG}'>
                        <div>
                            From Application: <a href='{fxApplicationURL}'>{fxApplicationName}</a>
                        </div>
                    </td>
                </tr>
            </table>
        </body></html>"
    );
);
```

---

## Optional: Persist Errors to a Data Source

If you'd like to store errors in a database or SharePoint list for historical tracking:

### Step 1: Create a Data Source

Create a table/list named `PowerAppsErrors` with these fields (all single-line text):

| Field Name     | Type   |
|----------------|--------|
| Kind           | Text   |
| Message        | Text   |
| Source         | Text   |
| Observed       | Text   |
| HttpResponse   | Text   |
| HttpStatusCode | Text   |
| TimeStamp      | Text   |
| Screen         | Text   |
| UserEmail      | Text   |
| UsersName      | Text   |

### Step 2: Add to End of App.OnError

Add these lines at the end of the `App.OnError` code (after the `Office365Outlook.SendEmailV2` call):

```PowerFx
// Persist errors to data source and clear collection
Patch(PowerAppsErrors, colAppErrors);
Clear(colAppErrors);
```

---

## Video Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/8qcPq4peows?si=pBbyWgpo1gV96U_4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
