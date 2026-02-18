# Replicate Workflow

Migrate existing websites to Framer templates while improving design and copy.

## Overview

The Replicate workflow takes an existing website and migrates it to a Framer template, ensuring brand consistency while allowing for design and copy improvements.

## Prerequisites

- Figma file with brand design system
- URL of existing website to migrate
- Selected Framer template (or template requirements)

## Phase 1: Analysis (Parallel)

Three agents work simultaneously to understand the current state.

### Creative Director Task
**Extract brand guidelines from Figma**

```
Input: Figma file URL
Output: website-workspace/data/design-system/

Actions:
1. Extract color palette with usage guidelines
2. Document typography scale and hierarchy
3. Catalog component library
4. Define spacing system
5. Document brand voice attributes
```

### Designer Task
**Analyze existing site structure**

```
Input: Website URL
Output: website-workspace/data/projects/[name]/analysis/

Actions:
1. Create sitemap of all pages
2. Document page layouts and sections
3. Identify reusable components
4. Screenshot key pages for reference
5. Note responsive breakpoints used
```

### Copywriter Task
**Audit existing copy**

```
Input: Website URL
Output: website-workspace/data/projects/[name]/analysis/

Actions:
1. Inventory all copy by page
2. Assess brand voice consistency
3. Evaluate readability metrics
4. Identify SEO opportunities
5. Note high-performing sections
```

### Phase 1 Deliverables
```
data/
├── design-system/
│   ├── colors.md
│   ├── typography.md
│   ├── components.md
│   └── spacing.md
└── projects/[name]/analysis/
    ├── sitemap.md
    ├── site-structure.md
    ├── copy-inventory.md
    ├── copy-audit.md
    └── screenshots/
```

---

## Phase 2: Mapping

Designer maps existing content to Framer template structure, Creative Director reviews.

### Designer Task
**Map content to Framer template**

```
Input: Analysis outputs + Framer template specs
Output: website-workspace/data/projects/[name]/mapping/

Actions:
1. Match existing sections to template sections
2. Identify gaps (content that won't fit)
3. Identify opportunities (template features not used)
4. Create page-by-page content mapping
5. Define CMS collection requirements
```

### Creative Director Task
**Review mapping for brand fit**

```
Input: Content mapping document
Output: Approved mapping with feedback

Actions:
1. Verify template can express brand
2. Identify where customization is needed
3. Flag any brand compromises
4. Approve or request revision
```

### Phase 2 Deliverables
```
data/projects/[name]/mapping/
├── content-mapping.md
├── template-gaps.md
├── cms-requirements.md
└── brand-review.md
```

---

## Phase 3: Improvement

Copywriter and Designer create improved versions, Creative Director reviews.

### Copywriter Task
**Rewrite and improve all copy**

```
Input: Copy audit + mapping + brand voice guide
Output: website-workspace/data/projects/[name]/copy/

Actions:
1. Rewrite headlines for clarity and impact
2. Improve body copy for persuasion
3. Optimize CTAs for conversion
4. Create microcopy for forms/interactions
5. Write SEO-optimized meta content
6. Create A/B variants for key sections
```

### Designer Task
**Create design overhaul specs**

```
Input: Analysis + mapping + design system
Output: website-workspace/data/projects/[name]/design/

Actions:
1. Extract design tokens for Framer
2. Create page-by-page design specs
3. Define component customizations
4. Specify animations and interactions
5. Document responsive behavior
```

### Creative Director Task
**Review all improvements**

```
Input: Copy drafts + design specs
Output: Approved deliverables or revision requests

Actions:
1. Review copy for brand voice
2. Review design for brand compliance
3. Provide specific, actionable feedback
4. Grant approval for implementation
```

### Phase 3 Deliverables
```
data/projects/[name]/
├── copy/
│   ├── home-copy.md
│   ├── about-copy.md
│   ├── [page]-copy.md
│   ├── variants.md
│   └── seo.md
├── design/
│   ├── tokens.json
│   ├── home-spec.md
│   ├── [page]-spec.md
│   ├── components.md
│   └── animations.md
└── reviews/
    ├── copy-review.md
    └── design-review.md
```

