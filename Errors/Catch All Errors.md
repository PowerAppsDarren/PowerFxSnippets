# Catching All Errors

If you'd like to literally catch all errors in your canvas Power Apps, simply copy and paste the code shown below. 

Related content: https://youtu.be/8qcPq4peows 📺

The code will work as is after you paste this in, but I recommend that you follow the steps outlined in the code comments. In fact most (**almost 70%**) of it is code comments for your benefit. 

```PowerFx
/*  ======================================================================
    NOTE:   Here are links to helpful documentation if you'd like to fully 
            understand the following code and, perhaps, add to it. 
    ======================================================================
    Topic:  Error, IfError, IsError, IsBlankOrError functions: 
            https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-iferror
    ======================================================================
    Topic:  Errors function
            https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-errors      
    ======================================================================
    Topic: Power Fx Error handling
            https://learn.microsoft.com/en-us/power-platform/power-fx/error-handling      
    // ================================================================ */      
    /* ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

        NOTE:   Please follow the instructions below to finalize the 
                "installation" of this useful snippet of code to your 
                Power Apps application. 

            ➡️🔴 Please be sure to add the Office365Outlook connector! 🔴⬅️

                Any global variables created here to make this code to 
                work should be moved to App.Formulas. 

    ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️*/
    /* ===================================================================
        VARIABLE 1️⃣ fxErrorHandlerEmail
        ===================================================================
        USE:        The email address you'd like to be notified of the 
                    errors that might occur in this application. 
                    If you'd like multiple developers to be emailed, 
                    include them all in the string and simply separate
                    them with semicolons as shown below
                    Example: "jon@domain.com;lisa@domain.com"
        STEP #1:    Change the email address below to your email address  
                    or the person who will be responsible for supporting 
                    this application!
        STEP #2:    Copy the code to App.Formulas ⬇️                    
                    fxErrorHandlerEmail = "YOUR_EMAIL_HERE"; 
        STEP #3:    Delete or comment out the use of the Set() function
    =================================================================== */
    Set(fxErrorHandlerEmail, ";" & User().Email);                           // Put your email address before the semicolon (;)
    // ==================================================================
    // 
    /* ===================================================================
        VARIABLE 2️⃣ fxApplicationName
        ==================================================================
        USE:        The name of the application to be used to let the 
                    developer know which app the Error(s) came from. 
        STEP #1:    Change the name in the string below to reflect the 
                    actual name of this application. 
        STEP #2:    Copy the code to App.Formulas ⬇️
                    fxApplicationName = "The Power Apps Application"; 
        STEP #3:    Delete or comment out the use of the Set() function
    =================================================================== */
    Set(fxApplicationName, "The Power Apps Application");
    // ==================================================================
    // 
    /* ===================================================================
        VARIABLE 3️⃣ fxApplicationURL
        ==================================================================
        USE:        The URL of this application. We use this to link back
                    to this App. 
        OPTION #1:  If you'd like to link to the app to play it as a user 
                    would, go to https://make.powerapps.com/ and find 
                    this app listed there. Click on the 3 virtical dots, 
                    and click on "Details" to copy the app link from. 
                    Replace this: "https://apps.powerapps.com/"
                    ...with that URL. 
                    The URL will look something like this: 
                    https://apps.powerapps.com/play/e/12345efb-ce00-e9be-9b13-42284f521909/a/12345dd2-33c6-43c8-9d4e-96e6bd55b914?tenantId=12345526-320f-46bb-8838-a0626db4c5e2&sourcetime=9921603599236 
        OPTION #2:  If you'd like to link to back here to Power Apps 
                    studio to easily edit the app, simply copy the URL 
                    you have listed above in your browser and 
                    Replace this: "https://apps.powerapps.com/"
                    ...with that URL. 
                    The URL will look something like this: 
                    https://make.powerapps.com/e/12345efb-ce00-e9be-9b13-55284f521909/canvas?referrer=AppsPage&action=edit&form-factor=tablet&app-id=%2Fproviders%2FMicrosoft.PowerApps%2Fapps%2F5fe123d2-33c6-43c8-9d4e-1236bd55b914
        ==================================================================
        STEP #1:    Pick one of the two options outlined above and update
                    the link below. 
        STEP #2:    Copy the code to App.Formulas ⬇️
                    fxApplicationURL = "https://apps.powerapps.com/"; 
        STEP #3:    Delete or comment out the use of the Set() function
    =================================================================== */
    Set(
        fxApplicationURL, 
        "https://apps.powerapps.com/"
    );
    // ==================================================================
    // 
    /* ===================================================================
        VARIABLE 4️⃣ fxLightGrayColor
        ==================================================================
        USE:        This is simply a light gray color assigned to this 
                    variable to be used in the email's formatting. 
                    If you do change it, keep in mind this will be used
                    in CSS style for the HTML format of the email. 
        STEP #1:    Feel free to change it to whatever color you wish.
        STEP #2:    Copy the code to App.Formulas ⬇️
                    fxLightGrayColor = "#e5e5e5"; 
        STEP #3:    Delete or comment out the use of the Set() function
    =================================================================== */
    Set(fxLightGrayColor, "#e5e5e5");
    // ==================================================================
    // 
    /* ===================================================================
        VARIABLE 5️⃣ colAppErrors (collection variable)
        ==================================================================
        USE:        This is a collection variable that will hold all the
                    errors that have occurred in this session for the 
                    user. 
        DECIDE:     No changes are needed for this collection variable
                    *UNLESS* you'd like to store these in a data source
                    which might prove advantageous. If you would like to 
                    implement this, then...
        STEP #1:    Create a database table or SharePoint list. 
                    You may call it whatever makes sense to you, but
                    a good name might be "PowerAppsErrors".
                    This name is used in the example below. 
        STEP #2:    Create 9 fields that are single line of text, 
                    string, or nvarchar(255) for SQL Server. 
                    {
                        Kind:                   "",
                        Message:                "",
                        Source:                 "",
                        Observed:               "",
                        HttpResponse:           "",
                        HttpStatusCode:         "",
                        TimeStamp:              "", 
                        Screen:                 "", 
                        UserEmail:              "",
                        UsersName:              ""
                    }
        STEP #3:    Add this data source to this project. 
        STEP #4:    At the bottom of this whole code block, 
                    patch your data source with the contents of 
                    this collection variable in one go:
                    //
                    Patch(PowerAppsErrors, colAppErrors);
                    Clear(colAppErrors);
                    //
    =================================================================== */

    
    /* ===================================================================

    👍👍 The rest of this code may remain unmodified 👍👍

    =================================================================== */
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
        Collect(
            colAppErrors,
            ForAll(
                AllErrors As My, 
                {
                    Kind:                   My.Kind,
                    Message:                Text(My.Message),
                    Source:                 Text(My.Source),
                    Observed:               Text(My.Observed),
                    HttpResponse:           Text(My.Details.HttpResponse),
                    HttpStatusCode:         Text(My.Details.HttpStatusCode),
                    TimeStamp:              Text(Now(), "mm/dd/yyyy hh:mm:ss:ffff AM/PM"),
                    Screen:                 ScreenName, 
                    UserEmail:              MyUsersEmail,
                    UsersName:              MyUsersName
                }
            )
        );
        //  
        // Now it is time to send out an email notification to the developer(s)
        // 
        Office365Outlook.SendEmailV2(
            // =============================================================
            // WHO TO SEND THE EMAIL TO
            // =============================================================
            fxErrorHandlerEmail, 
            // =============================================================
            // SUBJECT OF EMAIL
            // =============================================================
            SubjectLine,
            // =============================================================
            // BODY 
            // =============================================================
            $"<html><body>
                <h3>Error Report for {MyUsersName} ({MyUsersEmail})</h3>
                <table  style='width:100%;'
                        border='1' 
                        cellpadding='10' 
                        cellspacing='0'>
                    <tr style='{LightGrayColorHexBG} width:100%;'>     
                        <th>Time Stamp</th>       
                        <th>Screen Name</th>      
                        <th>Source</th>
                        <th>Error Message</th>
                        <th>Observed</th>  
                        <th>Http Response</th>
                        <th>Http Status Code</th>
                    </tr>" & 
                    Concat(
                        colAppErrors, 
                        $"<tr>
                            <td>{TimeStamp}</td>
                            <td>{ScreenName}</td>
                            <td>{Kind}</td>
                            <td>{Source}</td>
                            <td>{Message}</td>
                            <td>{Observed}</td>
                            <td>{HttpResponse}</td>
                            <td>{HttpStatusCode}</td>
                        </tr>"
                    ) & $"
                    <tr>
                        <td colspan='7' style='{LightGrayColorHexBG}'>
                            <div style=''>
                                From Application: <a href='{fxApplicationURL}'>{fxApplicationName}</a>
                            </div>
                        </td>
                    </tr>
                </table>
            </html></body>"
        );
    );
    //
    /* ===================================================================
        As mentioned at the top of all this code,         
        *IF* you'd like to store these in a data source, 🤔
        then uncomment out the two lines of code below.  👍
    =================================================================== */
    //Patch(PowerAppsErrors, colAppErrors);                 // ⬅️ 
    //Clear(colAppErrors);                                  // ⬅️ 
    // ===================================================================
    //
    //                      END OF App.OnError 🔚
    //
    // ===================================================================
```

## ...if you haven't seen it, here is the accompanying video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/8qcPq4peows?si=pBbyWgpo1gV96U_4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>