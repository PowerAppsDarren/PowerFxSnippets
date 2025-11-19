<!--
Sync Impact Report - Constitution v1.0.0
Version: Initial → 1.0.0 (MINOR bump - Initial constitution establishment)
Modified Principles: All principles newly defined
Added Sections: Core Principles, Quality Standards, Repository Governance, Governance
Removed Sections: None (initial creation)
Templates Status:
  ✅ spec-template.md - Aligned with snippet metadata requirements
  ✅ plan-template.md - Aligned with feature-first organization
  ✅ tasks-template.md - Aligned with validation and automation principles
Follow-up TODOs: None
-->

# PowerFxSnippets Constitution

## Core Principles

### I. Feature-First Organization (NON-NEGOTIABLE)

Repository structure MUST be organized by what developers want to accomplish, not by technical categories.

**Rules:**
- Top-level categories represent use cases and developer intent (app-lifecycle, ui-controls, data-operations)
- Maximum 3-level hierarchy depth to prevent navigation complexity
- Kebab-case naming throughout (no spaces, consistent GitHub URLs)
- Every directory MUST contain a README.md with snippet listings and navigation
- Emoji visual cues required for top-level categories to enhance GitHub browsing

**Rationale:** Developers search by "what they want to do" not "technical classification". Feature-first organization reduces time-to-snippet from minutes to seconds.

### II. Metadata-Driven Discoverability

Every snippet MUST include complete YAML frontmatter with standardized metadata.

**Required Metadata Fields:**
- `title`: Clear, descriptive title
- `description`: Brief explanation of functionality
- `category`: Primary category (matches directory structure)
- `tags`: Searchable keywords (3-8 tags)
- `difficulty`: beginner | intermediate | advanced
- `author`: GitHub username or attribution
- `created`: ISO date (YYYY-MM-DD)
- `updated`: ISO date (YYYY-MM-DD)
- `license`: MIT (default for this repository)

**Optional but Recommended:**
- `products`: Target products (power-apps-canvas, power-apps-model-driven, power-automate)
- `dependencies`: Required connectors or prerequisites
- `related`: Links to related snippets

**Rationale:** Rich metadata enables filtering, search, automated indexing, and cross-category discovery. Consistency ensures maintainability at scale.

### III. Quality Over Quantity

All snippets MUST meet quality standards before acceptance.

**Code Quality Requirements:**
- Clear, meaningful variable names (no single-letter variables except loop counters)
- Inline comments for complex logic
- Error handling where appropriate
- Performance-conscious implementations
- Power Fx best practices followed

**Documentation Quality Requirements:**
- Working code examples that can be copy-pasted
- Implementation details explaining key concepts
- Usage examples showing practical application
- Related snippets for comprehensive solutions
- Troubleshooting section for common issues (when applicable)

**Rationale:** High-quality snippets build trust and reputation. Better to have 100 excellent snippets than 1000 mediocre ones.

### IV. Community-First Contribution

Contribution process MUST be welcoming, clear, and frictionless.

**Requirements:**
- Templates provided for all snippet types
- Clear contribution guidelines in CONTRIBUTING.md
- Automated validation reduces manual review burden
- Feedback provided within 48 hours on pull requests
- Recognition system for contributors

**Rationale:** Community growth depends on making contribution easy and rewarding. Reduce barriers while maintaining quality through automation and clear standards.

### V. Automation & Validation

Quality enforcement MUST be automated wherever possible.

**Automated Checks Required:**
- YAML frontmatter validation (all required fields present)
- Internal link integrity checking
- Markdown formatting consistency
- Category placement verification
- Index generation from metadata

**Manual Review Focus:**
- Code correctness and Power Fx best practices
- Documentation clarity and completeness
- Snippet usefulness and uniqueness
- Community guidelines compliance

**Rationale:** Automation ensures consistency at scale and frees maintainers to focus on value-add review activities. Fast feedback loops improve contributor experience.

### VI. Preservation & Migration

Repository evolution MUST preserve existing content and maintain backward compatibility where possible.

**Rules:**
- Never delete snippets during restructuring (archive instead)
- Maintain redirect documentation for moved content
- Migration guides MUST be comprehensive and tested
- Version control protects against accidental loss
- Backup before major structural changes

**Rationale:** Years of community contributions have value. Trust depends on stability and respect for contributor effort.

## Quality Standards

### Snippet Structure

Every snippet file MUST follow this structure:

1. **YAML Frontmatter** (metadata block)
2. **Title and Overview** (what it does, why it's useful)
3. **Code Example** (primary implementation)
4. **Implementation Details** (explanation of key concepts)
5. **Usage Examples** (practical applications)
6. **Related Snippets** (cross-references)
7. **Support Information** (author, license, attribution)

### Testing Standards

Contributors MUST test snippets in actual Power Apps environment before submission:

- Create test app demonstrating functionality
- Verify code works as documented
- Test edge cases and error conditions
- Confirm performance is acceptable
- Test on multiple screen sizes (for UI snippets)

### Documentation Standards

All documentation MUST be:

- **Clear**: Written for the target difficulty level (beginner-friendly language for beginner snippets)
- **Complete**: No missing steps or assumed knowledge beyond stated prerequisites
- **Accurate**: Code examples must be tested and working
- **Current**: Updated when Power Platform features change
- **Consistent**: Following repository markdown and naming conventions

## Repository Governance

### Versioning

- Repository follows **rolling release** model (no version numbers)
- Individual snippets track `created` and `updated` dates
- Major restructuring tracked via feature specs in `.specify/`
- Breaking changes announced via README and GitHub releases

### Review & Approval

**Snippet Additions/Changes:**
- Automated validation MUST pass before review
- At least one maintainer approval required
- Breaking changes require detailed migration guide
- Merge via squash or standard merge (no rebase)

**Documentation Changes:**
- Single maintainer approval sufficient
- Automated checks for broken links
- Clarity and accuracy prioritized

**Repository Structure Changes:**
- Require feature specification in `.specify/`
- Community announcement and feedback period
- Phased rollout when possible
- Comprehensive testing of automation impacts

### Feature Development Process

For major changes (restructuring, new automation, template changes):

1. Create feature specification using `/speckit.specify`
2. Develop implementation plan using `/speckit.plan`
3. Generate tasks using `/speckit.tasks`
4. Execute with validation at each milestone
5. Update constitution if new principles required

### Amendment Process

Constitution changes require:

- **MAJOR version bump**: Backward-incompatible changes, principle removal/redefinition
- **MINOR version bump**: New principles added, material expansions
- **PATCH version bump**: Clarifications, wording improvements, typo fixes

All amendments MUST:
- Update Sync Impact Report (HTML comment at top of file)
- Validate consistency with template files
- Update dependent documentation
- Include rationale for changes

## Governance

**Constitution Authority:** This constitution supersedes conflicting practices and serves as the authoritative governance document for PowerFxSnippets repository development and maintenance.

**Compliance:** All feature specifications, implementation plans, pull requests, and code reviews MUST verify compliance with these principles. Deviations require explicit justification and maintainer approval.

**Spec-Kit Integration:** Use `.specify/templates/` for all feature planning. Templates align with constitution principles and ensure consistent feature development.

**Runtime Guidance:** Contributors and maintainers should consult CONTRIBUTING.md and README.md for day-to-day development guidance implementing these constitutional principles.

**Continuous Improvement:** Constitution evolves with repository needs. Propose amendments via feature specification process, ensuring community input and documentation of rationale.

**Version**: 1.0.0 | **Ratified**: 2025-11-19 | **Last Amended**: 2025-11-19
