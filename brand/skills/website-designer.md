---
name: website-designer
description: Use when planning website structure, designing pages or sections, writing content briefs, building in Framer, reviewing website content for effectiveness, or planning conversion paths
---

# Website Designer

The homepage is a brand film, not a feature list. Show the life Ditto enables — not the tool itself.

## When to Use

- Planning or restructuring the website
- Designing a new page or section
- Writing content briefs
- Building or modifying pages in Framer
- Reviewing website content for effectiveness

## Before Starting

Read these:
- `brand/strategy/positioning.md` — who we are, what we claim
- `brand/voice-and-tone/brand-voice.md` — voice principles
- `brand/skills/brand-designer.md` — visual identity rules
- `brand/skills/copywriter.md` — copy patterns and quality checks

## Quick Reference

| Decision | Default |
|---|---|
| One page for all audiences? | No. One primary audience per page. |
| Nav items? | Max 5-6. One primary CTA. No jargon. |
| Page opens with? | Emotional hook, not feature list. |
| Section structure? | Headline → subhead → (optional) body → CTA |
| Mobile? | Design mobile-first, verify all breakpoints. |
| Product screenshots? | Only with human context. Never isolated. |

---

## 1. Site Architecture

### Dual-Audience Model

Consumer-first homepage that builds desire. B2B lives one click away but never pollutes the consumer experience.

| Audience | What they need | Where they go |
|---|---|---|
| **Patients & families** | Emotional resonance, understand Ditto, download | Homepage → How it works → Download |
| **Professionals & partners** | Credibility, outcomes data, integration story | For Professionals → Partnership tiers |

### Navigation Rules

- Max 5-6 top nav items. Doesn't earn a spot? Footer.
- One primary CTA in nav. Not two. Not a dropdown.
- No jargon in labels. "How it works" > "Product". "For Professionals" > "Enterprise Solutions".
- Mobile-first nav. Hamburger is fine.

---

## 2. Page Design Patterns

### The Homepage Formula

The homepage is a brand film, not a feature list. Sequence matters.

| Section | Purpose | Pattern | Reference |
|---------|---------|---------|-----------|
| **Hero** | Emotional hook + clarity | Bold headline, one sentence, one CTA, photography or video | Hims: "health feels different now" |
| **Problem** | Make the pain real | Short statement or question. No solution yet. | Ditto deck: "When healthcare gets serious, people are lost" |
| **Solution** | What Ditto does (high level) | 3 pillars max. Visual, not wordy. | Tandem: icon + headline + one line per feature |
| **How it works** | Make it tangible | 3-step visual flow. Screenshots or illustrations. | Polarsteps: plan → track → relive |
| **Social proof** | Build trust | Numbers, logos, quotes. Mix quantitative + qualitative. | Hims: press logos + user count |
| **Differentiator** | Why Ditto, not alternatives | One bold claim. Care Circle section. | Ditto deck: "It's a care circle, not a chatbot" |
| **CTA** | Convert | App store badges + one sentence. | Clean, no distractions |

### The "For Organizations" Page

Different structure. Lead with credibility, end with contact.

| Section | Purpose |
|---------|---------|
| **Hero** | Outcome-focused headline ("Better-informed patients, lower costs") |
| **The opportunity** | Market size, the problem for insurers/providers |
| **What Ditto delivers** | Specific outcomes with data |
| **How it integrates** | Technical credibility without jargon |
| **Social proof** | Partner logos, case study snippets |
| **CTA** | "Let's talk" / contact form |

### Content Page Template (Blog, Stories)

- Hero image (editorial photography, not stock)
- Title + reading time
- Body content (generous whitespace, pull quotes)
- Related content
- CTA back to product

---

## 3. Content Principles

Four rules, each named after a brand that does it well:

| Rule | Principle | For Ditto |
|---|---|---|
| **Polarsteps** | Show the life, not the tool | Families understanding care, sharing with loved ones — not the recording feature |
| **Hims** | Premium consumer, not clinical | Healthcare with consumer brand confidence. Not a patient portal. |
| **Tandem** | Relatable specificity | "Record your visit. Get a summary. Share it with family." Not "AI-powered platform." |
| **Heidi** | Humanity over technology | "AI" appears late, if at all, on consumer pages. Outcomes first. |

### Copy Hierarchy (Every Section)

1. **Headline**: Outcome or emotion. Max 8 words.
2. **Subhead**: The "so what" — one sentence.
3. **Body** (optional): Only if complexity demands it. Max 2-3 sentences.
4. **CTA**: One per section. Verb-first.

---

## 4. Framer Implementation

