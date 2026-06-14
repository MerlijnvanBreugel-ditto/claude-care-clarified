# Brookflow — PM Workspace

Brookflow's working directory. All product management artifacts live here.

## Structure

```
pm-workspace/
├── QUICKSTART.md            # How to use Brookflow
├── context/                 # Product context, strategy docs, business docs
│   ├── product-context.md   # Foundation doc (update quarterly)
│   └── *.pdf                # Brand positioning, Care Circle docs
├── workflows/               # Workflow definitions
│   ├── functional-scoping.md
│   └── product-idea-refinement.md
├── agents/                  # Specialist agents (dispatched by Brookflow)
│   ├── product-designer.md  # Figma + Stitch + expert panel
│   └── user-researcher.md   # NotebookLM queries
├── commands/                # Slash commands
│   ├── refine-idea.md       # /refine-idea
│   ├── scope-feature.md     # /scope-feature
│   ├── mockup.md            # /mockup
│   └── review.md            # /review
├── specs/                   # Working specifications
│   └── ideas/               # Refined product ideas
├── registry/                # Live artifact index
│   └── registry.json
├── learnings/               # Self-reflection logs
├── backlog/                 # Brookflow's observation backlog
│   └── backlog.json
├── templates/               # Document templates
├── data/                    # Research, mockups, references, design system
└── archive/                 # Previous versions
```

## Commands

| Command | Workflow | What It Does |
|---------|----------|--------------|
| `/refine-idea` | Product Idea Refinement | Shape raw ideas into scored backlog items |
| `/scope-feature` | Functional Scoping | Turn ideas into delivery-ready specs + Jira tickets |
| `/mockup` | Product Designer agent | Generate 3 design directions with expert panel review |
| `/review` | Periodic / Multi-Perspective | Review backlog, registry, learnings — or stress-test an artifact |

## Integrations

- **Atlassian**: Jira tickets + Confluence pages via MCP
- **NotebookLM**: User research queries via user-researcher agent
- **Figma**: Design system extraction via product-designer agent
- **Stitch**: Mockup generation via product-designer agent
- **Mixpanel**: Analytics data (when configured)
