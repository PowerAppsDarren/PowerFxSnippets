# Exchange 02: Status Bar Fix

- **Timestamp:** 2025-12-10
- **Context:** Theme was updated but user noticed blue background on status bar item

## User Input

status bar at the bottom of VS Code where it says "screen reader optimized," it actually has a blue background. Can you fix that one too?

## AI Response

Added status bar item colors to fix the blue "Screen Reader Optimized" indicator:

```json
"statusBarItem.prominentBackground": "#932d89",
"statusBarItem.prominentForeground": "#ffffff",
"statusBarItem.prominentHoverBackground": "#ba39ad",
"statusBarItem.warningBackground": "#ba39ad",
"statusBarItem.warningForeground": "#ffffff",
"statusBarItem.errorBackground": "#932d89",
"statusBarItem.errorForeground": "#ffffff",
```

## Files Modified

- `C:\src\src-power-platform\PowerFxSnippets\.vscode\settings.json` - Added statusBarItem.prominent* colors
