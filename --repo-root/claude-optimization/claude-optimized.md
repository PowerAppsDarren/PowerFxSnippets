# Claude Code Optimization Guide: Multi-Project Development at Scale

**The definitive guide to orchestrated AI development with Claude Code, covering agent architecture, credit optimization, and production workflows for managing 5-12 simultaneous projects.**

## Critical Clarification: Two Products, One Confusion

Before diving into optimization strategies, **understand that "Claude Code" refers to two distinct tools** that developers often conflate. Your workflow optimization depends on identifying which one you're using—or deciding which better fits your needs.

**Claude Code (Anthropic Official)** is a CLI-first coding assistant that runs primarily in the terminal with a lightweight VS Code bridge extension. It uses file-based configuration (settings.json, CLAUDE.md), supports extensive hooks and automation, and excels at headless CI/CD integration. If you're running `claude` commands in your terminal and seeing diffs in VS Code's native viewer, you're using this.

**Cline (formerly Claude Dev)** is an open-source VS Code extension providing a GUI-based coding agent with chat interface, built-in browser testing, and visual checkpoints. Configuration happens through the extension's settings panel rather than JSON files. If you're interacting through a sidebar chat interface with @mentions and visual task management, you're using Cline.

The remainder of this guide covers **both tools** with clear distinctions where implementation differs. Core concepts like agent orchestration, MCP integration, and credit optimization apply universally.

## Orchestrator-Worker Architecture: The Cost-Efficient Pattern

The most powerful optimization for managing multiple projects simultaneously is implementing hierarchical agent architecture where **Claude Sonnet 4.5 acts as project manager and architect**, while **Haiku agents execute parallel tasks**. This pattern delivers 2-3x cost reduction while maintaining 90% of performance.

### Architecture fundamentals

Your orchestrator agent (Sonnet 4.5 at $3 input/$15 output per million tokens) handles high-level reasoning: breaking complex requests into subtasks, routing work to appropriate specialists, validating results, and synthesizing outputs. Worker agents (Haiku 4.5 at $1 input/$5 output per million tokens) execute focused implementation tasks in parallel—writing code, running tests, generating documentation, performing routine analysis.

The mathematical advantage is striking. A pure Sonnet workflow processing 100 tasks costs baseline X. An orchestrated approach using 1 Sonnet orchestrator coordinating 10 Haiku workers costs approximately 40% of X. The orchestrator consumes perhaps 5,000 tokens planning and validating, while each Haiku worker processes 10,000 tokens of implementation—totaling roughly 105,000 tokens at Haiku prices versus 500,000+ at Sonnet prices for equivalent sequential work.

### Practical implementation for Claude Code

Claude Code enables this pattern through careful prompt engineering and session management. Create a master orchestrator session that maintains project context and delegates discrete tasks to worker instances. The orchestrator analyzes your request, breaks it into parallel subtasks, spawns focused worker sessions, and aggregates results.

```bash
# Orchestrator session (keep running)
claude --model claude-sonnet-4-5-20250929

# In orchestrator, break down task
"Analyze this feature request and create 4 parallel implementation tasks:
1. Core business logic
2. Unit tests  
3. Integration tests
4. API documentation

For each task, provide exact implementation requirements."

# Spawn workers in separate terminals/tmux panes
claude -p "Task 1: Implement user authentication..." --model claude-haiku-3-5-20250514
claude -p "Task 2: Write unit tests for..." --model claude-haiku-3-5-20250514  
claude -p "Task 3: Create integration tests..." --model claude-haiku-3-5-20250514
claude -p "Task 4: Generate API docs..." --model claude-haiku-3-5-20250514

# Aggregate results back in orchestrator
"Review these four completed implementations and ensure consistency..."
```

### Implementation for Cline

Cline doesn't natively support multi-agent orchestration within a single session, but you can approximate the pattern by running multiple Cline instances across VS Code windows or using Cline CLI for worker tasks while maintaining orchestrator context in the main extension.

Configure different API settings per instance by creating project-specific MCP configurations that specify different models. The primary Cline instance (Sonnet) maintains architectural oversight while delegating implementation chunks that worker instances (Haiku) handle independently.

### Advanced orchestration patterns

**Supervisor pattern** works best for coding projects with clear specialization: a Sonnet orchestrator manages specialized Haiku workers (backend developer, frontend developer, test engineer, documentation writer). Each worker maintains narrow context focused on their domain, preventing context bloat while enabling true parallel execution.

**Handoff pattern** excels for dynamic routing: initial triage agent (Haiku) analyzes requests and routes to appropriate specialists. Simple bugs go to debugging agent (Haiku), architectural decisions escalate to senior agent (Sonnet), routine feature work routes to implementation agent (Haiku). This ensures you only pay Sonnet prices when truly necessary.

**Planning pattern** suits complex refactoring or new feature development: Sonnet orchestrator creates detailed execution plan with dependencies, Haiku workers execute steps in dependency order, Sonnet reviewer validates integration points and overall coherence. This three-phase approach balances cost and quality perfectly.

## Credit-Efficient MCP Strategy

