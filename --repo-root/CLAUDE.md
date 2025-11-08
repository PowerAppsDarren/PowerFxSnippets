
Follow all the ai protocols! this is not optional! this is mandatory!

`./ai-protocols/readme.md` and `./ai-protocols/index.md` and `./ai-chats/README.md`

# Timeless Message to AI

Timeless Message to AI regarding this repo:

## Git Configuration

Everything must be in place to ensure the repository is properly maintained, up-to-date, and in good working order.

- [ ] Git should be initialized
- [ ] If this was a forked repo, then we must make sure that the upstream is properly configured to the original repository.
- [ ] Self-hosted gitea installs (there are two of them) must be set up as the remote repositories: main and alt.
- [ ] Push to remote repositories: main and alt
- [ ] On every push, you should fetch to make sure we're not missing any updates. So, essentially, on push, do a bi-directional sync.

## AI Protocols

All AI coding assistants and tools **MUST** (**MANDATORY!!**) follow every one of these protocols:

### Core Mandatory Protocols

- [ ] **[AI-Chats Session Documentation](./ai-chats/README.md)** (v3.2)
  - Create session folder: `ai-chats/YYYY-MM-DD-NN-description/`
  - Create model-specific files: `[Model-Version]--00.md` (summary), `--01.md+` (verbatim exchanges)
  - NO SPACES in filenames, DOUBLE DASH before sequence numbers
  - Update session INDEX.md at end of session
  - Full protocol: [`ai-chats/README.md`](./ai-chats/README.md) | Condensed: [`ai-chats.md`](./ai-chats.md)

### Important Development Protocols

- [ ] **[Make-It-Work-First Philosophy](./ai-priorities.md)**
  - Build happy path first, no theoretical defenses
  - Learn from real failures, guard only what breaks
  - Keep code readable and honest

- [ ] **[AI-PROMPTS Optimization](./prompts.md)**
  - Transform imperfect prompts into precise, testable prompts
  - Generate multiple variants with test cases
  - Apply when crafting complex AI interactions

### Technical Reference Protocols

- [ ] **[Port Number Assignment](./port-numbers.md)**
  - Use random ports between 50000-60000
  - Verify availability with netstat/lsof/ss
  - Sequential assignment for multi-service apps

- [ ] **[Code Review Protocol](./review.md)**
  - Multi-stage review: Static, Dynamic, Security, Performance
  - Output to `./look-around/YYYY-MM-DD--HH-MM--{MODEL_NAME}`
  - Run when first assisting repo or after significant changes

**Quick Navigation:** See [`index.md`](./index.md) for complete protocol directory and quick reference guides.