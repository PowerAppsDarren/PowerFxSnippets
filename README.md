# Power Fx Snippets 🏆

> The world's most comprehensive collection of Power Fx code snippets for Microsoft Power Platform

[![GitHub stars](https://img.shields.io/github/stars/PowerAppsDarren/PowerFxSnippets?style=social)](https://github.com/PowerAppsDarren/PowerFxSnippets)
[![GitHub issues](https://img.shields.io/github/issues/PowerAppsDarren/PowerFxSnippets)](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
[![GitHub PRs](https://img.shields.io/github/issues-pr/PowerAppsDarren/PowerFxSnippets)](https://github.com/PowerAppsDarren/PowerFxSnippets/pulls)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

## 🚧 Repository Restructuring in Progress (2025-11-17)

**We're making PowerFxSnippets even better!** A comprehensive restructuring is underway to improve navigation, discoverability, and developer experience.

### 🆕 New Structure (In Progress)
The repository is being reorganized into a **feature-first architecture** with:
- 📱 **[app-lifecycle/](./app-lifecycle)** - App initialization, error handling, formulas *(NEW STRUCTURE)*
- 🎨 **[ui-controls/](./ui-controls)** - Control-specific snippets *(NEW STRUCTURE)*
- 🎭 **[ui-patterns/](./ui-patterns)** - Reusable UI patterns *(NEW STRUCTURE)*
- 🌈 **[visual-assets/](./visual-assets)** - SVGs, icons, colors, fonts *(NEW STRUCTURE)*
- 📊 **[data-operations/](./data-operations)** - Data sources and transformations *(NEW STRUCTURE)*
- 🔧 **[functions/](./functions)** - UDFs, UDTs, utilities *(NEW STRUCTURE)*
- 🔗 **[integrations/](./integrations)** - Connectors and flows *(NEW STRUCTURE)*
- 🎓 **[learning/](./learning)** - Tutorials and best practices *(NEW STRUCTURE)*
- 🧰 **[utilities/](./utilities)** - Templates and tools *(NEW STRUCTURE)*

📋 **[View Complete Restructuring Plan](./new-structure-claude-code.md)**

### 📚 Current Structure (Original)
The existing organization remains functional during migration:

## 🚀 Quick Start

**New to Power Fx?** Start here:
- [📚 Getting Started Guide](./README.md)
- [💡 Hello World Examples](learning/tutorials/getting-started/hello-world)
- 🔧 Common Patterns (Coming Soon)

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
- 🔍 People Picker ComboBox (Coming Soon)
- 🎨 Dynamic Theme Colors (Coming Soon)
- 💾 Offline Data Sync (Coming Soon)
- ⚡ Performance Optimization (Coming Soon)

### Advanced Solutions
- 🏗️ Custom Component Library (Coming Soon)
- 🔐 Row-Level Security (Coming Soon)
- 📊 Real-time Dashboard (Coming Soon)
- 🤖 AI Integration (Coming Soon)

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