Model Context Protocol servers are your secret weapon for minimizing token consumption while maximizing capability. Each MCP you configure adds 50-1,000 tokens to every conversation just for tool definitions, so **ruthless curation is essential**. The wrong MCP configuration can consume 15,000-30,000 tokens before you even start working.

### Essential MCPs by technology stack

**For React development**, install React MCP (`@Streen9/react-mcp`) which provides focused tools for creating apps, managing packages, and file operations—typically consuming 2,000-4,000 tokens in tool definitions. Pair this with filesystem MCP restricted to your src/ directory to prevent unnecessary context about node_modules. The combination enables React-aware assistance without the token bloat of loading entire documentation.

**Python projects** benefit immensely from FastMCP-based servers. The official Python SDK creates remarkably efficient servers with minimal overhead. Build custom MCPs exposing only the specific functions your project needs rather than generic Python servers with hundreds of unused tools. A targeted MCP might expose 5-10 tools (500-1,000 tokens) versus generic Python servers exposing 50+ tools (5,000+ tokens).

**Rust development** achieves the absolute lowest token overhead using native Rust MCP implementations. The official Rust SDK (`rmcp`) compiles to native binaries with zero runtime overhead. For performance-critical projects, consider implementing Python-Rust hybrid MCPs where Rust handles heavy processing (text diffing, syntax analysis) while Python provides the MCP interface—you get Python's ease-of-use with Rust's efficiency.

**Shell scripting and DevOps** work beautifully with bash-based MCPs (`mcpbash-sdk`) that require only `jq` as a dependency. These MCPs consume virtually no overhead since they're just bash functions exposed as tools. Perfect for system administration, CI/CD automation, and DevOps workflows where you want to expose existing shell scripts to AI assistants.

**Electron projects** should use the specialized Electron MCP Server which provides GUI monitoring and Chrome DevTools Protocol integration. This enables deep application debugging without manually gathering state—the MCP automatically exposes application internals through structured tools rather than requiring massive context dumps.

**Power Platform development** lacks dedicated MCPs currently, but you can create custom MCPs that expose Power Fx formula validation, Dataverse queries, or Power Automate flow templates. Since Power Fx uses YAML for formula storage, standard filesystem MCPs work well when restricted to `.pa.yaml` files.

### Profile-level MCP configuration

Claude Code and Cline both support MCP configuration, but the approaches differ significantly. **Claude Code** uses project-level `.mcp.json` files that git tracks, enabling team-wide MCP standardization. Place this in your project root with careful environment variable management for secrets.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"],
      "env": {
        "ALLOWED_OPERATIONS": "read,write"
      }
    },
    "github": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Cline** stores MCP configuration in `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json` (macOS) or equivalent Windows/Linux paths. This global configuration affects all Cline instances, though you can disable specific MCPs per-project through the extension GUI.

### Caching strategies for massive savings

**Prompt caching** is your most powerful cost optimization tool, delivering 90% savings on repeated content. Claude caches content blocks marked with `cache_control: ephemeral` for 5 minutes, refreshing on each hit. The minimum cacheable size is 1,024 tokens for Sonnet and 2,048 for Haiku.

Structure prompts to place stable content first: system instructions, then tool definitions, then project context, finally the variable user query. This ensures maximum cache hit rates. A cached 10,000-token system prompt costs $0.30 per read versus $3.00 uncached—a 10x improvement that compounds across hundreds of daily interactions.

MCP servers benefit from caching by using resource-based deduplication. Instead of sending full file contents repeatedly, MCPs return resource URIs that Claude caches and references. This is particularly powerful for RAG queries where the same documents appear across multiple conversations.

**Semantic caching** takes this further by caching based on similarity rather than exact matches. If you frequently ask variations of the same question ("How do I implement auth?" versus "What's the best way to add authentication?"), semantic caching returns the same cached response when similarity exceeds a threshold. This requires custom implementation but can reduce redundant processing by 50-70% for FAQ-style queries.

### Token budget best practices

Establish clear token budgets per conversation tier: **minimal setup** (1-2 simple MCPs, 1,000-5,000 tokens overhead), **standard setup** (5-10 targeted MCPs, 5,000-15,000 tokens overhead), **comprehensive setup** (15+ MCPs, 15,000-30,000 tokens overhead). Most solo developers should target standard setup—more than minimal but well short of comprehensive.

Monitor actual token consumption using the tools detailed in the next section. If a single MCP consistently consumes more tokens than the value it provides, disable it. The goal is surgical precision: expose exactly the capabilities you need, nothing more.

## Usage Monitoring and Real-Time Dashboards

Programmatic access to Claude Code usage data enables sophisticated monitoring, budget management, and multi-agent coordination. Two primary approaches exist: **local JSONL file parsing** (fastest, no API limits) and **official Analytics API** (organizational visibility, delayed data).

### Local JSONL parsing

Claude Code writes comprehensive usage data to `~/.config/claude/logs/` (Linux/macOS) or equivalent Windows paths in JSONL format. These files contain token counts, model information, session data, timestamps, and costs. Parsing them directly gives you real-time access to every interaction.

Several open-source tools handle parsing for you. **ccusage** (`npx ccusage@latest`) provides instant reports in daily, monthly, or 5-hour billing window formats with live monitoring via `--live` flag. **claude-monitor** (`uv tool install claude-monitor`) offers sophisticated terminal UIs with burn rate analytics, ML-based predictions, and automatic plan detection.