---

## Phase 4: Implementation

Website Developer builds in Framer, Creative Director provides final approval.

### Website Developer Task
**Build in Framer**

```
Input: Approved copy + design specs
Output: Live Framer site

Actions:
1. Set up Framer project structure
2. Import/configure design tokens
3. Build page templates
4. Set up CMS collections
5. Implement components with variants
6. Add animations and interactions
7. Configure SEO settings
8. Optimize performance
9. Test responsive behavior
```

### Creative Director Task
**Final brand review**

```
Input: Staging URL
Output: Final approval or punch list

Actions:
1. Review live site against brand guidelines
2. Check all pages and states
3. Verify copy matches approved versions
4. Test on multiple devices
5. Provide final approval or punch list
```

### Phase 4 Deliverables
```
data/projects/[name]/implementation/
├── plan.md
├── components/
│   └── [component].md
├── cms-schema.md
├── performance.md
├── seo.md
└── final-review.md
```

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 1: ANALYSIS                           │
│                        (Parallel)                               │
├─────────────────┬─────────────────┬─────────────────────────────┤
│ Creative Dir.   │ Designer        │ Copywriter                  │
│ → Brand extract │ → Site analysis │ → Copy audit                │
│                 │                 │                             │
│ Output:         │ Output:         │ Output:                     │
│ design-system/  │ analysis/       │ analysis/copy-*             │
└────────┬────────┴────────┬────────┴─────────────┬───────────────┘
         │                 │                      │
         └────────────────┼──────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 2: MAPPING                            │
├─────────────────────────────────────────────────────────────────┤
│ Designer → Content-to-template mapping                          │
│     ↓                                                           │
│ Creative Director → Brand fit review + approval                 │
│                                                                 │
│ Output: mapping/                                                │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 3: IMPROVEMENT                          │
│                        (Parallel)                               │
├─────────────────────────┬───────────────────────────────────────┤
│ Copywriter              │ Designer                              │
│ → Rewrite all copy      │ → Create design specs                 │
│ → A/B variants          │ → Token extraction                    │
│ → SEO optimization      │ → Animation specs                     │
│                         │                                       │
│ Output: copy/           │ Output: design/                       │
└────────────┬────────────┴──────────────┬────────────────────────┘
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ Creative Director → Review all improvements                     │
│                   → Approve or request revisions                │
│                                                                 │
│ Output: reviews/                                                │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 4: IMPLEMENTATION                        │
├─────────────────────────────────────────────────────────────────┤
│ Website Developer → Build in Framer                             │
│     ↓                                                           │
│ Creative Director → Final brand review + approval               │
│                                                                 │
│ Output: implementation/ + Live site                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Checkpoints

### After Phase 1
- [ ] Design system fully documented
- [ ] Sitemap and structure documented
- [ ] All copy inventoried and audited
- [ ] Screenshots of key pages saved

### After Phase 2
- [ ] Content-to-template mapping complete
- [ ] Gaps and opportunities identified
- [ ] CMS requirements defined
- [ ] Creative Director approved mapping

### After Phase 3
- [ ] All copy rewritten and approved
- [ ] Design specs complete for all pages
- [ ] Animations and interactions defined
- [ ] Creative Director approved all deliverables

### After Phase 4
- [ ] All pages built in Framer
- [ ] CMS populated with content
- [ ] Performance optimized
- [ ] SEO configured
- [ ] Final Creative Director approval

---

## Handoff Template

When transitioning between phases:

```markdown
## Phase [N] → Phase [N+1] Handoff

### Completed Deliverables
- [ ] [Deliverable 1] - [location]
- [ ] [Deliverable 2] - [location]

### Key Decisions Made
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]

### Open Questions for Next Phase
- [Question 1]
- [Question 2]

### Dependencies
- [What next phase needs from this one]

Handoff by: [Agent name]
Date: [Date]
```
