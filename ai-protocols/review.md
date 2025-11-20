# Look Around & Review

All AI models and tools should utilize this protocol:

1. When first assisting with this repo. How else are you going to know what this repo is about?
2. Stay up to date on this repo when changes by other AI tools have contributed. You will know this by seeing all the changes inside the `ai-chats` folder!


Execute a comprehensive, multi-stage code review to identify issues, deviations from best practices, security vulnerabilities, performance bottlenecks, and opportunities for optimization. Leverage AI to analyze the codebase holistically, propose targeted improvements, and generate actionable recommendations for tightening and refactoring.

YOU MUST FOLLOW THE DIRECTIONS FROM `./ai-chats/README.md`, including any guidelines on review methodology, tool usage, output formatting, and integration with project workflows.

Incorporate the following previous conversation context as needed to maintain continuity, reference prior analyses, and build upon completed tasks (e.g., project structure review, authentication/security checks, API route examinations, database schema validations, and todo list updates):

Structure the review in phases:
1. Static Analysis (linting, type checking, dependency audits)
2. Dynamic Analysis (runtime behavior, error handling)
3. Security Audit (OWASP checks, input validation)
4. Performance Profiling (code efficiency, bundle size)
5. Best Practices Alignment (code style, accessibility, maintainability), and (6) AI-Driven Refactoring Suggestions (automated code improvements, test generation).

Output a detailed report with prioritized issues, code snippets, proposed fixes, and an updated todo list. Ensure all recommendations are testable and aligned with the project's tech stack (Next.js, Prisma, TypeScript). If additional file reads or tool invocations are required, specify them explicitly.

Put all your of your output to a new file with this format for the name:
`./look-around/YYYY-MM-DD--HH-MM--{YOUR_MODEL_NAME}`
Create './look-around' if it does not exist!



----

# Comprehensive Codebase Review and Enhancement

Execute a thorough, multi-stage code review to detect issues, deviations from best practices, security vulnerabilities, performance bottlenecks, and optimization opportunities. Utilize AI for holistic codebase analysis, targeted improvement proposals, and actionable recommendations for tightening, refactoring, and modernization.

YOU MUST ADHERE TO THE GUIDELINES IN `./ai-chats/README.md`, encompassing review methodology, tool integration, output formatting, and seamless workflow alignment with the project.

Incorporate the following previous conversation context as necessary to ensure continuity, reference prior analyses, and iteratively build upon completed tasks (e.g., project structure assessments, authentication/security validations, API endpoint reviews, database schema audits, and todo list refinements):

Organize the review into the following phases: (1) Static Analysis (linting, type checking, dependency scanning, and code complexity metrics), (2) Dynamic Analysis (runtime behavior simulation, error handling robustness, and integration testing), (3) Security Audit (OWASP Top 10 compliance, input sanitization, authentication mechanisms, and vulnerability scanning), (4) Performance Profiling (code efficiency analysis, bundle size optimization, memory usage, and load testing), (5) Best Practices Alignment (code style consistency, accessibility standards, maintainability scoring, and documentation quality), and (6) AI-Driven Refactoring Suggestions (automated code improvements, test case generation, architectural enhancements, and dependency updates).

Produce a comprehensive report featuring prioritized issues with severity levels, relevant code snippets, proposed fixes with before/after examples, implementation steps, and an updated, prioritized todo list. Ensure all recommendations are verifiable, testable, and tailored to the project's tech stack (Next.js, Prisma, TypeScript), including compatibility with frameworks like React, Node.js, and deployment environments. If further file reads, tool executions (e.g., ESLint, SonarQube, Lighthouse), or external API calls are needed, explicitly list them with justifications.

Additionally, include a summary dashboard with key metrics (e.g., code coverage, cyclomatic complexity, security score), a risk assessment matrix, and suggestions for continuous integration improvements. Propose any necessary architectural changes, such as modularization or microservices adoption, and recommend tools for ongoing monitoring.

Direct all output to a new file named in this exact format: `./look-around/YYYY-MM-DD--HH-MM--{YOUR_MODEL_NAME}`, ensuring the `./look-around` directory is created if absent. Append a timestamp in UTC and use the model identifier (e.g., gpt-4) for {YOUR_MODEL_NAME}.--