For custom monitoring integrated with your own systems, parse JSONL files directly:

```javascript
const fs = require('fs');
const readline = require('readline');

async function parseUsage(logPath) {
  const fileStream = fs.createReadStream(logPath);
  const rl = readline.createInterface({ input: fileStream });
  
  let totalTokens = 0;
  let totalCost = 0;
  
  for await (const line of rl) {
    const entry = JSON.parse(line);
    totalTokens += entry.input_tokens + entry.output_tokens;
    totalCost += entry.cost;
  }
  
  return { totalTokens, totalCost };
}
```

Watch log files for real-time updates using `chokidar` (Node.js) or native file watching APIs. This enables sub-second monitoring latency versus the Analytics API's hour-long delay.

### Official Analytics API

For organizational deployments, the Claude Code Analytics Admin API (`/v1/organizations/usage_report/claude_code`) provides aggregated metrics including user-level activity, tool usage breakdown, lines of code statistics, and acceptance rates. Requires Admin API key (`sk-ant-admin-...`) and Team/Enterprise plans.

This API excels at understanding team-wide patterns: which developers use which models most heavily, which tools see highest adoption, where code quality issues concentrate. The hour delay makes it unsuitable for real-time monitoring but perfect for weekly reports and budget planning.

### Terminal dashboard implementation

Building custom dashboards provides exactly the visibility you need for orchestrator-worker coordination. The **blessed** library (Node.js) offers full terminal control with widgets for boxes, charts, tables, and real-time updates. **blessed-contrib** adds dashboard-specific widgets: line charts for token usage over time, gauges for credit consumption, tables for active agent status.

A minimal orchestrator dashboard shows active sub-agents, their current tasks, progress status, and real-time credit usage:

```javascript
const blessed = require('blessed');
const contrib = require('blessed-contrib');

const screen = blessed.screen({ smartCSR: true });
const grid = new contrib.grid({ rows: 12, cols: 12, screen: screen });

// Credit gauge
const creditGauge = grid.set(0, 0, 4, 4, contrib.gauge, {
  label: 'Credit Usage',
  stroke: 'green'
});

// Active agents table  
const agentsTable = grid.set(0, 4, 4, 8, contrib.table, {
  label: 'Active Sub-Agents',
  columnWidth: [15, 20, 10, 10]
});

// Update function
setInterval(() => {
  const usage = parseClaudeUsage();
  creditGauge.setPercent(usage.creditPercent);
  
  agentsTable.setData({
    headers: ['Agent', 'Task', 'Status', 'Tokens'],
    data: usage.agents.map(a => [
      a.name, a.task, a.status, a.tokens.toString()
    ])
  });
  
  screen.render();
}, 1000);

screen.key(['q'], () => process.exit(0));
```

For React developers, **ink** provides React components for terminals—write your dashboard using familiar React patterns. For simple status indicators, **ora** gives you elegant spinners with success/fail states.

### VS Code status bar integration

Extend VS Code's status bar to show Claude Code metrics without leaving your editor. The VS Code extension API makes this straightforward:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  const statusBarItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right,
    100
  );
  
  statusBarItem.text = '$(cloud) Claude: Loading...';
  statusBarItem.show();
  
  setInterval(() => {
    const usage = getClaudeUsage();
    statusBarItem.text = `$(cloud) ${usage.tokens}K tokens | $${usage.cost}`;
    statusBarItem.tooltip = `Burn: ${usage.burnRate}/min | ${usage.remaining} remaining`;
    
    if (usage.percentage > 80) {
      statusBarItem.color = new vscode.ThemeColor('errorForeground');
    }
  }, 5000);
  
  statusBarItem.command = 'claude.showDashboard';
  context.subscriptions.push(statusBarItem);
}
```

Click the status bar item to launch a terminal dashboard with detailed breakdowns. This gives you persistent visibility across all VS Code windows without consuming screen real estate.

### Context preservation for window switching

When managing 5-12 projects simultaneously, **terminal banners** help reorient yourself when switching windows. Use `boxen` and `chalk` to generate informative banners on terminal start:

```javascript
const boxen = require('boxen');
const chalk = require('chalk');

function generateBanner() {
  const context = getLastContext();
  
  const banner = `
${chalk.bold('Project:')} ${chalk.cyan(context.project)}
${chalk.bold('Last Task:')} ${context.lastTask.substring(0, 60)}
${chalk.bold('Status:')} ${context.status === 'complete' ? chalk.green('✓ Complete') : chalk.yellow('⏳ In Progress')}
${chalk.bold('Tokens:')} ${chalk.yellow(context.tokens)} | ${chalk.bold('Cost:')} ${chalk.magenta('$' + context.cost)}
`;
  
  console.log(boxen(banner, {
    padding: 1,
    borderStyle: 'round',
    borderColor: 'cyan'
  }));
}
```

Store context in `.claude_context` files per project or in a global state file. Load and display on terminal start. This 2-second orientation saves minutes of context reconstruction when returning to a project after hours working elsewhere.

## Multi-Project Workflow Architecture

Managing 5-12 simultaneous projects demands systematic configuration organization. VS Code Profiles (v1.76+) provide isolated configuration sets encompassing settings, extensions, UI layouts, keybindings, snippets, and tasks—exactly what you need for context-switching between different technology stacks.

### Profile-based project organization

Create **language/stack-specific profiles** rather than per-project profiles. A "React Development" profile includes Prettier, ESLint, and React-specific snippets. A "Python Development" profile includes Ruff, pytest extensions, and Python debugging configurations. A "DevOps" profile includes Docker, Kubernetes, and YAML tools.

This approach scales to dozens of projects because you maintain just 4-6 profiles instead of 12+ project configs. Similar projects share profiles automatically. When you open a React project, VS Code loads the React profile; opening a Python project switches to Python profile.

**Create profiles programmatically** via CLI for reproducible setups:

```bash
# Create and launch with profile
code ~/projects/react-app --profile "React Development"

