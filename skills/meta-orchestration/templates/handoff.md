# Handoff Document Template

Use this template for agent-to-agent communication between orchestration phases.

---

## ORCHESTRATION HANDOFF

### Metadata
- **Phase**: [N] of [Total]
- **From Agent(s)**: [agent name(s)]
- **To Agent(s)**: [agent name(s)]
- **Task**: [original task description]
- **Classification**: [feature/bugfix/refactor/security/performance/docs]

---

### Context Summary

[2-3 sentence summary of what was accomplished in this phase]

---

### Key Decisions Made

| Decision | Rationale |
|----------|-----------|
| [Decision 1] | [Why this choice was made] |
| [Decision 2] | [Why this choice was made] |

---

### Files Modified

| File | Change Type | Description |
|------|-------------|-------------|
| `path/to/file1.ts` | Created/Modified/Deleted | [Brief description] |
| `path/to/file2.ts` | Created/Modified/Deleted | [Brief description] |

---

### Code Changes Summary

```
[Key code changes or patterns introduced]
```

---

### Issues Found

| Severity | Issue | Status |
|----------|-------|--------|
| CRITICAL | [Description] | Resolved/Open |
| HIGH | [Description] | Resolved/Open |
| MEDIUM | [Description] | Resolved/Open |
| LOW | [Description] | Resolved/Open |

---

### Quality Gate Results (if applicable)

| Check | Result | Notes |
|-------|--------|-------|
| Build | PASS/FAIL | [Any notes] |
| Types | PASS/FAIL | [Any notes] |
| Tests | PASS/FAIL | [Any notes] |

---

### Next Phase Requirements

**What the next agent(s) need to do:**

1. [Specific task 1]
2. [Specific task 2]
3. [Specific task 3]

**Important context:**
- [Context item 1]
- [Context item 2]

**Files to focus on:**
- `path/to/important/file1.ts`
- `path/to/important/file2.ts`

---

### Open Questions

- [ ] [Question 1 that needs resolution]
- [ ] [Question 2 that needs resolution]

---

### Recommendations

1. **[Recommendation 1]**: [Details]
2. **[Recommendation 2]**: [Details]

---

### Dependencies/Blockers

- **Blocked by**: [None / list of blockers]
- **Blocks**: [None / list of items this blocks]

---

## Usage Instructions

When creating a handoff document:

1. **Be concise** - Focus on what the next agent needs to know
2. **Be specific** - Include exact file paths and line numbers
3. **Prioritize issues** - CRITICAL/HIGH issues first
4. **Include context** - Don't assume the next agent knows previous context
5. **List action items** - Clear next steps for the receiving agent

## Example Handoff

```markdown
## ORCHESTRATION HANDOFF

### Metadata
- **Phase**: 1 of 5
- **From Agent(s)**: planner
- **To Agent(s)**: architect, tdd-guide
- **Task**: Add OAuth login with Google
- **Classification**: feature

### Context Summary
Created comprehensive implementation plan for OAuth login. Identified 3 main components needed: auth service, OAuth provider integration, and session management. Estimated 5 files to create/modify.

### Key Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use NextAuth.js | Already in project dependencies, well-maintained |
| JWT sessions | Stateless, scalable, matches existing auth pattern |
| Server-side only | Security best practice, no client-side tokens |

### Files Modified
| File | Change Type | Description |
|------|-------------|-------------|
| `docs/PLAN.md` | Created | Implementation plan document |

### Issues Found
| Severity | Issue | Status |
|----------|-------|--------|
| MEDIUM | Existing auth may conflict | Open - needs architect review |

### Quality Gate Results
N/A - Planning phase only

### Next Phase Requirements
**architect**: Design the auth architecture based on the plan
**tdd-guide**: Write tests for OAuth flow before implementation

**Important context:**
- NextAuth.js is already installed
- Existing session handling in `lib/session.ts`

**Files to focus on:**
- `lib/auth.ts`
- `app/api/auth/[...nextauth]/route.ts`

### Open Questions
- [ ] Should we support multiple OAuth providers immediately or just Google first?

### Recommendations
1. **Start with Google only**: Add GitHub later to reduce complexity
2. **Add rate limiting**: Prevent OAuth callback spam
```
