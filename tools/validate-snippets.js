#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

/**
 * Power Fx Snippets Validator
 * Validates metadata and formatting of code snippets
 */

class SnippetValidator {
  constructor(options = {}) {
    this.options = {
      verbose: false,
      fix: false,
      category: null,
      ci: false,
      ...options
    };
    this.errors = [];
    this.warnings = [];
    this.stats = {
      total: 0,
      valid: 0,
      invalid: 0,
      fixed: 0
    };
  }

  log(message, level = 'info') {
    if (this.options.ci && level === 'info') return;
    if (level === 'error') console.error(`❌ ${message}`);
    else if (level === 'warning') console.warn(`⚠️  ${message}`);
    else if (level === 'success') console.log(`✅ ${message}`);
    else if (this.options.verbose) console.log(`ℹ️  ${message}`);
  }

  async validateRepository(rootPath = path.join(__dirname, '..')) {
    this.log('Starting snippet validation...', 'info');

    const categories = await this.findCategories(rootPath);
    const filteredCategories = this.options.category
      ? categories.filter(cat => cat.includes(this.options.category))
      : categories;

    for (const categoryPath of filteredCategories) {
      await this.validateCategory(categoryPath);
    }

    this.printSummary();
    return this.errors.length === 0;
  }

  async findCategories(rootPath) {
    const categories = [];
    const items = await fs.promises.readdir(rootPath, { withFileTypes: true });

    for (const item of items) {
      if (item.isDirectory() && item.name.match(/^\d{2}-/)) {
        categories.push(path.join(rootPath, item.name));
      }
    }

    return categories;
  }

  async validateCategory(categoryPath) {
    const categoryName = path.basename(categoryPath);
    this.log(`Validating category: ${categoryName}`, 'info');

    const files = await this.findMarkdownFiles(categoryPath);

    for (const file of files) {
      await this.validateSnippet(file);
    }
  }

  async findMarkdownFiles(dirPath) {
    const files = [];

    async function scan(dir) {
      const items = await fs.promises.readdir(dir, { withFileTypes: true });

      for (const item of items) {
        const fullPath = path.join(dir, item.name);

        if (item.isDirectory() && !item.name.startsWith('.') && item.name !== '_archive') {
          await scan(fullPath);
        } else if (item.isFile() && item.name.endsWith('.md') && item.name !== 'README.md') {
          files.push(fullPath);
        }
      }
    }

    await scan(dirPath);
    return files;
  }

  async validateSnippet(filePath) {
    this.stats.total++;
    const relativePath = path.relative(path.join(__dirname, '..'), filePath);
    this.log(`Validating: ${relativePath}`, 'info');

    try {
      const content = await fs.promises.readFile(filePath, 'utf8');
      const validation = this.validateSnippetContent(content, filePath);

      if (validation.isValid) {
        this.stats.valid++;
        this.log(`Valid: ${relativePath}`, 'success');
      } else {
        this.stats.invalid++;
        this.errors.push(...validation.errors);
        this.warnings.push(...validation.warnings);

        if (this.options.fix && validation.canFix) {
          await this.fixSnippet(filePath, validation.fixes);
          this.stats.fixed++;
        }
      }
    } catch (error) {
      this.errors.push(`Failed to read ${relativePath}: ${error.message}`);
      this.stats.invalid++;
    }
  }

