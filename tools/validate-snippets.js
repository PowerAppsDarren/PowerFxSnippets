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
    
    // Allowed top-level categories (feature-first + legacy)
    this.allowedCategories = [
      'app-lifecycle',
      'ui-controls',
      'data-operations',
      'business-logic',
      'integrations',
      'assets-and-media',
      'advanced-patterns',
      'learning-resources',
      '01-getting-started',
      '02-app-architecture',
      '03-user-interface',
      '04-data-management',
      '05-business-logic',
      '06-integrations',
      '07-assets-and-media',
      '08-advanced-patterns',
      '09-learning-resources',
      // Legacy directories
      'App.Formulas',
      'App.OnError',
      'App.OnMessage',
      'App.OnStart',
      'App.StartScreen',
      'Components',
      'Connectors',
      'Controls',
      'Data Sources',
      'Functions',
      'Icons',
      'Images',
      'JSON',
      'SVGs',
      'String Manipulation',
      'Text-Manipulation',
      'Themes-Color-Palettes',
      'Theming',
      'User Defined Functions',
      'User Defined Types'
    ];
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
      if (item.isDirectory() && !item.name.startsWith('.') && item.name !== 'node_modules' && item.name !== 'tools' && item.name !== '_archive') {
        // Check if it's a known category or contains markdown files
        if (this.allowedCategories.includes(item.name) || item.name.match(/^\d{2}-/)) {
           categories.push(path.join(rootPath, item.name));
        } else {
           // Also check if directory contains .md files directly (legacy structure)
           const subItems = await fs.promises.readdir(path.join(rootPath, item.name));
           if (subItems.some(f => f.endsWith('.md'))) {
             categories.push(path.join(rootPath, item.name));
           }
        }
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
        this.errors.push(...validation.errors.map(e => `${relativePath}: ${e}`));
        this.warnings.push(...validation.warnings.map(w => `${relativePath}: ${w}`));

        if (this.options.fix && validation.canFix) {
          await this.fixSnippet(filePath, validation.fixes);
          this.stats.fixed++;
          // Re-validate to confirm fix
          const newContent = await fs.promises.readFile(filePath, 'utf8');
          const revalidation = this.validateSnippetContent(newContent, filePath);
          if (revalidation.isValid) {
             this.stats.invalid--;
             this.stats.valid++;
             // Remove errors associated with this file from the list since it's fixed
             this.errors = this.errors.filter(e => !e.startsWith(relativePath));
          }
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
    // Allow for optional whitespace around delimiters and handle different newline styles
    const frontMatterMatch = content.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/);
    
    // Fix: Missing trailing newline after front matter
    if (!frontMatterMatch) {
        const looseMatch = content.match(/^---\s*\n([\s\S]*?)\n---([^\n][\s\S]*)$/);
        if (looseMatch) {
            result.canFix = true;
            result.fixes.push({ type: 'add_newline_after_frontmatter' });
        } else if (!content.startsWith('---')) {
             result.errors.push('Missing YAML front matter');
             result.isValid = false;
             return result;
        }
    }

    if (!frontMatterMatch && !result.canFix) {
        result.errors.push('Invalid YAML front matter format');
        result.isValid = false;
        return result;
    }

    const yamlContent = frontMatterMatch ? frontMatterMatch[1] : (content.match(/^---\n([\s\S]*?)\n---/) ? content.match(/^---\n([\s\S]*?)\n---/)[1] : '');
    const bodyContent = frontMatterMatch ? frontMatterMatch[2] : content.replace(/^---\n[\s\S]*?\n---/, '');

    // Validate YAML
    let metadata;
    try {
      metadata = yaml.load(yamlContent);
    } catch (error) {
      result.errors.push(`Invalid YAML: ${error.message}`);
      result.isValid = false;
      return result;
    }

    // Required fields validation (Constitution + Template)
    const requiredFields = [
        'title', 
        'description', 
        'category', 
        'tags', 
        'difficulty', 
        'author', 
        'created', 
        'updated', 
        'license'
    ];
    
    for (const field of requiredFields) {
      if (!metadata[field]) {
        // Backward compatibility: warn instead of error for some fields on legacy files
        if (['license', 'created', 'updated', 'author'].includes(field)) {
             result.warnings.push(`Missing recommended field: ${field}`);
             if (this.options.fix && ['created', 'updated'].includes(field)) {
                 result.canFix = true;
                 result.fixes.push({ type: 'add_missing_field', field: field });
             }
        } else {
            result.errors.push(`Missing required field: ${field}`);
            result.isValid = false;
        }
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
      // We don't strictly enforce path matching anymore due to legacy structure, 
      // but we can warn if it looks completely wrong
      const categoryPath = path.dirname(filePath);
      const expectedCategory = this.getCategoryFromPath(categoryPath);
      // Only warn if we could determine an expected category and it doesn't match
      if (expectedCategory && !metadata.category.includes(expectedCategory) && !expectedCategory.includes(metadata.category)) {
        result.warnings.push(`Category mismatch: path suggests '${expectedCategory}', metadata has '${metadata.category}'`);
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
    if (!bodyContent || !bodyContent.trim()) {
      result.errors.push('Snippet body is empty');
      result.isValid = false;
    }

    // Check for code blocks
    if (bodyContent && !bodyContent.includes('```')) {
      result.warnings.push('No code blocks found in snippet');
    }

    return result;
  }

  getCategoryFromPath(filePath) {
    const relativePath = path.relative(path.join(__dirname, '..'), filePath);
    const parts = relativePath.split(path.sep);
    // Use the first directory as the category
    if (parts.length > 1) {
        return parts[0];
    }
    return '';
  }

  isValidDate(dateString) {
    // Handle Date objects if yaml parser converted them
    if (dateString instanceof Date) return true;
    return /^\d{4}-\d{2}-\d{2}$/.test(dateString) && !isNaN(Date.parse(dateString));
  }

  async fixSnippet(filePath, fixes) {
    this.log(`Auto-fixing: ${path.relative(path.join(__dirname, '..'), filePath)}`, 'info');
    
    let content = await fs.promises.readFile(filePath, 'utf8');
    let modified = false;

    for (const fix of fixes) {
        if (fix.type === 'add_newline_after_frontmatter') {
            content = content.replace(/^(---\n[\s\S]*?\n---)([^\n])/, '$1\n$2');
            modified = true;
        } else if (fix.type === 'add_missing_field') {
            const today = new Date().toISOString().split('T')[0];
            if (fix.field === 'created' || fix.field === 'updated') {
                // Insert before the closing ---
                content = content.replace(/\n---/, `\n${fix.field}: ${today}\n---`);
                modified = true;
            }
        }
    }

    if (modified) {
        await fs.promises.writeFile(filePath, content, 'utf8');
        this.log(`Fixed ${fixes.length} issues in ${path.basename(filePath)}`, 'success');
    }
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