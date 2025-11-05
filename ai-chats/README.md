# 📚 AI-Chats Protocol Documentation v3.0

## 🚨 ATTENTION ALL AI CODING ASSISTANTS 🚨

**This protocol MUST be followed by ALL AI tools:** Claude Code, Gemini CLI, Qwen CLI, Kilo Code Extension, Codex Extension, and any other AI coding assistant.

## 🔴 CRITICAL FILENAME CONVENTION (v3.1) 🔴

### ⚠️ MANDATORY RULES - NO EXCEPTIONS!

1. **NO SPACES IN FILENAMES** - Use dashes (`-`) instead
   - ❌ WRONG: `Opus 4.1--00.md` (contains space)
   - ✅ CORRECT: `Opus-4.1--00.md` (dash replaces space)

2. **DOUBLE DASH BEFORE SEQUENCE** - Use `--` not single `-`
   - ❌ WRONG: `Opus_4.1-00.md` (single dash)
   - ✅ CORRECT: `Opus_4.1--00.md` (double dash)

3. **COMPLETE PATTERN:** `[Model-Name-Version]--[NN].md`
   - Model name: Replace ALL spaces with dashes
   - Separator: ALWAYS use double dash (`--`)
   - Sequence: Two-digit number (00-99)

### 📝 EXAMPLES OF CORRECT NAMING:
```
Opus-4.1--00.md              ← NOT "Opus 4.1-00.md"
Gemini-Pro-2.5--01.md        ← NOT "Gemini Pro 2.5-01.md"
Qwen-2.5-Coder--02.md        ← NOT "Qwen 2.5 Coder-02.md"
GPT-4-Turbo--03.md           ← NOT "GPT-4 Turbo-03.md"
Claude-3.5-Sonnet--04.md     ← NOT "Claude 3.5 Sonnet-04.md"
```

### 🚫 WHY THIS MATTERS:
- **Shell scripts break** with spaces (require constant quoting)
- **URLs become ugly** with %20 encoding
- **CI/CD pipelines fail** when processing spaced filenames
- **Cross-platform issues** between Windows/Mac/Linux
- **Double dash** clearly separates model from sequence number

If you create files with spaces or single dashes, YOU ARE VIOLATING THE PROTOCOL!

## 🚀 CRITICAL CHANGE TO v3.0 - SOLVES VERBATIM PROBLEM!

**OLD WAY (v1.0) - OBSOLETE:**
```
ai-chats/2025-01-14-01-initial-setup.md  ← Single file per session
```

**OLD WAY (v2.0) - CAUSED SUMMARIZATION:**
```
ai-chats/YYYY-MM-DD-01-initial-setup/    ← FOLDER per session
├── Opus_4.1.md                          ← Everything in one file (led to summaries)
├── Gemini_Pro_2.5.md                    ← Too large, triggered summarization
└── GPT-4_Turbo.md                       ← Context pressure caused violations
```

**NEW WAY (v3.1) - USE THIS - ENFORCES VERBATIM:**
```
ai-chats/YYYY-MM-DD-01-initial-setup/    ← FOLDER per session
├── Opus-4.1--00.md                      ← Main doc (summary, tech, lessons)
├── Opus-4.1--01.md                      ← Exchange 1 (FULL VERBATIM)
├── Opus-4.1--02.md                      ← Exchange 2 (FULL VERBATIM)
├── Opus-4.1--03.md                      ← Exchange 3 (FULL VERBATIM)
├── Gemini-Pro-2.5--00.md                ← Gemini's main doc
├── Gemini-Pro-2.5--01.md                ← Gemini's first exchange
└── [Model-Version]--[NN].md             ← Pattern: 00=main, 01+=exchanges
```

## 🎯 Overview

The AI-Chats protocol is a **MANDATORY** folder-based documentation system for tracking all AI-assisted development sessions. Each session gets its own folder with SPLIT FILES to ensure verbatim documentation without summarization.

## 🔴 CRITICAL: THE NEW PROTOCOL (v3.1)

