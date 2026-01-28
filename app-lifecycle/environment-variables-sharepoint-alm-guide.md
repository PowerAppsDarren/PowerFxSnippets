---
title: "Environment Variables & ALM Guide for SharePoint Solutions"
description: "Complete step-by-step checklist for setting up environment variables and deploying Power Platform solutions across environments and tenants"
category: "app-lifecycle"
subcategory: "alm"
tags:
  - environment-variables
  - sharepoint
  - alm
  - deployment
  - solutions
  - connection-references
  - cross-tenant
difficulty: intermediate
products:
  - power-apps-canvas
  - power-automate
  - power-platform
dependencies:
  - sharepoint-online
  - dataverse
author: "PowerAppsDarren"
created: 2025-12-18
updated: 2025-12-18
license: "MIT"
related:
  - ../learning/best-practices/readme.md
---

# Environment Variables & ALM Guide for SharePoint Solutions

## Table of Contents

- [Why This Matters](#why-this-matters)
- [Prerequisites Checklist](#prerequisites-checklist)
- [Part 1: Understanding the Components](#part-1-understanding-the-components)
  - [Environment Variable Types](#environment-variable-types)
  - [Connection References vs Environment Variables](#connection-references-vs-environment-variables)
- [Part 2: Initial Setup Checklist](#part-2-initial-setup-checklist)
  - [Step 2.1: Create Your Solution](#step-21-create-your-solution)
  - [Step 2.2: Create Connection References](#step-22-create-connection-references)
- [Part 3: SharePoint Environment Variables Setup](#part-3-sharepoint-environment-variables-setup)
  - [Step 3.1: Create Site URL Environment Variable](#step-31-create-site-url-environment-variable)
  - [Step 3.2: Create List Name Environment Variable](#step-32-create-list-name-environment-variable)
  - [Step 3.3: Create Supporting Text Environment Variables](#step-33-create-supporting-text-environment-variables)
- [Part 4: Using Environment Variables in Canvas Apps](#part-4-using-environment-variables-in-canvas-apps)
  - [Step 4.1: Enable Automatic Environment Variable Creation (Recommended)](#step-41-enable-automatic-environment-variable-creation-recommended)
  - [Step 4.2: Add SharePoint Data Source Using Environment Variables](#step-42-add-sharepoint-data-source-using-environment-variables)
  - [Step 4.3: Reference Environment Variables in Formulas](#step-43-reference-environment-variables-in-formulas)
- [Part 5: Using Environment Variables in Power Automate](#part-5-using-environment-variables-in-power-automate)
  - [Step 5.1: Add Environment Variables to Your Flow](#step-51-add-environment-variables-to-your-flow)
  - [Step 5.2: Use Text Environment Variables](#step-52-use-text-environment-variables)
- [Part 6: Deployment Checklist](#part-6-deployment-checklist)
  - [Step 6.1: Prepare for Export](#step-61-prepare-for-export)
  - [Step 6.2: Export the Solution](#step-62-export-the-solution)
  - [Step 6.3: Create Deployment Settings File](#step-63-create-deployment-settings-file)
  - [Step 6.4: Get Connection IDs from Target Environment](#step-64-get-connection-ids-from-target-environment)
  - [Step 6.5: Import to Target Environment](#step-65-import-to-target-environment)
- [Part 7: Cross-Tenant Deployment Checklist](#part-7-cross-tenant-deployment-checklist)
  - [Step 7.1: Pre-Deployment Preparation](#step-71-pre-deployment-preparation)
  - [Step 7.2: Update Deployment Settings for New Tenant](#step-72-update-deployment-settings-for-new-tenant)
  - [Step 7.3: Create Connections in New Tenant](#step-73-create-connections-in-new-tenant)
  - [Step 7.4: Import and Configure](#step-74-import-and-configure)
  - [Step 7.5: Post-Deployment Validation](#step-75-post-deployment-validation)
- [Part 8: Environment Variable Naming Conventions](#part-8-environment-variable-naming-conventions)
  - [Recommended Naming Pattern](#recommended-naming-pattern)
  - [Category Prefixes](#category-prefixes)
- [Part 9: Best Practices](#part-9-best-practices)
  - [Do's](#dos)
  - [Don'ts](#donts)
- [Part 10: Troubleshooting](#part-10-troubleshooting)
  - [Common Issues and Solutions](#common-issues-and-solutions)
- [Part 11: Quick Reference Card](#part-11-quick-reference-card)
  - [Environment Variable Creation Checklist](#environment-variable-creation-checklist)
  - [Deployment Checklist Summary](#deployment-checklist-summary)
- [Resources](#resources)
  - [Official Microsoft Documentation](#official-microsoft-documentation)
  - [Community Resources](#community-resources)

> A comprehensive step-by-step checklist for setting up environment variables, connection references, and deploying Power Platform solutions across environments and Microsoft tenants.

## Why This Matters

When building Power Platform solutions that use SharePoint (or any external data source), hardcoding URLs, list names, and connection details creates a maintenance nightmare. Environment variables solve this by:

- **Eliminating hardcoded values** - No more editing apps when moving between Dev/Test/Prod
- **Enabling true ALM** - Export once, deploy anywhere with different configurations
- **Supporting cross-tenant deployments** - Move solutions to completely different Microsoft 365 tenants
- **Reducing deployment errors** - Configuration is separated from application logic

---

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Power Platform environment access** - Admin or Maker role in target environments
- [ ] **Solution awareness** - Understanding that all components must be in a solution
- [ ] **SharePoint sites created** - Dev, Test, and Production SharePoint sites with identical list structures
- [ ] **Appropriate licensing** - Power Apps/Power Automate licenses (standard licenses work for data source environment variables)
- [ ] **Power Platform CLI installed** (optional but recommended) - For automated deployments

---

## Part 1: Understanding the Components

### Environment Variable Types

| Type        | Use Case                                      | Example                                    |
|-------------|-----------------------------------------------|--------------------------------------------|
| **Text**    | URLs, email addresses, simple strings         | `https://contoso.sharepoint.com/sites/HR`  |
| **Number**  | Numeric configuration values                  | `30` (days for retention)                  |
| **Yes/No**  | Boolean flags                                 | `true` (enable feature)                    |
| **JSON**    | Complex configuration objects                 | `{"timeout": 30, "retries": 3}`            |
| **Data Source** | SharePoint sites/lists, SQL connections   | SharePoint site + list combination         |
| **Secret**  | API keys, passwords (Azure Key Vault)         | Stored securely in Key Vault               |

### Connection References vs Environment Variables

| Component              | What It Stores                    | When to Use                          |
|------------------------|-----------------------------------|--------------------------------------|
| **Connection Reference** | Authentication/identity           | WHO connects (credentials, OAuth)    |
| **Environment Variable** | Configuration data                | WHERE to connect (URLs, list names)  |

**Key Insight**: You need BOTH for SharePoint - a connection reference for authentication AND environment variables for the site/list locations.

---

## Part 2: Initial Setup Checklist

### Step 2.1: Create Your Solution

- [ ] Sign in to [Power Apps](https://make.powerapps.com)
- [ ] Select your **Development environment**
- [ ] Navigate to **Solutions** in the left navigation
- [ ] Click **+ New solution**
- [ ] Fill in the details:
  - [ ] **Display name**: Your solution name (e.g., "HR Onboarding App")
  - [ ] **Name**: Technical name (e.g., "HROnboardingApp")
  - [ ] **Publisher**: Select or create a publisher with your prefix
  - [ ] **Version**: Start with `1.0.0.0`
- [ ] Click **Create**

### Step 2.2: Create Connection References

- [ ] Open your solution
- [ ] Click **+ New** > **More** > **Connection reference**
- [ ] Configure the connection reference:
  - [ ] **Display name**: Descriptive name (e.g., "SharePoint - HR Site")
  - [ ] **Connector**: Select **SharePoint**
  - [ ] **Connection**: Select an existing connection or create new
- [ ] Click **Create**
- [ ] **Repeat** for each connector type your solution uses

**Naming Convention Recommendation**:
```
[Connector] - [Purpose]
Examples:
- SharePoint - HR Documents
- SharePoint - Employee Data
- Office 365 Users - Directory Lookup
```

---

## Part 3: SharePoint Environment Variables Setup

### Step 3.1: Create Site URL Environment Variable

- [ ] In your solution, click **+ New** > **More** > **Environment variable**
- [ ] Configure:
  - [ ] **Display name**: `SharePoint Site URL - HR`
  - [ ] **Name**: `ev_SharePointSiteURL_HR` (auto-generated, customize if needed)
  - [ ] **Data type**: Select **Data source**
  - [ ] **Connector**: Select **SharePoint**
  - [ ] **Parameter type**: Select **Site**
  - [ ] **Default value**: Select your **Development** SharePoint site
  - [ ] **Current value**: Leave blank (set per environment)
- [ ] Click **Save**

### Step 3.2: Create List Name Environment Variable

- [ ] Click **+ New** > **More** > **Environment variable**
- [ ] Configure:
  - [ ] **Display name**: `SharePoint List - Employees`
  - [ ] **Name**: `ev_SharePointList_Employees`
  - [ ] **Data type**: Select **Data source**
  - [ ] **Connector**: Select **SharePoint**
  - [ ] **Parameter type**: Select **List**
  - [ ] **Default value**: Select your Development list
  - [ ] **Current value**: Leave blank
- [ ] Click **Save**
- [ ] **Repeat** for each SharePoint list your solution uses

### Step 3.3: Create Supporting Text Environment Variables

For additional configuration that might change per environment:

- [ ] **Email Recipients**
  ```
  Display name: Notification Email - HR Team
  Name: ev_NotificationEmail_HR
  Data type: Text
  Default value: hr-dev@contoso.com
  ```

- [ ] **Feature Flags**
  ```
  Display name: Enable Advanced Features
  Name: ev_EnableAdvancedFeatures
  Data type: Yes/No
  Default value: No
  ```

- [ ] **API Endpoints** (if applicable)
  ```
  Display name: API Base URL
  Name: ev_APIBaseURL
  Data type: Text
  Default value: https://dev-api.contoso.com
  ```

---

## Part 4: Using Environment Variables in Canvas Apps

### Step 4.1: Enable Automatic Environment Variable Creation (Recommended)

- [ ] Open your canvas app in **Edit mode**
- [ ] Go to **Settings** > **General**
- [ ] Enable **"Automatically create environment variables when adding data sources"**
- [ ] Click **Save**

### Step 4.2: Add SharePoint Data Source Using Environment Variables

**For NEW data sources:**

- [ ] In your canvas app, go to **Data** panel
- [ ] Click **+ Add data**
- [ ] Select **SharePoint**
- [ ] Click the **Advanced** tab
- [ ] Under **Site**, select your environment variable (e.g., `ev_SharePointSiteURL_HR`)
- [ ] Under **List**, select your list environment variable
- [ ] Click **Connect**

**For EXISTING apps (upgrade to use environment variables):**

- [ ] Remove the existing SharePoint data source
- [ ] Re-add it using the steps above with the Advanced tab
- [ ] Update any broken references in your formulas
- [ ] Test thoroughly

### Step 4.3: Reference Environment Variables in Formulas

For non-data-source environment variables, reference them using the `Environment` function:

```powerfx
// Get a text environment variable value
Set(varAPIBaseURL, Environment("ev_APIBaseURL"));

// Use in an HTTP request or other operation
Set(varFullURL, varAPIBaseURL & "/api/employees");

// Check a boolean environment variable
If(
    Environment("ev_EnableAdvancedFeatures") = "true",
    // Show advanced features
    Set(varShowAdvanced, true),
    Set(varShowAdvanced, false)
);
```

> **Note**: The `Environment()` function returns text values. Convert as needed for other data types.

---

## Part 5: Using Environment Variables in Power Automate

### Step 5.1: Add Environment Variables to Your Flow

- [ ] Open your cloud flow (must be in a solution)
- [ ] Add a SharePoint action (e.g., "Get items")
- [ ] For **Site Address**: Click the field, then select **Dynamic content**
- [ ] Search for your environment variable name
- [ ] Select it from the list
- [ ] Repeat for **List Name** field

### Step 5.2: Use Text Environment Variables

- [ ] In any action where you need configurable values
- [ ] Click the field > **Dynamic content**
- [ ] Search for your environment variable
- [ ] Select to insert it

**Example Flow Configuration:**
```
Trigger: When an item is created
├── Site Address: [ev_SharePointSiteURL_HR]
├── List Name: [ev_SharePointList_Employees]

Action: Send an email
├── To: [ev_NotificationEmail_HR]
├── Subject: New Employee Added
```

---

## Part 6: Deployment Checklist

### Step 6.1: Prepare for Export

- [ ] **Verify all components are in the solution**
  - [ ] Canvas apps
  - [ ] Cloud flows
  - [ ] Environment variables
  - [ ] Connection references
  - [ ] Any custom connectors

- [ ] **Test in Development environment**
  - [ ] All functionality works correctly
  - [ ] Environment variables are being used (not hardcoded values)

- [ ] **Check solution dependencies**
  - [ ] Run solution checker
  - [ ] Resolve any warnings or errors

### Step 6.2: Export the Solution

**For Manual Deployment:**

- [ ] Go to **Solutions**
- [ ] Select your solution
- [ ] Click **Export**
- [ ] Choose **Managed** for production, **Unmanaged** for further development
- [ ] Wait for export to complete
- [ ] Download the `.zip` file

**For Automated Deployment (Power Platform CLI):**

```bash
# Authenticate
pac auth create --environment https://[your-env].crm.dynamics.com

# Export solution
pac solution export --name YourSolutionName --path ./exports --managed
```

### Step 6.3: Create Deployment Settings File

- [ ] Generate the settings file template:

```bash
pac solution create-settings --solution-zip ./exports/YourSolution.zip --settings-file deployment-settings.json
```

- [ ] Edit `deployment-settings.json` with target environment values:

```json
{
  "EnvironmentVariables": [
    {
      "SchemaName": "ev_SharePointSiteURL_HR",
      "Value": "https://contoso.sharepoint.com/sites/HR-Production"
    },
    {
      "SchemaName": "ev_SharePointList_Employees",
      "Value": "Employees"
    },
    {
      "SchemaName": "ev_NotificationEmail_HR",
      "Value": "hr-team@contoso.com"
    },
    {
      "SchemaName": "ev_EnableAdvancedFeatures",
      "Value": "true"
    }
  ],
  "ConnectionReferences": [
    {
      "LogicalName": "your_sharepoint_connection_ref",
      "ConnectionId": "[Get from target environment]",
      "ConnectorId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline"
    }
  ]
}
```

### Step 6.4: Get Connection IDs from Target Environment

- [ ] Sign in to [Power Apps](https://make.powerapps.com)
- [ ] Switch to your **target environment**
- [ ] Go to **Data** > **Connections**
- [ ] Find the SharePoint connection
- [ ] Click on it and copy the **Connection ID** from the URL
  - URL format: `https://make.powerapps.com/.../connections/shared_sharepointonline/[CONNECTION_ID]/details`
- [ ] Update your `deployment-settings.json` with this ID

### Step 6.5: Import to Target Environment

**Manual Import:**

- [ ] Go to target environment in Power Apps
- [ ] Navigate to **Solutions**
- [ ] Click **Import solution**
- [ ] Upload your `.zip` file
- [ ] Click **Next**
- [ ] **Set environment variable values** for this environment
- [ ] **Configure connection references** - select appropriate connections
- [ ] Click **Import**
- [ ] Wait for import to complete

**Automated Import with Settings File:**

```bash
# Switch to target environment
pac auth create --environment https://[target-env].crm.dynamics.com

# Import with settings
pac solution import --path ./exports/YourSolution_managed.zip --settings-file deployment-settings-prod.json
```

---

## Part 7: Cross-Tenant Deployment Checklist

Deploying to a completely different Microsoft 365 tenant requires additional steps.

### Step 7.1: Pre-Deployment Preparation

- [ ] **Document all external dependencies**
  - [ ] SharePoint site URLs and structures
  - [ ] User/group references
  - [ ] External API endpoints
  - [ ] Custom connector configurations

- [ ] **Create matching infrastructure in target tenant**
  - [ ] SharePoint sites with identical structure
  - [ ] SharePoint lists with matching columns
  - [ ] User accounts with appropriate permissions
  - [ ] Any required Azure resources

### Step 7.2: Update Deployment Settings for New Tenant

- [ ] Create tenant-specific deployment settings file:

```json
{
  "EnvironmentVariables": [
    {
      "SchemaName": "ev_SharePointSiteURL_HR",
      "Value": "https://newtenant.sharepoint.com/sites/HR"
    },
    {
      "SchemaName": "ev_SharePointList_Employees",
      "Value": "Employees"
    }
  ],
  "ConnectionReferences": [
    {
      "LogicalName": "your_sharepoint_connection_ref",
      "ConnectionId": "[NEW TENANT CONNECTION ID]",
      "ConnectorId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline"
    }
  ]
}
```

### Step 7.3: Create Connections in New Tenant

- [ ] Sign in to the new tenant's Power Platform environment
- [ ] Go to **Data** > **Connections**
- [ ] Click **+ New connection**
- [ ] Create connections for each connector type:
  - [ ] SharePoint
  - [ ] Office 365 Users
  - [ ] Any other connectors used
- [ ] Note the Connection IDs for your deployment settings

### Step 7.4: Import and Configure

- [ ] Import the solution using the cross-tenant deployment settings
- [ ] **Verify all environment variable values** are correct for new tenant
- [ ] **Test all connection references** are working
- [ ] **Update any user/group references** that might be hardcoded

### Step 7.5: Post-Deployment Validation

- [ ] Test all canvas apps
- [ ] Test all cloud flows (manually trigger or use test data)
- [ ] Verify SharePoint data is reading/writing correctly
- [ ] Check all integrations and external connections
- [ ] Validate user permissions and sharing

---

## Part 8: Environment Variable Naming Conventions

### Recommended Naming Pattern

```
[prefix]_[Category]_[Purpose]

Examples:
ev_SharePoint_SiteURL_HR
ev_SharePoint_List_Employees
ev_Email_Notification_HR
ev_API_BaseURL
ev_Feature_EnableAdvanced
```

### Category Prefixes

| Prefix       | Use For                              |
|--------------|--------------------------------------|
| `SharePoint` | SharePoint sites and lists           |
| `Email`      | Email addresses and distribution     |
| `API`        | External API endpoints               |
| `Feature`    | Feature flags (Yes/No)               |
| `Config`     | General configuration values         |
| `Secret`     | Azure Key Vault references           |

---

## Part 9: Best Practices

### Do's

- [ ] **Always use solutions** - Environment variables only work within solutions
- [ ] **Create environment variables BEFORE building apps** - Easier than retrofitting
- [ ] **Use descriptive names** - Future you will thank present you
- [ ] **Document your variables** - Use the Description field
- [ ] **Set default values** - Provide sensible defaults for development
- [ ] **Use Data Source type for SharePoint** - Don't use Text type for SharePoint URLs
- [ ] **Test in isolated environment first** - Before deploying to production
- [ ] **Version your deployment settings files** - Store in source control
- [ ] **Create per-environment settings files** - `deployment-settings-dev.json`, `deployment-settings-prod.json`

### Don'ts

- [ ] **Don't hardcode SharePoint URLs in apps** - Use environment variables
- [ ] **Don't share connection credentials** - Use connection references
- [ ] **Don't skip testing after deployment** - Always validate
- [ ] **Don't forget to update Current Values** - Default values aren't used at runtime if Current Value exists
- [ ] **Don't use Text type for SharePoint sites/lists** - Use Data Source type instead

---

## Part 10: Troubleshooting

### Common Issues and Solutions

#### Issue: "Data source not found after import"

**Cause**: Environment variable values not set or incorrect

**Solution**:
- [ ] Go to solution > Environment variables
- [ ] Verify Current Value is set for each variable
- [ ] Ensure SharePoint site/list exists in target environment
- [ ] Remove and re-add data source in canvas app

#### Issue: "Connection reference not working"

**Cause**: Connection doesn't exist or user doesn't have access

**Solution**:
- [ ] Verify connection exists in target environment
- [ ] Check connection is shared with appropriate users
- [ ] Ensure connection owner has access to SharePoint site

#### Issue: "Environment variable shows old value"

**Cause**: Caching or Current Value overriding Default Value

**Solution**:
- [ ] Clear browser cache
- [ ] Check both Default Value AND Current Value
- [ ] Current Value always takes precedence over Default Value

#### Issue: "SharePoint list columns not appearing"

**Cause**: Known SharePoint ALM limitation

**Solution**:
- [ ] This is a known issue with SharePoint metadata refresh
- [ ] The app WILL work at runtime with correct values
- [ ] Use Monitor to verify correct data source is being used
- [ ] Don't rely on Power Apps Studio preview in target environment

---

## Part 11: Quick Reference Card

### Environment Variable Creation Checklist

```
For each configurable value:
[ ] Identify if it changes between environments
[ ] Choose appropriate data type
[ ] Create in solution with naming convention
[ ] Set default value (dev environment)
[ ] Document purpose in description
[ ] Update apps/flows to use variable
[ ] Test in dev environment
```

### Deployment Checklist Summary

```
Pre-Export:
[ ] All components in solution
[ ] Environment variables configured
[ ] Connection references created
[ ] Solution checker passed

Export:
[ ] Export as managed (production) or unmanaged (dev)
[ ] Generate deployment settings file

Pre-Import (Target):
[ ] Connections created
[ ] Connection IDs collected
[ ] Deployment settings updated
[ ] SharePoint infrastructure ready

Post-Import:
[ ] Environment variable values verified
[ ] Connection references connected
[ ] Functional testing completed
[ ] User permissions configured
```

---

## Resources

### Official Microsoft Documentation

- [Environment Variables Overview](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)
- [Data Source Environment Variables in Canvas Apps](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables-data-source-canvas-apps)
- [Connection References Overview](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)
- [ALM with Power Platform](https://learn.microsoft.com/en-us/power-platform/alm/)
- [Power Platform CLI](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction)

### Community Resources

- [Power Platform Community](https://powerplatform.microsoft.com/community/)
- [Data Source Environment Variables Blog Post](https://powerapps.microsoft.com/en-us/blog/announcing-data-source-environment-variables/)

---

## History

| Date       | Author          | Changes                                           |
|------------|-----------------|---------------------------------------------------|
| 2025-12-18 | PowerAppsDarren | Initial creation with comprehensive ALM checklist |

