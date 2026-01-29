# Release Instructions for v2.0.0

These instructions document how to create the GitHub release for PowerFxSnippets v2.0.0.

## Prerequisites

- The `gh` CLI must be installed and authenticated: `gh auth status`
- You must be on the `main` branch with all changes merged and pushed
- The `RELEASE-NOTES-v2.0.0.md` file must be present in the repository root

## Pre-Release Checklist

Before creating the release, verify the following:

- [ ] All Phase 6 branches are merged into `main`
- [ ] README.md is updated with v2.0.0 content
- [ ] RELEASE-NOTES-v2.0.0.md is accurate and complete
- [ ] MIGRATION-GUIDE.md exists and maps old paths to new paths
- [ ] PRODUCT-INDEX.md exists with product-based snippet groupings
- [ ] CONTRIBUTING.md is up to date
- [ ] GitHub Actions workflows (validate-snippets.yml, check-links.yml) are functional
- [ ] All snippet YAML frontmatter validates cleanly

## Create the Release

Run the following command from the repository root:

```bash
gh release create v2.0.0 \
  --title "v2.0.0 - Repository Restructuring" \
  --notes-file RELEASE-NOTES-v2.0.0.md
```

### Alternative: Draft Release First

If you want to review the release on GitHub before publishing:

```bash
gh release create v2.0.0 \
  --title "v2.0.0 - Repository Restructuring" \
  --notes-file RELEASE-NOTES-v2.0.0.md \
  --draft
```

Then visit the GitHub releases page to review and publish manually.

### Alternative: With a Specific Target Commit

If you need to tag a specific commit (not HEAD):

```bash
gh release create v2.0.0 \
  --title "v2.0.0 - Repository Restructuring" \
  --notes-file RELEASE-NOTES-v2.0.0.md \
  --target main
```

## Post-Release Steps

After creating the release:

1. **Verify the release page**: `gh release view v2.0.0`
2. **Share the announcement**: Post the release URL in relevant channels
3. **Monitor issues**: Watch for reports of broken links or missing files in the new structure
4. **Create a GitHub Discussion** (optional): Announce the release and invite feedback

```bash
# View the release
gh release view v2.0.0

# Open in browser
gh release view v2.0.0 --web
```

## Rollback (if needed)

If a critical issue is found after release:

```bash
# Delete the release (keeps the tag)
gh release delete v2.0.0 --yes

# Delete the tag as well (if needed)
git tag -d v2.0.0
git push origin --delete v2.0.0
```

---

## History

| Date       | Author  | Changes                                 |
|------------|---------|----------------------------------------|
| 2026-01-29 | Phase 6 | Created release instructions for v2.0.0 |