# Export profile for team sharing
code --profile "React Development" --export-profile ~/react-profile.code-profile

# Import on new machine  
code --profile "React Development" --import-profile ~/react-profile.code-profile
```

Store exported profiles in your dotfiles repository for instant replication on new development machines.

### Workspace configuration hierarchy

Understanding VS Code's settings precedence prevents configuration conflicts. From lowest to highest priority: **Default Settings** → **User Settings** → **Remote Settings** → **Workspace Settings** → **Workspace Folder Settings** → **Policy Settings**.

Profiles create separate user settings storage, but workspace settings still override profile settings. Use this hierarchy strategically:

**User Settings** (global preferences): editor font, font size, theme, window restore behavior, auto-save timing—preferences that apply everywhere regardless of project.

**Profile Settings** (workflow-specific): extensions, formatters, linters, debug configurations—tools and behaviors specific to a technology stack but shared across projects using that stack.

**Workspace Settings** (project-specific): TypeScript version, test framework configuration, build script paths—settings unique to this specific project that shouldn't apply elsewhere.

Multi-root workspaces add another layer: you can group related projects (frontend + backend + shared) into a single `.code-workspace` file with per-folder settings overrides:

```json
{
  "folders": [
    {
      "path": "frontend",
      "name": "Frontend App"
    },
    {
      "path": "backend", 
      "name": "API Server"
    },
    {
      "path": "shared",
      "name": "Shared Components"
    }
  ],
  "settings": {
    "editor.formatOnSave": true
  }
}
```

### Quick-switch mechanisms

**Project Manager extension** (`alefragnani.project-manager`) transforms project switching from slow to instant. Configure it to auto-detect Git repositories in your project directories:

```json
{
  "projectManager.git.baseFolders": [
    "$home/projects/work",
    "$home/projects/clients", 
    "$home/projects/personal"
  ],
  "projectManager.git.maxDepthRecursion": 3,
  "projectManager.sortList": "Recent",
  "projectManager.groupList": true
}
```

Access via `Alt+Shift+P` (Windows/Linux) or `Cmd+Option+P` (Mac). Projects appear sorted by recent use with grouping by base folder. Tag projects (`#react`, `#urgent`, `#client-a`) for filtered quick-switching.

Combine with **Peacock extension** for visual project identification—color-code each VS Code window by project. Your React projects glow green, Python projects show blue, DevOps projects display orange. Instant visual identification when Alt+Tabbing between 8 open VS Code windows.

### Terminal configuration strategies

**Integrated terminal profiles** enable project-specific environments without external multiplexers. Configure per-project shells with environment variables, paths, and startup commands:

```json
{
  "terminal.integrated.profiles.linux": {
    "React Dev": {
      "path": "/bin/bash",
      "args": ["--login"],
      "env": {
        "NODE_ENV": "development",
        "PATH": "${workspaceFolder}/node_modules/.bin:${env:PATH}"
      },
      "icon": "react",
      "color": "terminal.ansiCyan"
    },
    "Python Dev": {
      "path": "/bin/bash",
      "args": ["-c", "source .venv/bin/activate && exec bash"],
      "icon": "python",
      "color": "terminal.ansiYellow"
    }
  }
}
```

For power users managing long-running processes across projects, **Zellij** offers modern terminal multiplexing with intuitive defaults and plugin support. Unlike tmux's steep learning curve, Zellij provides visual keybinding hints and mouse support out of the box:

```bash
# Start project-specific session
zellij --session react-app

# Create layout with dev server, test watcher, logs
zellij --layout dev-layout.kdl
```

Define layouts per project type:

```kdl
// dev-layout.kdl
layout {
  pane split_direction="vertical" {
    pane size=70  // Code editor
    pane split_direction="horizontal" {
      pane command="npm" { args "run" "dev" }
      pane command="npm" { args "test" "--" "--watch" }
    }
  }
}
```

Sessions persist across terminal closes and VS Code restarts. Attach when switching projects to restore exact terminal state.

### Resource management at scale

Running 5-12 VS Code windows simultaneously requires aggressive resource optimization. **File watcher exclusions** provide the biggest single improvement—VS Code watches all files by default, consuming CPU and memory unnecessarily:

```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/*/**": true,
    "**/dist/**": true,
    "**/build/**": true,
    "**/.venv/**": true,
    "**/__pycache__/**": true,
    "**/target/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/*.lock": true
  }
}
```

