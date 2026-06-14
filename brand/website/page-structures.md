# Ditto Care — Website Page Structures

**Version**: Draft 1.0
**Date**: 2026-03-27
**Author**: Mewtwo (PM co-pilot)
**Status**: For team review

---

## Table of Contents

1. [Why Not StoryBrand](#1-why-not-storybrand)
2. [Navigation & Site Architecture](#2-navigation--site-architecture)
3. [Homepage](#3-homepage)
4. [For Professionals](#4-for-professionals)
5. [Our Story (About)](#5-our-story-about)
6. [Trust & Privacy (renamed from Privacy & AI)](#6-trust--privacy)
7. [Help & Contact](#7-help--contact)
8. [Care Circle Page Decision](#8-care-circle-page-decision)
9. [Bilingual Strategy](#9-bilingual-strategy)
10. [Mobile Considerations](#10-mobile-considerations)

---

## 1. Why Not StoryBrand

### The Problem with StoryBrand for Ditto

StoryBrand (Donald Miller) follows: Character → Problem → Guide → Plan → Call to Action → Success → Failure. It works well for products in established categories where the visitor already knows what they're looking for.

Ditto isn't in an established category. There is no "consumer layer in healthcare." The deck says it plainly: "Banking has Revolut. Women's health has Flo. Fitness has Strava. Healthcare has your hospital's patient portal from 2008." Ditto is creating something new.

StoryBrand's weaknesses for Ditto:

| Issue | Why it hurts Ditto |
|-------|-------------------|
| Assumes the category exists | Visitors don't know they need a "care companion" — the category doesn't exist yet |
| Positions the brand as "guide" | Too humble for a company claiming to be "the consumer layer in healthcare." Ditto isn't Gandalf — it's building a new world |
| Formulaic | Produces homepages that look like every B2B SaaS site. Not befitting a consumer health brand aspiring to Hims-level premium |
| Linear narrative | StoryBrand is a straight line. Ditto's story has an emotional dimension (family, vulnerability, connection) that needs breathing room |

### Instead: Recognition → Revelation → Resolution → Reassurance → Resolve

A framework built for category-creating consumer products:

| Phase | What it does | Ditto application |
|-------|-------------|-------------------|
| **Recognition** | Make the visitor say "that's my life" | The messy reality of navigating healthcare as a family — WhatsApp groups, phone calls, one person becomes the project manager |
| **Revelation** | "Wait — someone built something for this?" | Show the product. Full app, full experience. Not features — the actual feeling of using Ditto |
| **Resolution** | "Here's how it works" | Concrete steps. Capture → Clarify → Connect. Simple, tangible, doable |
| **Reassurance** | "I can trust this" | Social proof, professional endorsement, privacy, press |
| **Resolve** | "I'm doing this" | Single, clean CTA. No distractions |

The key difference: StoryBrand starts with the problem and positions the brand as a guide who gives you a plan. Recognition-Revelation starts with *empathy* (I see your life) and moves to *surprise* (this exists?). The emotional temperature is different — it's warmer, more personal, more suited to healthcare.

---

## 2. Navigation & Site Architecture

### Recommended Nav

| Current proposal | Recommended | Rationale |
|-----------------|-------------|-----------|
| Home | Home | — |
| For Professionals | For Professionals | Clear, accurate. "Professionals" is better than "Zorgverleners" for a bilingual nav |
| About | Our Story | "About" is generic. "Our Story" signals there's something worth reading. Sets expectation of narrative, not boilerplate |
| Privacy & AI | Trust & Privacy | "Privacy & AI" sounds like a compliance page. "Trust & Privacy" positions it as something *for* the visitor, not *about* the company. Also: "AI" in the nav can trigger skepticism in healthcare |
| Help & Contact | Help | Shorter. "Contact" is implied. Every help page has contact info |

**Final nav**: `Home` · `For Professionals` · `Our Story` · `Trust & Privacy` · `Help`

**Primary CTA in nav**: "Download Ditto" (persistent, contrasting button style)

### Professional Access (Critical)

Doctors frequently land on the consumer homepage. They need to reach the pro page in one click. Three access points:

1. **Persistent top bar** on consumer pages: "Are you a healthcare professional? →" (subtle, always visible)
2. **"For Professionals" in main nav** with distinct visual weight (contrasting color or button treatment)
3. **"For Professionals" button in the homepage hero** — secondary to the download CTA

### Site Map

```
Home (consumer-facing)
├── For Professionals (HCP-facing)
│   └── Partner deep-dive pages (UMCG, Menzis, Juvoly)
├── Our Story (about, manifesto, team, careers)
├── Trust & Privacy (data, AI, GDPR, certifications)
├── Help (FAQ by audience, contact form, video resources)
└── Footer: Press, Legal, Social, App Store badges
```

**Not in v1** (plan for later): Blog, Stories, SEO landing pages, Download page (download is a CTA everywhere, not a destination).

---

## 3. Homepage

### Purpose
**Who**: Patients and their families/caregivers (equal weight)
**Goal**: Understand what Ditto does, feel emotionally moved, download the app
**Success metric**: A first-time visitor can explain Ditto to a friend after one scroll

### Narrative Arc: Recognition → Revelation → Resolution → Reassurance → Resolve

---

### Section 1: Hero

**Content**:
- Headline (1 line, max 8 words)
- Subheadline (1-2 sentences, what Ditto does concretely)
- Primary CTA: "Download Ditto" with App Store + Google Play badges
- Secondary CTA: "For Healthcare Professionals →"
- Trust signals: "75,000+ users · 4.7★ · Trusted by hundreds of doctors"
- Press logos row: NOS, AD, Hart van Nederland, Quote — **in the hero area**, not further down. Trust must be above the fold (Heidi pattern).

**Copy direction**:
The headline must be concrete, not abstract. "Care is something you carry together" is a nice sentiment but doesn't tell you what Ditto *does*. The subheadline should do the explaining.

**The narrative tension**: We don't want pure feature-first ("we make summaries") — that's a utility. But the family/sharing angle ("loop in your loved ones") feels aspirational when most users today use Ditto for understanding first. The honest bridge is **understanding as the core promise**: summaries create understanding, Care Circle *shares* understanding. The promise is: "you'll understand your healthcare, and so will the people around you."

Headline candidates to explore (not final copy — directions):
- Understanding angle: "Your doctor explained it. Now you can too."
- Understanding + family: "Understand your healthcare. Help your loved ones understand too."
- Bold angle: "You shouldn't need a medical degree to understand your own health"
- Recognition: "Healthcare finally makes sense"

The subheadline then grounds it concretely: "Record your doctor's visit. Get a clear summary. Share it with the people who matter."

**Visual treatment**:
- **App mockup is the primary visual element.** Visitors must immediately see "this is an app" — before they read a word. Show a real screen (summary view or Care Circle view), full-size phone mockup, large enough to recognize the UI.
- Layout: copy left, app mockup right (like Tandem's hero). The mockup creates instant product comprehension.
- Press logos in the hero area, below the trust stats line. Small but visible, full opacity. This is the Heidi pattern — trust signals above the fold because in healthcare, trust comes before features.
- Gradient background (blue-yellow direction), Bricolage Grotesque headline.
- App Store + Google Play badges at a visible size, near the mockup.
- Consider: QR code for desktop→mobile bridge (Tandem pattern).

**Rationale**:
The hero has 5 seconds. It must answer three questions: What is this? (app mockup answers visually) Is it for me? (headline + subheadline) What do I do? (CTA + badges). Press logos in the hero build immediate trust — don't make visitors scroll to find credibility. Professional access point ensures doctors don't bounce.

**Why app mockup over photography**: People don't know Ditto. They need to see it's an app — a concrete thing they can download and use. Photography creates emotion but doesn't create product comprehension. The mockup does both: it shows what Ditto is AND (if showing a summary or Care Circle screen) hints at the value.

**Avoid**:
- Abstract headlines that sound nice but say nothing ("Care is something you carry together")
- Feature lists in the hero
- Photography-only hero without product (saves emotion for later sections)
- Multiple CTAs competing for attention
- Stock photography
- "Free" as the lead value prop (free is a surprise, not the headline)
- Pure feature framing ("AI-powered summaries") — lead with the outcome (understanding)
- Pure sharing/family framing without grounding in what the app actually does today

---

### Section 2: The Problem (Recognition)

**Content**:
3 empathetic pain point cards that make the visitor say "that's exactly my life."

NOT generic pain ("healthcare is overwhelming"). YES specific, vivid scenarios:

| Card | Pain point | Example direction |
|------|-----------|-------------------|
| 1 | **You forget** | "Research shows patients forget 40-80% of what doctors say. The more serious the diagnosis, the less you remember." |
| 2 | **You can't explain it to family** | "Your partner asks 'what did the doctor say?' You try to explain but the words don't come. The worry on their face makes it worse." |
| 3 | **You're managing it alone** | "WhatsApp groups. Phone calls after every appointment. One family member who becomes the unofficial project manager. Sound familiar?" |

**Visual treatment**:
- Clean cards on white or soft gradient background
- No illustrations — let the copy do the emotional work
- Possibly: subtle icons (not decorative — functional, like a ?, a phone, a message bubble)
- Generous whitespace between cards

**Rationale**:
This is the Recognition phase. The visitor must see their own life reflected before they're ready to hear about a product. The pain must feel *personal*, not *statistical*. The deck nails this — "WhatsApp groups. Phone calls. Shared Google Docs." — that's recognition.

Leading with pain quantification (Heidi's "$65K" approach) would work for the professionals page but is wrong here. Consumers respond to emotional recognition, not stats.

**Avoid**:
- Generic "healthcare is broken" statements
- More than 3 cards (diminishing returns)
- Solution hints in this section (earn the right to show the product first)
- Sad imagery — empathize, don't depress

---

### Section 3: Product Showcase (Revelation)

**Content**:
Scroll-and-scrub animation (or static fallback) showing the actual app in action. This is the "revelation" moment — "wait, someone built something for this?"

5 features, shown through full-screen phone mockups large enough to read the UI:

| # | Feature | What the visitor sees |
|---|---------|----------------------|
| 1 | **Record** | Phone recording a doctor's conversation. One tap to start. |
| 2 | **Summarize** | The AI summary appearing — plain language, structured, clear. Show real (anonymized) content. |
| 3 | **Understand** | Medical document → photo → plain-language explanation. The "aha" moment. |
| 4 | **Care Circle** | Inviting a family member. Their view: a summary adapted for them. The partner gets detail, the adult child gets key decisions. Show the *difference* in what each person receives. |
| 5 | **Your Journey** | Timeline view — multiple appointments, one story. Your health journey, organized. |

Section intro text: something like "Ditto puts your complete health story in your pocket" or "See how it works" — brief, transition-only.

**Care Circle integration**:
This is critical. Care Circle is NOT shown as a separate feature at the end. It's woven into the narrative: you record → you get a summary → you share it with your family → *they each get what they need*. The "different people need different things" insight from the deck must be visible here.

Consider showing side-by-side: what the patient sees vs. what the partner sees vs. what the adult child sees. This is the moment people understand why Ditto is different from just sending a screenshot.

**Visual treatment**:
- Phone mockups must be FULL SCREEN and READABLE. If you can't read the UI text, the mockups fail.
- Scroll-and-scrub: phone stays fixed (or moves subtly), context text updates alongside as user scrolls. References: Apple MacBook product page, Neo computer.
- Fallback: static two-column layout — phone left, text right, alternating per feature.
- Background: gradient (blue-yellow direction from MCO-337) with subtle grain texture.

**Rationale**:
Polarsteps teaches us: product-as-demo beats description. Showing the actual app — real screens, real content — is more convincing than any copy. The scroll-and-scrub format creates a sense of discovery and control.

Care Circle must be here, not in a separate "sharing" section, because it's not a feature — it's the core identity. The deck's strongest slide is "It's a care circle, not a chatbot." The product showcase is where this lands.

**Avoid**:
- Tiny phone mockups where you can't read anything
- Feature bullet points alongside mockups (let the visuals speak)
- Separating Care Circle into its own section (it must be woven into the flow)
- Generic mockups without real content (use anonymized but realistic summaries)
- More than 5 features (decision fatigue)

---

### Section 4: Social Proof (Reassurance, Part 1)

**Content**:
Mixed evidence from multiple angles:

| Type | Content | Why |
|------|---------|-----|
| **User testimonials** (2-3) | Real quotes from diverse users: a patient, a caregiver/family member, and ideally someone from a specific care journey (oncology, chronic). Names, photos, real stories. | Emotional proof — "people like me use this" |
| **Professional endorsement** | Brief line: "Trusted by hundreds of healthcare professionals across the Netherlands and beyond" + 1 sharp doctor quote | Authority proof — "doctors approve" |
| **Numbers** | 75,000+ users · 4.7★ rating · App Store + Google Play | Scale proof — "this is real" |
| **Press logos** | NOS, AD, Hart van Nederland, Quote, 3FM, RTL (repeat from hero or show here if not in hero) | Media proof — "serious people cover this" |

**Visual treatment**:
- Testimonial cards with real photos (not stock), name, and a short identifier ("Maria, 67 — living with breast cancer" or "Thomas — caregiver for his father")
- Press logos at full opacity, not greyed out (MCO-340 feedback)
- Clean grid or carousel layout
- Consider: star rating visualization from App Store

**Rationale**:
Social proof works best when it's diverse — multiple *types* of evidence, not just 5 testimonials in a row. Heidi does this well: named clinicians with role and specialty. Tandem uses App Store reviews. Ditto should mix user stories, professional endorsement, numbers, and press.

The testimonials should reflect the equal weight of patients and caregivers. At least one testimonial should be from a family member/caregiver perspective — this reinforces the Care Circle differentiator and makes caregivers feel seen.

**Avoid**:
- Anonymous testimonials ("User123")
- All-patient testimonials (caregivers are half the audience)
- Testimonial walls with 10+ quotes (3-4 strong ones beat 10 mediocre ones)
- Duplicate testimonials (MCO-340: Jacky appeared twice)
- Greyed-out/low-opacity logos (signals you're ashamed of the list)

---

### Section 5: USPs — Why Ditto (Reassurance, Part 2)

**Content**:
3 unique selling points that address remaining objections. These are the "yeah but..." answers:

| USP | "Yeah but..." it answers | Content direction |
|-----|-------------------------|-------------------|
| **Works across providers** | "My care involves multiple doctors/hospitals" | "One app for your GP, your specialist, your physiotherapist. Ditto works regardless of which healthcare provider you see." |
| **You control the sharing** | "I'm not comfortable sharing everything with everyone" | "Share exactly what you want, with exactly who you want. Your partner gets the full picture. Your colleague gets the basics. You decide." |
| **Your data stays yours** | "What about privacy? This is health data..." | "Your data is stored on your device. When we process it, we use secure EU servers and delete it immediately. We can't read your summaries. By design, not by promise." Link to Trust & Privacy page. |

**Visual treatment**:
- Icon + headline + 2 sentences per USP
- Possibly full-width horizontal layout (3 columns)
- One of these (privacy) includes a link to the Trust & Privacy page
- Consider: Iman's privacy video as a thumbnail that plays inline, bridging to the Trust page

**Rationale**:
By this point, the visitor has been emotionally engaged (problem + product showcase), socially reassured (testimonials + numbers), and now needs the rational objections answered. Privacy is the biggest one in healthcare — Heidi puts compliance badges in the hero. We're less aggressive but still address it prominently.

The "works across providers" USP is important because it separates Ditto from hospital patient portals (which only show one hospital's data). The "you control sharing" USP is important because sharing health data with family raises immediate privacy/control concerns.

**Avoid**:
- More than 3 USPs (if everything is a USP, nothing is)
- Repeating features already shown in the product showcase
- Technical jargon ("end-to-end encryption", "AES-256") — save that for the Trust page
- Treating privacy as a checkbox rather than a selling point

---

### Section 6: The Story Behind the Summary (Resolve, Part 1)

**Content**:
Full-width narrative video. This is the emotional closer — the moment that transforms rational interest into emotional commitment.

The video should tell one real story: a patient and their family navigating a healthcare moment. Not a product demo — a *human* story where Ditto happens to be present.

Format:
- Full-width, edge-to-edge
- Video plays on scroll or click (NOT autoplay with sound)
- Brief text above: "The Story Behind the Summary" or similar
- No UI chrome around the video — let it breathe
- After the video: a brief emotional tagline. Something like "This is why we built Ditto" or simply "Care. Clarified."

**Visual treatment**:
- Cinematic quality: editorial photography aesthetic in motion
- Warm color grading, film grain
- Subtle music, real voices
- This should feel like a short film, not a product video
- Navy/dark overlay with light text for any captions

**Rationale**:
The consumer deck's strongest moments are emotional, not rational. The deck *shows* a grandmother who's exhausted from retelling her diagnosis. The deck *shows* a family around the kitchen table. These moments are what makes someone download an app.

Every great consumer brand has a "belief video" — Apple has their "Think Different" moments, Headspace has their meditation animations, Polarsteps has travel footage that creates wanderlust. Ditto needs a healthcare equivalent that creates *warmth* — "I want to be part of this."

This section exists because data and features convince the mind, but emotion converts. The product showcase convinced them Ditto works. The social proof convinced them others trust it. The video makes them *feel* it.

**Avoid**:
- Product demo disguised as a story
- Multiple videos (one powerful video > three mediocre ones)
- Autoplay with sound (instant bounce)
- Placing this section earlier (it's the emotional climax — earned, not given)

---

### Section 7: Closing CTA (Resolve, Part 2)

**Content**:
- Headline: "Start using Ditto" or "Download Ditto — it's free" (here, "free" is the surprise, not the lead)
- App Store + Google Play badges (large, prominent)
- QR code for desktop visitors (Tandem pattern)
- Secondary link: "Questions? Talk to the team →"

**Visual treatment**:
- Clean, generous whitespace
- Navy background with white text, or gradient
- Badges and QR code at a large, comfortable size
- No competing elements — this section has ONE job

**Rationale**:
Polarsteps and Ada Health both end with a single, clear conversion moment. No sidebar offers, no newsletter signup, no "also check out our blog." One CTA, one decision.

The QR code (from Tandem) is smart for an app-only product — many visitors browse on desktop but need to download on mobile. The QR code bridges that gap.

"It's free" works here because it's a surprise, not the lead value prop. By this point they know what Ditto does and why it matters. Learning it's free removes the last objection.

**Avoid**:
- Multiple CTAs (newsletter signup, demo booking, etc.)
- "Learn more" buttons that lead somewhere else
- This section appearing too early or being repeated throughout the page
- Tiny App Store badges

---

### Homepage Summary Table

| # | Section | Phase | Duration (scroll) | Primary job |
|---|---------|-------|-------------------|-------------|
| 1 | Hero | — | First screen | Answer: what is this, is it for me, what do I do |
| 2 | The Problem | Recognition | 1 screen | Make visitor say "that's my life" |
| 3 | Product Showcase | Revelation | 2-3 screens (scroll-and-scrub) | Show the product, weave in Care Circle |
| 4 | Social Proof | Reassurance | 1 screen | Diverse evidence: users, doctors, press, numbers |
| 5 | USPs | Reassurance | 1 screen | Answer remaining objections (privacy, control, cross-provider) |
| 6 | Narrative Video | Resolve | 1 screen | Emotional commitment — feel it, not just know it |
| 7 | Closing CTA | Resolve | Half screen | Single conversion moment: download |

**Total**: ~7-8 screens of scroll. Tight, purposeful, no filler.

---

## 4. For Professionals

### Purpose
**Who**: Healthcare professionals (Dutch GPs, specialists, midwives; international HCPs)
**Goal**: Assess credibility in 30 seconds, understand what Ditto means for their practice, book a conversation
**Success metric**: A skeptical doctor reaches the CTA feeling reassured, not sold to

### Key Principle
This page is a different *world* from the homepage. Different audience, different tone, different evidence. Patient testimonials don't belong here. Marketing fluff doesn't belong here. Research, precision, and peer credibility are what doctors respond to.

**Tone**: Medical-professional appropriate. Direct, evidence-led, zero fluff. Think: a well-written journal abstract, not a SaaS landing page.

---

### Section 1: Hero

**Content**:
- Headline: outcome-focused, addressing what doctors actually care about
- Copy direction: "Better-informed patients, fewer repeated questions" or "Your patients understand what you said. Their family does too." — avoid generic "AI transforms healthcare" language
- Secondary text: 1-2 sentences positioning Ditto as a tool that makes the doctor's job easier, not harder
- CTA: "Talk to a fellow doctor →" (Calendly link to medical team member)
- Trust signals: "Used by 75,000+ patients · Endorsed by hundreds of professionals"

**Visual treatment**:
- Copy left, visual right (consistent hero pattern across all pages — MCO-339)
- Visual: app mockup showing a professional-relevant screen, or a photo of a real doctor in a real setting
- Clean, premium feel. More structured than the consumer hero.

**Avoid**:
- Patient-facing language ("your health journey")
- AI-forward messaging ("our AI technology")
- Vague claims without evidence

---

### Section 2: Why It Matters (Pain + Evidence)

**Content**:
Lead with the problem doctors face — in quantified terms (Heidi's pattern):

| Stat | Source | Purpose |
|------|--------|---------|
| "40-80% of medical information is forgotten immediately" | Published research | Establishes the problem is real, not anecdotal |
| "~50% of patients leave with misunderstandings about their diagnosis" | Research reference | Escalates the severity |
| "Patients who understand their treatment plan have X% better adherence" | Research reference | Shows the outcome doctors care about |

Then: "Ditto helps. Here's how."

**Visual treatment**:
- Stats prominently displayed (large type, Bricolage Grotesque)
- Research references cited (small, linked)
- Clean white/gradient background

**Rationale**:
Doctors respond to evidence, not testimonials. Heidi leads with "$65K lost per year" — pain quantification *before* solution. This section earns the right to show the product by first proving the problem is real and measured.

**Avoid**:
- Emotional framing (save that for the consumer page)
- Unsubstantiated claims
- Citing internal stats without context

---

### Section 3: Product Walkthrough (Professional Experience)

**Content**:
Show what Ditto means for the doctor's workflow specifically:

1. **Patient records the consultation** — no setup required from the doctor. Passive, zero friction.
2. **AI generates a plain-language summary** — show what a summary actually looks like. Make it real.
3. **Patient shares with Care Circle** — fewer phone calls from family members asking "what did the doctor say?"
4. **Patient comes back informed** — next appointment starts from understanding, not confusion.

**Visual treatment**:
- App screenshots showing the professional-relevant flow
- Consider: side-by-side of "before Ditto" (confused patient, repeated calls) vs. "after Ditto" (informed patient, family aligned)
- Full-screen mockups (same readability requirement as homepage)

**Avoid**:
- Consumer-facing feature descriptions
- Technical AI details (save for Trust page)
- Making it look like the doctor needs to do anything

---

### Section 4: Research & Evidence

**Content**:
- Published research Ditto has been involved in or cited in
- Ongoing studies and collaborations
- Clinical validation data (if available)
- Link to full research papers or summaries

**Visual treatment**:
- Academic/credible design: clean typography, proper citations
- Possibly a timeline of research milestones
- Links to external publications

**Rationale**:
This section doesn't exist on any current Ditto web page. It's the single biggest gap for professional credibility. Heidi Health has named clinician testimonials AND research. Ditto needs at minimum a research section with UMCG collaboration mentioned.

---

### Section 5: Partners & Collaboration

**Content** (embedded, not standalone — per MCO-335):
- Partner logos at full opacity with organization type label
- Three collaboration tiers explained:
  1. **Promotional partnerships** — organizations recommending Ditto to patients
  2. **Research collaborations** — academic and clinical research
  3. **Guided pilots** — structured implementation programs
- Each partner clickable → deep-dive sub-page with more detail
- Current partners: UMCG, Menzis, Juvoly
- CTA: "Explore a partnership →" or "Let's work together"

**Visual treatment**:
- Clean card grid, each partner with logo + brief description
- Full opacity logos (not greyed out)
- Tier labels as tags or badges on each card

---

### Section 6: Professional Testimonials

**Content**:
- HCP testimonials ONLY — no patient testimonials on this page
- Named doctors with specialty and institution
- Christian's GP video (featured prominently if ready)
- 2-3 written quotes from different specialties (GP, specialist, midwife)

**Visual treatment**:
- Video testimonial featured large (not in a tiny player)
- Written quotes in cards with photo, name, specialty
- Subtle differentiation from the consumer testimonial style (more structured, less emotional)

**Avoid**:
- Patient testimonials (wrong audience for this page)
- Anonymous quotes
- Too many testimonials (3-4 strong > 8 mediocre)

---

### Section 7: Privacy & Data Summary

**Content**:
- Brief summary of how Ditto handles data (3-4 bullet points)
- Specifically address: what happens to the recording, where data is stored, GDPR compliance
- Link to full Trust & Privacy page
- Iman's privacy video thumbnail (optional, links to Trust page)

**Rationale**:
Doctors are gatekeepers. If they're not comfortable with the data handling, they won't recommend Ditto. This doesn't need to be exhaustive (that's the Trust page), but it needs to be present and confident.

---

### Section 8: CTA

**Content**:
- Primary: "Talk to a fellow doctor" — Calendly link to Hester/Jasper (medical team)
- Secondary: "Or explore our research →"
- Context: make it clear they'll speak to someone with medical background, not a sales rep

**Rationale**:
Niek's feedback: add actual demo for professionals. "Schedule Demo" is too salesy. "Talk to a fellow doctor" is peer-to-peer, which is how doctors prefer to evaluate new tools.

---

## 5. Our Story (About)

### Purpose
**Who**: Anyone curious about who built Ditto and why
**Goal**: Feel the mission. Understand the people. Possibly explore careers.
**Success metric**: Visitor leaves with a feeling, not just information

---

### Section 1: Manifesto

**Content**:
NOT a generic mission statement. A founder's manifesto — 2-3 paragraphs on why Ditto exists.

Copy direction:
- Start with a personal moment (Merlijn's story, or a founding insight)
- Move to the systemic problem ("It's easier to follow your niece's gap year than your mother's healthcare journey")
- End with the vision ("We're building the consumer layer in healthcare")

This should read like a letter, not like a corporate about page. Think: Patagonia's founder letter, not "Our mission is to leverage technology to improve healthcare outcomes."

**Visual treatment**:
- Full-width text section, generous whitespace
- Possibly: photography of the founding team or the Rotterdam office
- Bricolage Grotesque for the opening line, Inter for the body
- Consider: Merlijn's signature or photo for authenticity

---

### Section 2: What We Believe

**Content**:
3-5 beliefs that define Ditto's approach. Not corporate values — actual beliefs that drive decisions.

Examples (directions, not final):
- "The patient is the hero, not the technology"
- "Healthcare information belongs to the person it's about"
- "Understanding your care shouldn't require a medical degree"
- "The people who care about you should be able to help you"
- "Privacy is architecture, not policy"

**Visual treatment**:
- Short, bold statements
- Could be a simple vertical list with generous spacing
- Or: cards with brief elaboration beneath each belief

**Avoid**:
- Generic values ("Innovation", "Integrity", "Excellence")
- More than 5 items
- Long explanations (the belief should be self-evident)

---

### Section 3: The Team

**Content**:
- Team photos with name, role, and one personal line (not title-only)
- Photos should be consistent in style: same color grading, same setting (MCO-337: Rebeka unifying team photo color grading)
- Optionally: a team group photo in a candid setting

**Visual treatment**:
- Card grid, clean, consistent
- Photos with warm color grading matching brand evolution direction
- Name and role visible, personal line on hover or below

---

### Section 4: Careers

**Content**:
- Brief text: "We're growing" or similar
- "See open positions →" button linking to Homerun careers page
- NOT individual vacancy pages on the website (those should live on Homerun)

**Rationale**:
MCO-339: vacancies link to Homerun. Don't replicate job listings on the marketing site — they go stale.

---

### Section 5: Press

**Content**:
- Press mentions with logos and links to articles
- Press contact email
- "For press inquiries: press@ditto.care" (per Niek's feedback)

**Rationale**:
MCO-340: press in footer + press email. But if the About page includes a press section, it gives journalists a clear destination. Also serves as additional social proof.

---

## 6. Trust & Privacy

### Purpose
**Who**: Anyone with privacy concerns — skeptical patients, cautious doctors, compliance-focused partners
**Goal**: Transform concern into confidence. Answer every data question.
**Success metric**: A skeptical doctor comes away reassured (MCO-336 acceptance criterion)

### Key Principle
This is a content-first page. Information density is a feature, not a bug. This page exists because healthcare trust requires depth — you can't checkbox your way to trust. But the information must be well-organized, scannable, and jargon-free for patients while thorough enough for professionals.

**Renamed from "Privacy & AI"** because: "AI" in a nav label triggers skepticism in healthcare contexts. "Trust & Privacy" positions the page as reassuring, not defensive. It's about what Ditto does *for you*, not what Ditto does *with your data*.

---

### Section 1: Hero

**Content**:
- Headline: "Your health data, your rules" or "How Ditto protects your information" or "Built for trust"
- Brief subtext: 1-2 sentences establishing the principle (privacy by architecture, not policy)
- Trust badges: GDPR, any certifications, EU server badges

**Visual treatment**:
- Clean, confident, not defensive
- Badge/certification icons prominent (Heidi pattern: compliance above the fold)

---

### Section 2: How Recording Works

**Content**: Step-by-step explanation of what happens when someone records a conversation
- You tap record
- Audio is processed on secure EU servers
- Summary is generated and sent to your device
- Audio is deleted from our servers
- We never store or access your raw audio

**Visual treatment**:
- Simple flow diagram or numbered steps
- Icons per step

---

### Section 3: Data Storage & Encryption

**Content**:
- Where data lives (on-device)
- When data leaves the device (only for AI processing)
- Encryption standards (brief, link to technical doc if needed)
- What Ditto can and cannot access

---

### Section 4: AI Transparency

**Content**:
- What the AI does: transcription, summarization, translation
- What the AI does NOT do: diagnosis, medical advice, treatment recommendations
- How the AI is trained and validated
- Clinical validation efforts

---

### Section 5: GDPR Compliance

**Content**:
- Ditto's GDPR position
- Data subject rights (access, deletion, portability)
- Data processing agreement information (relevant for professionals/partners)

---

### Section 6: What Ditto Does NOT Do

**Content**:
A clear, bold list of what Ditto explicitly does NOT do:
- We do NOT sell your data
- We do NOT share data with insurers
- We do NOT provide medical advice
- We do NOT store audio after processing
- We do NOT access your summaries

**Rationale**:
Negation is powerful in trust-building. Saying what you *don't* do is often more reassuring than saying what you do. This section addresses the unspoken fears directly.

---

### Section 7: Iman's Video

**Content**:
- Featured video: Iman explaining Ditto's privacy approach
- Context label: "Watch Iman, our [role], explain how Ditto protects your data" (MCO-338 pattern: every video has a context label)

---

### Section 8: Certifications & Badges

**Content**:
- All relevant certifications displayed
- Partner logos (UMCG, Menzis) as implicit trust signals
- Links to detailed compliance documentation

---

## 7. Help & Contact

### Purpose
**Who**: Anyone with questions — patients, professionals, partners, press
**Goal**: Find answers quickly, contact the right person if needed
**Success metric**: 80%+ of questions answered without needing to contact anyone

---

### Section 1: FAQ (Organized by Audience)

**Content**:
Full FAQ organized into tabs or sections:

| Audience | Example questions |
|----------|-----------------|
| **Patients** | "How do I record a consultation?" "How do I share a summary?" "Does my doctor need to know?" |
| **Professionals** | "How does it work in my practice?" "What about patient consent?" "How accurate is the AI?" |
| **Partners** | "How do we integrate?" "What collaboration models exist?" |
| **Privacy & Data** | "Where is my data stored?" "Can I delete my data?" "Who can see my summaries?" |

**Note**: Homepage should show only 3-4 top questions with a "See all questions →" link here.

**Writing style**: First person ("We" — per MCO-340 feedback). Direct answers, not hedged language.

---

### Section 2: Contact Form

**Content**:
- Subject field
- Role/type selector (Patient, Healthcare Professional, Partner, Press, Other)
- Message field
- For professionals: prominent "Talk to a fellow doctor →" CTA above the form
- Email fallback: info@ditto.care
- Phone: +31 85 115 5421

---

### Section 3: Video Resources

**Content**:
- Curated videos with context labels
- Example: "Watch Merlijn explain how Ditto works" / "Watch Iman on privacy"
- Future: tutorial videos, getting-started guides

---

## 8. Care Circle Page Decision

### Recommendation: No standalone page in v1. Revisit after launch.

**Arguments for a standalone page**:
- It's the biggest differentiator — "the thing that separates Ditto from every health AI chatbot"
- Could serve as a landing page for Care Circle invite links
- Depth needed to explain different roles (partner, child, parent, friend)
- Privacy concerns specific to sharing deserve dedicated space

**Arguments against (for now)**:
- Brand-first means fewer, sharper pages — not more
- The homepage product showcase should carry the Care Circle narrative (Section 3)
- A standalone page splits attention and adds a nav decision
- The "different people need different things" insight works *better* within the product showcase (visually showing different views) than as standalone copy

**Compromise**: Weave Care Circle deeply into the homepage product showcase. If Care Circle invite links need a landing page (for sharing flows), create a lightweight `/care-circle` page later that's not in the main nav but serves as a destination for in-app sharing invites.

---

## 9. Bilingual Strategy

### Recommendation: Full NL + EN, locale-based routing

| Decision | Recommendation | Rationale |
|----------|---------------|-----------|
| **Default language** | Dutch (NL) | Primary market is Netherlands. Most users are Dutch. |
| **URL structure** | `/nl/` and `/en/` prefixes | Clean, SEO-friendly when SEO phase comes. Framer supports this. |
| **Locale detection** | Auto-detect browser language, default to NL | Reduces friction for Dutch users. EN users see language switcher. |
| **Language switcher** | Small, persistent (in nav or footer) | Not a flag (flags represent countries, not languages). Use "NL / EN" text toggle. |
| **Content parity** | 100% parity for all 5 pages | No "Dutch-only" or "English-only" pages. Every page exists in both languages. |
| **Copy approach** | Write NL first, adapt (not translate) to EN | NL is the primary voice. EN should feel native, not translated. |

**For Professionals page**: Both languages equally important since the audience includes international HCPs.

---

## 10. Mobile Considerations

| Element | Desktop | Mobile |
|---------|---------|--------|
| **Nav** | Full horizontal: Home · For Professionals · Our Story · Trust & Privacy · Help · [Download Ditto] | Hamburger menu. "Download Ditto" stays visible outside hamburger. |
| **Professional top bar** | "Are you a healthcare professional? →" persistent bar | Same bar, but shorter text: "Healthcare professional? →" |
| **Hero headline** | Full size (Bricolage Grotesque, ~56-64px) | Scaled ~25% (~42-48px) |
| **Product showcase** | Scroll-and-scrub with fixed phone + updating context | Simplified: vertical scroll through features. Phone mockup per section. Scrub interaction may not work well on mobile — test. |
| **Video sections** | Full-width, inline play | Full-width, tap to play (never autoplay) |
| **Testimonials** | Card grid (2-3 columns) | Horizontal carousel (swipe) |
| **App Store badges** | Prominent but proportional | LARGE. This is where most downloads happen. |
| **QR code** | Show (for desktop→mobile bridge) | Hide (you're already on mobile) |
| **Touch targets** | N/A | 44px minimum everywhere |
| **Photography** | Full-frame editorial | Cropped for impact, not just shrunk |

**Critical mobile point**: The closing CTA section with App Store badges is the most important mobile section. It should be impossible to miss. Consider: sticky bottom bar with download button on mobile (after scrolling past the hero).

---

## Appendix: Quick Reference — What Goes Where

| Content | Homepage | Professionals | Our Story | Trust | Help |
|---------|:--------:|:------------:|:---------:|:-----:|:----:|
| Product showcase | ✅ (primary) | ✅ (HCP view) | | | |
| Care Circle | ✅ (woven into showcase) | ✅ (patient-side benefit) | | | |
| Patient testimonials | ✅ | | | | |
| HCP testimonials | | ✅ | | | |
| Research/evidence | | ✅ | | | |
| Partner logos | ✅ (light) | ✅ (full, detailed) | | ✅ (trust signal) | |
| Press logos | ✅ | | ✅ | | |
| Privacy summary | ✅ (brief) | ✅ (brief) | | ✅ (full) | ✅ (FAQ) |
| Narrative video | ✅ | | | | |
| Iman's video | | | | ✅ | ✅ |
| Christian's video | | ✅ | | | |
| Download CTA | ✅ (hero + closing) | | | | |
| "Talk to a doctor" CTA | | ✅ | | | |
| FAQ | ✅ (3-4 Qs) | | | | ✅ (full) |
| Team photos | | | ✅ | | |
| Careers | | | ✅ | | |
| Manifesto | | | ✅ | | |