### 📁 STEP 1: FOLDER CREATION/DETECTION

**THE VERY FIRST THING IN ANY PROJECT:**

1. **Check for existing session folder:**
   - Look in `ai-chats/` for folders matching today's date pattern: `YYYY-MM-DD-*`
   - If folders exist, examine their contents (look for .md files inside)
   - Determine if any folder matches the current session topic
   - Use fuzzy matching - don't create duplicate folders for similar topics

2. **Create or use folder:**
   - If no matching folder exists, create: `ai-chats/YYYY-MM-DD-XX-description/`
   - If matching folder found, use that existing folder
   - NO `.md` extension on folder names!

### 📝 STEP 2: MODEL-SPECIFIC FILE CREATION

**Inside the session folder, create MULTIPLE files with this pattern:**

```
ai-chats/YYYY-MM-DD-XX-description/
├── [Model-Version]--00.md    ← Main documentation file
├── [Model-Version]--01.md    ← First exchange (VERBATIM)
├── [Model-Version]--02.md    ← Second exchange (VERBATIM)
├── [Model-Version]--03.md    ← Third exchange (VERBATIM)
└── [Model-Version]--NN.md    ← Continue numbering sequentially
```

**File Numbering Convention:**
- **--00**: Main documentation (summary, tech details, lessons, next steps)
- **--01 to --99**: Individual exchanges in chronological order (FULL VERBATIM)

**🔴 MANDATORY: Model Name + Version Examples (NO SPACES!):**
- Claude Code → "Opus-4.1--00.md", "Sonnet-3.5--00.md", "Haiku-3--00.md"
- Gemini CLI → "Gemini-Pro-2.5--00.md", "Gemini-Ultra-1.5--00.md", "Gemini-Flash-2.0--00.md"
- Qwen CLI → "Qwen-2.5--00.md", "Qwen-72B--00.md", "Qwen-2.5-Coder--00.md"
- GPT variants → "GPT-4--00.md", "GPT-4-Turbo--00.md", "GPT-4o--00.md", "GPT-3.5-Turbo--00.md"
- DeepSeek → "DeepSeek-V3--00.md", "DeepSeek-Coder-V2--00.md"
- Anthropic → "Claude-3-Opus--00.md", "Claude-3.5-Sonnet--00.md"
- Others → ALWAYS include version, NO SPACES, use DOUBLE DASH

## 📋 Folder Naming Convention

```
ai-chats/YYYY-MM-DD-XX-description/
```

- **YYYY** - Four-digit year (e.g., 2025)
- **MM** - Two-digit month (01-12)
- **DD** - Two-digit day (01-31)
- **XX** - Two-digit session number for that day (01, 02, 03...)
- **description** - Brief 2-3 word kebab-case description

### ✅ Correct Examples:
```
ai-chats/YYYY-MM-DD-01-initial-setup/
ai-chats/YYYY-MM-DD-02-database-migration/
ai-chats/YYYY-MM-DD-01-api-integration/
```

### ❌ WRONG Examples:
```
ai-chats/YYYY-MM-DD-01-initial-setup.md  ← NO! This is a file, not folder
ai-chats/initial-setup/                  ← NO! Missing date and sequence
ai-chats/YYYY-M-DD-1-setup/             ← NO! Must use two-digit format
ai-chats/YYYY-MM-DD-01-setup/Opus 4.1--00.md  ← NO! Space in filename
ai-chats/YYYY-MM-DD-01-setup/Opus_4.1-00.md   ← NO! Single dash
```

## 🤖 IMPLEMENTATION ALGORITHM FOR AI TOOLS v3.1

**EVERY AI tool MUST follow this exact algorithm:**