**Limit open editors** prevents memory bloat from dozens of forgotten tabs:

```json
{
  "workbench.editor.limit.enabled": true,
  "workbench.editor.limit.value": 10,
  "workbench.editor.limit.perEditorGroup": true
}
```

**Profile-based extension loading** eliminates waste from running unused extensions. Create a "Lightweight" profile with only essential extensions for quick tasks, a "Full Stack" profile with everything for major projects. Monitor extension overhead via `Developer: Show Running Extensions`—sort by activation time and memory usage to identify problematic extensions.

## Claude Code Configuration Deep-Dive

Claude Code's configuration system balances power with simplicity through hierarchical file-based settings. Understanding this hierarchy and mastering configuration enables team-wide standardization and reproducible setups.

### Configuration file locations and precedence

Settings load hierarchically with later entries overriding earlier ones:

1. **Global defaults** (`~/.claude/settings.json`): Your personal preferences applying to all projects
2. **Global instructions** (`~/.claude/CLAUDE.md`): Universal coding standards and patterns
3. **Project settings** (`.claude/settings.json`): Team-shared project configuration, git-tracked
4. **Project instructions** (`CLAUDE.md` in project root): Project-specific context and standards
5. **Local overrides** (`.claude/settings.local.json`): Personal tweaks, git-ignored

This hierarchy enables powerful workflows: establish baseline standards globally, specify project requirements in tracked files, allow individual developer customization in local files.

### Complete settings.json example

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "maxTokens": 8096,
  "temperature": 0.7,
  
  "permissions": {
    "allowedTools": [
      "Read",
      "Write", 
      "Edit",
      "Bash(git *)",
      "Bash(npm *)",
      "Bash(pytest *)"
    ],
    "deny": [
      "Read(.env*)",
      "Write(production.config.*)",
      "Bash(rm -rf *)"
    ]
  },
  
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.ts)",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $file"
          }
        ]
      },
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {
            "type": "command", 
            "command": "black $file && ruff check --fix $file"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash(*)",
        "hooks": [
          {
            "type": "command",
            "command": "echo '[Claude] Executing: $command'"
          }
        ]
      }
    ]
  },
  
  "context": {
    "maxContextFiles": 50,
    "excludePatterns": [
      "node_modules/**",
      "dist/**",
      ".git/**"
    ]
  }
}
```

### CLAUDE.md: Project context documentation

The CLAUDE.md file acts as persistent context injected into every conversation. Write this as documentation for an intelligent collaborator joining your project:

```markdown
# Project: E-Commerce Platform API

## Architecture Overview
- **Framework**: Next.js 14 with App Router
- **Database**: PostgreSQL with Prisma ORM  
- **Auth**: NextAuth.js with JWT
- **Payment**: Stripe integration
- **Deployment**: Vercel

## Code Standards

### TypeScript
- Use strict mode
- Prefer functional components with hooks
- Avoid `any` type—use proper types or `unknown`
- Interface names: `IUserProfile` (PascalCase with I prefix)

### File Organization
```
src/
├── app/           # Next.js 14 app routes
├── components/    # React components
├── lib/          # Utility functions
├── server/       # Server-only code
└── types/        # TypeScript definitions
```

### Testing
- Unit tests: Jest + React Testing Library
- Integration tests: Playwright
- Test files: `component.test.tsx` alongside component
- Target 80% coverage

### Git Workflow
- Branch naming: `feature/user-auth`, `fix/payment-bug`
- Commit messages: Conventional Commits format
- PR requirements: tests pass, no lint errors, approved review

## Common Tasks

### Adding New API Endpoint
1. Create route in `src/app/api/[endpoint]/route.ts`
2. Implement GET/POST/PUT/DELETE handlers
3. Add Zod schema validation
4. Write integration tests
5. Update API documentation

### Database Changes
1. Modify `prisma/schema.prisma`
2. Run `npx prisma migrate dev --name migration-name`
3. Update TypeScript types
4. Update seed data if needed
```

This documentation transforms every Claude session into domain-expert consulting without repeatedly explaining architecture.

### Custom commands

Custom commands (`/commandname`) provide reusable prompt templates. Create them in `.claude/commands/`:

```markdown
<!-- .claude/commands/review.md -->
Perform comprehensive code review of: $ARGUMENTS

Focus on:
1. **Security**: SQL injection, XSS, authentication bypass, secrets exposure
2. **Performance**: N+1 queries, unnecessary re-renders, memory leaks
3. **Maintainability**: Code duplication, complex logic, missing documentation
4. **Testing**: Edge cases, error handling, test coverage

Provide:
- Severity rating (Critical/High/Medium/Low)
- Specific line numbers
- Recommended fixes
- Example code corrections
```

Usage: `/review src/auth/login.ts`

Commands accept arguments via `$ARGUMENTS` placeholder, enabling flexible reuse. Build a library of project-specific commands for common workflows.

### Hooks for automation

Hooks trigger commands before or after Claude uses tools, enabling automatic formatting, linting, testing, and validation without manual intervention.

**PostToolUse hooks** run after file writes:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.{ts,tsx,js,jsx})",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $file && eslint --fix $file"
          }
        ]
      },
      {
        "matcher": "Write(**/__tests__/*.test.ts)",
        "hooks": [
          {
            "type": "command",
            "command": "npm test -- $file"
          }
        ]
      }
    ]
  }
}
```

