# Website Feedback & Critical Analysis

**Date**: 2026-03-26
**Sources**: MCO-95 (Jira epic), team feedback session (Mar 16), Framer draft, current live site

---

## Part 1: Team Feedback (from MCO-95)

### Full-Team Feedback Session (Mar 16)

The session resulted in a complete rebuild plan across 11 workstreams. The core verdict: the Framer draft's structure doesn't work, the narrative isn't convincing, and the visual style needs a direction shift.

### Structural Feedback

**Homepage structure is wrong.** The team agreed on a new section order following StoryBrand:

1. Hero → 2. Problem cards → 3. Product showcase (scroll-and-scrub) → 4. Social proof → 5. USPs → 6. Narrative video → 7. Closing CTA

Key changes from current draft:
- **Problem before solution** — current draft jumps to features too fast
- **Care Circle woven into product showcase** — not a separate section
- **Narrative video as emotional closer** — "The Story Behind the Summary", full-width, no UI chrome
- **Single closing CTA** — not scattered CTAs throughout
- **Homepage FAQ reduced to 3-4 questions** — full FAQ moves to Help & Contact page

**Navigation is broken on desktop.** Hamburger menu on desktop is unacceptable. New nav: Home | For Professionals | About | Privacy & AI | Help & Contact. All visible, no hamburger.

**"For Professionals" is invisible.** Doctors landing on the consumer page can't find the pro page. Fix: persistent top bar ("Are you a healthcare professional?"), button in hero, contrasting nav item. One-click access required.

**Partners page shouldn't exist standalone.** Embed in Professionals page with clickable deep-dive sub-pages per partner. Three tiers: promotional, research, guided pilots.

### Copy Feedback

**Headline direction undecided.** Three candidates:
- Social/family angle ("Care is something you carry together")
- Confidence/control angle
- Innovation angle

**Current draft copy is wrong in multiple places:**
- Factually wrong on the professionals page
- Tonally wrong — marketing fluff where precision is needed
- Typos: "Wether", "afterevery", broken sentences, duplicate text
- FAQ written in third person — should be first person ("We")

**Professionals page copy must be completely rewritten.** Doctors need credibility in 30 seconds: research references, HCP testimonials (NOT patient testimonials), "Talk to a fellow doctor" CTA.

### Visual Feedback

**Beige/cream backgrounds need to go.** Direction: blue-yellow gradient with grain texture (from the app), more whitespace, white cards with glass/opacity effect, dark blue text.

**Typography decision pending.** Test Bricolage Grotesque in 2-3 app screens before committing site-wide.

**Product mockups are too small.** Phone mockups must be full-screen and readable — users should be able to read the actual UI text.

### Niek's Feedback (Feb 20)

- Add press section to footer for journalist access
- Set up a press email address
- Add press mentions higher up the page for trust
- Add actual demo for professionals (not just a "Schedule Demo" link)

### Bug/Polish Items

- Logo not clickable
- No close button on medical advisor popup
- "Schedule Demo" appears on consumer pages (should be pro-only)
- Press/partner logos not clickable, shown at reduced opacity
- Inconsistent button icons and icon styles
- Broken chat widget
- Text contrast issues on beige cards
- Heading hierarchy inconsistent
- Missing App Store + Google Play badges
- Duplicate testimonial (Jacky appears twice)

---

## Part 2: Critical Analysis — Current Live Site (dittocare.com)

### What It Gets Right
- "Care. Clarified." tagline is strong
- Privacy-first messaging is present
- Press logos provide initial trust
- The three pillars (record/understand/share) are clear feature anchors

### What's Fundamentally Wrong

**It tells the wrong story.** The site says "we're a medical recording app." The brand strategy says "we're the consumer layer in healthcare." These are completely different companies. The live site undersells Ditto by an order of magnitude.

**No emotional dimension.** The site describes features. It never makes you *feel* anything. No family moments, no relief after a confusing diagnosis, no "I finally understood what the doctor said." The consumer deck has this in spades — the website has none of it.

**Feature-led, not outcome-led.** "Record your consultation and receive a summary" is a feature. "Never leave a doctor's appointment confused again" is an outcome. The site leads with features every time.

**38 pages of chaos.** Duplicate pages, blank pages, dead campaign pages, mixed Dutch/English, vacancy pages on the marketing site. No information architecture — just accumulated Wix pages.

**B2B is an afterthought.** A single "Healthcare partners" page with weak narrative. No research references, no clinical validation, no "talk to a doctor" CTA. A skeptical doctor would close the tab in 10 seconds.

**Generic mission.** "Everyone deserves clarity and control over their own health" — swap "Ditto" for any health app name and it still works. Fails the Onlyness test completely.

**"Free" leads the value proposition.** Saying "free" first signals low value. The product should feel so valuable that free is a surprise, not the headline.

---

## Part 3: Critical Analysis — Framer Draft (fulfilled-screen-670844.framer.app)

