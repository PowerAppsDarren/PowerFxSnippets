# Tools & Utilities 🔧

## Table of Contents

- [📋 Available Tools](#available-tools)
  - [Validation Scripts](#validation-scripts)
  - [Migration Tools](#migration-tools)
  - [Development Tools](#development-tools)
  - [Maintenance Scripts](#maintenance-scripts)
- [🚀 Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Basic Usage](#basic-usage)
- [📖 Tool Documentation](#tool-documentation)
  - [validate-snippets.js](#validate-snippetsjs)
  - [migrate-content.js](#migrate-contentjs)
  - [create-snippet.js](#create-snippetjs)
- [🔧 Development](#development)
  - [Adding New Tools](#adding-new-tools)
  - [Code Standards](#code-standards)
  - [Example Tool Structure](#example-tool-structure)
- [📊 Monitoring & Analytics](#monitoring-analytics)
  - [Repository Statistics](#repository-statistics)
  - [Link Health Monitoring](#link-health-monitoring)
- [🔄 Automation](#automation)
  - [GitHub Actions Integration](#github-actions-integration)
  - [Pre-commit Hooks](#pre-commit-hooks)
- [🐛 Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Getting Help](#getting-help)
- [🤝 Contributing](#contributing)
  - [Improving Tools](#improving-tools)
  - [Adding New Tools](#adding-new-tools)
- [📈 Performance](#performance)
  - [Optimization Tips](#optimization-tips)
  - [Benchmarking](#benchmarking)
- [🔒 Security](#security)
  - [Best Practices](#best-practices)
  - [Security Scanning](#security-scanning)
- [📞 Support](#support)

This directory contains scripts, tools, and utilities to help maintain and work with the Power Fx Snippets repository.

## 📋 Available Tools

### Validation Scripts
- [`validate-snippets.js`](./validate-snippets.js) - Validate snippet metadata and formatting
- [`check-links.js`](./check-links.js) - Check internal and external links
- [`lint-markdown.js`](./lint-markdown.js) - Markdown formatting validation

### Migration Tools
- [`migrate-content.js`](./migrate-content.js) - Migrate existing content to new structure
- [`bulk-rename.js`](./bulk-rename.js) - Bulk rename files and update references
- [`category-mover.js`](./category-mover.js) - Move snippets between categories

### Development Tools
- [`create-snippet.js`](./create-snippet.js) - Interactive snippet creation wizard
- [`generate-index.js`](./generate-index.js) - Generate category index files
- [`search-indexer.js`](./search-indexer.js) - Create searchable content indexes

### Maintenance Scripts
- [`cleanup-orphans.js`](./cleanup-orphans.js) - Find and clean up orphaned files
- [`update-metadata.js`](./update-metadata.js) - Bulk update metadata fields
- [`stats-generator.js`](./stats-generator.js) - Generate repository statistics

## 🚀 Quick Start

### Prerequisites
```bash
# Install Node.js (version 16 or higher)
npm install -g nvm
nvm install 18
nvm use 18

# Install dependencies
cd tools
npm install
```

### Basic Usage
```bash
# Validate all snippets
node validate-snippets.js

# Check for broken links
node check-links.js

# Generate category indexes
node generate-index.js
```

## 📖 Tool Documentation

### validate-snippets.js

Validates snippet metadata and formatting across the repository.

**Usage:**
```bash
node validate-snippets.js [options]

Options:
  --category <name>    Validate only specific category
  --fix                Auto-fix common issues
  --verbose           Detailed output
  --help              Show help
```

**Checks Performed:**
- ✅ YAML front matter validity
- ✅ Required metadata fields
- ✅ File naming conventions
- ✅ Markdown formatting
- ✅ Code block syntax

**Auto-fix Capabilities:**
When running with `--fix`, the validator can automatically repair:
- Missing trailing newlines after front matter
- Missing `created` and `updated` date fields (populates with current date)

### migrate-content.js

Migrates existing content from old structure to new organization.

**Usage:**
```bash
node migrate-content.js --source <old-path> --target <new-category> --dry-run
```

**Features:**
- Preserves all metadata
- Updates internal links
- Creates backup of original files
- Dry-run mode for safe testing

### create-snippet.js

Interactive wizard for creating new snippets with proper structure.

**Usage:**
```bash
node create-snippet.js
```

**Wizard Flow:**
1. Category selection
2. Metadata collection
3. Code template generation
4. Documentation scaffolding
5. File creation

## 🔧 Development

### Adding New Tools

1. **Create Script**: Add your tool to the `tools/` directory
2. **Add Documentation**: Update this README with usage instructions
3. **Test Thoroughly**: Ensure tool works across different environments
4. **Update Package.json**: Add any new dependencies

### Code Standards

- Use ES6+ syntax
- Include JSDoc comments
- Handle errors gracefully
- Provide clear console output
- Support `--help` and `--version` flags

### Example Tool Structure

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Tool description
 * @param {Object} options - Tool options
 */
function main(options) {
  // Tool implementation
}

// CLI interface
if (require.main === module) {
  const args = process.argv.slice(2);
  // Parse arguments and call main
  main(parseArgs(args));
}

module.exports = { main };
```

## 📊 Monitoring & Analytics

### Repository Statistics
```bash
node stats-generator.js --output stats.json
```

Generates comprehensive statistics about:
- Snippet counts by category
- Metadata completeness
- Link health
- Contribution patterns
- Code quality metrics

### Link Health Monitoring
```bash
node check-links.js --watch --report health-report.md
```

Continuously monitors link health and generates reports.

## 🔄 Automation

### GitHub Actions Integration

Tools are designed to work with GitHub Actions for automated validation:

```yaml
- name: Validate Snippets
  run: |
    cd tools
    npm install
    node validate-snippets.js --ci
```

### Pre-commit Hooks

Use tools in pre-commit hooks for quality assurance:

```bash
#!/bin/sh
cd tools
node validate-snippets.js --pre-commit
```

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
# Clean install dependencies
rm -rf node_modules package-lock.json
npm install
```

**Permission errors:**
```bash
# Make scripts executable
chmod +x tools/*.js
```

**Path resolution issues:**
```bash
# Run from repository root
cd /path/to/PowerFxSnippets
node tools/validate-snippets.js
```

### Getting Help

- **Check Logs**: Most tools provide detailed error logs
- **Verbose Mode**: Use `--verbose` flag for detailed output
- **Dry Run**: Test changes with `--dry-run` before applying
- **GitHub Issues**: Report bugs in the main repository

## 🤝 Contributing

### Improving Tools
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

### Adding New Tools
1. Follow the established patterns
2. Include comprehensive documentation
3. Add error handling and logging
4. Test across different environments
5. Update this README

## 📈 Performance

### Optimization Tips
- Use streaming for large file operations
- Cache expensive computations
- Parallelize independent operations
- Provide progress indicators for long-running tasks

### Benchmarking
```bash
# Benchmark tool performance
time node validate-snippets.js --benchmark
```

## 🔒 Security

### Best Practices
- Validate all file paths
- Sanitize user inputs
- Use safe file operations
- Avoid executing external commands
- Regular dependency updates

### Security Scanning
```bash
# Run security audit
npm audit

# Update dependencies
npm update
```

---

## 📞 Support

- **Issues**: [Report tool problems](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
- **Discussions**: [Ask questions](https://github.com/PowerAppsDarren/PowerFxSnippets/discussions)
- **Documentation**: [Tool guides](../docs)

---

**Last Updated**: November 2024
**Version**: 1.0.0
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
