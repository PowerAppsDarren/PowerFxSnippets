# Continue on this project!

If spec-kit is not installed, we should run this: `specify init --here --ai claude --script sh --force`

- do a git commit now!
- follow the `ai-chats/README.md` protocol!!
- Next priority is to get this app to run in a docker compose/stack locally so I can use the app even when vs code is not open! get this done asap! make sure to create all the necessary files including a docker-compose.yml file, a Dockerfile, and any setup scripts needed. Document the setup process in a DOCKER-SETUP.md file and provide a quick start guide in DOCKER-QUICK-START.md. make sure the url & port is listed near at the top of the readme.md. any/all ports used must be randomly selected from 50000 to 60000.

THEN!!!...

# Comprehensive Codebase Review and Enhancement

Do this at least once. write out your findings. if the file you create is 5 days old, then to this review & enhancement again!

Execute a thorough, multi-stage code review to detect issues, deviations from best practices, security vulnerabilities, performance bottlenecks, and optimization opportunities. Utilize AI for holistic codebase analysis, targeted improvement proposals, and actionable recommendations for tightening, refactoring, and modernization.

YOU MUST ADHERE TO THE GUIDELINES IN `./ai-chats/README.md`, encompassing review methodology, tool integration, output formatting, and seamless workflow alignment with the project.

Incorporate the following previous conversation context as necessary to ensure continuity, reference prior analyses, and iteratively build upon completed tasks (e.g., project structure assessments, authentication/security validations, API endpoint reviews, database schema audits, and todo list refinements):

Organize the review into the following phases: (1) Static Analysis (linting, type checking, dependency scanning, and code complexity metrics), (2) Dynamic Analysis (runtime behavior simulation, error handling robustness, and integration testing), (3) Security Audit (OWASP Top 10 compliance, input sanitization, authentication mechanisms, and vulnerability scanning), (4) Performance Profiling (code efficiency analysis, bundle size optimization, memory usage, and load testing), (5) Best Practices Alignment (code style consistency, accessibility standards, maintainability scoring, and documentation quality), and (6) AI-Driven Refactoring Suggestions (automated code improvements, test case generation, architectural enhancements, and dependency updates).

Produce a comprehensive report featuring prioritized issues with severity levels, relevant code snippets, proposed fixes with before/after examples, implementation steps, and an updated, prioritized todo list. Ensure all recommendations are verifiable, testable, and tailored to the project's tech stack (Next.js, Prisma, TypeScript), including compatibility with frameworks like React, Node.js, and deployment environments. If further file reads, tool executions (e.g., ESLint, SonarQube, Lighthouse), or external API calls are needed, explicitly list them with justifications.

Additionally, include a summary dashboard with key metrics (e.g., code coverage, cyclomatic complexity, security score), a risk assessment matrix, and suggestions for continuous integration improvements. Propose any necessary architectural changes, such as modularization or microservices adoption, and recommend tools for ongoing monitoring.

Direct all output to a new file named in this exact format: `./look-around/YYYY-MM-DD--HH-MM--{YOUR_MODEL_NAME}`, ensuring the `./look-around` directory is created if absent. Append a timestamp in UTC and use the model identifier (e.g., gpt-4) for {YOUR_MODEL_NAME}.--

---

THEN!!!...

use /speckit and continually make progress on this project:
   2.1 /speckit.constitution - Establish project principles
   2.2 /speckit.specify - Create baseline specification
   2.3 /speckit.plan - Create implementation plan
   2.4 /speckit.tasks - Generate actionable tasks
   2.5 /speckit.implement - Execute implementation

Enhancement Commands - Optional commands that you can use for your specs (improve quality & confidence)
   - /speckit.clarify (optional) - Ask structured questions to de-risk ambiguous areas before planning (run before /speckit.plan if used)
   - /speckit.analyze (optional) - Cross-artifact consistency & alignment report (after /speckit.tasks, before /speckit.implement)
   - /speckit.checklist (optional) - Generate quality checklists to validate requirements completeness, clarity, and consistency (after /speckit.plan)

Be sure to do a git commit at each step!