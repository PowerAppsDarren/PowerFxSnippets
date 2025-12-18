# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Power Fx snippets repository containing reusable code patterns, formulas, and components for Microsoft Power Platform development. The repository serves as a comprehensive collection of Power Apps development resources.

## Editing Markdown Files

When adding or updating any `.md` file in this repository:

1. **Update the History section** at the bottom of the file (create one if it doesn't exist)
2. Use this format:
   ```markdown
   ## History

   | Date       | Author      | Changes                          |
   |------------|-------------|----------------------------------|
   | YYYY-MM-DD | Author Name | Brief description of changes     |
   ```
3. Add new entries at the **top** of the table (most recent first)

## Repository Structure

```
PowerFxSnippets/
├── Algorithms/          # Algorithm implementations and patterns
├── App.Formulas/       # Named formulas and app-level formulas
├── App.OnError/        # Error handling patterns
├── App.OnMessage/      # Message handling patterns
├── App.OnStart/        # App initialization patterns
├── App.StartScreen/    # Start screen configurations
├── Components/         # Reusable Power Apps components
├── Connectors/         # Connector-specific patterns (Office365, etc.)
├── Controls/           # Control-specific implementations
├── Data Sources/       # Database schemas and SQL patterns
├── Data Samples/       # Sample data files (CSV, JSON)
├── SVGs/              # SVG graphics and icons
├── Fonts/             # Font resources and configurations
├── Icons/             # Icon collections
└── ai-chats/          # AI session documentation
```

## Key File Types

- **`.md` files**: Documentation and code snippets in markdown format
- **`.yaml` files**: Power Fx formula definitions and configurations
- **`.msapp` files**: Power Apps application packages
- **`.csv` files**: Sample data sets
- **`.svg` files**: Scalable vector graphics for UI elements
- **`.json` files**: Configuration and schema definitions

## Working with Power Fx Code

### Formula Patterns
- Power Fx formulas are typically stored in `.yaml` files or documented in `.md` files
- Named formulas use the prefix `fx` (e.g., `fxMenuItems.yaml`)
- User-defined types and schemas follow specific syntax patterns documented in the repository

### Common Tasks

1. **Adding New Snippets**: Create markdown files in the appropriate category folder with clear examples
2. **Documenting Components**: Include both the Power Fx code and usage instructions
3. **Sample Data**: Place CSV files in `Data Samples/` with descriptive names
4. **SVG Resources**: Store in `SVGs/SVG Files/` organized by provider (Azure, Fabric, Power BI)

## Documentation Standards

- Use clear, descriptive file names
- Include code examples with proper Power Fx syntax highlighting
- Document any dependencies or prerequisites
- Add images/screenshots where helpful for visual components

## AI Session Documentation

Document AI-assisted work sessions in `ai-chats/` using the format:
`YYYY-MM-DD-XX-description.md`

## Related Resources

- Power Fx GitHub: https://github.com/microsoft/Power-Fx
- PowerApps Tooling: https://github.com/microsoft/PowerApps-Tooling
- Community Materials: https://tinyurl.com/DarrensStuffPower
