---
title: "Basic Hello World"
description: "Your first Power Fx expression - display text and understand basic syntax"
category: "01-getting-started/hello-world"
tags: ["basics", "syntax", "text", "fundamentals", "first-steps"]
difficulty: "beginner"
prerequisites: []
author: "Power Fx Snippets Community"
created: "2024-11-17"
updated: "2024-11-17"
featured: true
related: ["interactive-hello-world", "data-hello-world"]
---

# Basic Hello World

## Table of Contents

- [🎯 What This Snippet Does](#what-this-snippet-does)
- [📋 Prerequisites](#prerequisites)
- [🛠️ Implementation](#implementation)
  - [Simple Text Display](#simple-text-display)
  - [Adding to a Label Control](#adding-to-a-label-control)
  - [YAML Configuration](#yaml-configuration)
- [📖 Usage Examples](#usage-examples)
  - [Different Text Messages](#different-text-messages)
  - [Combining Text](#combining-text)
  - [Dynamic Text with Variables](#dynamic-text-with-variables)
- [🔧 Understanding the Code](#understanding-the-code)
  - [Power Fx Basics](#power-fx-basics)
  - [Key Concepts](#key-concepts)
- [🐛 Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
- [🚀 Next Steps](#next-steps)
  - [Build on This Knowledge](#build-on-this-knowledge)
  - [Related Snippets](#related-snippets)
- [🔗 External Resources](#external-resources)
  - [Official Documentation](#official-documentation)
  - [Community Resources](#community-resources)
- [🤝 Contributing](#contributing)
  - [Improving This Snippet](#improving-this-snippet)
  - [Found an Issue?](#found-an-issue)
- [📊 Version History](#version-history)

> Display your first text in Power Apps and understand the fundamental Power Fx expression syntax.

## 🎯 What This Snippet Does

This is your starting point with Power Fx! It demonstrates the most basic expression - displaying static text. While simple, it teaches you:

- How to write Power Fx expressions
- The difference between static text and dynamic expressions
- Basic syntax rules
- How expressions are evaluated in Power Apps

## 📋 Prerequisites

No prerequisites required! This is designed for absolute beginners.

## 🛠️ Implementation

### Simple Text Display

The most basic Power Fx expression is just text in quotes:

```powerfx
/* ===========================================================================================

    Basic Hello World
    Display static text in Power Apps

    This is your first Power Fx expression!

    ===========================================================================*/

"Hello, World!"
```

### Adding to a Label Control

1. **Add a Label control** to your screen
2. **Set the Text property** to:
   ```powerfx
   "Hello, World!"
   ```
3. **Run your app** - you should see "Hello, World!" displayed

### YAML Configuration

```yaml
# Label control configuration
- lblHelloWorld:
    Control: Classic/Label
    Properties:
      Text: ="Hello, World!"
      X: =100
      Y: =100
      Width: =200
      Height: =50
      Color: =RGBA(0, 0, 0, 1)
      FontSize: =16
```

## 📖 Usage Examples

### Different Text Messages

```powerfx
// Welcome message
"Welcome to Power Apps!"

// Personal greeting
"Hello, Developer!"

// Instructional text
"Click the button to continue"
```

### Combining Text

```powerfx
// Simple concatenation
"Hello, " & "World!"

// With line breaks
"Hello," & Char(10) & "World!"

// With emoji
"🚀 Hello, Power Apps! 🌟"
```

### Dynamic Text with Variables

```powerfx
// Using a variable (covered in next snippet)
Set(userName, "Developer");
"Hello, " & userName & "!"
```

## 🔧 Understanding the Code

### Power Fx Basics

1. **Expressions**: Everything in Power Fx is an expression that returns a value
2. **Quotes**: Text literals are enclosed in double quotes
3. **Evaluation**: Expressions are calculated whenever their inputs change
4. **Types**: This expression returns a Text value

### Key Concepts

- **Static vs Dynamic**: This is static text (always the same)
- **Data Types**: Returns a Text/String type
- **Context**: Works anywhere in Power Apps
- **Performance**: Very lightweight, no performance impact

## 🐛 Troubleshooting

### Common Issues

#### Issue: Text doesn't appear
**Symptoms**: Label shows nothing or "false"
**Cause**: Missing quotes or incorrect syntax
**Solution**:
```powerfx
// Correct
"Hello, World!"

// Incorrect - missing quotes
Hello, World!

// Incorrect - wrong quotes
'Hello, World!'
```

#### Issue: Special characters don't work
**Symptoms**: Quotes or special chars break the expression
**Cause**: Power Fx uses specific escaping rules
**Solution**:
```powerfx
// Use double quotes for text
"This is ""quoted"" text"

// Use Char() for special characters
"Hello" & Char(13) & "World"
```

## 🚀 Next Steps

### Build on This Knowledge

1. **Variables**: Learn to store and reuse values
   ```powerfx
   Set(myMessage, "Hello, World!");
   myMessage
   ```

2. **Functions**: Use built-in Power Fx functions
   ```powerfx
   Upper("hello, world!")
   ```

3. **Dynamic Content**: Combine text with data
   ```powerfx
   "Hello, " & User().FullName & "!"
   ```

### Related Snippets

- [**Interactive Hello World**](./interactive-hello-world.md) - Add user interaction
- [**Data Hello World**](./data-hello-world.md) - Display data from collections
- [**Variable Declaration**](learning/tutorials/getting-started/common-patterns/variable-declaration.md) - Learn about variables

## 🔗 External Resources

### Official Documentation
- [Power Fx Overview](https://learn.microsoft.com/en-us/power-platform/power-fx/overview)
- [Text Functions](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-text)
- [Expression Basics](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference)

### Community Resources
- [Power Apps Getting Started](https://learn.microsoft.com/en-us/power-apps/getting-started)
- [Power Fx Formula Reference](https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference)

## 🤝 Contributing

### Improving This Snippet
- Add more examples for different scenarios
- Include screenshots of the result
- Add translations for different languages
- Create video tutorials

### Found an Issue?
[Report it here](learning/tutorials/issues/new?template=bug-report.md&title=[BUG]%20Basic%20Hello%20World)

---

## 📊 Version History

| Version | Date       | Changes                              |
|---------|------------|--------------------------------------|
| 1.0.0   | 2024-11-17 | Initial release with basic examples  |

---

**🎉 Congratulations!** You've written your first Power Fx expression! 🌟

**Ready for more?** Try the [Interactive Hello World](./interactive-hello-world.md) next!
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
