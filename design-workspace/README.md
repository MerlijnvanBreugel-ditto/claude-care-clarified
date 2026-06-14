# Design Workspace

Workspace for testing Figma MCP write-to-canvas capabilities. Uses the direct Figma remote MCP server to create and modify designs programmatically.

## Setup

### 1. Add the Figma remote MCP server (write access)

The Claude.ai Figma integration is **read-only**. For write-to-canvas, you need the direct remote server.

**Option A: CLI command**
```bash
claude mcp add --scope user --transport http figma-write https://mcp.figma.com/mcp
```

**Option B: Manual JSON config** (`~/.claude/settings.json` or project `.mcp.json`)
```json
{
  "mcpServers": {
    "figma-write": {
      "type": "http",
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

After adding, restart Claude Code. First use will trigger Figma OAuth login.

### 2. Verify setup

Ask Claude to run the `whoami` tool on the figma-write server. It should return your Figma identity and confirm you have a Full or Dev seat on a paid plan.

### 3. Requirements

- Figma account with **Full or Dev seat** on a paid plan
- Write-to-canvas is currently **free during beta** (will become usage-based)
- Dev seats have read-only access outside drafts

## Available Write Tools

| Tool | What it does |
|---|---|
| `use_figma` | General-purpose: create, edit, or inspect any object (frames, components, variables, styles, text, images) |
| `generate_figma_design` | Generate design layers from interfaces — converts descriptions into native Figma objects |
| `search_design_system` | Search connected design libraries for components, variables, and styles |
| `create_new_file` | Create a new blank Figma Design or FigJam file in drafts |

### Read Tools (also available)

| Tool | What it does |
|---|---|
| `get_design_context` | Get code + screenshot + hints for a selection (default: React + Tailwind) |
| `get_variable_defs` | Get variables/styles used in a selection (colors, spacing, typography) |
| `get_metadata` | Sparse XML of layer structure (IDs, names, types, positions) |
| `get_screenshot` | Screenshot of a selection |
| `get_figjam` | Convert FigJam diagrams to XML |
| `generate_diagram` | Create FigJam diagrams from Mermaid syntax |

## Skills

Skills are markdown instructions that teach the agent how to work with your design system. They live in `design-workspace/skills/`.

### Available skills

| Skill | Purpose |
|---|---|
| `build-screens.md` | Create or update screens using your design system components |
| `ditto-design-rules.md` | Ditto-specific design conventions and component usage |

## Rate Limits

- Full/Dev seats on Professional+: standard per-minute REST API limits
- Write operations: currently exempt (beta)
- Starter/View/Collab seats: 6 tool calls/month (read only)

## Best Practices

**File structure matters.** The agent reads your file structure to understand conventions:
- Use components for reusable elements
- Apply variables for spacing, color, radius, typography
- Name layers semantically (not "Group 5" or "Frame 47")
- Use Auto Layout for responsive intent
- Add annotations for complex behaviors

**Prompting tips:**
- Reference specific Figma files by URL
- Point to existing frames as reference: "Use the style of frame X"
- Specify what design system components to use
- For large files, select specific frames rather than the whole page

## Test Log

Track experiments with write-to-canvas here:

| Date | Test | File | Result |
|---|---|---|---|
| — | — | — | — |
