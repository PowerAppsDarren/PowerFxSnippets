# Exchange 07: Editor Gutter and Padding

- **Timestamp:** 2025-12-10
- **Context:** User wanted to style the line number gutter and add left padding

## User Input

wait a sec. where the line numbers are in the code editor, there is a faint blue color. Should we make that whole column where the line numbers are at, should we make that dark like our terminal window here?

## AI Response

Added editor gutter background - first tried dark (#371236) like terminal, but user said too dark.

Changed to pale pink (#f5e8f1) with updated line number colors.

### Colors Added
- `editorGutter.background`: `#f5e8f1`
- `editorGutter.modifiedBackground`: `#ba39ad`
- `editorGutter.addedBackground`: `#932d89`
- `editorGutter.deletedBackground`: `#d467b9`
- `editorLineNumber.foreground`: `#932d89`
- `editorLineNumber.activeForeground`: `#541f54`

## User Follow-up: Left Padding

User also wanted left padding between gutter and code. Attempted `editor.padding.left` but VS Code shows "Unknown Configuration Setting" - this setting doesn't exist (it's an open feature request).

### Workaround Options
1. Custom CSS Extension with `.monaco-editor .lines-content { padding-left: 12px; }`
2. Enable glyph margin: `"editor.glyphMargin": true`
