# Catching All Errors

If you'd like to literally catch all errors in your canvas Power Apps, simply copy and paste the code shown below.

Related content: https://youtu.be/8qcPq4peows
![thumbnail](catch-all-errrors-thumbnail.png)

## Table of Contents

- [Catching All Errors](#catching-all-errors)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Documentation Links](#documentation-links)
  - [How It Works: Signature-Based Deduplication](#how-it-works-signature-based-deduplication)
    - [The Approach](#the-approach)
  - [Step 1: Add Named Formulas to `App.Formulas`](#step-1-add-named-formulas-to-appformulas)
  - [Step 2: Add Error Handler to `App.OnError`](#step-2-add-error-handler-to-apponerror)
  - [Diagnostic Logging](#diagnostic-logging)
    - [How to View Diagnostic Logs](#how-to-view-diagnostic-logs)
    - [Trace Events](#trace-events)
    - [Example Monitor Output](#example-monitor-output)
    - [Disabling Diagnostic Logging](#disabling-diagnostic-logging)
  - [Collection Schema: `colErrorSignatures`](#collection-schema-colerrorsignatures)
  - [Optional: View Error Collection in App](#optional-view-error-collection-in-app)
  - [Optional: Clear Errors on App Start](#optional-clear-errors-on-app-start)
  - [Optional: Persist Errors to a Data Source](#optional-persist-errors-to-a-data-source)
    - [Step 1: Create a Data Source](#step-1-create-a-data-source)
    - [Step 2: Persist on App Close](#step-2-persist-on-app-close)
  - [History](#history)

---

## Prerequisites

- ➡️ 🔴 **Add the Office365Outlook connector!** 🔴 ⬅️

## Documentation Links

- [Error, IfError, IsError, IsBlankOrError functions](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-iferror)
- [Errors function](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-errors)
- [Power Fx Error handling](https://learn.microsoft.com/en-us/power-platform/power-fx/error-handling)

---

## How It Works: Signature-Based Deduplication

This error handler uses **smart deduplication** to prevent email floods:

| What Happens | Old Behavior | New Behavior |
|--------------|--------------|--------------|
| Error A occurs 50× | 50 emails | 1 email |
| Error B occurs 10× | 10 emails | 1 email (includes "Error A: 50×") |
| **Total** | **60 emails** | **2 emails** |

### The Approach

1. **Unique Signatures** - Each error gets a signature: `Screen|Source|Message`
2. **Collection Tracking** - `colErrorSignatures` stores unique errors with occurrence counts
3. **Smart Emailing** - Only sends email on **first occurrence** of each unique error
4. **Full Context** - Every email includes the **complete session error summary** with counts

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
// ERROR HANDLER WITH SIGNATURE-BASED DEDUPLICATION - Add to App.OnError
// ============================================================================
// Only sends email on FIRST occurrence of each unique error.
// Subsequent occurrences just increment the counter - no spam!
// ============================================================================
With(
    {
        ScreenName:             App.ActiveScreen.Name,
        MyUsersName:            User().FullName,
        MyUsersEmail:           User().Email,
        CurrentTime:            Now(),
        LightGrayColorHexBG:    "background-color:" & fxLightGrayColor & ";",
        CountBefore:            CountRows(colErrorSignatures),
        SubjectLine:            Concatenate(
                                    "Error(s) occurred in the ",
                                    fxApplicationName,
                                    " application for ",
                                    User().FullName
                                )
    },
    // ═══════════════════════════════════════════════════════════════════════
    // DIAGNOSTIC: Log incoming errors (view in Monitor tool)
    // ═══════════════════════════════════════════════════════════════════════
    Trace(
        "ErrorHandler: START",
        TraceSeverity.Information,
        {
            IncomingErrorCount: CountRows(AllErrors),
            ExistingSignatureCount: CountBefore,
            Screen: ScreenName,
            User: MyUsersEmail
        }
    );
    // Process each error - add new signatures or update existing counts
    ForAll(
        AllErrors As Err,
        With(
            {
                // Generate unique signature: Screen|Source|Message
                ErrSignature: ScreenName & "|" & Text(Err.Source) & "|" & Text(Err.Message),
                IsNewError: IsBlank(LookUp(colErrorSignatures, Signature = ScreenName & "|" & Text(Err.Source) & "|" & Text(Err.Message)))
            },
            // ═══════════════════════════════════════════════════════════
            // DIAGNOSTIC: Log each error being processed
            // ═══════════════════════════════════════════════════════════
            Trace(
                "ErrorHandler: Processing Error",
                TraceSeverity.Information,
                {
                    Signature: ErrSignature,
                    IsNew: IsNewError,
                    Kind: Text(Err.Kind),
                    Message: Text(Err.Message)
                }
            );
            If(
                IsNewError,
                // ═══════════════════════════════════════════════════════════
                // NEW UNIQUE ERROR - Add to tracking collection
                // ═══════════════════════════════════════════════════════════
                Collect(
                    colErrorSignatures,
                    {
                        Signature:       ErrSignature,
                        Screen:          ScreenName,
                        Source:          Text(Err.Source),
                        Kind:            Text(Err.Kind),
                        Message:         Text(Err.Message),
                        Observed:        Text(Err.Observed),
                        HttpResponse:    Text(Err.Details.HttpResponse),
                        HttpStatusCode:  Text(Err.Details.HttpStatusCode),
                        Occurrences:     1,
                        FirstOccurrence: Text(CurrentTime, "MM/dd/yyyy hh:mm:ss AM/PM"),
                        LastOccurrence:  Text(CurrentTime, "MM/dd/yyyy hh:mm:ss AM/PM"),
                        UserEmail:       MyUsersEmail,
                        UsersName:       MyUsersName
                    }
                ),
                // ═══════════════════════════════════════════════════════════
                // EXISTING ERROR - Just increment counter, NO EMAIL
                // ═══════════════════════════════════════════════════════════
                Patch(
                    colErrorSignatures,
                    LookUp(colErrorSignatures, Signature = ErrSignature),
                    {
                        Occurrences:    LookUp(colErrorSignatures, Signature = ErrSignature).Occurrences + 1,
                        LastOccurrence: Text(CurrentTime, "MM/dd/yyyy hh:mm:ss AM/PM")
                    }
                )
            )
        )
    );
    // ═══════════════════════════════════════════════════════════════════════
    // DIAGNOSTIC: Log collection state before email decision
    // ═══════════════════════════════════════════════════════════════════════
    Trace(
        "ErrorHandler: Pre-Email Check",
        TraceSeverity.Information,
        {
            CountBefore: CountBefore,
            CountAfter: CountRows(colErrorSignatures),
            NewErrorsAdded: CountRows(colErrorSignatures) - CountBefore,
            WillSendEmail: CountRows(colErrorSignatures) > CountBefore,
            TotalOccurrences: Sum(colErrorSignatures, Occurrences)
        }
    );
    // ═══════════════════════════════════════════════════════════════════════
    // ONLY SEND EMAIL IF NEW UNIQUE ERROR(S) WERE ADDED
    // ═══════════════════════════════════════════════════════════════════════
    If(
        CountRows(colErrorSignatures) > CountBefore,
        // ═══════════════════════════════════════════════════════════════════════
        // DIAGNOSTIC: Log email content details
        // ═══════════════════════════════════════════════════════════════════════
        Trace(
            "ErrorHandler: Sending Email",
            TraceSeverity.Warning,
            {
                To: fxErrorHandlerEmail,
                Subject: SubjectLine,
                UniqueErrorCount: CountRows(colErrorSignatures),
                ErrorSummary: Concat(colErrorSignatures, ThisRecord.Screen & ": " & ThisRecord.Message & " (" & ThisRecord.Occurrences & "×)", ", ")
            }
        );
        Office365Outlook.SendEmailV2(
            fxErrorHandlerEmail,
            SubjectLine,
            $"<html><body>
                <h3>Error Report for {MyUsersName} ({MyUsersEmail})</h3>
                <p><strong>New unique error detected.</strong> Full session error summary below:</p>
                <table style='width:100%;' border='1' cellpadding='8' cellspacing='0'>
                    <tr style='{LightGrayColorHexBG}'>
                        <th style='text-align:center;'>Count</th>
                        <th>Screen</th>
                        <th>Kind</th>
                        <th>Source</th>
                        <th>Message</th>
                        <th>First Seen</th>
                        <th>Last Seen</th>
                    </tr>" &
                    Concat(
                        colErrorSignatures,
                        $"<tr>
                            <td style='text-align:center;font-weight:bold;font-size:1.2em;'>{ThisRecord.Occurrences}×</td>
                            <td>{ThisRecord.Screen}</td>
                            <td>{ThisRecord.Kind}</td>
                            <td>{ThisRecord.Source}</td>
                            <td>{ThisRecord.Message}</td>
                            <td style='font-size:0.9em;'>{ThisRecord.FirstOccurrence}</td>
                            <td style='font-size:0.9em;'>{ThisRecord.LastOccurrence}</td>
                        </tr>"
                    ) & $"
                    <tr>
                        <td colspan='7' style='{LightGrayColorHexBG}'>
                            <div>
                                <strong>Total unique errors:</strong> {CountRows(colErrorSignatures)} |
                                <strong>Total occurrences:</strong> {Sum(colErrorSignatures, Occurrences)}
                            </div>
                            <div style='margin-top:8px;'>
                                From Application: <a href='{fxApplicationURL}'>{fxApplicationName}</a>
                            </div>
                        </td>
                    </tr>
                </table>
            </body></html>"
        )
    );
);
```

---

## Diagnostic Logging

The error handler includes `Trace()` statements that output to **Power Apps Monitor**. This helps you debug and verify the error handling flow.

### How to View Diagnostic Logs

1. Open your app in **Power Apps Studio**
2. Click **Advanced tools** in the left panel (or press `Alt+T`)
3. Select **Monitor** (opens in new tab)
4. Click **Play** to run your app with monitoring enabled
5. Trigger an error - you'll see trace entries in the Monitor

### Trace Events

| Event | Severity | What It Shows |
|-------|----------|---------------|
| `ErrorHandler: START` | Information | Incoming error count, existing signatures, screen, user |
| `ErrorHandler: Processing Error` | Information | Each error's signature, whether it's new, kind, message |
| `ErrorHandler: Pre-Email Check` | Information | Count before/after, new errors added, will send email flag |
| `ErrorHandler: Sending Email` | Warning | Recipient, subject, unique error count, summary of all errors |

### Example Monitor Output

```
[Information] ErrorHandler: START
    IncomingErrorCount: 3
    ExistingSignatureCount: 0
    Screen: "HomeScreen"
    User: "user@domain.com"

[Information] ErrorHandler: Processing Error
    Signature: "HomeScreen|Button1.OnSelect|Network error"
    IsNew: true
    Kind: "Network"
    Message: "Network error"

[Information] ErrorHandler: Pre-Email Check
    CountBefore: 0
    CountAfter: 1
    NewErrorsAdded: 1
    WillSendEmail: true
    TotalOccurrences: 1

[Warning] ErrorHandler: Sending Email
    To: "admin@domain.com"
    Subject: "Error(s) occurred in the My App application for John Doe"
    UniqueErrorCount: 1
    ErrorSummary: "HomeScreen: Network error (1×)"
```

### Disabling Diagnostic Logging

To disable logging for production, remove or comment out the `Trace()` statements. They have minimal performance impact but may clutter your Monitor during normal debugging.

---

## Collection Schema: `colErrorSignatures`

This collection is automatically created and managed by the error handler:

| Field Name      | Type   | Description |
|-----------------|--------|-------------|
| Signature       | Text   | Unique key: `Screen\|Source\|Message` |
| Screen          | Text   | Screen where error occurred |
| Source          | Text   | Control/function that caused error |
| Kind            | Text   | Error type (Sync, Network, etc.) |
| Message         | Text   | Error message text |
| Observed        | Text   | Where error was observed |
| HttpResponse    | Text   | HTTP response (if applicable) |
| HttpStatusCode  | Text   | HTTP status code (if applicable) |
| Occurrences     | Number | How many times this error occurred |
| FirstOccurrence | Text   | Timestamp of first occurrence |
| LastOccurrence  | Text   | Timestamp of most recent occurrence |
| UserEmail       | Text   | User's email address |
| UsersName       | Text   | User's display name |

---

## Optional: View Error Collection in App

Add a gallery to a debug/admin screen to see all tracked errors:

```PowerFx
// Gallery Items property
colErrorSignatures

// Useful label formulas for the gallery template
ThisItem.Occurrences & "× - " & ThisItem.Message
"First: " & ThisItem.FirstOccurrence
"Last: " & ThisItem.LastOccurrence
```

---

## Optional: Clear Errors on App Start

Add to `App.OnStart` if you want a fresh collection each session:

```PowerFx
Clear(colErrorSignatures);
```

---

## Optional: Persist Errors to a Data Source

If you'd like to store errors in a database or SharePoint list for historical tracking:

### Step 1: Create a Data Source

Create a table/list named `PowerAppsErrors` with these fields:

| Field Name      | Type   |
|-----------------|--------|
| Signature       | Text   |
| Screen          | Text   |
| Source          | Text   |
| Kind            | Text   |
| Message         | Text   |
| Observed        | Text   |
| HttpResponse    | Text   |
| HttpStatusCode  | Text   |
| Occurrences     | Number |
| FirstOccurrence | Text   |
| LastOccurrence  | Text   |
| UserEmail       | Text   |
| UsersName       | Text   |

### Step 2: Persist on App Close

Add to a "Save & Exit" button or similar:

```PowerFx
// Persist all unique errors with their occurrence counts
ForAll(
    colErrorSignatures,
    Patch(
        PowerAppsErrors,
        Defaults(PowerAppsErrors),
        {
            Signature:       Signature,
            Screen:          Screen,
            Source:          Source,
            Kind:            Kind,
            Message:         Message,
            Observed:        Observed,
            HttpResponse:    HttpResponse,
            HttpStatusCode:  HttpStatusCode,
            Occurrences:     Occurrences,
            FirstOccurrence: FirstOccurrence,
            LastOccurrence:  LastOccurrence,
            UserEmail:       UserEmail,
            UsersName:       UsersName
        }
    )
);
Clear(colErrorSignatures);
```

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude Opus 4.5 | Added diagnostic logging with Trace() statements |
| 2025-12-17 | Claude Opus 4.5 | Fixed multi-row email output with explicit ThisRecord references |
| 2025-12-17 | Claude Opus 4.5 | Added table of contents and history log |
| 2025-12-04 | Claude Opus 4.5 | Implemented v2.2 with signature-based deduplication |
| 2025-12-04 | Claude Opus 4.5 | Added occurrence counting and full session reports |