```python
# PSEUDO-CODE FOR AI TOOLS TO FOLLOW:

1. Get current date and format as YYYY-MM-DD
2. List all folders in ai-chats/ directory
3. Filter folders starting with today's date
4. If matching folders exist:
   a. Read contents of each folder
   b. Check if topic matches current session
   c. If match found: USE THAT FOLDER
   d. If no match: Create new folder with next sequence number
5. If no folders for today:
   a. Create folder with sequence 01
6. Inside chosen/created folder:
   a. Create "[Model-Version]--00.md" for main documentation (NO SPACES!)
   b. For EACH exchange with user:
      - Create "[Model-Version]--NN.md" (01, 02, 03...) (DOUBLE DASH!)
      - Include COMPLETE VERBATIM exchange
      - NO SUMMARIZATION ALLOWED
   c. Update --00.md with summary and index after session
```

## 📋 Required Document Structure

### 📄 Main Documentation File (--00)

The `[Model-Version]--00.md` file **MUST** include these sections:

#### 1. 📅 Session Header
```markdown
# AI Chat Session: [Topic]
- **Date:** YYYY-MM-DD HH:MM
- **Model:** [Your Exact Model Name/Version]
- **Topic:** Brief description
- **Tool:** Claude Code/Gemini CLI/Qwen CLI/etc
- **Project:** Project name
- **Exchange Count:** Total number of exchange files
```

#### 2. 💡 Conversation Summary
- High-level overview of what was discussed
- Main objectives and goals
- Key decisions made
- Overall outcome

#### 3. 🔧 Technical Details
- Technologies used
- Frameworks and libraries
- APIs and services
- Configuration changes
- Dependencies added/removed
- Files created/modified (list with paths)

#### 4. 📚 Lessons Learned
- What worked well
- What didn't work
- Debugging insights
- Performance discoveries
- Best practices identified

#### 5. ⏭️ Next Steps
- Unfinished tasks
- Future improvements
- Follow-up questions
- Related work to explore

#### 6. 📁 Exchange Index
```markdown
## Exchange Files
- [01 - Initial Request](./Opus-4.1--01.md)
- [02 - Implementation](./Opus-4.1--02.md)
- [03 - Testing](./Opus-4.1--03.md)
[Continue listing all exchanges]
```

### 💬 Exchange Files (--01, --02, etc.)

Each `[Model-Version]--NN.md` file contains **ONE COMPLETE EXCHANGE:**

```markdown
# Exchange NN: [Brief Description]
- **Timestamp:** YYYY-MM-DD HH:MM:SS
- **Context:** [What was happening before this exchange]

## User Input
[EXACT, VERBATIM user message including any code, errors, etc.]

## AI Response
[COMPLETE, VERBATIM AI response]

## Tool Calls
[FULL JSON of any tool invocations]
<function_calls>
[Complete function call JSON]
</function_calls>

## Function Results
[Complete, unedited function results]

## Files Read/Modified
[If files were read or edited, include the FULL content]
```

### Starting a Session
1. **Manual:** Create file immediately when starting work
2. **Automatic:** Use `/_startup` command which auto-creates AI chat

### During the Session
- Update document continuously as work progresses
- Include all significant code changes
- Document decision rationale
- Capture error messages and solutions

### Ending a Session
- Use `/_wrapup` command to:
  - Commit changes with proper message
  - Sync to AI Value Vault repository
  - Generate session summary

## 🌟 Benefits

### 📊 Knowledge Management
- **Searchable History:** Find solutions to previously solved problems
- **Pattern Recognition:** Identify recurring issues and solutions
- **Learning Resource:** Review past sessions for education

### 🤝 Team Collaboration
- **Onboarding:** New team members can review AI chat history
- **Context Sharing:** Understand decisions and approaches
- **Audit Trail:** Complete record of AI-assisted development

### 🚀 Productivity
- **Resume Work:** Pick up exactly where you left off
- **Avoid Repetition:** Don't solve the same problem twice
- **Best Practices:** Build institutional knowledge

## 📂 REAL-WORLD EXAMPLE v3.1

