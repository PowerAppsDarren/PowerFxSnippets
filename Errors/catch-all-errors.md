# Catching All Errors in Power Apps

> 📧 **Get notified of every error without inbox overload** — smart deduplication sends 2 emails instead of 60.

Power Apps can silently swallow errors, leaving users frustrated and developers blind to problems. This error handler catches **every** error in your canvas app and emails you a detailed report — but intelligently groups duplicate errors so you don't get flooded with 50 identical emails.

Whether it's a network timeout, a formula error, or a connector failure, you'll know about it immediately with full context: which screen, which control, the error message, and how many times it occurred.

<img src="catch-all-errrors-thumbnail.png" alt="thumbnail" width="300">

🎬 [Watch the video tutorial](https://youtu.be/8qcPq4peows)

---

## ⚡ Quick Start

| Step | Action | Where |
|:----:|--------|-------|
| 1 | Add **Office365Outlook** connector | Data → Add data |
| 2 | Copy [configuration formulas](#step-1-configure-settings) | `App.Formulas` |
| 3 | Copy [error handler code](#step-2-add-error-handler) | `App.OnError` |

**That's it!** You'll receive email notifications for every unique error.

---

## How It Works

```
Error occurs → Generate signature → Already seen?
                                         ↓
                    ┌────────────────────┴────────────────────┐
                    │ NO (new error)                          │ YES (repeat)
                    │ • Add to collection                     │ • Increment counter
                    │ • Send email with full summary          │ • No email
                    └─────────────────────────────────────────┘
```

**Result:** 60 errors → 2 emails (one per unique error type)

| Scenario | Without This | With This |
|----------|:------------:|:---------:|
| Error A × 50 | 50 emails | 1 email |
| Error B × 10 | 10 emails | 1 email |
| **Total** | **60 emails** | **2 emails** |

---

## Step 1: Configure Settings

Copy to **App.Formulas** and update the highlighted values:

```PowerFx
// ══════════════════════════════════════════════════════════════
// ERROR HANDLER SETTINGS
// ══════════════════════════════════════════════════════════════

// 📧 Who receives error emails (semicolon-separated for multiple)
fxErrorHandlerEmail = "YOUR_EMAIL_HERE";

// 📛 App name (shown in email subject/body)
fxApplicationName = "My Power App";

// 🔗 App URL (Player or Studio link from make.powerapps.com)
fxApplicationURL = "https://apps.powerapps.com/";

// 🎨 Email theme colors (customize to match your brand)
fxEmailColors = {
    HeaderBg:       "#dc2626",      // Red banner background
    HeaderText:     "#ffffff",      // White header text
    CardBg:         "#ffffff",      // White card background
    CardBorder:     "#e5e7eb",      // Light gray border
    TableHeaderBg:  "#f9fafb",      // Very light gray
    TableHeaderText:"#374151",      // Dark gray text
    TableBorder:    "#e5e7eb",      // Light gray
    CountBadgeBg:   "#fef2f2",      // Light red background
    CountBadgeText: "#dc2626",      // Red text
    FooterBg:       "#f3f4f6",      // Light gray footer
    FooterText:     "#6b7280",      // Medium gray
    LinkColor:      "#2563eb"       // Blue links
};
```

> 💡 **Finding your App URL:** Go to make.powerapps.com → Your App → `...` → Details → Web link

---

## Step 2: Add Error Handler

Copy to **App.OnError** — no modifications needed:

```PowerFx
// ══════════════════════════════════════════════════════════════
// ERROR HANDLER - Paste into App.OnError (no changes needed)
// ══════════════════════════════════════════════════════════════
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
            $"<html>
            <head>
                <meta charset='utf-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            </head>
            <body style='margin:0;padding:0;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background-color:#f3f4f6;'>
                <!-- Header Banner -->
                <table width='100%' cellpadding='0' cellspacing='0' style='background-color:{fxEmailColors.HeaderBg};'>
                    <tr>
                        <td style='padding:24px 32px;'>
                            <table width='100%' cellpadding='0' cellspacing='0'>
                                <tr>
                                    <td>
                                        <span style='font-size:28px;'>⚠️</span>
                                        <span style='color:{fxEmailColors.HeaderText};font-size:22px;font-weight:600;margin-left:12px;vertical-align:middle;'>
                                            Error Alert
                                        </span>
                                    </td>
                                    <td style='text-align:right;'>
                                        <span style='color:{fxEmailColors.HeaderText};font-size:14px;opacity:0.9;'>
                                            {Text(CurrentTime, ""mmm dd, yyyy · hh:mm AM/PM"")}
                                        </span>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>

                <!-- Main Content Card -->
                <table width='100%' cellpadding='0' cellspacing='0' style='padding:24px;'>
                    <tr>
                        <td>
                            <table width='100%' cellpadding='0' cellspacing='0' style='background-color:{fxEmailColors.CardBg};border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.1);overflow:hidden;'>
                                <!-- User Info -->
                                <tr>
                                    <td style='padding:24px 24px 16px 24px;border-bottom:1px solid {fxEmailColors.CardBorder};'>
                                        <table width='100%' cellpadding='0' cellspacing='0'>
                                            <tr>
                                                <td>
                                                    <div style='font-size:18px;font-weight:600;color:#111827;margin-bottom:4px;'>
                                                        {MyUsersName}
                                                    </div>
                                                    <div style='font-size:14px;color:#6b7280;'>
                                                        {MyUsersEmail}
                                                    </div>
                                                </td>
                                                <td style='text-align:right;vertical-align:top;'>
                                                    <span style='display:inline-block;background-color:{fxEmailColors.CountBadgeBg};color:{fxEmailColors.CountBadgeText};font-size:14px;font-weight:600;padding:6px 12px;border-radius:20px;'>
                                                        {CountRows(colErrorSignatures)} unique error{If(CountRows(colErrorSignatures)>1,""s"","""")}
                                                    </span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>

                                <!-- Error Table -->
                                <tr>
                                    <td style='padding:0;'>
                                        <table width='100%' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'>
                                            <tr style='background-color:{fxEmailColors.TableHeaderBg};'>
                                                <th style='padding:12px 16px;text-align:center;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};width:70px;'>Count</th>
                                                <th style='padding:12px 16px;text-align:left;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};'>Screen</th>
                                                <th style='padding:12px 16px;text-align:left;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};'>Kind</th>
                                                <th style='padding:12px 16px;text-align:left;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};'>Source</th>
                                                <th style='padding:12px 16px;text-align:left;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};'>Message</th>
                                                <th style='padding:12px 16px;text-align:right;font-size:12px;font-weight:600;color:{fxEmailColors.TableHeaderText};text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid {fxEmailColors.TableBorder};width:140px;'>Timestamps</th>
                                            </tr>" &
                                            Concat(
                                                colErrorSignatures,
                                                $"<tr style='border-bottom:1px solid {fxEmailColors.TableBorder};'>
                                                    <td style='padding:16px;text-align:center;vertical-align:top;'>
                                                        <span style='display:inline-block;background-color:{fxEmailColors.CountBadgeBg};color:{fxEmailColors.CountBadgeText};font-size:16px;font-weight:700;padding:8px 14px;border-radius:8px;min-width:40px;'>
                                                            {ThisRecord.Occurrences}×
                                                        </span>
                                                    </td>
                                                    <td style='padding:16px;vertical-align:top;'>
                                                        <span style='display:inline-block;background-color:#dbeafe;color:#1e40af;font-size:13px;font-weight:500;padding:4px 10px;border-radius:6px;'>
                                                            {ThisRecord.Screen}
                                                        </span>
                                                    </td>
                                                    <td style='padding:16px;vertical-align:top;'>
                                                        <span style='display:inline-block;background-color:#fef3c7;color:#92400e;font-size:13px;font-weight:500;padding:4px 10px;border-radius:6px;'>
                                                            {ThisRecord.Kind}
                                                        </span>
                                                    </td>
                                                    <td style='padding:16px;vertical-align:top;font-size:14px;color:#374151;font-family:ui-monospace,monospace;'>
                                                        {ThisRecord.Source}
                                                    </td>
                                                    <td style='padding:16px;vertical-align:top;font-size:14px;color:#111827;max-width:300px;'>
                                                        {ThisRecord.Message}
                                                    </td>
                                                    <td style='padding:16px;vertical-align:top;text-align:right;'>
                                                        <div style='font-size:12px;color:#6b7280;margin-bottom:4px;'>
                                                            <strong>First:</strong> {ThisRecord.FirstOccurrence}
                                                        </div>
                                                        <div style='font-size:12px;color:#6b7280;'>
                                                            <strong>Last:</strong> {ThisRecord.LastOccurrence}
                                                        </div>
                                                    </td>
                                                </tr>"
                                            ) & $"
                                        </table>
                                    </td>
                                </tr>

                                <!-- Summary Footer -->
                                <tr>
                                    <td style='padding:20px 24px;background-color:{fxEmailColors.FooterBg};border-top:1px solid {fxEmailColors.CardBorder};'>
                                        <table width='100%' cellpadding='0' cellspacing='0'>
                                            <tr>
                                                <td>
                                                    <span style='font-size:14px;color:{fxEmailColors.FooterText};'>
                                                        <strong style='color:#374151;'>{CountRows(colErrorSignatures)}</strong> unique errors ·
                                                        <strong style='color:#374151;'>{Sum(colErrorSignatures, Occurrences)}</strong> total occurrences
                                                    </span>
                                                </td>
                                                <td style='text-align:right;'>
                                                    <a href='{fxApplicationURL}' style='display:inline-block;background-color:{fxEmailColors.LinkColor};color:#ffffff;font-size:14px;font-weight:500;padding:10px 20px;border-radius:8px;text-decoration:none;'>
                                                        Open {fxApplicationName}
                                                    </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>

                <!-- Footer -->
                <table width='100%' cellpadding='0' cellspacing='0'>
                    <tr>
                        <td style='padding:16px 24px 32px 24px;text-align:center;'>
                            <div style='font-size:12px;color:#9ca3af;'>
                                Automated error report from {fxApplicationName}
                            </div>
                        </td>
                    </tr>
                </table>
            </body>
            </html>"
        )
    );

);
```

---

## Debugging with Monitor

The error handler logs to **Power Apps Monitor** so you can see exactly what's happening.

**To open Monitor:** Power Apps Studio → Advanced tools (`Alt+T`) → Monitor → Play your app

| Trace Event | What It Shows |
|-------------|---------------|
| `ErrorHandler: START` | How many errors came in, current screen, user |
| `ErrorHandler: Processing Error` | Each error's signature and whether it's new |
| `ErrorHandler: Pre-Email Check` | Will an email be sent? How many new errors? |
| `ErrorHandler: Sending Email` | Email recipient, subject, error summary |

<details>
<summary>📋 Example Monitor Output</summary>

```
[Information] ErrorHandler: START
    IncomingErrorCount: 3, Screen: "HomeScreen", User: "user@domain.com"

[Information] ErrorHandler: Processing Error
    Signature: "HomeScreen|Button1.OnSelect|Network error"
    IsNew: true, Kind: "Network"

[Information] ErrorHandler: Pre-Email Check
    CountBefore: 0, CountAfter: 1, WillSendEmail: true

[Warning] ErrorHandler: Sending Email
    To: "admin@domain.com"
    UniqueErrorCount: 1
    ErrorSummary: "HomeScreen: Network error (1×)"
```

</details>

> 💡 **For production:** Remove the `Trace()` statements to declutter your Monitor.

---

## Reference: `colErrorSignatures` Collection

The error handler automatically creates this collection to track errors:

| Field | Description |
|-------|-------------|
| `Signature` | Unique key: `Screen\|Source\|Message` |
| `Screen` | Where the error occurred |
| `Source` | Control or function that caused it |
| `Kind` | Error type (Sync, Network, etc.) |
| `Message` | The error message |
| `Occurrences` | How many times this error happened |
| `FirstOccurrence` / `LastOccurrence` | Timestamps |
| `UserEmail` / `UsersName` | Who triggered the error |
| `HttpResponse` / `HttpStatusCode` | API details (if applicable) |

---

## Optional Enhancements

### Display Errors in Your App

Add a gallery bound to `colErrorSignatures` on a debug screen:

```PowerFx
// Gallery.Items
colErrorSignatures

// Label formulas
ThisItem.Occurrences & "× - " & ThisItem.Message
```

### Clear Errors on App Start

Add to `App.OnStart` for a fresh collection each session:

```PowerFx
Clear(colErrorSignatures);
```

### Persist Errors to SharePoint/Database

<details>
<summary>📋 Click to expand persistence code</summary>

Create a table/list with columns matching the collection fields, then add to a "Save & Exit" button:

```PowerFx
ForAll(
    colErrorSignatures,
    Patch(
        PowerAppsErrors,        // Your data source
        Defaults(PowerAppsErrors),
        {
            Signature:       Signature,
            Screen:          Screen,
            Source:          Source,
            Kind:            Kind,
            Message:         Message,
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

</details>

---

## Further Reading

- [Error, IfError, IsError functions](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-iferror)
- [Errors function](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-errors)
- [Power Fx Error handling](https://learn.microsoft.com/en-us/power-platform/power-fx/error-handling)

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude Opus 4.5 | Redesigned email template with modern styling: header banner, color-coded badges, card layout |
| 2025-12-17 | Claude Opus 4.5 | Added `fxEmailColors` record for customizable email theming |
| 2025-12-17 | Claude Opus 4.5 | Created `email-template-preview.html` for live preview and color customization |
| 2025-12-17 | Claude Opus 4.5 | Rewrote documentation for clarity: added quick-start, visual flow diagram, collapsible sections |
| 2025-12-17 | Claude Opus 4.5 | Added diagnostic logging with Trace() statements |
| 2025-12-17 | Claude Opus 4.5 | Fixed multi-row email output with explicit ThisRecord references |
| 2025-12-04 | Claude Opus 4.5 | Implemented v2.2 with signature-based deduplication |
| 2025-12-04 | Claude Opus 4.5 | Added occurrence counting and full session reports |
