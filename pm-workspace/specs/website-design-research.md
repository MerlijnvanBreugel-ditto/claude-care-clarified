# Website Design Pattern Research

**Date:** 2026-03-26
**Purpose:** Structural analysis of 4 reference websites for Ditto Care website development

---

## 1. Hims (forhims.com / hims.com) — Consumer Health

### Site Structure

**Navigation:** Intentionally minimal. Four items visible at top level:
- Left: **Shop**, **Learn**
- Right: **Cart**, **Login**

Both Shop and Learn trigger slide-in menus that reveal product categories. No mega-menu, no cluttered dropdowns. The constraint forces users into one of two mindsets: buying or educating themselves.

**Product verticals (each gets its own landing page):**
- Hair Loss
- Sexual Health (ED, PE, low testosterone)
- Weight Loss
- Skin Care
- Mental Health
- Oral Health
- Lab Testing
- Merchandise

**Page types:**
- Category landing pages (one per health vertical)
- Product detail pages
- Educational/blog content ("Good Health by Hims")
- Consultation flow pages
- Account/pharmacy pages

### Hero/Homepage Approach

Strong vertical layout — not a grid. Each section answers one piece of the puzzle. The homepage scrolls through health categories sequentially, each featuring bold imagery with minimal text and a single CTA overlaid in a clean black box.

Background uses dynamic GIFs, rollover effects, and captivating photography featuring real men — not stock photos. The vibe is magazine editorial, not medical catalog.

### Dual Audience Handling

Hims solved this by creating **entirely separate brands and domains**:
- **forhims.com / hims.com** — men's health
- **forhers.com** — women's health (launched in 20 days using the same component architecture)
- **forhims.co.uk** — UK market (launched in 30 days)

This is a critical design decision: rather than splitting one site with tabs or toggles, they built parallel experiences. Each audience gets a fully tailored brand voice, imagery, and product set. The underlying component library and CMS (Contentful headless) are shared.

### CTA Strategy

- Primary CTAs sit in **bold black boxes overlaid on images** — high contrast, impossible to miss
- CTAs are direct: "Get started," "Shop now" — no vague "Learn more"
- Each health category section has exactly one CTA, reducing decision paralysis
- Checkout flow is streamlined (identified as a key optimization area)
- AI-powered photo ID validation for prescription verification

### Content Patterns

| Pattern | How Hims Uses It |
|---|---|
| **Social proof** | "2.5M+ subscribers" as headline stat. No testimonial walls — the number does the work |
| **Destigmatization** | Frank, approachable tone around sensitive topics (ED, hair loss, mental health). Photography normalizes these conversations |
| **Editorial content** | "Good Health by Hims" blog for SEO and education. "Learn" nav item puts content on equal footing with commerce |
| **Product simplicity** | Each category page shows only a few products — sometimes just one. This is the opposite of Amazon-style choice overload |
| **Visual storytelling** | GIFs, dynamic imagery, real people. The site feels alive, not static |

### What Makes It Distinctive

1. **Radical simplicity in navigation.** Two items. That's it. Forces clarity of intent.
2. **Magazine aesthetic for healthcare.** Subdued pastels (blue, coral, orange), massive negative space, editorial photography. Doesn't look or feel medical.
3. **Separate brands, shared architecture.** Instead of awkward "For Men / For Women" toggles, each audience gets a dedicated home with shared tech underneath.
4. **Vertical product pages.** One category, one page, one scroll, minimal products. The constraint builds confidence — "this is the thing, not one of 47 options."
5. **Content as first-class citizen.** "Learn" sits alongside "Shop" in the nav. Education is part of the conversion funnel, not an afterthought.

---

## 2. Heidi Health (heidihealth.com) — Healthcare AI

### Site Structure

**Navigation (7 items + 3 actions):**
- Product, Features, Get Started, Specialties, Success Stories, Resources, Pricing
- Actions: Login, Sign Up, Contact Sales
- Region selector: US, UK, AU, CA, NZ, EU, DE, FR, ES

More complex than Hims, reflecting the B2B/SaaS nature of the product. But still clean — no mega-menus.

**Page types:**
- Homepage (conversion-focused)
- Solutions pages by audience (clinicians, clinics, enterprise, allied health)
- Solutions by specialty (medical specialties, psychologists, dietitians, veterinarians, etc.)
- Customer success stories
- Pricing page
- Blog / resources
- Trust/security center
- Downloads
- Help center

### Hero/Homepage Approach

**Headline:** "The AI medical scribe for all clinicians"

**Sub:** "Heidi is the ambient AI medical scribe that automates clinical documentation to reduce administrative burden and enable healthcare professionals to focus more on patient care."

