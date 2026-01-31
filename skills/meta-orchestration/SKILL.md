---
name: meta-orchestration
description: Configuration and documentation for the self-orchestrating meta-agent system. Provides agent pool documentation, parallel execution rules, and orchestration configuration.
---

# Meta-Orchestration Skill

This skill provides the configuration, templates, and documentation for the self-orchestrating meta-agent system.

## Overview

The meta-orchestration system enables autonomous task handling by:
- Classifying tasks automatically
- Selecting appropriate specialized agents
- Building dependency graphs
- Executing agents in parallel phases
- Implementing quality gates
- Generating comprehensive reports

## Configuration Schema

### Orchestration Config

```yaml
meta-orchestration:
  # Maximum loop-back iterations for quality gate failures
  max_iterations: 3

  # Quality gate checks
  quality_gates:
    build: true
    types: true
    tests: true

  # Build commands (customize per project)
  commands:
    build: "npm run build"
    types: "npx tsc --noEmit"
    tests: "npm test"
    e2e: "npx playwright test"

  # Default agents by task category
  workflows:
    feature:
      - planner
      - architect
      - tdd-guide
      - code-reviewer
      - security-reviewer
      - e2e-runner
      - doc-updater
    bugfix:
      - planner
      - tdd-guide
      - code-reviewer
      - build-error-resolver
    refactor:
      - architect
      - code-reviewer
      - refactor-cleaner
      - tdd-guide
    security:
      - security-reviewer
      - code-reviewer
      - architect
    performance:
      - architect
      - database-reviewer
      - code-reviewer
    docs:
      - planner
      - doc-updater
```

## Agent Pool

### Available Agents

| Agent | Description | Tools | Model |
|-------|-------------|-------|-------|
| `planner` | Creates implementation plans | Read, Grep, Glob | opus |
| `architect` | Designs system architecture | Read, Grep, Glob | opus |
| `tdd-guide` | Test-driven development | Read, Write, Edit, Bash | sonnet |
| `code-reviewer` | Code quality review | Read, Grep, Glob | sonnet |
| `security-reviewer` | Security audit | Read, Grep, Glob | opus |
| `database-reviewer` | Database/query review | Read, Grep, Glob | sonnet |
| `e2e-runner` | End-to-end tests | Read, Bash | sonnet |
| `refactor-cleaner` | Code cleanup | Read, Write, Edit | sonnet |
| `build-error-resolver` | Fix build errors | Read, Write, Edit, Bash | sonnet |
| `doc-updater` | Documentation updates | Read, Write, Edit | sonnet |

### Agent Capabilities

```
planner:
  - Analyze requirements
  - Create implementation plans
  - Identify dependencies and risks
  - Suggest implementation order

architect:
  - Design system architecture
  - Create component diagrams
  - Define interfaces and contracts
  - Evaluate design trade-offs

tdd-guide:
  - Write tests first
  - Implement code to pass tests
  - Ensure 80%+ coverage
  - Handle edge cases

code-reviewer:
  - Review code quality
  - Check for patterns and anti-patterns
  - Suggest improvements
  - Verify readability

security-reviewer:
  - Audit for vulnerabilities
  - Check authentication/authorization
  - Verify data handling
  - OWASP compliance

database-reviewer:
  - Review queries for performance
  - Check schema design
  - Validate indexes
  - Identify N+1 queries

e2e-runner:
  - Execute Playwright tests
  - Verify user flows
  - Check critical paths
  - Report failures

refactor-cleaner:
  - Remove dead code
  - Improve naming
  - Reduce duplication
  - Simplify complexity

build-error-resolver:
  - Fix compilation errors
  - Resolve type errors
  - Handle missing dependencies
  - Fix configuration issues

doc-updater:
  - Update README
  - Document APIs
  - Create usage examples
  - Maintain changelogs
```

## Parallel Execution Rules

### Dependency Graph

```
Phase 1: planner
    │
    ├── No dependencies
    │
    ▼
Phase 2: architect + tdd-guide
    │
    ├── Both depend on planner
    ├── Independent of each other → PARALLEL
    │
    ▼
Phase 3: code-reviewer + security-reviewer + database-reviewer
    │
    ├── All depend on tdd-guide (need code to review)
    ├── Independent of each other → PARALLEL
    │
    ▼
Phase 4: e2e-runner + refactor-cleaner + build-error-resolver
    │
    ├── Depend on reviewers
    ├── Independent of each other → PARALLEL
    │
    ▼
Phase 5: doc-updater
    │
    ├── Depends on all previous phases
    └── Always runs last
```

