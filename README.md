# Power Fx Snippets 🏆

> The world's most comprehensive collection of Power Fx code snippets for Microsoft Power Platform

[![GitHub stars](https://img.shields.io/github/stars/PowerAppsDarren/PowerFxSnippets?style=social)](https://github.com/PowerAppsDarren/PowerFxSnippets)
[![GitHub issues](https://img.shields.io/github/issues/PowerAppsDarren/PowerFxSnippets)](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
[![GitHub PRs](https://img.shields.io/github/issues-pr/PowerAppsDarren/PowerFxSnippets)](https://github.com/PowerAppsDarren/PowerFxSnippets/pulls)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

## 🎉 What's New -- v2.0.0 Release

**Major repository restructuring complete!** The repository has been reorganized with a **feature-first architecture** for better navigation, discoverability, and developer experience.

📣 **[Read the full v2.0.0 Announcement](./docs/ANNOUNCEMENT-v2.0.0.md)** | 📋 **[Release Notes](./RELEASE-NOTES-v2.0.0.md)**

### ✅ New Structure (9 Categories)

| Category | Description | Highlights |
|----------|-------------|------------|
| 📱 **[app-lifecycle/](./app-lifecycle)** | App initialization & lifecycle | Named formulas, OnStart, OnError |
| 🎨 **[ui-controls/](./ui-controls)** | Control-specific snippets | Gallery, buttons, inputs, charts |
| 🎭 **[ui-patterns/](./ui-patterns)** | Reusable UI patterns | Dialogs, menus, theming, components |
| 🌈 **[visual-assets/](./visual-assets)** | Visual resources | SVGs, icons, colors, fonts, emojis |
| 📊 **[data-operations/](./data-operations)** | Data & transformations | Sample data, JSON, geocoding |
| 🔧 **[functions/](./functions)** | Functions & utilities | UDFs, algorithms, string manipulation |
| 🔗 **[integrations/](./integrations)** | External services | Office 365, Power Automate connectors |
| 🎓 **[learning/](./learning)** | Educational content | Tutorials, certification, best practices |
| 🧰 **[utilities/](./utilities)** | Tools & templates | Validation scripts, templates |

### 🆕 January 2026 Highlights

- **468 markdown files** with standardized structure
- **YAML frontmatter** on all snippets for searchability
- **Table of Contents** auto-generated in all files
- **History sections** tracking changes in every file
- **GitHub Actions** for automated snippet validation and weekly link checking
- **Unit test coverage** for all repository tools (validator, index generator, migration helper)
- **Issue & PR templates** for consistent contributions
- **[PRODUCT-INDEX.md](./PRODUCT-INDEX.md)** -- Browse snippets by Power Platform product
- **[MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md)** -- Find where your old bookmarks moved

📋 **[View Migration Details](./MIGRATION-GUIDE.md)** | 🔍 **[Browse by Product](./PRODUCT-INDEX.md)**

## 🚀 Quick Start

**New to Power Fx?** Start here:
- [📚 Getting Started Guide](./learning/tutorials/getting-started)
- [💡 Hello World Examples](./learning/tutorials/getting-started/hello-world)
- [⚠️ Power Fx Gotchas](./Reference/power-fx-gotchas.md) -- Syntax quirks that differ from .NET/Excel/JavaScript

### Copy-Paste Code Examples

**1. Detect if the app is running in Studio (edit) mode:**

```powerfx
// Named formula -- place in App.Formulas
fxIsInStudioMode = StartsWith(Host.Version, "PowerApps-Studio");
```
> Source: [app-lifecycle/formulas/expressions/boolean-is-in-studio-mode.md](./app-lifecycle/formulas/expressions/boolean-is-in-studio-mode.md)

**2. Alternating row colors (zebra striping) in a Gallery:**

```powerfx
// Set TemplateFill on your Gallery control
If(
    Mod(ThisItem.OrderNumber, 2) = 0,
    Color.White,
    ColorFade(App.Theme.Colors.Lighter80, 50%)
)
```
> Source: [ui-controls/gallery/styling/alternating-row-colors.md](./ui-controls/gallery/styling/alternating-row-colors.md)

**3. Convert a Color value to its hex string:**

```powerfx
// User-defined function -- place in App.Formulas
fxGetHexFromColor(ColorValue: Color): Text = Left(
    Substitute(
        JSON(ColorValue, JSONFormat.Compact),
        """",
        ""
    ),
    7
);
```
> Source: [ui-patterns/theming/Theming.md](./ui-patterns/theming/Theming.md)

**4. Random screen transition effect (UDF):**

```powerfx
// User-defined function -- place in App.Formulas
fxRandomScreenTransition(): Text =
    With(
        { RandomNumber: RandBetween(1, 5) },
        Switch(
            RandomNumber,
            1, ScreenTransition.Cover,
            2, ScreenTransition.CoverRight,
            3, ScreenTransition.Fade,
            4, ScreenTransition.UnCover,
            5, ScreenTransition.UnCoverRight,
            ScreenTransition.None
        )
    );
```
> Source: [app-lifecycle/formulas/user-defined-functions/screen-transition-random.md](./app-lifecycle/formulas/user-defined-functions/screen-transition-random.md)

**5. Parse JSON returned from a Power Automate flow:**

```powerfx
UpdateContext(
    {
        locFlowResult: ParseJSON(MyFlow.Run(ThisItem.URL).response).value
    }
);
ClearCollect(
    colParsedData,
    ForAll(
        locFlowResult As MyRecord,
        {
            Name:        Text(MyRecord.Name),
            DisplayName: Text(MyRecord.DisplayName),
            Type:        Text(MyRecord.Type)
        }
    )
);
```
> Source: [data-operations/json/parsing-flows-json.md](./data-operations/json/parsing-flows-json.md)

## 📖 Table of Contents

### 🎯 Core Categories

| Category                                                      | Description                          | Quick Access                                                                                                                       |
|---------------------------------------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**01-getting-started**](learning/tutorials/getting-started)               | Entry point for new developers       | [Hello World](learning/tutorials/getting-started/hello-world) • Common Patterns (Coming Soon)                        |
| [**02-app-architecture**](./app-lifecycle)             | Application structure and lifecycle  | [App Events](app-lifecycle) • [Navigation](app-lifecycle)                         |
| [**03-user-interface**](./ui-controls)                 | UI components and user experience    | [Controls](./controls) • [Themes](design)                                      |
| [**04-data-management**](./data-operations)               | Data operations and sources          | [Data Sources](./data-sources) • [Validation](data-operations)                           |
| [**05-business-logic**](./functions)                 | Functions and calculations           | [Functions](./functions) • [Error Handling](app-onerror)                                |
| [**06-integrations**](./integrations)                     | External services and APIs           | [Microsoft 365](integrations) • [Azure](integrations)                                     |
| [**07-assets-and-media**](./visual-assets)             | Visual assets and media              | [Icons](./icons) • [SVGs](visual-assets/svgs)                                                       |
| [**08-advanced-patterns**](./best-practices)           | Expert techniques and architecture   | [Custom Components](ui-patterns/components/custom-components) • [Security](best-practices)             |
| [**09-learning-resources**](./learning)         | Tutorials and educational content    | [Tutorials](learning/tutorials) • [Best Practices](./best-practices)                        |

### 🛠️ Repository Tools

- [**📋 Contribution Guide**](./CONTRIBUTING.md) - How to add your own snippets
- [**🔧 Tools & Utilities**](./tools) - Helper scripts and utilities
- [**📚 Documentation**](./docs) - Detailed guides and references
- [**⚠️ Power Fx Gotchas**](reference/power-fx-gotchas.md) - Syntax quirks that differ from .NET/Excel/JavaScript
- [**🏛️ Code of Conduct**](./CODE_OF_CONDUCT.md) - Community standards

## 🔥 Popular Snippets

### Quick Wins (5 minutes or less)

| Snippet | Category | Difficulty |
|---------|----------|------------|
| [Alternating Row Colors](./ui-controls/gallery/styling/alternating-row-colors.md) | ui-controls / gallery | Intermediate |
| [Detect Studio Mode](./app-lifecycle/formulas/expressions/boolean-is-in-studio-mode.md) | app-lifecycle / formulas | Beginner |
| [Color to Hex Conversion](./ui-patterns/theming/Theming.md) | ui-patterns / theming | Intermediate |
| [Random Screen Transition](./app-lifecycle/formulas/user-defined-functions/screen-transition-random.md) | app-lifecycle / formulas | Beginner |
| [Error Kinds Collection](./app-lifecycle/formulas/collections/error-kinds.md) | app-lifecycle / formulas | Beginner |

### Advanced Solutions

| Snippet | Category | Difficulty |
|---------|----------|------------|
| [Responsive Hero Cards Gallery](./ui-controls/gallery/layouts/responsive-gallery.md) | ui-controls / gallery | Intermediate |
| [Get Manager Rollup (Org Hierarchy)](./integrations/connectors/office365-users/get-manager-rollup.md) | integrations / Office 365 | Advanced |
| [Parse JSON from Power Automate Flows](./data-operations/json/parsing-flows-json.md) | data-operations / json | Intermediate |
| [Proportional Value Calculator (UDF)](./app-lifecycle/formulas/user-defined-functions/fxfindproportionalvalue.md) | app-lifecycle / formulas | Intermediate |
| [Microsoft Base Themes](./ui-patterns/theming/Microsoft-Base-Themes.md) | ui-patterns / theming | Beginner |

> **Browse all snippets:** [By Category](#-core-categories) | [By Product](./PRODUCT-INDEX.md) | [By Tag](./SEARCH-INDEX.md)

## 🎯 How to Use This Repository

### For Beginners
1. Start with [**Getting Started**](learning/tutorials/getting-started) category
2. Browse by **difficulty level** (beginner/intermediate/advanced)
3. Use the **search function** with keywords like "gallery", "form", or "SharePoint"

### For Experienced Developers
1. Jump directly to specific **categories** that match your needs
2. Filter by **tags** and **prerequisites**
3. Check **related snippets** for comprehensive solutions

### For Teams
1. Use [**Learning Resources**](./learning) for onboarding
2. Implement [**Best Practices**](./best-practices) across projects
3. Leverage [**Advanced Patterns**](./best-practices) for complex scenarios

## 🔍 Search & Discovery

### By Technology
- **Power Apps**: [Canvas Apps](./ui-controls), [Data Sources](./data-operations)
- **Power Automate**: [Flows](integrations/power-automate), [API Calls](integrations)
- **Dataverse**: [Data Operations](./data-operations), [Security](best-practices)
- **SharePoint**: [Integration](integrations), [Document Management](./data-sources)

### By Use Case
- **Business Apps**: [Forms](./controls), [Workflows](./functions)
- **Dashboards**: [Charts](data-operations), [KPIs](functions)
- **Mobile Apps**: Responsive Design (Coming Soon), [Offline](data-operations)
- **Admin Tools**: [User Management](integrations), [Audit Logs](best-practices)

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Ways to Contribute
- **📝 Add Snippets**: Share your Power Fx solutions
- **🐛 Report Issues**: Help improve existing content
- **💡 Suggest Improvements**: Propose new categories or features
- **📚 Improve Documentation**: Enhance guides and navigation

### Getting Started
1. Read our [**Contribution Guide**](./CONTRIBUTING.md)
2. Check existing [**Issues**](https://github.com/PowerAppsDarren/PowerFxSnippets/issues) for ideas
3. Fork the repository and create your branch
4. Add your snippet with proper metadata
5. Submit a pull request

### Snippet Requirements
- ✅ **Metadata**: Complete YAML front matter with title, description, category, tags, difficulty
- ✅ **Documentation**: Clear explanation and usage examples
- ✅ **Code Quality**: Well-formatted, commented Power Fx code
- ✅ **Testing**: Include test scenarios where applicable

## 📊 Repository Stats

- **📁 Categories**: 9 main categories with 40+ subcategories
- **📄 Snippets**: 500+ code examples and patterns
- **🏷️ Tags**: 200+ searchable tags for filtering
- **👥 Contributors**: 50+ community members
- **⭐ Stars**: Your support helps grow the community!

## 🏢 About Power Fx

Power Fx is the low-code language that powers Microsoft Power Platform applications. It combines the familiarity of Excel formulas with the power of a programming language, enabling both citizen developers and professional developers to create sophisticated business applications.

**Key Features:**
- 📊 **Excel-like syntax** you already know
- 🔧 **IntelliSense** and formula suggestions
- 🌐 **Cross-platform** compatibility
- ⚡ **Real-time evaluation** and debugging
- 🔗 **Rich integrations** with Microsoft 365 and Azure

## 📞 Support & Community

### Get Help
- 🐛 **Issues**: [Report bugs or request features](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
- 💬 **Discussions**: [Join community conversations](https://github.com/PowerAppsDarren/PowerFxSnippets/discussions)

### Community Resources
- 🌐 **Power Platform Community**: [powerplatform.com](https://powerplatform.microsoft.com/)
- 📚 **Microsoft Learn**: [Power Fx documentation](https://learn.microsoft.com/en-us/power-platform/power-fx/)
- 🎓 **Training**: [Power Apps training](https://learn.microsoft.com/en-us/training/paths/create-powerapps/)

## ❓ FAQ / Troubleshooting

**Where did my old bookmark go?**
The repository was restructured in v2.0.0 (January 2026). All files were reorganized into 9 feature-based categories. See the **[Migration Guide](./MIGRATION-GUIDE.md)** for a complete mapping of old paths to new locations.

**How do I find snippets by product (Canvas Apps, Model-Driven, Power Automate)?**
Check the **[Product Index](./PRODUCT-INDEX.md)** which groups every snippet by the Power Platform product it applies to.

**How do I contribute a snippet?**
Read the **[Contributing Guide](./CONTRIBUTING.md)** for instructions on adding snippets, reporting issues, or proposing improvements. Every snippet needs YAML frontmatter, a clear description, and working Power Fx code.

**Power Fx is not working the way I expected.**
Power Fx has important syntax differences from .NET, Excel, and JavaScript. Before debugging further, read the **[Power Fx Gotchas](./Reference/power-fx-gotchas.md)** document -- especially the section on date/time formatting where `m`/`mm` is context-sensitive.

**How do I validate my snippet before submitting?**
Run the snippet validator tool: `python utilities/tools/snippet-validator.py your-file.md`. This checks YAML frontmatter, required fields, and valid category/tag values.

## 📄 License

This repository is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- **Power Apps Community** for inspiration and contributions
- **Microsoft Power Platform** team for creating Power Fx
- **All Contributors** who share their knowledge and expertise
- **You** for being part of this amazing community!

---

**⭐ Found this helpful?** [Star this repository](https://github.com/PowerAppsDarren/PowerFxSnippets) to show your support!

**🤝 Want to contribute?** Check out our [Contribution Guide](./CONTRIBUTING.md) to get started!
---

## History

| Date       | Author    | Changes                                                                      |
|------------|-----------|------------------------------------------------------------------------------|
| 2026-01-29 | Phase 6   | v2.0.0 launch updates: enhanced Quick Start, Popular Snippets, FAQ, What's New |
| 2026-01-27 | Migration | Initial TOC and history section added                                        |
