# Claude Code Setup TL;DR - Quick Start Guide

**For solo developers managing 5-12 projects with React/Electron/CLI/Power Platform**

## 🎯 The Core Strategy: Orchestrator + Workers = 60% Cost Savings

**Use Sonnet 4.5 as your "project manager"** - handles planning, routing, validation  
**Use Haiku 4.5 as your "workers"** - parallel execution of specific tasks

```bash
# Orchestrator terminal (keep open)
claude --model claude-sonnet-4-5-20250929

# Worker terminals (spawn as needed)
claude -p "Task: Build authentication..." --model claude-haiku-4-5-20250514
claude -p "Task: Write tests..." --model claude-haiku-4-5-20250514
claude -p "Task: Generate docs..." --model claude-haiku-4-5-20250514
```

**Why this works:** Sonnet costs $3 input/$15 output per 1M tokens. Haiku costs $1 input/$5 output. Use expensive model for thinking, cheap model for doing.

---

## 🔧 Essential Setup (30 minutes)

### 1. Install Core Tools
```bash
# Claude Code
npm install -g @anthropic-ai/claude-code

# Usage monitoring
npm install -g ccusage
# OR
uv tool install claude-monitor

# VS Code extensions
code --install-extension alefragnani.project-manager
code --install-extension johnpapa.vscode-peacock
```

### 2. Create Global Config
```bash
mkdir -p ~/.claude/commands
```

**~/.claude/settings.json:**
```json
{
  "model": "claude-sonnet-4-5-20250929",
  "maxTokens": 8096,
  "permissions": {
    "allowedTools": ["Read", "Write", "Edit", "Bash(git *)", "Bash(npm *)"],
    "deny": ["Read(.env*)", "Bash(rm -rf *)"]
  }
}
```

### 3. Set Up Project Templates
```bash
# In each project root
mkdir -p .claude

# .claude/settings.json (team-shared, git-tracked)
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.{ts,tsx})",
        "hooks": [{"type": "command", "command": "prettier --write $file"}]
      }
    ]
  }
}

# CLAUDE.md (project context)
# Tell Claude about your architecture, standards, common tasks
```

---

## 💰 MCPs: Less is More

**Only install MCPs you'll use daily.** Each MCP adds 50-1,000 tokens per conversation.

### Recommended by Stack

**React/Electron:**
- `@modelcontextprotocol/server-filesystem` (restrict to src/)
- `@Streen9/react-mcp`
- `@modelcontextprotocol/server-github`

**Python:**
- FastMCP-based custom servers (make your own!)
- `@modelcontextprotocol/server-filesystem`

**Shell/DevOps:**
- `mcpbash-sdk`
- `@modelcontextprotocol/server-github`

**Power Platform:**
- Custom MCP for Power Fx validation (build your own)
- Standard filesystem MCP for .pa.yaml files

### Configuration
```bash
# Project-level: .mcp.json (git-tracked)
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]
    }
  }
}
```

**Pro tip:** Use `ccusage --live` to monitor token consumption and cut underperforming MCPs.

---

## 📊 Usage Monitoring Setup

### Option 1: Quick Command Line
```bash
# Check today's usage
ccusage

# Live monitoring
ccusage --live

# Last 5 hours (billing window)
ccusage --interval 5h
```

### Option 2: VS Code Status Bar
Create simple extension or use terminal in sidebar with `watch -n 5 ccusage`

### Option 3: Terminal Dashboard
```bash
# Parse Claude logs directly
~/.config/claude/logs/
```

---

## 🗂️ Managing 5-12 Projects

### VS Code Profiles (THE game-changer)

**Create 4-6 stack profiles, NOT per-project profiles:**

```bash
# Create profiles
code --profile "React Dev"
code --profile "Python Dev"
code --profile "DevOps"

# Launch project with profile
code ~/projects/react-app --profile "React Dev"

# Export for team/backup
code --profile "React Dev" --export-profile ~/react.code-profile
```

**Configure Project Manager:**
```json
{
  "projectManager.git.baseFolders": [
    "$home/projects"
  ],
  "projectManager.git.maxDepthRecursion": 3
}
```

**Quick switch:** `Alt+Shift+P` → type project name

**Color coding with Peacock:** Each project gets unique VS Code window color

