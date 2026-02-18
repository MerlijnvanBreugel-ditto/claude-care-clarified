# Website Workspace

A specialized workspace for website generation and maintenance, with agents for brand consistency, design, copy, and Framer implementation.

## Agents

| Agent | Role | Primary Tools |
|-------|------|---------------|
| **Creative Director** | Brand guardian ensuring Figma design system compliance | Figma MCP |
| **Designer** | Creates Framer-compatible visual design specifications | Figma MCP, WebSearch |
| **Copywriter** | Writes and reviews website copy | WebSearch, WebFetch |
| **Website Developer** | Implements designs in Framer | Figma MCP, Bash |

## Workflows

### 1. Replicate Workflow
Migrate existing websites to Framer templates while maintaining brand consistency.

**Phases:**
1. **Analysis** (Parallel) - Extract brand guidelines, analyze site structure, audit copy
2. **Mapping** - Map content to Framer template structure
3. **Improvement** - Rewrite copy, create design overhaul specs
4. **Implementation** - Build in Framer, final brand review

### 2. Template Customization Workflow
Create new projects from Framer templates with brand customization.

**Phases:**
1. **Discovery** - Understand brand, select template
2. **Customization** - Apply brand tokens, customize components
3. **Content** - Create/adapt copy for template
4. **Implementation** - Build and configure in Framer

## Directory Structure

```
website-workspace/
├── README.md
├── agents/
│   ├── creative-director.md   # Brand guardian
│   ├── designer.md            # Design specs
│   ├── copywriter.md          # Copy creation/review
│   └── website-developer.md   # Framer implementation
├── data/
│   ├── design-system/         # Figma brand reference docs
│   ├── templates/             # Framer template specs
│   ├── projects/              # Per-project working directories
│   └── references/            # Brand voice, Framer patterns
└── workflows/
    ├── replicate-workflow.md
    └── template-customization.md
```

## Project Output Structure

Each project generates output in `data/projects/[project-name]/`:

```
data/projects/[project-name]/
├── analysis/        # Site audit, sitemap, copy inventory
├── mapping/         # Content-to-template mapping
├── copy/            # Page-by-page copy drafts
├── design/          # Design specs, component overrides
└── implementation/  # Framer structure, CMS schema
```

## Quick Start

1. **Start a Replicate project:**
   ```
   @creative-director Extract brand guidelines from [Figma URL]
   ```

2. **Analyze existing site:**
   ```
   @designer Analyze site structure at [URL]
   ```

3. **Audit copy:**
   ```
   @copywriter Audit copy at [URL] for brand voice consistency
   ```

4. **Implement in Framer:**
   ```
   @website-developer Build [page] using specs in data/projects/[name]/design/
   ```

## Integration

These agents work best in sequence following the Replicate or Template Customization workflow. The Creative Director has final approval authority on all deliverables to ensure brand consistency.
