# /visualize

> Scans the entire pm-workspace, extracts metadata from every file, and generates a single self-contained HTML repo explainer. Shows all capabilities, process flows, integrations, and gaps — shareable via Slack, no setup needed.

## Usage

```
/visualize
```

## What It Does

1. Runs `node scripts/generate-dashboard.mjs`
2. Scans `pm-workspace/` recursively
3. Extracts metadata from every file: title, description, status, TODO markers, references, git author, last modified
4. Enriches with `registry.json` and `backlog.json` data
5. Generates `repo-explainer.html` in the repo root
6. Reports scan results (file counts per category)

## Output

`repo-explainer.html` (repo root) — open in any browser, no server needed. Share via Slack or commit to git.

### Sections

- **Capabilities** — Commands, workflows, and agents as interactive cards with side panel detail view
- **Process Flow** — Visual pipeline: Discover → Refine → Scope → Design → Measure → Ship → Learn
- **Knowledge Base** — Context files, process docs, templates, learnings, specs, research data
- **Integrations** — MCP tool status (configured vs pending)
- **Gaps** — Backlog items and files with unresolved TODOs

### Features

- Click any card → side panel with full details, metadata, and VS Code file links
- Search/filter across all cards
- Info button (top-right) → system overview, rules, anti-patterns
- Light/dark mode toggle
- Mobile-friendly responsive layout
- Zero dependencies — single self-contained HTML file

## $ARGUMENTS

None. Scans the workspace as-is.
