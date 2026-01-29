# Feedback Templates for v2.0.0 Restructuring

This document provides templates for collecting community feedback on the v2.0.0 repository restructuring.

## Table of Contents

- [Feedback Survey Template](#feedback-survey-template)
- [GitHub Discussion Category Setup](#github-discussion-category-setup)
- [Issue-Based Feedback Template](#issue-based-feedback-template)

---

## Feedback Survey Template

Use the following questions when collecting structured feedback (e.g., in a GitHub Discussion post, a Microsoft Forms survey, or a community poll).

### Survey: PowerFxSnippets v2.0.0 Restructuring Feedback

**1. Overall Impression**

How would you rate the new repository structure compared to the previous one?

- [ ] Much better
- [ ] Somewhat better
- [ ] About the same
- [ ] Somewhat worse
- [ ] Much worse

**2. Navigation**

How easy is it to find the snippets you need in the new structure?

- [ ] Very easy
- [ ] Easy
- [ ] Neutral
- [ ] Difficult
- [ ] Very difficult

**3. Category Organization**

The repository now uses 9 feature-based categories (app-lifecycle, ui-controls, ui-patterns, visual-assets, data-operations, functions, integrations, learning, utilities). Do these categories make sense to you?

- [ ] Yes, they are intuitive
- [ ] Mostly, but some categories could be renamed or reorganized
- [ ] No, I find them confusing

If you selected "Mostly" or "No," please describe what you would change:

> (free text)

**4. YAML Frontmatter**

Every snippet now includes YAML frontmatter (title, description, category, tags, difficulty). How useful do you find this metadata?

- [ ] Very useful
- [ ] Somewhat useful
- [ ] Neutral
- [ ] Not useful

**5. Search & Discovery**

Which of the following do you use to find snippets? (Select all that apply)

- [ ] Browsing folders directly
- [ ] SEARCH-INDEX.md
- [ ] TAG-INDEX.md
- [ ] PRODUCT-INDEX.md
- [ ] GitHub search
- [ ] README table of contents
- [ ] Other: _________

**6. Missing Content**

Are there Power Fx topics or patterns you wish were covered but are not currently in the repository?

> (free text)

**7. Contribution Experience**

Have you tried contributing a snippet using the new Contributing Guide and templates?

- [ ] Yes, and it was straightforward
- [ ] Yes, but I encountered issues
- [ ] No, but I plan to
- [ ] No, and I do not plan to

If you encountered issues, please describe:

> (free text)

**8. Migration Experience**

If you had bookmarks to the old structure, were you able to find your files using the Migration Guide?

- [ ] Yes, easily
- [ ] Yes, but it took some effort
- [ ] No, I could not find what I was looking for
- [ ] Not applicable (new user)

**9. Open Feedback**

Any other comments, suggestions, or concerns about the restructuring?

> (free text)

---

## GitHub Discussion Category Setup

### Instructions for Creating a Feedback Discussion Category

1. Go to your repository on GitHub
2. Navigate to **Settings** > **General** > scroll to **Features**
3. Enable **Discussions** if not already enabled
4. Go to the **Discussions** tab
5. Click the gear icon next to **Categories**
6. Click **New category** and fill in:

| Field       | Value                                         |
|-------------|-----------------------------------------------|
| Name        | v2.0.0 Feedback                               |
| Description | Share your feedback on the v2.0.0 repository restructuring |
| Format      | Open-ended discussion                         |
| Emoji       | 💬                                            |

7. Click **Create**

### Pinned Discussion Post Template

Create a new Discussion in the "v2.0.0 Feedback" category with the following content:

---

**Title:** Share Your Feedback on the v2.0.0 Restructuring

**Body:**

```markdown
We have completed a major restructuring of the PowerFxSnippets repository (v2.0.0).
We would love to hear your thoughts!

## What Changed
- 468 markdown files reorganized into 9 feature-based categories
- YAML frontmatter added to every snippet for searchability
- New search indexes (SEARCH-INDEX.md, TAG-INDEX.md, PRODUCT-INDEX.md)
- GitHub Actions for automated validation
- Contribution infrastructure (issue templates, PR template, Contributing Guide)

## How to Share Feedback
Reply to this discussion with your thoughts on any of the following:

1. **Navigation** -- Is it easier or harder to find what you need?
2. **Categories** -- Do the 9 categories make sense?
3. **Search** -- Are the indexes helpful?
4. **Missing content** -- What snippets or topics are you looking for?
5. **Contributions** -- Have you tried the new Contributing Guide?
6. **Anything else** -- General thoughts, suggestions, or concerns.

If you had old bookmarks, check the [Migration Guide](./MIGRATION-GUIDE.md).

Thank you for helping us improve!
```

---

## Issue-Based Feedback Template

For structured feedback collected through GitHub Issues, create a new issue template.

### File: `.github/ISSUE_TEMPLATE/restructuring-feedback.yml`

```yaml
name: "v2.0.0 Restructuring Feedback"
description: "Share feedback about the v2.0.0 repository restructuring"
title: "[Feedback] "
labels:
  - feedback
  - v2.0.0
body:
  - type: markdown
    attributes:
      value: |
        Thank you for sharing your feedback on the v2.0.0 restructuring!
        Your input helps us improve the repository for everyone.

  - type: dropdown
    id: overall-rating
    attributes:
      label: "Overall Rating"
      description: "How would you rate the new structure?"
      options:
        - "Much better than before"
        - "Somewhat better"
        - "About the same"
        - "Somewhat worse"
        - "Much worse"
    validations:
      required: true

  - type: dropdown
    id: navigation
    attributes:
      label: "Navigation"
      description: "How easy is it to find snippets?"
      options:
        - "Very easy"
        - "Easy"
        - "Neutral"
        - "Difficult"
        - "Very difficult"
    validations:
      required: true

  - type: textarea
    id: categories-feedback
    attributes:
      label: "Category Feedback"
      description: "Any thoughts on the 9 categories (app-lifecycle, ui-controls, ui-patterns, visual-assets, data-operations, functions, integrations, learning, utilities)?"
      placeholder: "The categories make sense / I would rename X to Y / I would merge X and Y..."
    validations:
      required: false

  - type: textarea
    id: missing-content
    attributes:
      label: "Missing Content"
      description: "Are there Power Fx topics or patterns you wish were covered?"
      placeholder: "I would like to see snippets for..."
    validations:
      required: false

  - type: textarea
    id: migration-experience
    attributes:
      label: "Migration Experience"
      description: "If you had old bookmarks, were you able to find your files?"
      placeholder: "I was able to / I could not find..."
    validations:
      required: false

  - type: textarea
    id: other-feedback
    attributes:
      label: "Other Feedback"
      description: "Any other comments, suggestions, or concerns?"
      placeholder: "Your thoughts here..."
    validations:
      required: false
```

### Manual Issue Template (Markdown Alternative)

If you prefer a markdown-based issue template, create `.github/ISSUE_TEMPLATE/restructuring-feedback.md`:

```markdown
---
name: "v2.0.0 Restructuring Feedback"
about: "Share feedback about the v2.0.0 repository restructuring"
title: "[Feedback] "
labels: feedback, v2.0.0
---

## Overall Rating

<!-- Select one: Much better / Somewhat better / About the same / Somewhat worse / Much worse -->

## Navigation

<!-- How easy is it to find snippets in the new structure? -->

## Category Feedback

<!-- Any thoughts on the 9 categories? -->

## Missing Content

<!-- Power Fx topics or patterns you wish were covered? -->

## Migration Experience

<!-- If you had old bookmarks, were you able to find them? -->

## Other Feedback

<!-- Any other comments, suggestions, or concerns? -->
```

---

## History

| Date       | Author  | Changes                                       |
|------------|---------|-----------------------------------------------|
| 2026-01-29 | Phase 6 | Created feedback templates for v2.0.0 launch  |
