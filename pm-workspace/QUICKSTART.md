# Mewtwo — Quick Start

## Setup Checklist

### 1. Fill Product Context
Open `pm-workspace/context/product-context.md` and fill in all `[TODO]` sections:
- North star metric
- Technical stack details
- Team structure
- Current strategic priorities (update quarterly)

### 2. MCP Integrations
These should be configured in your Claude Code environment:

- **Atlassian** (Jira + Confluence): `https://mcp.atlassian.com/v1/sse`
- **Mixpanel**: `https://mcp-eu.mixpanel.com/mcp`
- **Figma**: `https://mcp.figma.com/mcp`
- **Stitch**: `https://stitch.googleapis.com/mcp`
- **NotebookLM**: Already configured

---

## Daily Usage

### Workflows

```
"Let's refine this idea: [idea]"           → /refine-idea
"Scope this feature: [feature]"            → /scope-feature
"Create mockups for [feature]"             → /mockup
"Periodic review — what needs attention?"  → /review
"Review this spec from all angles"         → /review [spec]
```

### Proactive Discovery

```
"What have you noticed while we've been working?"
"Any patterns in recent learnings?"
"Show me the backlog"
```

### Feedback

Mewtwo asks after each workflow. You can also give feedback anytime:
```
"Feedback: the edge cases section was too generic"
"You're being too verbose — tighten up"
"That was perfect, keep doing that"
```

---

## Directory Structure

```
pm-workspace/
├── QUICKSTART.md       → This file
├── context/            → Product context, strategy docs
├── workflows/          → Workflow definitions
├── agents/             → Specialist agents (product-designer, user-researcher)
├── commands/           → Slash command definitions
├── specs/              → Working specifications
│   └── ideas/          → Refined product ideas
├── registry/           → Live index of all artifacts
├── learnings/          → Self-reflection logs
├── backlog/            → Mewtwo's observation backlog
├── templates/          → Document templates
├── data/               → Research, mockups, references
└── archive/            → Previous versions
```

## Evolution

This system starts lean. It gets smarter through:
1. **Your feedback** → Learnings → Workflow improvements
2. **Usage patterns** → Mewtwo notices what works and proposes improvements
3. **New workflows** → Added as needed, not in advance

Start with one workflow, battle-test it, refine it, then expand.
