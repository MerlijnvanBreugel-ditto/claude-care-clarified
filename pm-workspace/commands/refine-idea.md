# /refine-idea

> Takes a raw idea, scores it with RISCE, validates the problem, and outputs a structured backlog item ready for prioritization. Supports single ideas, batches, and strategic themes.

## Usage

```
/refine-idea [idea or batch description]
/refine-idea "Care Circle push notifications for family members"
/refine-idea batch: [list of backlog items or Jira filter]
```

## What It Does

1. Loads `pm-workspace/context/product-context.md`
2. Reads `pm-workspace/workflows/product-idea-refinement.md`
3. Checks registry for related artifacts
4. Executes the workflow: Capture → Validate → Score → Refine → Place → Document
5. Saves refined ideas to `pm-workspace/specs/ideas/`
6. Updates registry and backlog
7. Offers feedback prompt

## $ARGUMENTS

Raw idea, batch of ideas, strategic theme, or Jira reference. Examples:
- "Voice health check-in reminders"
- "batch: review our 5 lowest-scored backlog items"
- "theme: what could improve activation?"
