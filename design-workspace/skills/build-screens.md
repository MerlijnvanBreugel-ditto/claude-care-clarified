# Skill: Build or Update Screens from Design System

## When to use
When creating new screens, updating existing screens, or generating UI mockups in Figma using the write-to-canvas tools.

## Workflow

### Step 1: Understand the target file
Before writing anything, read the existing file structure:
1. Call `get_metadata` on the target file/page to understand layer hierarchy
2. Call `get_variable_defs` to understand the design tokens (colors, spacing, typography)
3. Call `search_design_system` to find available components in connected libraries
4. Call `get_screenshot` on reference frames if adapting an existing style

### Step 2: Plan the structure
Before generating, plan:
- Which existing components to reuse (prefer library components over new ones)
- Which variables to apply (never hardcode colors or spacing if variables exist)
- Auto Layout structure (how frames nest, padding, gap values)
- Responsive behavior intent

### Step 3: Generate
Use `generate_figma_design` or `use_figma` to create the design:
- Start with the outermost frame (device frame / screen container)
- Build top-down: container → sections → components → details
- Apply variables for all colors, spacing, and typography
- Use Auto Layout on every container
- Name every layer semantically

### Step 4: Verify
After generating:
1. Call `get_screenshot` on the created frame to visually verify
2. Check that variables are correctly applied via `get_variable_defs`
3. Fix any issues using `use_figma`

## Rules
- Never hardcode hex colors if a variable exists — use `search_design_system` first
- Always use Auto Layout, never absolute positioning
- Name layers descriptively: "Onboarding / Screen 1 / Option Card" not "Frame 47"
- Group related elements into named frames
- Match existing file conventions (check get_metadata first)