**PreToolUse hooks** run before operations:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write(src/lib/**)",
        "hooks": [
          {
            "type": "command",
            "command": "git diff src/lib/ > /tmp/pre-claude-changes.diff"
          }
        ]
      }
    ]
  }
}
```

This creates pre-change diffs for easy rollback if Claude's modifications prove problematic.

### Headless mode for automation

Headless mode (`-p` flag) enables non-interactive execution critical for CI/CD:

```bash
# Single-shot execution
claude -p "Run all tests and fix any failures"

# With specific model
claude -p "Refactor auth module for security" --model claude-sonnet-4-5

# Output to file
claude -p "Generate API documentation" --output-format json > docs.json

# CI/CD usage
claude --non-interactive --yolo "Build production bundle and run smoke tests"
```

The `--yolo` flag automatically approves all actions, enabling truly headless operation. Use cautiously—only in trusted environments where automatic tool execution is safe.

### Skills and specialized agents

Skills represent specialized sub-agents with focused capabilities configured via `--agents` flag or settings. Define agent configurations specifying their role, allowed tools, and system prompts:

```json
{
  "agents": {
    "code-reviewer": {
      "model": "claude-sonnet-4-5",
      "systemPrompt": "You are an expert code reviewer focusing on security and maintainability.",
      "allowedTools": ["Read", "View", "GrepTool"]
    },
    "test-writer": {
      "model": "claude-haiku-4-5", 
      "systemPrompt": "You write comprehensive tests using Jest and React Testing Library.",
      "allowedTools": ["Read", "Write", "Bash(npm test)"]
    },
    "refactoring-specialist": {
      "model": "claude-sonnet-4-5",
      "systemPrompt": "You refactor code for improved architecture and maintainability.",
      "allowedTools": ["Read", "Write", "Edit", "Bash(npm test)"]
    }
  }
}
```

Invoke specific agents: `claude --agent code-reviewer` or switch between agents during conversation.

## CI/CD Integration with Gitea Actions

Gitea Actions provides GitHub Actions-compatible CI/CD with full AI integration capabilities. Since version 1.21.0, Gitea Actions runs production-ready workflows using `act_runner`, supporting 20,000+ marketplace actions.

### Gitea Actions setup

Register and start act_runner:

```bash
# Download act_runner
wget https://dl.gitea.com/act_runner/latest/act_runner-latest-linux-amd64

# Register with Gitea instance  
./act_runner register --instance https://gitea.example.com --token YOUR_TOKEN

# Start runner daemon
./act_runner daemon
```

**Critical**: Never use loopback addresses (127.0.0.1) for runner registration—job containers won't reach Gitea. Use actual hostname or IP.

### AI-powered code review workflow

Create `.gitea/workflows/ai-review.yaml`:

```yaml
name: AI Code Review
on: [pull_request]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      
      - name: Get Changed Files
        id: changes
        run: |
          CHANGED=$(git diff --name-only ${{ github.event.pull_request.base.sha }})
          echo "files=$CHANGED" >> $GITHUB_OUTPUT
      
      - name: AI Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Comprehensive security and quality review of:
          ${{ steps.changes.outputs.files }}
          
          Check for:
          1. Security vulnerabilities (OWASP Top 10)
          2. Performance issues
          3. Code quality problems
          4. Test coverage gaps
          
          Output JSON with critical_issues array" \
            --output-format json \
            --allowedTools "Read,View,GrepTool" \
            --model claude-sonnet-4-5 > review.json
      
      - name: Check for Critical Issues
        run: |
          CRITICAL=$(jq -r '.critical_issues // empty' review.json)
          if [ ! -z "$CRITICAL" ]; then
            echo "❌ Critical issues found!"
            jq -r '.critical_issues[]' review.json
            exit 1
          fi
          echo "✅ Review passed"
      
      - name: Upload Review Results
        uses: actions/upload-artifact@v3
        with:
          name: ai-review-results
          path: review.json
```

### Automated test generation workflow

```yaml
name: AI Test Generation
on:
  push:
    branches: [main]
    paths:
      - 'src/**/*.ts'

jobs:
  generate-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Find Files Without Tests
        id: find
        run: |
          FILES=""
          for file in $(find src -name '*.ts' -not -name '*.test.ts'); do
            test_file="${file/src/src/__tests__}"
            test_file="${test_file/.ts/.test.ts}"
            if [ ! -f "$test_file" ]; then
              FILES="$FILES $file"
            fi
          done
          echo "missing_tests=$FILES" >> $GITHUB_OUTPUT
      
      - name: Generate Tests
        if: steps.find.outputs.missing_tests != ''
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for file in ${{ steps.find.outputs.missing_tests }}; do
            claude -p "Generate comprehensive Jest tests for $file
            
            Requirements:
            - Test all exported functions
            - Include edge cases and error handling
            - Use React Testing Library for components
            - Mock external dependencies
            - Achieve 90%+ coverage" \
              --allowedTools "Read,Write" \
              --model claude-haiku-4-5
          done
      
      - name: Commit Generated Tests
        run: |
          git config user.name "AI Test Bot"
          git config user.email "bot@example.com"
          git add src/__tests__/
          git commit -m "chore: generate tests for uncovered files" || exit 0
          git push
```

### Git hooks for commit assistance

Pre-commit hook for automatic commit message generation (`.git/hooks/prepare-commit-msg`):

```bash
#!/bin/bash

# Only generate for regular commits (not merges, amends, etc.)
if [ -z "$2" ]; then
  DIFF=$(git diff --cached)
  
  if [ -z "$DIFF" ]; then
    exit 0
  fi
  
  # Generate conventional commit message
  MSG=$(echo "$DIFF" | claude -p "Generate conventional commit message for these changes:
  
  Format: type(scope): description
  
  Types: feat, fix, docs, style, refactor, test, chore
  
  Keep description under 50 characters" --output-format text)
  
  echo "$MSG" > "$1"
fi
```

Pre-commit hook for issue detection:

```bash
#!/bin/bash

CHANGED=$(git diff --cached --name-only)

if [ -z "$CHANGED" ]; then
  exit 0
fi

echo "🤖 Running AI pre-commit checks..."

claude -p "Quick review of staged changes: $CHANGED

Flag only critical issues:
- Security vulnerabilities
- Syntax errors
- Obvious bugs
- Committed secrets/credentials

Output JSON: { \"critical_issues\": [] }" \
  --output-format json \
  --allowedTools "Read,View" \
  --model claude-haiku-4-5 > /tmp/precommit.json

if jq -e '.critical_issues | length > 0' /tmp/precommit.json; then
  echo "❌ Critical issues found. Fix or use --no-verify to bypass:"
  jq -r '.critical_issues[]' /tmp/precommit.json
  exit 1
fi

echo "✅ Pre-commit checks passed"
```

Make executable: `chmod +x .git/hooks/prepare-commit-msg .git/hooks/pre-commit`

### Security best practices

**OWASP LLM Top 10** risks demand specific mitigations:

**Prompt injection prevention**: Validate and sanitize all user inputs before including in prompts. Never trust data from untrusted sources (PR comments, issue bodies, external APIs):

```yaml
- name: Sanitize Input
  run: |
    INPUT=$(echo "${{ github.event.comment.body }}" | sed 's/[^a-zA-Z0-9 .-]//g')
    # Additional validation
    if echo "$INPUT" | grep -qiE "(ignore|bypass|sudo|rm -rf)"; then
      echo "Potentially malicious input detected"
      exit 1
    fi
```

**Least privilege tools**: Restrict AI to read-only operations in untrusted contexts:

```yaml
- name: Safe AI Operation
  run: |
    claude -p "Analyze code for issues" \
      --allowedTools "Read,View"  # No Write, no Bash
      --max-turns 5
```

**Output validation**: Always validate AI-generated code before merging or deploying:

```yaml
- name: Validate Generated Code
  run: |
    # Lint generated code
    eslint generated-code.js
    
    # Security scan
    semgrep --config=auto generated-code.js
    
    # Run tests
    npm test
```

**Audit logging**: Record all AI actions for security review:

```yaml
- name: Log AI Action
  run: |
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | ${{ github.actor }} | AI review | ${{ github.sha }}" >> /var/log/ai-audit.log
```

**Human-in-the-loop**: Require manual approval before deploying AI-generated changes:

```yaml
- name: Manual Approval Required
  uses: trstringer/manual-approval@v1
  with:
    approvers: tech-leads
    minimum-approvals: 1
```

## Implementation Roadmap

Deploy this optimized setup systematically over 4-6 weeks:

**Week 1-2: Foundation**
Configure VS Code profiles for each technology stack. Install essential extensions (Project Manager, Peacock, GitLens). Create `.claude` directories in all projects with basic settings.json and CLAUDE.md files. Set up file watcher exclusions and resource optimization settings.

**Week 2-3: MCP Integration**  
Identify essential MCPs for your stacks. Install and configure 3-5 high-value MCPs per technology profile. Set up profile-level MCP configurations. Test token consumption with `ccusage` or `claude-monitor` to validate optimization.

**Week 3-4: Agent Architecture**
Implement orchestrator-worker pattern. Create orchestrator session templates using Sonnet 4.5. Build worker agent configurations with Haiku 4.5. Develop delegation workflows for common tasks. Measure cost savings against baseline.

**Week 4-5: Monitoring \u0026 Dashboard**
Deploy usage monitoring solution (ccusage or claude-monitor). Build custom terminal dashboard if needed. Integrate VS Code status bar indicators. Set up terminal context banners. Establish alert thresholds for budget management.

**Week 5-6: CI/CD Automation**
Set up Gitea Actions infrastructure. Deploy act_runner. Create AI-powered review workflows. Implement git hooks for commit assistance. Establish security controls and audit logging. Test workflows on non-critical projects before production rollout.

**Week 6+: Optimization \u0026 Scaling**
Fine-tune prompts based on usage patterns. Optimize MCP selection based on actual value. Refine orchestrator delegation logic. Share configurations across team. Document learnings and best practices.

## Critical Configuration Files Reference

### Directory structure for optimal organization

```
~/projects/
├── .claude/                    # Global Claude config
│   ├── settings.json
│   ├── CLAUDE.md
│   └── commands/
│       ├── review.md
│       ├── test.md
│       └── refactor.md
│
├── .vscode-profiles/          # Exported VS Code profiles
│   ├── react-dev.code-profile
│   ├── python-dev.code-profile
│   └── devops.code-profile
│
├── project-a/
│   ├── .claude/
│   │   ├── settings.json      # Project-specific
│   │   └── settings.local.json # Git-ignored personal
│   ├── CLAUDE.md              # Project context
│   ├── .mcp.json              # MCP servers
│   ├── .vscode/
│   │   ├── settings.json
│   │   └── extensions.json
│   └── .gitea/
│       └── workflows/
│           └── ai-review.yaml
│
└── project-b/
    └── (same structure)
```

### Replication script for new machines

```bash
#!/bin/bash
# setup-claude-workspace.sh - Replicate optimized setup

set -euo pipefail

echo "🚀 Setting up Claude Code optimized workspace..."

# Install core tools
if ! command -v claude &> /dev/null; then
  echo "Installing Claude Code..."
  npm install -g @anthropic-ai/claude-code
fi

# Install monitoring tools
echo "Installing usage monitoring..."
npm install -g ccusage
uv tool install claude-monitor

# Create global Claude config
mkdir -p ~/.claude/commands
cat > ~/.claude/settings.json << 'EOF'
{
  "model": "claude-sonnet-4-5-20250929",
  "maxTokens": 8096,
  "permissions": {
    "allowedTools": ["Read", "Write", "Edit", "Bash(git *)"],
    "deny": ["Read(.env*)", "Bash(rm -rf *)"]
  }
}
EOF

cat > ~/.claude/CLAUDE.md << 'EOF'
# Global Coding Standards

## General Principles
- Write clear, maintainable code
- Test thoroughly before committing
- Document complex logic
- Follow language-specific best practices
EOF

# Set up VS Code profiles
echo "Setting up VS Code profiles..."
code --install-extension alefragnani.project-manager
code --install-extension eamodio.gitlens
code --install-extension johnpapa.vscode-peacock

# Import profiles if they exist
for profile in ~/.dotfiles/vscode-profiles/*.code-profile; do
  if [ -f "$profile" ]; then
    code --import-profile "$profile"
  fi
done

# Configure git hooks globally
mkdir -p ~/.git_hooks
# Copy hook scripts
cp ~/.dotfiles/git-hooks/* ~/.git_hooks/
chmod +x ~/.git_hooks/*
git config --global core.hooksPath ~/.git_hooks

echo "✅ Setup complete! Open a project with 'code ~/project --profile \"Profile Name\"'"
```

### Environment variable reference

```bash
# ~/.zshrc or ~/.bashrc

# Claude Code configuration
export ANTHROPIC_API_KEY="your-key-here"
export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"

# Project-specific model overrides (optional)
export CLAUDE_ORCHESTRATOR_MODEL="claude-sonnet-4-5-20250929"
export CLAUDE_WORKER_MODEL="claude-haiku-4-5-20250514"

# MCP configuration
export GITHUB_TOKEN="ghp_your_token"
export OPENAI_API_KEY="sk-your-key"  # For hybrid workflows

# Usage monitoring
export CLAUDE_MONITOR_THEME="dark"
export CLAUDE_MONITOR_REFRESH="2"

# VS Code configuration
export VSCODE_DEFAULT_PROFILE="React Development"

# Gitea Actions (for CI/CD)
export GITEA_RUNNER_REGISTRATION_TOKEN="your-token"
```

## Key Takeaways

**Agent orchestration** using Claude Sonnet 4.5 as orchestrator and Haiku 4.5 as parallel workers delivers 2-3x cost reduction while maintaining quality. Implement this pattern immediately for any project involving repeated tasks or requiring multiple perspectives.

**MCP curation** matters more than quantity. Five carefully selected MCPs beat twenty generic ones. Measure token overhead, ruthlessly cut underperforming MCPs, enable aggressive prompt caching for 90% savings on repeated context.

**VS Code profiles** eliminate configuration overhead across multiple projects. Create stack-specific profiles, not per-project configs. Combined with Project Manager and Peacock extensions, you achieve sub-second context switching between a dozen active projects.

**Usage monitoring** shifts from reactive to proactive. Local JSONL parsing provides real-time visibility enabling budget management, orchestrator coordination, and optimization opportunities. Terminal dashboards transform abstract token counts into actionable operational intelligence.

**CI/CD integration** amplifies productivity through automated code review, test generation, and commit assistance. Gitea Actions plus Claude Code headless mode creates powerful automation pipelines—but demands rigorous security controls following OWASP LLM Top 10 guidelines.

**Configuration as code** enables instant replication across machines and teams. File-based settings, exported profiles, and replication scripts transform a 4-hour setup into a 10-minute automated process.

The optimization pattern is clear: invest upfront in systematic configuration, aggressive tool curation, and orchestrator-worker architecture. These multipliers compound across hundreds of daily interactions, transforming development velocity while slashing costs. A solo developer managing 5-12 simultaneous projects isn't just feasible—it's efficient.