### What It Gets Right
- Moving to Framer is the right platform choice
- "Care is something you carry together" is a stronger emotional opening than the live site
- The 4-step flow (Capture → Clarify → Connect → Stay Connected) is a better structure than the live site's feature list
- Social proof numbers are present (4.9/5 professionals, 4.7/5 users, 60K downloads)
- Bilingual (NL/EN) setup exists

### What's Still Wrong

**The narrative arc is broken.** The draft goes: Hero → "healthcare feels overwhelming" → "feel confident" → testimonials → how it works → FAQ. This is:
- Solution before problem (hero promises before establishing pain)
- Features in the wrong place (how-it-works appears late, after testimonials)
- No emotional climax (testimonials are mid-page filler, not a crescendo)
- FAQ dominates the bottom (7 questions — this is a support page, not a homepage)

**The hero is soft.** "Care is something you carry together" is a nice sentiment, but it's abstract. What does it *mean*? A first-time visitor still doesn't know what Ditto does. Compare: "You talk to your doctor. We make sure you remember." — that's concrete. The subheadline ("Ditto turns any medical conversations into clear summaries") does the work, but it's the secondary text.

**"When healthcare feels overwhelming" is a vague section.** It names the right emotion but doesn't make it real. The consumer deck does this brilliantly — "WhatsApp groups. Phone calls. Shared Google Docs. One family member who becomes the unofficial project manager." That's vivid. The Framer draft just says "GP visits, specialist appointments, midwife consultations" — a list of settings, not a pain story.

**Care Circle is invisible.** The biggest differentiator — the thing that separates Ditto from every health AI chatbot — is buried in step 3 of a 4-step flow as "Invite loved ones to follow your updates." That's a feature bullet, not a brand story. The deck's "It's a care circle, not a chatbot" framing is completely absent.

**"Schedule Demo" on the consumer page.** Consumers don't schedule demos. This CTA leaked from the B2B page.

**The professionals page is factually and tonally wrong.** The team flagged this themselves — it needs a complete rebuild. Doctors need research, evidence, and peer credibility. Not marketing copy.

**Visual direction needs work.** Beige/cream backgrounds feel dated, not premium. The team already decided to shift toward blue-yellow gradient with grain texture. Phone mockups are too small to read.

**Desktop hamburger menu.** On a desktop viewport, hiding navigation behind a hamburger is a UX anti-pattern. The team already flagged this.

---

## Part 4: The Gap Between Deck and Website

This is the most important observation. The consumer deck tells a compelling, emotionally resonant story:

| Deck says | Website says |
|-----------|-------------|
| "The Consumer Layer in Healthcare" | "Clear summaries of medical conversations" |
| "When healthcare gets serious, people are lost, overwhelmed, and feel alone" | "When healthcare feels overwhelming" (vague) |
| "It's a care circle, not a chatbot" | Care Circle is step 3 of 4 |
| "WhatsApp groups. Phone calls. Shared Google Docs." | (not present) |
| "Different people need different things" (partner, child, parent, friend) | "Share with loved ones" (generic) |
| "Everyone is building personal health AI. None are building the social layer." | (not present) |
| "Five layers of moat" | (not present) |
| 75,000 users | 60,000 downloads |
| Photography-forward, editorial, film-grain | Beige backgrounds, small mockups |

The deck is the company Ditto wants to be. The website is the company Ditto was six months ago. The new site needs to close this gap.

---

## Part 5: What the Rebuild Plan Gets Right

The 11-workstream plan from the team feedback session is solid. Specifically:

1. **StoryBrand framework for homepage** — Problem → Solution → Social proof → Emotional closer → CTA. This is the right narrative arc.
2. **Scroll-and-scrub product showcase** — Apple-style product storytelling. Care Circle woven in, not separate. This is how you show a product without listing features.
3. **Professionals page as a separate world** — Different audience, different tone, different evidence. Research, HCP testimonials, "Talk to a fellow doctor." Correct.
4. **Privacy & AI as a dedicated page** — Smart. Healthcare trust requires depth, not a checkbox. Content-first design.
5. **Partners embedded in Professionals** — Not a standalone page nobody finds. Tiered, clickable, with context.
6. **Visual direction shift** — Gradient + grain from the app, more whitespace, glass effects. Moves toward premium.
7. **Persistent professional access** — Top bar + hero button + nav item. Solves the "doctor on consumer page" problem.

---

## Part 6: Open Questions & Risks

| Question | Impact | My Take |
|----------|--------|---------|
| **Headline direction** (social vs. confidence vs. innovation) | P1 — sets the tone for everything | Social/family angle aligns with the deck and the Care Circle differentiator. But it needs to be concrete, not abstract. |
| **Scroll-and-scrub feasibility in Framer** | P1 — fallback is static two-column | The fallback is fine. Don't let the animation block the launch. |
| **Bricolage Grotesque commitment** | P2 — typography defines brand feel | Test it. If it works at app-screen scale, commit. Half-measures on type look worse than either option. |
| **User count discrepancy** (deck says 75K, draft says 60K) | P2 — credibility | Use the accurate, current number. Don't inflate or deflate. |
| **When does this ship?** | P1 — due date was Feb 28, it's now Mar 26 | The rebuild plan is good but scope is large. What's the new target? |