### Working with Framer MCP

Use the Framer MCP tools for building and modifying the website. Key tools:

| Tool | When to use |
|------|------------|
| `getProjectXml` | Understand current site structure |
| `getNodeXml` | Inspect specific page/component |
| `createPage` | Add new pages |
| `updateXmlForNode` | Modify existing pages/sections |
| `getCMSCollections` / `upsertCMSItem` | Manage blog/content |
| `manageColorStyle` / `manageTextStyle` | Set up design tokens |
| `getComponentInsertUrlAndTypes` | Use existing components |
| `searchFonts` | Find and apply fonts |

### Framer Design Token Setup

Before building pages, ensure the design system is configured:

**Colors** (via `manageColorStyle`):
- Navy: `#0D164F`
- Teal: `#58B6D2`
- Gold: `#D4A832`
- Light Blue: `#7DD4E8`
- Red: `#D94F4F`
- Soft BG: `#F7F6F3`
- White: `#FFFFFF`

**Typography** (via `manageTextStyle`):
- Heading XL: Bricolage Grotesque, 600, 64px, line-height 1.06
- Heading L: Bricolage Grotesque, 600, 46px, line-height 1.14
- Heading M: Bricolage Grotesque, 500, 30px, line-height 1.28
- Body L: Inter, 400, 18px, line-height 1.6
- Body M: Inter, 400, 16px, line-height 1.6
- Label: Inter, 600, 11px, uppercase, letter-spacing 2.5px

### Framer Page Structure Convention

Every page follows this skeleton:

```
Page
├── Nav (shared component)
├── Hero section
├── Content sections (page-specific)
├── CTA section (shared component)
└── Footer (shared component)
```

### Responsive Rules

- **Desktop first** in Framer, but verify mobile breakpoints for every section
- **Hero**: Full-width, min-height 80vh on desktop, auto on mobile
- **Grid sections**: 3-col → 2-col → 1-col responsive
- **Typography**: Scale down headings by ~25% on mobile
- **Photography**: Crop to maintain impact. Don't just shrink.
- **Touch targets**: 44px minimum on mobile

---

## 5. Website Audit Checklist

Run this against any page before publishing.

| # | Check | Pass/Fail |
|---|-------|-----------|
| 1 | **5-second test**: Can a stranger understand what Ditto does? | |
| 2 | **One audience**: Is this page clearly for patients OR for organizations? | |
| 3 | **Emotional hook**: Does the hero make you feel something? | |
| 4 | **Show, don't tell**: Photography/visuals carry emotion, not words? | |
| 5 | **CTA clarity**: Is there one obvious next step? | |
| 6 | **Brand consistency**: Passes the brand-designer visual audit? | |
| 7 | **Copy quality**: Passes the brand-strategist audit? | |
| 8 | **Mobile**: Works and looks great on mobile? | |
| 9 | **Speed**: No unnecessary animations, heavy images optimized? | |
| 10 | **Privacy**: No misleading claims about data? Cookie/privacy compliant? | |

---

## 6. Multi-Perspective Website Review

When reviewing website pages or major changes:

| Perspective | Key Questions |
|---|---|
| **First-time visitor** | Do I understand what this is in 5 seconds? Do I trust it? Would I download? |
| **Patient in crisis** | Does this feel calm and supportive, not salesy? Can I find what I need fast? |
| **Caregiver** | Can I quickly understand how this helps my family member? |
| **Insurer/Partner** | Does this look credible enough to put in front of my board? Can I find the B2B page? |
| **Competitor** | Is there anything here they can't easily copy? |
| **SEO/Growth** | Is the content structured for discoverability? Are CTAs optimized? |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Page tries to serve both patients and professionals | One primary audience per page. Always. |
| Hero leads with features | Hero = emotional hook. Features come after the problem is felt. |
| "Learn more" as CTA | About what? Be specific: "See how it works" / "Download Ditto" |
| Opening with "AI-powered" on consumer pages | Outcome first. AI is the how, not the what. |
| Multiple CTAs competing in one section | One CTA per section. One. |
| Dense text blocks on mobile | Short paragraphs, generous whitespace. If it's a wall, break it up. |
| Screenshots without human context | Show the person using the product, not the product alone. |

## Sources & Influences

- **Hims & Hers** — Consumer health as lifestyle brand. Dual audience handled cleanly.
- **Heidi Health / DixonBaxi** — Healthcare AI with humanity. Technology buried.
- **Polarsteps** — Shows the life, not the tool. Framer-built.
- **Tandem** — Relatable specificity. Names exact pain points.
- **Apple** — Obsessive whitespace. One idea per section.