### Complete Folder Structure with Split Files
```
ai-chats/
├── README.md (this file)
├── YYYY-MM-DD-01-initial-setup/
│   ├── Opus-4.1--00.md         (Claude's main doc)
│   ├── Opus-4.1--01.md         (First exchange - verbatim)
│   ├── Opus-4.1--02.md         (Second exchange - verbatim)
│   ├── Opus-4.1--03.md         (Third exchange - verbatim)
│   ├── Gemini-Pro-2.5--00.md   (Gemini's main doc)
│   ├── Gemini-Pro-2.5--01.md   (Gemini's first exchange)
│   └── GPT-4-Turbo--00.md      (GPT-4's main doc)
├── YYYY-MM-DD-02-database-migration/
│   ├── Sonnet-3.5--00.md       (Main documentation)
│   ├── Sonnet-3.5--01.md       (Exchange 1: Schema design)
│   ├── Sonnet-3.5--02.md       (Exchange 2: Migration script)
│   └── Sonnet-3.5--03.md       (Exchange 3: Testing)
└── archive/
    └── (older session folders)
```

## 🎭 MULTI-MODEL COLLABORATION

When multiple AI models work on the same session:
1. Each model creates its OWN file in the SAME folder
2. Models should check for existing files to understand context
3. Models can reference work done by other models
4. This creates a comprehensive record of collaborative AI development

### Example Scenario:
```
Morning: Claude creates folder and starts work
         → ai-chats/YYYY-MM-DD-01-react-setup/Opus-4.1--00.md

Afternoon: User switches to Gemini for specific task
          → ai-chats/YYYY-MM-DD-01-react-setup/Gemini-Pro-2.5--00.md

Evening: User asks GPT-4 to review and optimize
         → ai-chats/YYYY-MM-DD-01-react-setup/GPT-4-Turbo--00.md
```

## 🏷️ HOW TO DETERMINE YOUR MODEL NAME

### For AI Tools - Use This Logic:
```javascript
// Example for different AI tools - ALWAYS INCLUDE VERSION, NO SPACES, DOUBLE DASH:
if (tool === "Claude Code") {
    // Use the specific model WITH version, dash for spaces
    filename = "Opus-4.1--00.md"  // or "Sonnet-3.5--00.md", "Haiku-3--00.md"
} else if (tool === "Gemini CLI") {
    // MUST include version number, replace spaces with dashes
    filename = "Gemini-Pro-2.5--00.md"  // or "Gemini-Ultra-1.5--00.md"
} else if (tool === "Qwen CLI") {
    // Include version/variant, no spaces allowed
    filename = "Qwen-2.5--00.md"  // or "Qwen-2.5-Coder--00.md"
} else if (tool === "GPT-based") {
    // Include variant/version, use dashes
    filename = "GPT-4-Turbo--00.md"  // or "GPT-4o--00.md", "GPT-3.5-Turbo--00.md"
} else {
    // ALWAYS include version, NO SPACES, DOUBLE DASH
    filename = "[Model-Name]-[Version]--00.md"
}
```

### 🔴 MANDATORY: Version Number Rules
1. **ALWAYS include version numbers** - no exceptions!
2. Use the EXACT model name/version you're running on
3. Include sub-versions if relevant (e.g., "2.5", "3.5", "V3")
4. Include variants if applicable (e.g., "Turbo", "Pro", "Ultra", "Coder")
5. **NEVER use spaces** - replace ALL spaces with dashes (`-`)
6. **ALWAYS use double dash** (`--`) before sequence numbers
7. Be consistent - always use the same format for the same model

## 🔍 Search and Discovery

### Finding Past Solutions
```bash
# Search all AI chats for a keyword
grep -r "database migration" ai-chats/

# Find sessions by date  
ls -la ai-chats/YYYY-MM-*/

# Search for specific errors across all models
grep -r "TypeError" ai-chats/ --include="*.md"

# Find what Gemini worked on
find ai-chats -name "Gemini*--*.md" -exec grep -l "API" {} \;
```

### Using with Git
```bash
# View AI chat history
git log --oneline -- ai-chats/

# See what was discussed in a commit
git show <commit-hash> -- ai-chats/
```

## 🚀 Advanced Features