  validateSnippetContent(content, filePath) {
    const result = {
      isValid: true,
      errors: [],
      warnings: [],
      canFix: false,
      fixes: []
    };

    // Check for YAML front matter
    const frontMatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
    if (!frontMatterMatch) {
      result.errors.push('Missing YAML front matter');
      result.isValid = false;
      return result;
    }

    const yamlContent = frontMatterMatch[1];
    const bodyContent = frontMatterMatch[2];

    // Validate YAML
    let metadata;
    try {
      metadata = yaml.load(yamlContent);
    } catch (error) {
      result.errors.push(`Invalid YAML: ${error.message}`);
      result.isValid = false;
      return result;
    }

    // Required fields validation
    const requiredFields = ['title', 'description', 'category', 'difficulty'];
    for (const field of requiredFields) {
      if (!metadata[field]) {
        result.errors.push(`Missing required field: ${field}`);
        result.isValid = false;
      }
    }

    // Difficulty validation
    if (metadata.difficulty) {
      const validDifficulties = ['beginner', 'intermediate', 'advanced', 'expert'];
      if (!validDifficulties.includes(metadata.difficulty)) {
        result.errors.push(`Invalid difficulty: ${metadata.difficulty}. Must be one of: ${validDifficulties.join(', ')}`);
        result.isValid = false;
      }
    }

    // Category validation
    if (metadata.category) {
      const categoryPath = path.dirname(filePath);
      const expectedCategory = this.getCategoryFromPath(categoryPath);
      if (metadata.category !== expectedCategory) {
        result.warnings.push(`Category mismatch: expected '${expectedCategory}', got '${metadata.category}'`);
      }
    }

    // Tags validation
    if (metadata.tags && !Array.isArray(metadata.tags)) {
      result.errors.push('Tags must be an array');
      result.isValid = false;
    }

    // Date validation
    if (metadata.created) {
      if (!this.isValidDate(metadata.created)) {
        result.warnings.push('Invalid created date format (use YYYY-MM-DD)');
      }
    }

    if (metadata.updated) {
      if (!this.isValidDate(metadata.updated)) {
        result.warnings.push('Invalid updated date format (use YYYY-MM-DD)');
      }
    }

    // Content validation
    if (!bodyContent.trim()) {
      result.errors.push('Snippet body is empty');
      result.isValid = false;
    }

    // Check for code blocks
    if (!bodyContent.includes('```')) {
      result.warnings.push('No code blocks found in snippet');
    }

    return result;
  }

  getCategoryFromPath(filePath) {
    const relativePath = path.relative(path.join(__dirname, '..'), filePath);
    const parts = relativePath.split(path.sep);
    const categoryIndex = parts.findIndex(part => part.match(/^\d{2}-/));
    if (categoryIndex >= 0) {
      return parts.slice(categoryIndex, categoryIndex + 2).join('/');
    }
    return '';
  }

  isValidDate(dateString) {
    return /^\d{4}-\d{2}-\d{2}$/.test(dateString) && !isNaN(Date.parse(dateString));
  }

  async fixSnippet(filePath, fixes) {
    // Implementation for auto-fixing common issues
    this.log(`Auto-fixing: ${path.relative(path.join(__dirname, '..'), filePath)}`, 'info');
    // TODO: Implement specific fixes
  }

  printSummary() {
    console.log('\n' + '='.repeat(50));
    console.log('VALIDATION SUMMARY');
    console.log('='.repeat(50));

    console.log(`Total snippets: ${this.stats.total}`);
    console.log(`Valid: ${this.stats.valid}`);
    console.log(`Invalid: ${this.stats.invalid}`);
    if (this.stats.fixed > 0) {
      console.log(`Auto-fixed: ${this.stats.fixed}`);
    }

    if (this.errors.length > 0) {
      console.log(`\n❌ Errors (${this.errors.length}):`);
      this.errors.forEach(error => console.log(`  • ${error}`));
    }

    if (this.warnings.length > 0) {
      console.log(`\n⚠️  Warnings (${this.warnings.length}):`);
      this.warnings.forEach(warning => console.log(`  • ${warning}`));
    }

    console.log('\n' + '='.repeat(50));

    if (this.errors.length === 0) {
      console.log('✅ All validations passed!');
    } else {
      console.log('❌ Validation failed. Please fix the errors above.');
      process.exit(1);
    }
  }
}

// CLI interface
function parseArgs(args) {
  const options = {};

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--verbose':
      case '-v':
        options.verbose = true;
        break;
      case '--fix':
        options.fix = true;
        break;
      case '--category':
      case '-c':
        options.category = args[++i];
        break;
      case '--ci':
        options.ci = true;
        break;
      case '--help':
      case '-h':
        console.log(`
Power Fx Snippets Validator

Usage: node validate-snippets.js [options]

Options:
  --verbose, -v       Show detailed output
  --fix               Auto-fix common issues
  --category, -c <name> Validate only specific category
  --ci                CI mode (less verbose)
  --help, -h          Show this help

Examples:
  node validate-snippets.js
  node validate-snippets.js --category "03-user-interface"
  node validate-snippets.js --fix --verbose
`);
        process.exit(0);
    }
  }

  return options;
}

// Main execution
if (require.main === module) {
  const options = parseArgs(process.argv.slice(2));
  const validator = new SnippetValidator(options);

  validator.validateRepository()
    .then(success => {
      if (!success && !options.ci) {
        process.exit(1);
      }
    })
    .catch(error => {
      console.error('Validation failed:', error);
      process.exit(1);
    });
}

module.exports = SnippetValidator;