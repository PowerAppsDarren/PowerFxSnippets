# Contributing to Power Fx Snippets

Thank you for your interest in contributing to the Power Fx Snippets repository! 🎉

This document provides guidelines and information for contributors. Whether you're fixing a bug, adding a new snippet, or improving documentation, your contributions help make this repository better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Contribution Process](#contribution-process)
- [Snippet Guidelines](#snippet-guidelines)
- [Documentation Standards](#documentation-standards)
- [Testing](#testing)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Recognition](#recognition)

## 🤝 Code of Conduct

This project follows our [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to uphold these standards and foster an inclusive community.

## 🚀 Getting Started

### Prerequisites
- Basic understanding of Power Fx
- GitHub account
- Text editor (VS Code recommended)
- Basic knowledge of Markdown and YAML

### Quick Setup
1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/PowerFxSnippets.git
   cd PowerFxSnippets
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-snippet-name
   ```
4. **Make** your changes
5. **Test** your changes (see [Testing](#testing))
6. **Commit** your changes (see [Commit Messages](#commit-messages))
7. **Push** to your fork:
   ```bash
   git push origin feature/your-snippet-name
   ```
8. **Create** a Pull Request on GitHub

## 🎯 Types of Contributions

### Code Snippets
- New Power Fx code examples
- Improvements to existing snippets
- Bug fixes in code samples

### Documentation
- README improvements
- Tutorial creation
- Guide enhancements
- Translation additions

### Repository Maintenance
- Issue triage
- Code review
- Testing improvements
- Tool development

### Community Support
- Answering questions
- Mentoring new contributors
- Community event organization

## 🔄 Contribution Process

### For New Snippets
1. **Check Existing Content**: Search for similar snippets to avoid duplication
2. **Choose Category**: Select the most appropriate category from our [structure](./new-structure-kilo-code.md)
3. **Create Snippet**: Use the canonical template at `utilities/templates/snippet-template.md`
4. **Add Metadata**: Include complete YAML front matter as defined in the template
5. **Test Thoroughly**: Ensure the code works as expected
6. **Submit PR**: Create a pull request with clear description

### For Bug Fixes
1. **Identify Issue**: Find or create an issue describing the problem
2. **Reproduce Bug**: Confirm you can reproduce the issue
3. **Fix Code**: Implement the fix
4. **Test Fix**: Verify the fix works and doesn't break other functionality
5. **Update Documentation**: Update any affected documentation
6. **Submit PR**: Reference the issue in your pull request

### For Documentation
1. **Identify Need**: Find areas needing improvement
2. **Plan Changes**: Outline what needs to be updated
3. **Make Changes**: Update documentation following our standards
4. **Review**: Check for clarity, accuracy, and completeness
5. **Submit PR**: Include rationale for changes

## 📝 Snippet Guidelines

### File Structure
```
your-snippet-name.md
├── YAML Front Matter (metadata)
├── Title and Description
├── Code Example(s)
├── Implementation Details
├── Usage Examples
├── Best Practices
├── Related Snippets
└── Support Information
```

### Required Metadata (YAML Front Matter)
```yaml
---
title: "Descriptive Title"
description: "Brief explanation of what the snippet does"
category: "XX-category-name/subcategory"
tags: ["tag1", "tag2", "tag3"]
difficulty: "beginner|intermediate|advanced|expert"
prerequisites: ["Prerequisite 1", "Prerequisite 2"]
author: "YourGitHubUsername"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
featured: true|false
related: ["path/to/related/snippet1", "path/to/related/snippet2"]
---
```

### Content Standards

#### Code Quality
- ✅ **Clear and Readable**: Use meaningful variable names
- ✅ **Well-Commented**: Include inline comments for complex logic
- ✅ **Error Handling**: Include appropriate error handling
- ✅ **Performance**: Consider performance implications
- ✅ **Best Practices**: Follow Power Fx best practices

#### Documentation Quality
- ✅ **Complete Examples**: Provide working code samples
- ✅ **Multiple Scenarios**: Show different use cases
- ✅ **YAML Configuration**: Include control configurations where applicable
- ✅ **Screenshots**: Add screenshots for complex UIs (optional but recommended)
- ✅ **Troubleshooting**: Include common issues and solutions

### Category Selection
Choose the most specific appropriate category:

- **01-getting-started**: Basic concepts and first steps
- **02-app-architecture**: App structure and lifecycle
- **03-user-interface**: Controls, themes, and UX
- **04-data-management**: Data operations and sources
- **05-business-logic**: Functions and calculations
- **06-integrations**: External services and APIs
- **07-assets-and-media**: Visual assets and media
- **08-advanced-patterns**: Complex scenarios and expert techniques
- **09-learning-resources**: Tutorials and educational content

## 📚 Documentation Standards

### README Files
- Use clear, descriptive language
- Include table of contents for longer documents
- Provide examples and code snippets
- Link to related content
- Keep up-to-date with changes

### Markdown Formatting
- Use consistent heading hierarchy (H1 → H2 → H3)
- Format code blocks with appropriate language hints
- Use tables for structured data
- Include alt text for images
- Use relative links for internal references

### Naming Conventions
- **Files**: `kebab-case-with-descriptive-names.md`
- **Directories**: `kebab-case-category-names/`
- **Images**: `descriptive-name.png` or `descriptive-name.jpg`

## 🧪 Testing

### Manual Testing
1. **Create Test App**: Test snippets in a new Power Apps canvas app
2. **Verify Functionality**: Ensure code works as documented
3. **Test Edge Cases**: Check error conditions and edge cases
4. **Cross-Platform**: Test on different devices/browsers if applicable
5. **Performance**: Verify performance is acceptable

### Automated Validation
Our GitHub Actions will automatically check:
- ✅ Markdown formatting
- ✅ YAML front matter validity
- ✅ Required metadata fields
- ✅ Internal link integrity
- ✅ Code syntax (where possible)

### Before Submitting
- [ ] Tested in Power Apps environment
- [ ] All metadata fields completed
- [ ] Links are valid and working
- [ ] Code follows style guidelines
- [ ] Documentation is clear and complete
- [ ] No sensitive information included

## 🎨 Style Guidelines

### Power Fx Code Style
```powerfx
// Good: Clear variable names and comments
Set(
    userFullName,
    User().FullName
);

// Calculate total with tax
Set(
    orderTotal,
    Sum(cartItems, Quantity * Price) * 1.08
);
```

```powerfx
// Avoid: Unclear names and no comments
Set(x, User().FullName);
Set(y, Sum(z, a * b) * 1.08);
```

### YAML Style
```yaml
# Good: Consistent formatting
---
title: "User Profile Display"
description: "Display user information with photo and details"
category: "03-user-interface/controls"
tags: ["gallery", "user-profile", "display"]
difficulty: "intermediate"
---
```

### Markdown Style
```markdown
# Good: Clear structure and formatting

## Overview
Brief description of the snippet.

## Implementation
```powerfx
// Code example here
Set(variableName, "value");
```

## Usage
Step-by-step usage instructions.
```

## 📝 Commit Messages

Use clear, descriptive commit messages:

### Format
```
type(scope): description

[optional body]

[optional footer]
```

### Types
- **feat**: New feature or snippet
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Testing related changes
- **chore**: Maintenance tasks

### Examples
```
feat(profile-gallery): add user profile gallery with search

Add a comprehensive gallery control for displaying user profiles
with search and filter capabilities.

Closes #123
```

```
fix(people-picker): correct Office365Users.SearchUser syntax

Fix incorrect parameter usage in Office365Users connector call.
Updated to use proper searchTerm parameter.
```

## 🔄 Pull Request Process

### PR Checklist
- [ ] **Title**: Clear, descriptive title following format `type: description`
- [ ] **Description**: Detailed explanation of changes
- [ ] **Issue Reference**: Link to related issue (if applicable)
- [ ] **Testing**: Describe how changes were tested
- [ ] **Screenshots**: Include before/after screenshots for UI changes
- [ ] **Breaking Changes**: Note any breaking changes
- [ ] **Documentation**: Update documentation if needed

### Review Process
1. **Automated Checks**: GitHub Actions will run validation
2. **Peer Review**: At least one maintainer will review
3. **Feedback**: Address any review comments
4. **Approval**: Maintainers will approve when ready
5. **Merge**: PR will be merged using squash or merge commit

### PR Template
When creating a PR, use this template:

```markdown
## Description
Brief description of the changes.

## Type of Change
- [ ] New snippet
- [ ] Bug fix
- [ ] Documentation update
- [ ] Other (please specify)

## Testing
Describe how you tested the changes.

## Screenshots (if applicable)
Add screenshots to show the changes.

## Related Issues
Fixes #issue_number
```

## 🏆 Recognition

### Contributor Recognition
- All contributors are listed in our [contributors file](./contributors.md)
- Significant contributions may be highlighted in release notes
- Top contributors may be invited to become maintainers

### Badges and Recognition
- **First PR**: Welcome badge for first contribution
- **Regular Contributor**: For consistent contributions
- **Expert Contributor**: For complex or high-impact contributions
- **Mentor**: For helping other contributors

## 📞 Getting Help

### Questions
- **GitHub Discussions**: Ask questions in our [discussions](https://github.com/PowerAppsDarren/PowerFxSnippets/discussions)
- **Issues**: Create an issue with the "question" label
- **Community**: Join our [Power Platform Community](https://powerplatform.microsoft.com/community/)

### Support
- **Documentation**: Check our [detailed guides](./docs)
- **Examples**: Look at existing snippets for reference
- **Maintainers**: Tag maintainers in issues/PRs for help

## 📋 Additional Resources

- [Power Fx Documentation](https://learn.microsoft.com/en-us/power-platform/power-fx/)
- [Power Apps Best Practices](https://learn.microsoft.com/en-us/power-apps/guidance/)
- [Power Platform Community](https://powerplatform.microsoft.com/community/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

Thank you for contributing to Power Fx Snippets! Your efforts help build a better resource for the entire Power Platform community. 🚀
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
