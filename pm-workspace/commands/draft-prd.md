# Draft PRD Command

Generate Product Requirements Documents from discovery insights.

## Usage

```
/draft-prd [feature name]
/draft-prd [feature] --lean
/draft-prd [feature] --comprehensive
/draft-prd [feature] --from=[insights-file]
```

## Description

The `/draft-prd` command generates structured Product Requirements Documents based on discovery insights, user feedback, and competitive analysis. It supports both lean (1-2 page) and comprehensive (5-10 page) formats.

## Options

### Default (Auto-select Format)
```
/draft-prd "OAuth login with Google"
```
Automatically selects format based on feature complexity.

### --lean
```
/draft-prd "Dark mode" --lean
```
Generate a 1-2 page lean PRD focused on problem, solution, and metrics.

### --comprehensive
```
/draft-prd "Real-time collaboration" --comprehensive
```
Generate a full PRD with user stories, edge cases, and technical considerations.

### --from
```
/draft-prd "Search improvements" --from=./data/research/insights-2024-01.md
```
Use specific insights file as input.

### --template
```
/draft-prd "Feature X" --template=rice
/draft-prd "Feature X" --template=jtbd
```
Use specific PRD template (RICE-based, Jobs-to-be-Done, etc.).

### --priority
```
/draft-prd "Critical fix" --priority=P0
```
Set priority level in the PRD.

## PRD Types

### Lean PRD
Best for:
- Small features
- Experiments
- Quick iterations
- Well-understood problems

Includes:
- Problem statement
- Proposed solution
- Success metrics
- Timeline

### Comprehensive PRD
Best for:
- Major features
- New products
- Cross-team initiatives
- Complex requirements

Includes:
- Everything in Lean PRD, plus:
- Detailed user stories
- Acceptance criteria
- Edge cases
- Technical considerations
- Launch plan
- Risks and mitigations

## Output

### Lean PRD Output
```markdown
# PRD: [Feature Name]

**Priority**: P1
**Status**: Draft

## Problem Statement
[What problem we're solving]

## Proposed Solution
[How we'll solve it]

## Success Metrics
| Metric | Target |
|--------|--------|
| [Metric] | [Target] |

## Out of Scope
- [Item]

## Open Questions
- [ ] [Question]
```

### Comprehensive PRD Output
```markdown
# PRD: [Feature Name]

## Document Info
[Metadata table]

## Executive Summary
[Overview]

## 1. Problem Definition
[Detailed problem analysis]

## 2. Solution Overview
[Solution details]

## 3. User Stories & Requirements
[Detailed requirements]

## 4. User Experience
[UX specifications]

## 5. Technical Considerations
[Technical notes and questions]

## 6. Success Metrics
[Metrics and measurement]

## 7. Launch Plan
[Rollout strategy]

## 8. Risks & Mitigations
[Risk analysis]

## 9. Open Questions
[Unresolved items]
```

## Examples

### Simple Feature
```
/draft-prd "Add dark mode toggle" --lean
```

### Complex Feature
```
/draft-prd "Multi-tenant workspace permissions" --comprehensive
```

### From Specific Research
```
/draft-prd "AI-powered search" --from=./insights-synthesis.md
```

### With Priority
```
/draft-prd "Security vulnerability fix" --priority=P0 --lean
```

## $ARGUMENTS

The feature or product to create a PRD for:
- "User authentication with OAuth"
- "Real-time collaboration"
- "Mobile push notifications"
- "API rate limiting"

## Input Sources

The PRD generator pulls from:

1. **Discovery Insights** (primary)
   - `pm-workspace/data/research/insights-*.md`

2. **Competitive Analysis**
   - `pm-workspace/data/competitors/*.md`

3. **User Feedback**
   - `pm-workspace/data/feedback/*.md`

4. **Market Research**
   - `pm-workspace/data/research/market-*.md`

## Output Location

PRDs are saved to:
```
pm-workspace/data/prds/
└── prd-[feature-name]-[date].md
```

## Workflow Integration

After drafting:
1. Review and refine the PRD
2. Share with stakeholders for feedback
3. Update based on feedback
4. Approve and move to wireframe phase

```
/draft-prd → Review → /wireframe → /mockup
```

## Tips

1. **Run discovery first** - Better inputs = better PRDs
2. **Start lean** - Expand to comprehensive if needed
3. **Include quotes** - User feedback adds credibility
4. **Be specific** - Vague PRDs lead to vague products
5. **Iterate** - PRDs evolve as you learn more

## Related Commands

- `/discover` - Run discovery before drafting
- `/wireframe` - Create wireframes from PRD
- `/mockup` - Create visual mockups