Immediately followed by compliance badges: ISO, GDPR, HIPAA, PIPEDA, APP, NHS, Cyber Essentials. This is smart — in healthcare AI, trust comes before features.

**Primary CTA:** "Try Heidi - it's free" — repeated throughout the page.

### Homepage Sections (in order)

1. **Hero** — headline + compliance badges + primary CTA
2. **Pain stats** — "50% of clinicians' time is not spent on patient care" / "$65,000 lost per year" / "2 hours/day on non-care tasks"
3. **How It Works** — 3-step process: Transcribe > Customize > Output
4. **Feature deep-dives** — Ask Heidi, Context, Custom Templates, Memory, Teams, Multilingual, Documents
5. **Value propositions** — "Restore eye contact" / "Offer warmer care. Get home on time"
6. **Clinician testimonials** — Named quotes with role and specialty
7. **Security section** — "Unbreakable" headline, full certification list
8. **Specialty showcase** — By profession type
9. **Pricing tiers** — Free, Clinician, Practice, Enterprise
10. **Final CTA** — "Try Heidi - it's free"

### Dual Audience Handling

Heidi segments by **role and scale**, not demographics:

| Audience | How They're Addressed |
|---|---|
| Individual clinicians | Default homepage messaging + "Clinician" plan |
| Clinics/practices | Dedicated "/for-clinics" page + "Practice" plan |
| Enterprise/health systems | Dedicated solutions + "Enterprise" plan + "Contact Sales" CTA |
| By specialty | Dedicated pages per specialty (psychologists, vets, nurses, etc.) |

The homepage speaks to individual clinicians first (the actual user), then the pricing page and nav reveal the clinic/enterprise tiers. This bottom-up strategy makes sense — win the user, then sell to the org.

### CTA Strategy

- **Primary:** "Try Heidi - it's free" — appears at least 3 times on the homepage. Low friction, high repetition.
- **Secondary:** "Contact Sales" — reserved for enterprise
- **Tertiary:** "View all" (customer stories), "Download," "Sign up"
- The free tier does heavy lifting as the entry point

### Content Patterns

| Pattern | How Heidi Uses It |
|---|---|
| **Pain quantification** | Lead with dollar amounts and time stats before showing the solution. Makes the problem concrete |
| **Compliance-first trust** | Badge wall immediately in the hero. "We know you're worried about privacy — here's proof" |
| **3-step simplification** | Transcribe > Customize > Output. Reduces a complex AI product to a simple mental model |
| **Named testimonials** | Real clinicians with name, role, specialty. Not anonymous reviews |
| **"Unbreakable" security** | Dedicated section with dramatic framing. Privacy isn't a footnote, it's a selling point |
| **Specialty-specific pages** | Each specialty gets custom messaging. "Heidi for Psychologists" hits differently than "Heidi for Surgeons" |

### What Makes It Distinctive

1. **Compliance badges in the hero.** Most SaaS sites bury these in the footer. Heidi puts them above the fold because in healthcare, trust is the first conversion barrier.
2. **Pain before solution.** The stats section ("$65K lost per year") hits before any feature explanation. Creates urgency.
3. **Bottom-up GTM reflected in site architecture.** Homepage targets the individual clinician. Enterprise is a secondary path. This mirrors their actual adoption motion.
4. **"Try Heidi - it's free" as a mantra.** Not "Start free trial" or "Get started." The phrasing is personal and low-pressure.
5. **Global from day one.** 9-region selector in the nav. Per-region compliance messaging. This is unusual for a startup-stage product.

---

## 3. Tandem (usetandem.com) — Consumer Couples App

### Site Structure

**Navigation:** Ultra-minimal.
- Logo (Tandem)
- Cart icon
- Menu (hamburger)
- **"Download"** button (App Store link)

The site is essentially a single long-form landing page. No subpages for features, pricing, or about. The entire conversion funnel lives on one scroll.

**Blog:** "Tea with Tandem" — separate content hub via Webflow.

### Hero/Homepage Approach

**Headline:** "The essential app for living together"

**Sub:** Describes four core functions — expense sharing, spending tracking, purchasing planning, and daily coordination.

**Visual:** QR code for app download + phone mockup showing the app interface. The QR code is a clever touch — reduces friction for mobile download from a desktop browser.

### Homepage Sections (in order)

1. **Hero** — headline + phone mockup + QR code + App Store badge
2. **Media logos** — TechCrunch, Forbes, People Magazine, TODAY
3. **Feature cards (4 primary + 2 secondary):**
   - Split expenses ("eliminates Venmo friction and spreadsheet management")
   - Track spending (monthly analytics by category)
   - Coordinate tasks (joint to-do list with assignment)
   - Curate wishlist (Pinterest-style saving for shared purchases)
   - Plan home purchase (affordability calculators)
   - Shared home tools
