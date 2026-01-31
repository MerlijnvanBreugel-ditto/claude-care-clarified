# Auto Command

Self-orchestrating workflow that automatically analyzes tasks, selects appropriate agents, and executes them with optimal parallelization.

## Usage

```
/auto [task-description]
/auto --dry-run [task-description]
/auto --skip=agent1,agent2 [task-description]
/auto --agents=agent1,agent2,agent3 [task-description]
```

## Description

The `/auto` command invokes the meta-orchestrator agent to autonomously handle complex tasks. It:

1. **Classifies** the task (feature, bugfix, refactor, security, performance, docs)
2. **Selects** appropriate agents based on classification
3. **Builds** a dependency graph for optimal execution order
4. **Executes** agents in phases, running independent agents in parallel
5. **Validates** with quality gates between phases
6. **Reports** comprehensive results at the end

## Options

### --dry-run
Show the execution plan without actually running any agents.

```
/auto --dry-run "Add user authentication"
```

Output shows:
- Task classification
- Selected agents
- Execution phases
- Expected workflow

### --skip=agents
Skip specific agents from the workflow.

```
/auto --skip=security-reviewer,e2e-runner "Add a simple utility function"
```

### --agents=agents
Override automatic agent selection with a custom list.

```
/auto --agents=planner,tdd-guide,code-reviewer "Quick feature implementation"
```

### --max-iterations=N
Set maximum loop-back iterations for quality gate failures (default: 3).

```
/auto --max-iterations=5 "Complex feature with expected issues"
```

### --no-quality-gates
Skip quality gate checks between phases (not recommended).

```
/auto --no-quality-gates "Prototype feature"
```

## Task Classification

The orchestrator automatically classifies tasks:

| Category | Keywords | Default Workflow |
|----------|----------|------------------|
| feature | add, implement, create, build, new | planner → architect + tdd-guide → reviewers → e2e-runner → doc-updater |
| bugfix | fix, bug, broken, error, issue | planner → tdd-guide → code-reviewer → build-error-resolver |
| refactor | refactor, clean, reorganize | architect → code-reviewer → refactor-cleaner → tdd-guide |
| security | security, auth, password, audit | security-reviewer → code-reviewer → architect |
| performance | slow, performance, database | architect → database-reviewer → code-reviewer |
| docs | docs, document, readme | planner → doc-updater |

## Examples

### Feature Implementation
```
/auto "Add OAuth login with Google and GitHub providers"
```

Executes:
1. Planner creates implementation plan
2. Architect designs auth architecture + TDD Guide writes tests (parallel)
3. Code Reviewer + Security Reviewer audit implementation (parallel)
4. E2E Runner verifies user flows
5. Doc Updater updates documentation

### Bug Fix
```
/auto "Fix login button not responding on mobile"
```

Executes:
1. Planner analyzes the bug
2. TDD Guide writes regression test and fix
3. Code Reviewer validates the fix
4. Build Error Resolver handles any build issues

### Security Audit
```
/auto "Security audit of payment processing"
```

Executes:
1. Security Reviewer performs comprehensive audit
2. Code Reviewer validates security patterns
3. Architect reviews system design for vulnerabilities

### Refactoring
```
/auto "Refactor user service to use repository pattern"
```

Executes:
1. Architect designs new structure
2. Code Reviewer validates approach
3. Refactor Cleaner performs the refactoring
4. TDD Guide ensures tests pass

### Documentation
```
/auto "Document the API endpoints"
```

Executes:
1. Planner outlines documentation structure
2. Doc Updater creates/updates documentation

## Quality Gates

Between phases, the orchestrator runs:

1. **Build Check**: `npm run build`
2. **Type Check**: `npx tsc --noEmit`
3. **Test Check**: `npm test`

If a gate fails:
- Loops back to the appropriate agent
- Maximum 3 iterations per gate
- Reports failure if max iterations exceeded

## Parallel Execution

Agents without dependencies run in parallel:

```
Phase 2: architect + tdd-guide (parallel)
    ↓
Phase 3: code-reviewer + security-reviewer + database-reviewer (parallel)
    ↓
Phase 4: e2e-runner + refactor-cleaner + build-error-resolver (parallel)
```

This significantly reduces total execution time.

## Output

### During Execution
Progress updates for each phase:
```
[Phase 1/5] Running: planner
[Phase 1/5] Complete: planner

[Phase 2/5] Running: architect, tdd-guide (parallel)
[Phase 2/5] Complete: architect, tdd-guide

[Quality Gate] Build: PASS | Types: PASS | Tests: PASS

[Phase 3/5] Running: code-reviewer, security-reviewer (parallel)
...
```

### Final Report
Comprehensive summary including:
- Task classification
- Agents used and their outputs
- Files modified
- Quality gate results
- Issues found and resolved
- Recommendations

## $ARGUMENTS

The task description to be orchestrated. Can include any combination of:
- Feature descriptions
- Bug reports
- Refactoring requests
- Security audit requests
- Performance optimization requests
- Documentation tasks

## Tips

1. **Use --dry-run first** for complex tasks to verify the plan
2. **Be descriptive** - more context leads to better agent selection
3. **Use --skip** for tasks where certain agents aren't needed
4. **Use --agents** for custom workflows
5. **Trust the orchestrator** - it handles parallelization and quality gates automatically

## Troubleshooting

### "Unknown task type"
The orchestrator defaults to `feature` workflow. Use `--agents` for custom workflows.

### "Max iterations exceeded"
Quality gate failed repeatedly. Check the report for specific errors and fix manually.

### "Agent failed"
An agent encountered an error. Check the agent's output in the report.

## Related Commands

- `/orchestrate` - Manual sequential agent workflow
- `/plan` - Planning only (no execution)
- `/code-review` - Code review only
- `/tdd` - TDD workflow only
