# Orchestration Report Template

Use this template for the final comprehensive report after all phases complete.

---

# Orchestration Report

## Executive Summary

| Field | Value |
|-------|-------|
| **Task** | [Original task description] |
| **Classification** | [feature/bugfix/refactor/security/performance/docs] |
| **Status** | SUCCESS / PARTIAL / FAILED |
| **Agents Used** | [List of agents] |
| **Total Phases** | [N] |
| **Loop-backs** | [N] |
| **Files Modified** | [N] |
| **Tests Added** | [N] |
| **Issues Resolved** | [N] |

---

## Task Analysis

### Original Request
> [Original task description as provided by user]

### Classification Reasoning
[Why this task was classified as X]

### Scope
- [Scope item 1]
- [Scope item 2]
- [Scope item 3]

---

## Phase Results

### Phase 1: [Phase Name]

**Agent(s)**: [agent name(s)]
**Status**: Complete / Partial / Failed
**Duration**: [if available]

**Summary**:
[What was accomplished in this phase]

**Key Outputs**:
- [Output 1]
- [Output 2]

**Issues**:
- [Issue 1]: [Resolution]

---

### Phase 2: [Phase Name]

**Agent(s)**: [agent name(s)] (parallel)
**Status**: Complete / Partial / Failed

**Summary**:
[What was accomplished in this phase]

**Key Outputs**:
- [Output 1]
- [Output 2]

---

[Continue for all phases...]

---

## Quality Gate Results

| Phase | Gate | Result | Iterations | Notes |
|-------|------|--------|------------|-------|
| 2 | Build | PASS | 1 | - |
| 2 | Types | PASS | 1 | - |
| 2 | Tests | PASS | 2 | Required loop-back to tdd-guide |
| 3 | Build | PASS | 1 | - |
| 3 | Types | PASS | 1 | - |
| 3 | Tests | PASS | 1 | - |
| 4 | E2E | PASS | 1 | - |

### Loop-back Details

| Iteration | Phase | Gate | Issue | Resolution |
|-----------|-------|------|-------|------------|
| 1 | 2 | Tests | 3 tests failing | tdd-guide fixed assertion |
| 2 | 2 | Tests | PASS | - |

---

## Files Modified

### Created
| File | Purpose |
|------|---------|
| `path/to/new/file.ts` | [Purpose] |

### Modified
| File | Changes |
|------|---------|
| `path/to/existing/file.ts` | [What changed] |

### Deleted
| File | Reason |
|------|--------|
| `path/to/removed/file.ts` | [Why removed] |

---

## Test Summary

### Unit Tests
- **Added**: [N] new tests
- **Modified**: [N] existing tests
- **Coverage**: [X]%

### Integration Tests
- **Added**: [N] new tests
- **Coverage**: [X]%

### E2E Tests
- **Added**: [N] new tests
- **Critical Paths Covered**: [List]

### Test Results
```
Tests: X passed, Y failed, Z skipped
Coverage: X%
```

---

## Issues Summary

### Resolved Issues

| Severity | Issue | Resolved By | Solution |
|----------|-------|-------------|----------|
| CRITICAL | [Issue] | [Agent] | [How resolved] |
| HIGH | [Issue] | [Agent] | [How resolved] |
| MEDIUM | [Issue] | [Agent] | [How resolved] |

### Remaining Issues

| Severity | Issue | Recommendation |
|----------|-------|----------------|
| LOW | [Issue] | [Suggested action] |

### Issues by Category

```
Security:    [N] found, [N] resolved
Performance: [N] found, [N] resolved
Code Quality:[N] found, [N] resolved
Testing:     [N] found, [N] resolved
```

---

## Security Audit Results

*(If security-reviewer was used)*

| Check | Status | Notes |
|-------|--------|-------|
| Authentication | PASS/WARN/FAIL | [Notes] |
| Authorization | PASS/WARN/FAIL | [Notes] |
| Input Validation | PASS/WARN/FAIL | [Notes] |
| Data Handling | PASS/WARN/FAIL | [Notes] |
| Dependencies | PASS/WARN/FAIL | [Notes] |

---

## Performance Considerations

*(If performance-related agents were used)*

- [Performance consideration 1]
- [Performance consideration 2]
- [Optimization recommendations]

---

## Architecture Decisions

*(If architect was used)*

| Decision | Choice | Alternatives Considered |
|----------|--------|------------------------|
| [Decision area] | [What was chosen] | [Other options] |

---

## Recommendations

### Immediate Actions
1. **[Action 1]**: [Why and how]
2. **[Action 2]**: [Why and how]

### Future Improvements
1. **[Improvement 1]**: [Description]
2. **[Improvement 2]**: [Description]

### Technical Debt
- [ ] [Tech debt item 1]
- [ ] [Tech debt item 2]

---

## Next Steps

### Before Merge
- [ ] Review all changes
- [ ] Run full test suite
- [ ] Manual testing of [specific flows]

### After Merge
- [ ] Monitor [specific metrics]
- [ ] Update [related documentation]
- [ ] Notify [stakeholders]

---

## Final Status

| Criteria | Status |
|----------|--------|
| All phases completed | YES / NO |
| All quality gates passed | YES / NO |
| No CRITICAL issues remaining | YES / NO |
| Tests passing | YES / NO |
| Build successful | YES / NO |

### Verdict

**[SHIP / NEEDS WORK / BLOCKED]**

[Final recommendation and any caveats]

---

## Appendix

### Agent Outputs

<details>
<summary>Planner Output</summary>

[Full planner output]

</details>

<details>
<summary>Architect Output</summary>

[Full architect output]

</details>

[Continue for all agents...]

### Command History

```bash
[List of significant commands run]
```

### Error Logs

```
[Any significant errors encountered]
```

---

*Report generated by meta-orchestrator*
*Agents: [list]*
*Phases: [N]*
*Status: [SUCCESS/PARTIAL/FAILED]*