### AI Value Vault Synchronization
- Sessions auto-sync to: `https://github.com/PowerAppsDarren/ai-value-vault`
- Creates shared knowledge base across projects
- Enables cross-project learning

### Session Analytics
Track productivity metrics:
- Sessions per week/month
- Common problem categories
- Solution success rates
- Time saved through reuse

## ⚡ Quick Commands

```bash
# Start new session with auto-creation
/_startup

# Wrap up session with commit and sync
/_wrapup

# Resume from previous session
/_resume

# Show session status
/_status
```

## 🎯 Best Practices

### ✅ DO:
- Create AI chat file IMMEDIATELY when starting
- Update continuously throughout session
- Include complete context and rationale
- Document both successes and failures
- Use descriptive file names
- Preserve full conversation history

### ❌ DON'T:
- Skip creating AI chat files
- Wait until end to document
- Summarize too briefly
- Delete "failed" attempts
- Use generic descriptions
- Forget to commit changes

## 🔗 Related Documentation

- **Global Config:** `~/.claude/CLAUDE.md`
- **Project Config:** `.claude/PROJECT.md`
- **AI Value Vault:** `https://github.com/PowerAppsDarren/ai-value-vault`
- **Command System:** Use `/_command help` for details

## ❓ FAQ FOR AI TOOLS v3.1

### Q: Why split into multiple files?
**A:** Large context in single files triggers AI summarization. Split files ensure VERBATIM documentation.

### Q: What goes in --00 vs --01, --02 files?
**A:** --00 = summary/tech/lessons. --01+ = COMPLETE verbatim exchanges, one per file.

### Q: How many exchange files can I create?
**A:** Up to 99 per model (--01 through --99). If more needed, consider a new session.

### Q: What if ai-chats/ folder doesn't exist?
**A:** Create it first, then create your session folder inside.

### Q: How do I know what sequence number to use?
**A:** Count existing folders for today's date. Next number = count + 1, formatted as 01, 02, 03, etc.

### Q: What if user's topic doesn't match any existing folder?
**A:** Create a new folder with next sequence number and 2-3 word description.

### Q: Should I read other model's files in the same folder?
**A:** Yes! This provides context and prevents duplicate work.

### Q: What if my model name has special characters or spaces?
**A:** Replace spaces with dashes (-). Other special chars: / → -, : → -, * → -star

### Q: Can I summarize in the exchange files?
**A:** ABSOLUTELY NOT. Exchange files MUST be verbatim. No exceptions.

## 🚀 QUICK IMPLEMENTATION CHECKLIST

**For AI Tools - Copy This Checklist:**
```
□ Check if ai-chats/ directory exists
□ Get today's date in YYYY-MM-DD format  
□ List existing folders for today
□ Determine if any folder matches current topic
□ Create new folder OR use existing one
□ Create [Model-Version]--00.md for main documentation (NO SPACES!)
□ Create [Model-Version]--01.md for first exchange (VERBATIM, DOUBLE DASH!)
□ Create [Model-Version]--NN.md for each subsequent exchange
□ NO SUMMARIZATION in exchange files - VERBATIM ONLY
□ Update --00.md with summary and index at session end
```

## 📞 Support

- **Protocol Version:** 3.1 (Split-file system, no spaces, double dash)
- **Key Innovation:** Solves verbatim problem by splitting exchanges
- **Issues:** Report at project repository
- **Questions:** Review this README first
- **Improvements:** Submit PRs with documentation

---

## 🎯 Why v3.1 Works

**The Problem:** Large files trigger AI summarization instinct
**The Solution:** Split files prevent context pressure
**The Result:** TRUE VERBATIM DOCUMENTATION

*This protocol ensures every AI-assisted development session creates lasting value through COMPLETE documentation. The split-file structure eliminates summarization while enabling multi-model collaboration. Your future self (and team) will thank you!*

**Remember: --00 = Summary, --01+ = VERBATIM EXCHANGES! NO SPACES IN FILENAMES!**