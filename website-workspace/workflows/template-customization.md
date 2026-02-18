# Template Customization Workflow

Create new websites from Framer templates with brand customization.

## Overview

The Template Customization workflow starts with a Framer template and customizes it to match a brand's design system and content needs. This is faster than building from scratch while still achieving brand-consistent results.

## Prerequisites

- Figma file with brand design system (or brand guidelines)
- Selected Framer template
- Content brief or existing content to adapt

## Phase 1: Discovery

Understand the brand and evaluate the template fit.

### Creative Director Task
**Extract and document brand guidelines**

```
Input: Figma file URL or brand guidelines
Output: website-workspace/data/design-system/

Actions:
1. Document color palette with usage rules
2. Define typography scale and hierarchy
3. Catalog component patterns
4. Define spacing system
5. Document brand voice and tone
6. Identify non-negotiable brand elements
```

### Designer Task
**Evaluate template and plan customization**

```
Input: Framer template + brand guidelines
Output: website-workspace/data/projects/[name]/discovery/

Actions:
1. Audit template structure and components
2. Map template tokens to brand tokens
3. Identify customization requirements
4. Estimate customization complexity
5. Flag any template limitations
6. Create customization plan
```

### Phase 1 Deliverables
```
data/
├── design-system/
│   ├── colors.md
│   ├── typography.md
│   ├── components.md
│   └── voice.md
└── projects/[name]/discovery/
    ├── template-audit.md
    ├── token-mapping.md
    ├── customization-plan.md
    └── template-limitations.md
```

---

## Phase 2: Customization

Apply brand tokens and customize components.

### Designer Task
**Apply brand to template**

```
Input: Token mapping + customization plan
Output: website-workspace/data/projects/[name]/design/

Actions:
1. Create token override specifications
2. Define component customizations
3. Specify new sections if needed
4. Document responsive modifications
5. Create animation specifications
```

### Creative Director Task
**Review customization specs**

```
Input: Customization specifications
Output: Approved specs or revision requests

Actions:
1. Verify brand integrity in customizations
2. Check for brand compromises
3. Approve token mappings
4. Approve component modifications
```

### Phase 2 Deliverables
```
data/projects/[name]/design/
├── token-overrides.json
├── component-customizations.md
├── new-sections.md
├── responsive-modifications.md
└── brand-approval.md
```

---

## Phase 3: Content

Create or adapt content for the template structure.

### Copywriter Task
**Create content for template**

```
Input: Template structure + brand voice guide + content brief
Output: website-workspace/data/projects/[name]/copy/

Actions:
1. Write headlines for each section
2. Create body copy that fits template structure
3. Write CTAs for all buttons/links
4. Create form microcopy
5. Write SEO meta content
6. Adapt existing content if provided
```

### Creative Director Task
**Review copy for brand voice**

```
Input: Draft copy
Output: Approved copy or revision requests

Actions:
1. Check voice consistency
2. Verify messaging alignment
3. Review tone appropriateness
4. Approve or request revisions
```

### Phase 3 Deliverables
```
data/projects/[name]/copy/
├── home-copy.md
├── [page]-copy.md
├── microcopy.md
├── seo.md
└── voice-review.md
```

---

## Phase 4: Implementation

Build the customized site in Framer.

### Website Developer Task
**Implement customizations in Framer**

```
Input: Approved design specs + copy
Output: Live Framer site

Actions:
1. Duplicate template to new project
2. Apply token overrides
3. Customize components per spec
4. Add new sections if required
5. Populate all copy
6. Set up CMS if needed
7. Configure SEO
8. Test and optimize
```

### Creative Director Task
**Final brand approval**

```
Input: Staging URL
Output: Final approval or punch list

Actions:
1. Full site review
2. Brand compliance check
3. Cross-device testing
4. Final approval or punch list
```

### Phase 4 Deliverables
```
data/projects/[name]/implementation/
├── token-changes.md
├── component-changes.md
├── cms-setup.md
├── performance.md
└── final-approval.md
```

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 1: DISCOVERY                           │
├─────────────────────────────┬───────────────────────────────────┤
│ Creative Director           │ Designer                          │
│ → Extract brand guidelines  │ → Audit template                  │
│ → Document design system    │ → Map tokens                      │
│                             │ → Create customization plan       │
│                             │                                   │
│ Output: design-system/      │ Output: discovery/                │
└─────────────┬───────────────┴───────────────────┬───────────────┘
              │                                   │
              └─────────────────┬─────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 2: CUSTOMIZATION                        │
