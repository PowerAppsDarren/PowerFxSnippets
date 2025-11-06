---
name: Port Assignment
description: Assign random port numbers between 50000-60000, verify availability, and allocate sequential ports for multi-service applications
---

# Port Assignment Skill

## Purpose

Automatically assign and verify port numbers for applications, avoiding common ports that are likely already in use.

## When to Use This Skill

Use this skill whenever:
- Setting up a new service that needs a port number
- Configuring multi-tier applications (frontend, API, backend, etc.)
- The user asks for port numbers or mentions ports in the context of service configuration
- Docker compose files, server configs, or development environments need port assignments

## Protocol

### 1. Choose Random Port Range

**ALWAYS** pick a random port between **50000 and 60000**.

**NEVER** use common ports like:
- 80, 443 (HTTP/HTTPS)
- 8080, 8000, 8001 (common dev servers)
- 3000, 3001 (Node.js defaults)
- 5000, 5001 (Flask/Python defaults)

### 2. Check Port Availability

**IMMEDIATELY** after selecting a port, verify it's not in use:

**Linux/macOS:**
```bash
# Using netstat
netstat -tuln | grep :PORT

# Using lsof (more reliable)
lsof -i :PORT

# Using ss (modern alternative)
ss -tuln | grep :PORT
```

**Windows:**
```bash
netstat -ano | findstr :PORT
```

**If the port is in use:** Pick another random number in the 50000-60000 range and repeat the check.

### 3. Sequential Port Assignment for Multi-Service Apps

When assigning ports for multiple services:

1. Pick and verify the **first port** (e.g., 55123)
2. Assign **sequential ports** for additional services:
   - Frontend: 55123
   - API: 55124
   - Backend: 55125
   - Database: 55126
   - etc.

3. **Verify EACH port** in the sequence for availability before finalizing

### 4. Document the Assignments

After assigning ports, clearly document them for the user:
- List each service and its assigned port
- Include the commands used to verify availability
- Suggest how to configure each service with its port

## Example Workflow

```
User: "I need to set up a web app with a frontend, API, and database"

1. Generate random starting port: 54892
2. Check: lsof -i :54892 → (empty, available)
3. Assign sequential:
   - Frontend: 54892 ✓
   - API: 54893 → Check: lsof -i :54893 ✓
   - Database: 54894 → Check: lsof -i :54894 ✓

4. Report:
   "I've assigned the following ports:
   - Frontend: 54892
   - API: 54893
   - Database: 54894

   All ports verified as available using lsof."
```

## Implementation Notes

- Use `shuf -i 50000-60000 -n 1` or similar to generate random port numbers
- Always show the user which commands were used to verify ports
- If multiple consecutive ports are occupied, pick a new random starting point
- Consider the user's platform (Linux/macOS/Windows) when choosing verification commands