4. **App Store review carousel** — 5+ reviews with star ratings
5. **Android waitlist** — email signup ("Android app coming soon")
6. **Footer** — legal links, social media (TikTok, Instagram, LinkedIn, X, Substack), company address

### Dual Audience Handling

Not applicable in the traditional sense. But Tandem subtly addresses **both partners** — the copy speaks to "couples" as a unit while the app is downloaded individually. The tagline "Built by couples, for couples" reinforces this.

### CTA Strategy

- **Single CTA repeated:** "Download" (App Store) — appears multiple times
- **Secondary:** Android waitlist email signup
- No "pricing" page — the subscription ($10/couple/month annual, $12 monthly) is revealed in-app, not on the website
- Blog link for content engagement

### Content Patterns

| Pattern | How Tandem Uses It |
|---|---|
| **Media logos** | TechCrunch, Forbes, People, TODAY — credibility through press coverage, not user stats |
| **Anti-competitor positioning** | "Eliminates Venmo friction" — names the alternative and explains why it's worse |
| **App Store reviews** | Native reviews reproduced on the site, complete with star ratings and usernames. Feels authentic |
| **Feature-per-card** | Each feature gets a card with icon, headline, description, and screenshot. Scannable |
| **Emotional framing** | "No mental math required" / "No money fights" — solving relationship friction, not financial tooling |
| **Single-page persuasion** | Everything on one scroll. No navigation choices to make. Read top-to-bottom, download at the end |

### What Makes It Distinctive

1. **Single-page architecture.** The entire site is one scroll. No nav decisions, no subpages. Pure top-to-bottom narrative.
2. **QR code in the hero.** Bridges desktop browsing to mobile download instantly. Clever for an app-only product.
3. **Press logos over user stats.** Early-stage company leverages credibility of publications instead of user numbers they don't have yet.
4. **Anti-competitor copy.** "Eliminates Venmo friction and spreadsheet management" — directly names the status quo tools and positions against them.
5. **Pricing hidden from website.** No pricing page. Removes a potential objection and lets the app experience sell the subscription.
6. **"Built by couples, for couples."** The tagline positions founders as users — authenticity play.

---

## 4. Polarsteps (polarsteps.com) — Consumer Travel App

### Site Structure

**Navigation:**
- Search (destinations and profiles)
- Login / Create account (Facebook or email)
- Sidebar with: Account settings, Explore, FAQ, Travel Book info/pricing, Help center, Social links (Instagram, Facebook, Twitter), About page

**Key pages:**
- Homepage (app showcase)
- Travel Book page (monetization)
- Download page
- Explore / community
- About / Our Story
- Support / Help Center
- Blog (news.polarsteps.com)

### Hero/Homepage Approach

**Headline:** "Plan, Track & Relive Your Trips"

**Tagline:** "Explore. Dream. Discover."

The hero features a **background video** playing travel content, with a short description overlaying it and app store download buttons. Below, a sample interactive map shows a real traveler's route.

The three-word framework ("Plan, Track, Relive") structures the entire homepage and product narrative.

### Homepage Sections (in order)

1. **Hero** — video background + headline + app download CTAs
2. **Sample map** — pinned route displaying an example traveler's journey
3. **Plan section** — Itinerary Planner, Transport Planner, AI-powered itinerary builder, Polarsteps Guides
4. **Track section** — automatic GPS tracking, photos/videos/thoughts added to steps, digital world map
5. **Relive section** — scroll through memories, travel stats, Trip Reels (shareable video), Travel Book
6. **Community/social proof** — staff-picked profiles, explore section
7. **Travel Book promo** — premium product showcase
8. **Download CTA** — app store badges
9. **Footer** — social links, about, help

### Dual Audience Handling

Polarsteps is purely consumer. No B2B play. However, they have an implicit dual audience:
- **Active travelers** (the core user — plans and tracks trips)
- **Memory preservers** (the monetization target — buys Travel Books after the trip)

The homepage narrative mirrors this: Plan/Track appeals to active travelers, Relive/Travel Book appeals to memory preservers.

### CTA Strategy

- **Primary:** Download the free app (App Store + Google Play badges, repeated)
- **Secondary:** Travel Book purchase (monetization CTA)
- No signup wall — the app is free, Travel Book is the revenue model
- "Join 19M+ travelers" — social proof embedded in the CTA itself

### Content Patterns

