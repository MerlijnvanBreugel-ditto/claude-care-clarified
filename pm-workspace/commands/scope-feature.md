# /scope-feature

> Turns a product idea into a delivery-ready spec with problem statement, impact assessment, multi-perspective review, epic breakdown, and optional Jira ticket creation.

## Usage

```
/scope-feature [feature name or idea reference]
/scope-feature "Care Circle v2 invitation flow"
/scope-feature --from=pm-workspace/specs/ideas/voice-health-checkin.md
```

## What It Does

1. Loads `pm-workspace/context/product-context.md`
2. Reads `pm-workspace/workflows/functional-scoping.md`
3. Checks registry for related artifacts
4. Executes the workflow: Problem → Impact → Spec → Multi-Perspective Review → Tickets → Document
5. Saves spec to `pm-workspace/specs/`
6. Updates registry
7. Optionally pushes to Confluence and creates Jira tickets (asks first)
8. Offers feedback prompt

## $ARGUMENTS

Feature name, idea reference, or file path. Examples:
- "Share summary via WhatsApp"
- "--from=pm-workspace/specs/ideas/care-circle-v2.md"
- "DPMA-1964" (Jira reference)