---

## ⚡ Performance Optimizations

### File Watcher Exclusions (CRITICAL)
```json
{
  "files.watcherExclude": {
    "**/node_modules/*/**": true,
    "**/dist/**": true,
    "**/.venv/**": true,
    "**/target/**": true
  }
}
```

### Editor Limits
```json
{
  "workbench.editor.limit.enabled": true,
  "workbench.editor.limit.value": 10
}
```

---

## 🚀 Quick Workflows

### Code Review
```bash
claude --agent code-reviewer
```

### Test Generation
```bash
claude -p "Generate Jest tests for src/auth/login.ts with 90% coverage"
```

### Refactoring
```bash
# Orchestrator analyzes
claude -p "Break down refactoring auth module into 4 parallel tasks"

# Workers execute
claude -p "Task 1: Extract validation logic" --model haiku
claude -p "Task 2: Separate API calls" --model haiku
claude -p "Task 3: Update tests" --model haiku
claude -p "Task 4: Update documentation" --model haiku
```

---

## 🎨 Status Bar Example (Your Current Setup)

Your status bar shows:
- Model version
- Tokens (input/output/cached)
- Session time
- Cost tracking

**To replicate on new machine:**
1. Export VS Code profile: `code --export-profile ~/my-profile.code-profile`
2. Copy to new machine
3. Import: `code --import-profile ~/my-profile.code-profile`

---

## 🔐 Security Checklist

- [ ] Never commit `.env` files
- [ ] Add `.claude/settings.local.json` to `.gitignore`
- [ ] Use `deny` rules in permissions for dangerous commands
- [ ] Restrict MCP filesystem access to specific directories
- [ ] Review all AI-generated code before committing
- [ ] Use `--allowedTools` to limit tool access in CI/CD

---

## 📋 Daily Workflow

**Morning:**
```bash
# Check usage from yesterday
ccusage --interval 24h

# Start orchestrator session
claude --model sonnet
```

**During work:**
```bash
# Switch projects with Alt+Shift+P
# Peacock shows which project by color
# Spawn Haiku workers for parallel tasks
# Monitor with: ccusage --live
```

**End of day:**
```bash
# Review burn rate
claude-monitor

# Adjust MCPs if token usage is high
```

---

## 🆘 Troubleshooting

**High token usage?**
- Run `ccusage` to see breakdown
- Disable unused MCPs
- Switch more tasks to Haiku workers

**Claude not finding files?**
- Check filesystem MCP is configured
- Verify paths in .mcp.json
- Ensure .gitignore isn't blocking access

**Context getting lost between projects?**
- Use CLAUDE.md in each project root
- Create terminal banners (see full guide)
- Use Project Manager for quick switching

**Performance issues with many projects?**
- Add file watcher exclusions
- Limit open editors
- Create lightweight profile for quick tasks

---

## 📦 Quick Setup Script

```bash
#!/bin/bash
# One-command setup

npm install -g @anthropic-ai/claude-code ccusage
mkdir -p ~/.claude/commands
cat > ~/.claude/settings.json << 'EOF'
{
  "model": "claude-sonnet-4-5-20250929",
  "maxTokens": 8096
}
EOF

code --install-extension alefragnani.project-manager
code --install-extension johnpapa.vscode-peacock

echo "✅ Setup complete!"
```

---

## 💡 Key Numbers to Remember

- **Sonnet 4.5:** $3 input / $15 output per 1M tokens
- **Haiku 4.5:** $1 input / $5 output per 1M tokens  
- **Savings:** 2-3x cost reduction with orchestrator pattern
- **Caching:** 90% discount on cached tokens (lasts 5 minutes)
- **MCPs:** 50-1,000 tokens overhead each
- **Target MCP count:** 3-7 per project type

---

## 🎯 Your Next 30 Minutes

1. **Install monitoring:** `npm install -g ccusage`
2. **Create global config:** `~/.claude/settings.json` 
3. **Set up VS Code profiles:** React, Python, DevOps
4. **Install Project Manager extension**
5. **Pick 2-3 essential MCPs** for your main stack
6. **Try orchestrator pattern:** One Sonnet + two Haiku workers

**Full details in main guide - this TL;DR gets you 80% of the value in 20% of the time.**