### Execution Matrix

| Agent | Depends On | Can Run With |
|-------|-----------|--------------|
| planner | - | - |
| architect | planner | tdd-guide |
| tdd-guide | planner/architect | architect |
| code-reviewer | tdd-guide | security-reviewer, database-reviewer |
| security-reviewer | tdd-guide | code-reviewer, database-reviewer |
| database-reviewer | tdd-guide | code-reviewer, security-reviewer |
| e2e-runner | reviewers | refactor-cleaner, build-error-resolver |
| refactor-cleaner | reviewers | e2e-runner, build-error-resolver |
| build-error-resolver | tdd-guide | e2e-runner, refactor-cleaner |
| doc-updater | all | - |

### Parallel Execution Pattern

To execute agents in parallel, spawn them in a single message:

```markdown
I will now spawn Phase 2 agents in parallel.

[Task call: architect with context from planner]
[Task call: tdd-guide with context from planner]
```

**Critical**: Both Task tool calls must be in the same assistant message to achieve true parallelism.

## Quality Gates

### Gate Configuration

```yaml
quality_gates:
  build:
    command: "npm run build"
    on_failure: build-error-resolver
    max_retries: 3

  types:
    command: "npx tsc --noEmit"
    on_failure: tdd-guide
    max_retries: 3

  tests:
    command: "npm test"
    on_failure: tdd-guide
    max_retries: 3

  e2e:
    command: "npx playwright test"
    on_failure: e2e-runner
    max_retries: 2
```

### Gate Execution

1. Run command
2. If success → proceed to next phase
3. If failure:
   - Increment retry counter
   - If retries < max → spawn recovery agent
   - If retries >= max → report failure and stop

## Task Classification Rules

### Keyword Matching

```javascript
const classificationRules = {
  feature: ['add', 'implement', 'create', 'build', 'new', 'integrate', 'support'],
  bugfix: ['fix', 'bug', 'broken', 'error', 'issue', 'crash', 'wrong', 'fails'],
  refactor: ['refactor', 'clean', 'reorganize', 'restructure', 'improve', 'simplify'],
  security: ['security', 'auth', 'password', 'audit', 'vulnerability', 'encrypt', 'token'],
  performance: ['slow', 'performance', 'database', 'optimize', 'speed', 'latency', 'cache'],
  docs: ['docs', 'document', 'readme', 'comment', 'explain', 'guide']
};

const priority = ['security', 'bugfix', 'feature', 'performance', 'refactor', 'docs'];
```

### Classification Algorithm

1. Lowercase task description
2. Extract words
3. Match against each category's keywords
4. If multiple matches, use priority order
5. If no matches, default to 'feature'

## Handoff Protocol

Between phases, agents communicate via handoff documents.

### Handoff Location

Handoffs are passed as context in the Task tool prompt, not as files.

### Handoff Contents

See `templates/handoff.md` for the full template.

Key sections:
- Phase completed
- Context summary
- Key decisions
- Files modified
- Issues found
- Next phase requirements

## Report Generation

After all phases complete, generate a comprehensive report.

### Report Location

The report is output as the final response, not saved to a file.

### Report Contents

See `templates/report.md` for the full template.

Key sections:
- Summary
- Phase results
- Quality gate results
- Files modified
- Issues resolved
- Remaining issues
- Recommendations

## Error Handling

### Agent Failure

```
if agent_fails:
    log_error()
    if retries < max_retries:
        retry_agent()
    else:
        skip_agent()
        note_in_report()
        continue_if_possible()
```

### Quality Gate Failure

```
if gate_fails:
    if iterations < max_iterations:
        spawn_recovery_agent()
        rerun_gate()
    else:
        generate_failure_report()
        stop_execution()
```

### Unknown Classification

```
if no_keyword_match:
    classification = 'feature'
    note_uncertainty_in_report()
```

## Best Practices

1. **Use --dry-run first** for complex tasks
2. **Provide detailed task descriptions** for better classification
3. **Let the orchestrator parallelize** - don't force sequential
4. **Trust quality gates** - they prevent broken code
5. **Review the final report** - it contains important recommendations

## Templates

- `templates/handoff.md` - Agent-to-agent handoff document
- `templates/report.md` - Final orchestration report

## Related

- `/auto` command - Invokes the meta-orchestrator
- `/orchestrate` command - Manual sequential orchestration
- `meta-orchestrator` agent - The orchestrator itself