| Pattern | How Polarsteps Uses It |
|---|---|
| **Video hero** | Moving travel footage creates emotional pull. Not a static image or text |
| **Interactive map sample** | Shows a real route on a real map. The product IS the demo |
| **Three-word framework** | "Plan, Track, Relive" — entire product narrative in 3 words, used as section headers |
| **User number** | "19M+ travelers" — massive social proof stat woven into CTAs and headlines |
| **Physical product upsell** | Travel Book converts digital memories into a premium physical product (EUR 36-150) |
| **Staff-picked profiles** | Curated community content shows what the product looks like when used well |
| **Feature → emotional outcome** | "Automatically track your path" → "a beautiful world map that is unique to you" |

### What Makes It Distinctive

1. **Product-as-demo homepage.** The interactive map on the homepage IS the product. Users see a real trip visualized before downloading anything.
2. **Three-word narrative architecture.** "Plan, Track, Relive" structures the entire site, the app, and the product story. Everything maps to one of three words.
3. **Freemium with physical upsell.** The app is free. Revenue comes from Travel Books (physical photo albums auto-generated from trip data). This is unusual — digital free, physical paid.
4. **Video hero creates wanderlust.** The emotional hook isn't a headline — it's moving footage of travel. The site makes you want to go somewhere.
5. **19M users as social proof.** For a consumer app, raw user count is the most compelling proof. They lead with it.
6. **AI itinerary builder.** Recent addition — converts Polarsteps from a passive tracker into an active planning tool, increasing pre-trip engagement.

---

## Cross-Site Pattern Comparison

| Dimension | Hims | Heidi Health | Tandem | Polarsteps |
|---|---|---|---|---|
| **Nav items** | 2 (Shop, Learn) | 7 + actions | 1 (Download) | Search + sidebar |
| **Hero approach** | Editorial imagery + category scroll | Headline + compliance badges + stats | Phone mockup + QR code | Video background + map |
| **Primary CTA** | "Get started" (black box) | "Try Heidi - it's free" | "Download" (App Store) | Download app |
| **Social proof type** | Subscriber count (2.5M) | Pain stats + named testimonials | Press logos + App Store reviews | User count (19M) |
| **Audience split** | Separate domains per gender | Role-based (clinician/clinic/enterprise) | N/A (couples as unit) | Implicit (active travelers vs. memory preservers) |
| **Content depth** | Deep (blog, education, categories) | Deep (specialties, success stories, resources) | Shallow (single page) | Medium (Plan/Track/Relive sections) |
| **Trust mechanism** | Subscriber count + medical expertise | Compliance badges + named clinicians | Press coverage + real reviews | Massive user base + community |
| **Monetization visibility** | Products priced on site | Pricing page with 4 tiers | Hidden (in-app only) | Travel Book pricing separate |
| **Distinctive move** | Magazine aesthetic for healthcare | Compliance badges above the fold | Single-page narrative | Product-as-demo (interactive map) |

---

## Key Takeaways for Ditto Care

### Patterns worth stealing:

1. **Hims' navigation simplicity.** Don't build a complex nav because you have complex content. Force clarity through constraints.

2. **Heidi's compliance-first hero.** For a healthcare product, trust badges above the fold are table stakes. Ditto should consider leading with GDPR/medical compliance visual proof.

3. **Heidi's pain quantification.** Leading with "50% of clinicians' time wasted" before showing the solution creates urgency. What's Ditto's equivalent? ("X% of patients forget medical advice within 24 hours"?)

4. **Tandem's anti-competitor positioning.** Naming the status quo ("eliminates Venmo friction") is more persuasive than abstract benefit claims. What's Ditto's version? ("No more Googling your symptoms after a doctor visit"?)

5. **Polarsteps' product-as-demo.** If you can show the actual product working on the homepage, it beats any description. Can Ditto show a real (anonymized) consultation summary as a live demo?

6. **Heidi's bottom-up architecture.** Homepage targets the end user (clinician), not the buyer (clinic admin). Ditto's homepage should target patients, not hospitals.

7. **Three-word frameworks.** "Plan, Track, Relive" (Polarsteps) and "Transcribe, Customize, Output" (Heidi) make complex products instantly understandable. What's Ditto's three words?

### Patterns to avoid:

1. **Over-complex navigation early.** Wait until you have the content to justify 7+ nav items.
2. **Generic SaaS "Hero + Features + Testimonials + CTA" layout.** Every site above breaks this template in a distinctive way.
3. **Hiding trust signals.** In healthcare, compliance and privacy are conversion drivers, not footer details.
4. **Pricing on the homepage when the product is early.** Tandem hides it entirely. Polarsteps separates it. Both work for different reasons.