├─────────────────────────────────────────────────────────────────┤
│ Designer → Create customization specs                           │
│     ↓                                                           │
│ Creative Director → Review and approve specs                    │
│                                                                 │
│ Output: design/                                                 │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 3: CONTENT                            │
├─────────────────────────────────────────────────────────────────┤
│ Copywriter → Create/adapt copy for template                     │
│     ↓                                                           │
│ Creative Director → Review for brand voice                      │
│                                                                 │
│ Output: copy/                                                   │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 4: IMPLEMENTATION                        │
├─────────────────────────────────────────────────────────────────┤
│ Website Developer → Build customized site                       │
│     ↓                                                           │
│ Creative Director → Final brand approval                        │
│                                                                 │
│ Output: implementation/ + Live site                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Template Evaluation Criteria

When selecting a template, evaluate:

| Criterion | Weight | Questions |
|-----------|--------|-----------|
| Structure Fit | High | Does layout match content needs? |
| Customizability | High | Can brand tokens be applied easily? |
| Component Match | Medium | Do components align with brand patterns? |
| Animation Quality | Medium | Are interactions appropriate for brand? |
| CMS Ready | Medium | Does it support content management needs? |
| Performance | Medium | Is baseline performance acceptable? |

### Template Fit Score

```markdown
## Template Evaluation: [Template Name]

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| Structure Fit | X | [notes] |
| Customizability | X | [notes] |
| Component Match | X | [notes] |
| Animation Quality | X | [notes] |
| CMS Ready | X | [notes] |
| Performance | X | [notes] |

**Total Score**: XX/30
**Recommendation**: [Use / Don't Use / Use with modifications]
**Key Modifications Needed**: [list]
```

---

## Token Mapping Template

```markdown
## Token Mapping: [Template] → [Brand]

### Colors
| Template Token | Template Value | Brand Token | Brand Value |
|----------------|----------------|-------------|-------------|
| --primary | #3B82F6 | primary-500 | #4F46E5 |
| --secondary | #10B981 | secondary-500 | #059669 |
| --background | #FFFFFF | neutral-0 | #FAFAFA |

### Typography
| Template Token | Template Value | Brand Token | Brand Value |
|----------------|----------------|-------------|-------------|
| --font-heading | system-ui | font-heading | Inter |
| --font-body | system-ui | font-body | Inter |

### Spacing
| Template Token | Template Value | Brand Token | Brand Value |
|----------------|----------------|-------------|-------------|
| --space-4 | 16px | spacing-4 | 16px |
| --space-8 | 32px | spacing-8 | 32px |

### Effects
| Template Token | Template Value | Brand Token | Brand Value |
|----------------|----------------|-------------|-------------|
| --radius-md | 8px | radius-md | 12px |
| --shadow-md | [value] | shadow-md | [value] |
```

---

## Checkpoints

### After Phase 1
- [ ] Brand design system documented
- [ ] Template fully audited
- [ ] Token mapping complete
- [ ] Customization plan approved

### After Phase 2
- [ ] All token overrides specified
- [ ] Component customizations defined
- [ ] Creative Director approved specs

### After Phase 3
- [ ] All copy written
- [ ] SEO content complete
- [ ] Creative Director approved copy

### After Phase 4
- [ ] Site built and customized
- [ ] CMS configured (if needed)
- [ ] Performance optimized
- [ ] Final Creative Director approval

---

## Quick Start Commands

```
# Phase 1
@creative-director Extract brand guidelines from [Figma URL]
@designer Audit template at [Framer template URL] against brand in data/design-system/

# Phase 2
@designer Create customization specs for [template] using brand in data/design-system/
@creative-director Review customization specs in data/projects/[name]/design/

# Phase 3
@copywriter Write copy for [template] following structure in data/projects/[name]/design/ and voice in data/design-system/voice.md
@creative-director Review copy in data/projects/[name]/copy/

# Phase 4
@website-developer Build site using specs in data/projects/[name]/design/ and copy in data/projects/[name]/copy/
@creative-director Final review of staging site at [URL]
```
