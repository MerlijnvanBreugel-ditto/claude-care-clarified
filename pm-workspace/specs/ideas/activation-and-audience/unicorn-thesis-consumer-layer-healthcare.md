# The Consumer Layer in Healthcare — Unicorn Thesis

**Date**: 2026-03-22
**Status**: Strategic brainstorm — VC perspective
**Context**: What would it take for Ditto to become a billion-euro company?

---

## The Premise

There is no consumer product that helps people navigate healthcare. Banking has Revolut. Women's health has Flo. Fitness has Strava. Healthcare — the domain that generates more anxiety, information overload, and coordination burden than any other — has your hospital's patient portal from 2008.

**Why?** Three structural barriers have prevented this:

| Barrier | Why it blocked progress | What's changing |
|---|---|---|
| **Fragmented data** | Every provider has their own system. No aggregation possible without 1000 integrations. | EHDS (European Health Data Space) — entered into force March 2025. Patient-portable health records across the EU by 2029. |
| **Episodic usage** | People only think about health when sick. Hard to build habits. | AI changes this — proactive, contextual, always-on value between episodes. |
| **Trust** | Healthcare data is the most sensitive. People won't give it to a random app. | Trust is earned at vulnerable moments. The app that helps you through cancer earns trust no ad campaign can buy. |

All three barriers are weakening simultaneously. The window is opening.

---

## What Ditto Already Does Well

Before mapping the future, it's worth grounding in what's already working:

- **Conversation recording + AI summarization**: The core product. Produces patient-friendly summaries that users value immediately.
- **Document explanation**: Users can photograph letters, lab results, and medical documents — Ditto explains them in plain language. This already extends value beyond the appointment.
- **Proven domains**: Cancer (oncology) and cardiology are the two dominant use cases. Most summaries come from these domains. This isn't hypothetical product-market fit — it's observed.
- **35,000+ users**: Early traction with organic pull, especially in high-stakes care journeys.
- **Menzis partnership**: 2M-member insurer partnership — proof that B2B2C works.

The foundation exists. The question is how to compound it.

---

## The Competitive Landscape (March 2026)

### Big Tech is moving fast

| Player | Move | Positioning |
|---|---|---|
| **Apple** | Health+ AI Coach (launching 2026) | Wearable data + wellness coaching. General health, not care journeys. |
| **OpenAI** | ChatGPT Health + Torch Health acquisition ($100M) | Health data interoperability + general-purpose health Q&A. |
| **Microsoft** | Copilot Health (launched March 2026) | Aggregates wearable + EHR + lab data. Enterprise-adjacent. |
| **Google** | b.well partnership + Health AI features | Health records + search-based health answers. |

**What they all have in common**: They're building **personal health AI** — an individual interacting with a general-purpose AI about their health. One person, one chatbot, one screen.

**What NONE of them are building**: The social layer. The coordination layer. The shared understanding between patient and family. They're solving "I want to understand my health" — not "we need to navigate this together."

### Existing care coordination platforms

| Player | What they do | Limitation |
|---|---|---|
| **CaringBridge** | Health journey blog + support coordination. ~900K patients. | Not AI-native. Not European. Blog format — broadcast, not coordination. No health data integration. |
| **Lotsa Helping Hands** | Care calendar + task coordination for caregivers. | Logistics tool, not understanding tool. No AI, no health context. |
| **Patient portals** | Provider-specific health records + messaging. | Fragmented (one per provider), terrible UX, provider-centric not patient-centric. |

### European health unicorns

| Company | Model | Why it's not this |
|---|---|---|
| **Doctolib** (~€6B) | Appointment booking + telemedicine. B2B2C. | Access layer — what happens BEFORE the appointment. |
| **Alan** (~€4B) | Health insurance + benefits platform. B2B. | Payment layer. |
| **Kry/Livi** | Telemedicine. B2C/B2B. | Virtual access. |
| **Neko Health** ($1.8B) | AI-powered preventive body scans. B2C. | Detection, not navigation. One-time moments, not journeys. |

**The gap**: Nobody is building the layer between "I have access to healthcare" and "I understand what's happening and the people around me can help." That's the consumer layer.

---

## What Problem Are We Actually Solving?

Not "I want to be healthier" (wellness). Not "I need to see a doctor" (access). Not "I want to track my fitness" (quantified self).

**The problem: When healthcare gets serious, people are lost, overwhelmed, and alone — and so is everyone around them.**

### Who experiences this most acutely?

| Segment | Intensity | Duration | Circle size | EU population at any time |
|---|---|---|---|---|
| **Cancer patients + circle** | Extreme | Months-years | 3-7 people | ~18M patients + ~70M circle members |
| **Chronic condition escalation** | High | Ongoing | 2-5 people | ~50M patients + ~150M circle |
| **New parents** | Moderate-high | 12-18 months | 3-6 people | ~10M parents/year + ~30M circle |
| **Cognitive decline (patient + family)** | High, increasing | Years | 3-8 people | ~10M patients + ~50M circle |
| **Serious acute events** | Very high, short | Weeks-months | 3-5 people | ~15M/year + ~50M circle |

**Key math**: In the EU (~450M adults), roughly **80-100M people are in a care journey at any given time**. Each involves **3-5 circle members**. That's potentially **250-400M people** who could benefit — not as "health app users" but as people navigating care together.

### Are they looking for a solution?

**Yes, but they don't know what to look for.** They're currently solving this with:
- WhatsApp groups ("papa's gezondheid")
- Phone calls where the patient retells everything
- Shared Google Docs with medication lists
- One family member who becomes the unofficial "project manager"
- Forgetting, miscommunicating, and suffering in silence

They're not searching for "care coordination software." They're searching for "how to help my mom with cancer" or "what did the doctor mean by stage 3b" or "how to talk to my dad about his diagnosis." The need is huge. The category doesn't exist yet.

### Why hasn't this been solved?

| Reason | Detail |
|---|---|
| **Data fragmentation** | Until EHDS, you couldn't aggregate health data across providers without building integrations with every hospital system in every country. |
| **The chicken-and-egg problem** | You need health context to be useful, but you need users to get health context. AI breaks this — you can generate value from a conversation recording, a letter photo, a voice narrative. |
| **Trust** | Healthcare data trust must be earned, not bought. This means slow initial growth, which doesn't fit the VC playbook of "grow fast then monetize." |
| **Episodic = hard to monetize** | If usage spikes during illness and drops after, LTV is hard to predict. The care circle model breaks this — patients come and go, but circle members persist across multiple journeys. |
| **Regulation** | GDPR, medical device regulations, country-specific health data laws. Real barriers but also real moats once you've navigated them. |

---

## What Should the Solution Look Like?

### Core thesis: It's a graph, not a chatbot

The defensible asset is not the AI (Big Tech will commoditize that). It's not the content (everyone has medical knowledge). It's not the features (features can be copied).

**The defensible asset is the Care Graph** — the map of who cares about whom, what they need to know, and how they coordinate. This is the social graph of healthcare. It doesn't exist anywhere today.

```
                    ┌──────────────┐
                    │   Patient    │
                    │  (source of  │
                    │   context)   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────┴─────┐ ┌───┴───┐ ┌─────┴─────┐
        │  Partner   │ │ Child │ │  Sibling  │
        │ (daily,    │ │(weekly│ │ (monthly, │
        │  full      │ │ key   │ │  emotional│
        │  context)  │ │ updates│ │  support) │
        └───────────┘ └───────┘ └───────────┘
              │                       │
         ┌────┴────┐            ┌─────┴─────┐
         │ Parent  │            │  Friend   │
         │ of the  │            │ (check-in │
         │ partner │            │  support) │
         └─────────┘            └───────────┘
```

**Every person in the graph has different information needs, different access rights, different emotional proximity.** The partner needs everything. The friend abroad needs high-level updates. The sibling needs to know when practical help is needed. No existing product models this.

### Product architecture

Three layers, each building on the previous:

**Layer 1: Intelligence (AI engine)**
- Transforms raw healthcare moments (conversations, letters, lab results, voice narratives) into structured, understandable information
- This is the input layer. It's powerful but it's NOT the moat — it's what everyone else is also building

**Layer 2: Memory (care journey)**
- The longitudinal record of a person's health journey — across providers, across time, across document types
- This accumulates value: the more Ditto knows about your journey, the more contextual everything becomes
- EHDS makes this vastly more powerful — health data portability means Ditto can become the single pane of glass

**Layer 3: Connection (care graph)**
- The social layer that distributes understanding across the circle
- This is where the network effects live and the real moat forms
- Each patient creates value for 3-7 circle members. Each circle member is a future patient (or already following another patient)

### How social should it be?

**Not social-media social. Inner-circle social.** Think private family group, not public feed.

| Social model | What it looks like | Right for Ditto? |
|---|---|---|
| **Broadcast** (CaringBridge) | Patient posts updates, circle reads. One-to-many. | Partially — but passive. Circle is just an audience. |
| **Community** (Reddit, support groups) | Strangers sharing experiences. Many-to-many. | No — this isn't Ditto's strength. Others do it well. |
| **Coordination** (Lotsa Helping Hands) | Task management — who's bringing food, who's driving. | Adjacent — practical but doesn't require Ditto's AI. |
| **Shared understanding** (nothing exists) | Circle members have contextual, personalized access to the patient's journey. They understand what's happening, what's coming, and what they can do. Not broadcasting — translating. | **YES. This is the gap.** |

The key insight: **different people in the circle need different things at different times.** The partner needs the full summary. The elderly parent needs the simplified version. The friend abroad needs the emotional check-in. The sibling who's a doctor needs the clinical detail.

Ditto's social layer is not "share one post to everyone." It's **contextual distribution of understanding** — the right information, to the right person, in the right format, at the right time.

This is a fundamentally different kind of social product. Not about engagement or content creation. About **reducing the cognitive and emotional burden of caring.**

### How AI-native should it be?

**AI should be invisible infrastructure, not the interface.**

The risk you identified is real: if the product IS an AI chatbot, you're competing with Google, Apple, OpenAI, and Microsoft — all of whom have more data, more compute, and more distribution. You lose.

**The strategic positioning:**

| Approach | Description | Defensibility | Risk |
|---|---|---|---|
| **AI as feature** | Summaries, explanations, Q&A. AI does specific things. | Low — features get copied in months. | Commoditization |
| **AI as interface** | Everything through a chat/voice AI. "Talk to your health AI." | Low — this is exactly what Big Tech is building. | Direct competition with $T companies |
| **AI as agent** | Proactive AI that manages your health: reminds, suggests, coaches. | Medium — but "health coach" is everyone's pitch. | Crowded, undifferentiated |
| **AI as connective tissue** | AI that makes the care graph work — transforms raw health moments into structured understanding, then distributes it contextually across the circle. The AI is not what you interact with. It's what makes interaction unnecessary. | **High** — tied to your unique data (care graph + journey history), improves with network density. | Requires the graph to exist first |

**Recommendation: AI as connective tissue.** The AI doesn't talk TO you (like ChatGPT Health). The AI talks BETWEEN you — it translates the doctor's words into a summary the patient understands, then into an update the partner can act on, then into a simplified version the elderly parent can follow.

The AI's job is not to be smart. It's to make the care graph smart.

**One exception: the contextual chatbot.** There IS a place for a conversational AI interface — but only when it operates on the care graph, not on general knowledge. "Ask follow-up questions about mom's summary" is fundamentally different from "ask ChatGPT about cancer." One has context, the other has knowledge. Context wins for care circles.

This is a frequently heard request from users: the ability to ask follow-up questions about a summary. "What did the doctor mean by 'we'll monitor the markers'?" — answered using the actual conversation context, the patient's history, and their specific situation. This chatbot isn't competing with Big Tech because it's useless without Ditto's data. It's a care-graph-native interface, not a general-purpose one.

**Concrete example**: Patient records oncologist visit. Ditto AI:
1. Creates structured summary for patient (Clarity)
2. Extracts key decisions and next steps (Convenience)
3. Generates partner-appropriate update: full context + action items
4. Generates child-appropriate update: key info + how parent is feeling
5. Generates friend-appropriate update: high-level status + what would help
6. Flags medication change to circle member who manages the medication list
7. Prepares questions for the follow-up appointment based on what was discussed

None of this requires the user to "talk to an AI." The AI works behind the scenes on the care graph. This is **defensible** because it requires both the AI AND the graph AND the journey history. Big Tech has #1 (better AI) but not #2 or #3.

---

## The 50+ Audience: Constraint and Advantage

Ditto's primary users are 50+. This shapes everything about how the product should feel.

**The constraint**: This audience is behind on AI adoption. Interfaces that feel "techy" — chatbots, voice assistants, complex settings — create anxiety rather than confidence. The product must feel safe, not smart.

**The advantage**: Because this audience hasn't been saturated by AI tools, every AI feature feels magical. What's "table stakes" for a 30-year-old ChatGPT user is a genuine wow moment for a 60-year-old cancer patient seeing their doctor's words turned into a clear summary. The bar for impressive is lower, which means simpler AI features land harder.

**Design implication: voice as input, visual as output.**

| Voice mode | Feels like | 50+ comfort level |
|---|---|---|
| **Recording a conversation** | "I'm capturing what happens" — like a voice recorder | High — passive, familiar concept |
| **Telling Ditto about your health** | "I'm talking to my phone" | Medium — needs framing as "tell your story" not "talk to AI" |
| **Voice AI interface** (Siri-like) | "I'm talking to a robot" | Lower — can feel uncanny for sensitive topics |

The sweet spot: the patient speaks naturally, Ditto shows what it understood — structured, readable, tappable cards on screen. This feels like "Ditto listened to me" rather than "I'm using AI." Voice removes the typing barrier that's real for elderly users. Visual output provides the control and confirmation they need.

**Strategic implication**: Don't compete on AI sophistication. Compete on AI that feels human, safe, and personally relevant. The 50+ audience won't compare Ditto to ChatGPT — they'll compare it to "calling my daughter to explain what the doctor said." That's the bar to beat.

---

## Data Completeness: The Fragmentation Challenge

### The problem

The care graph is only as valuable as the data flowing through it. If Ditto only captures recorded conversations, it has a subset of the patient's health information. Letters, lab results, portal messages, pharmacy interactions, phone calls with the hospital — all of this lives elsewhere and requires manual effort to bring in.

If data entry burden is too high, patients stop inputting, and the graph goes dark. This is a real risk to the entire thesis.

### The reframe: care understanding, not clinical completeness

There's a crucial difference between what's needed:

| Goal | What it requires | Who needs it |
|---|---|---|
| **Clinical completeness** | Every lab value, medication dose, scan report | The EHR / hospital system |
| **Care understanding** | What happened, what it means, what's next, how I'm feeling | The patient and their circle |

Ditto's job is care understanding, not clinical completeness. For a partner to feel informed, they need the summary of the oncologist visit + "they're changing the chemo protocol" + "next scan in 6 weeks." They do NOT need the lab values or medication dosages.

### Data sources and how they get into Ditto

| Data source | How it gets in | Current status | Effort level |
|---|---|---|---|
| **Doctor conversations** | Recording (press one button) | Core feature, works well | Very low |
| **Letters & documents** | Document scan (photograph) | Exists, produces explanations | Low — but requires remembering |
| **Lab results** | Photo → AI extraction | Extension of document scan | Low |
| **Medication changes** | Voice capture: "They changed my meds to X" | Not yet built | Very low (10 seconds) |
| **Portal information** | Screenshot → AI extraction | Not yet built | Medium |
| **Quick updates** | Voice: "I called the hospital, surgery moved to April 15" | Not yet built | Very low |
| **Full health records** | EHDS patient data portability | 2029 — automatic | Zero (once connected) |

### The 80/20 rule applies

Conversations + documents + occasional voice input captures ~80% of what the care circle needs to understand. The remaining 20% (detailed lab values, portal messages, pharmacy records) matters for clinical management but less for shared understanding.

### Five mitigations for the effort problem

1. **Primary action is already effortless**: Recording a conversation = one button press. This is the highest-value input and it's already solved.

2. **Smart prompting after events**: After creating a summary, Ditto asks one question: "Did you also receive any letters or results from this visit?" — captures adjacent data while the moment is fresh.

3. **Care circle as input multiplier**: The daughter who reads the portal adds the lab results. The partner who goes to the pharmacy adds the medication change. The graph doesn't depend on the patient alone — the circle contributes.

4. **Voice for everything that isn't a document**: Quick voice updates ("the appointment is moved," "I'm feeling better today," "they prescribed a new medication") take 10 seconds and capture context no other tool gets.

5. **Declining effort over time**: As journey history builds, Ditto needs less input to be contextual. Early in the journey = more effort. Later = Ditto already knows the context and can infer more.

### EHDS as the long-term unlock

When EHDS patient data portability goes live (priority categories by 2029), the data completeness problem largely resolves. Patient summaries, prescriptions, and key clinical data flow automatically with patient consent. Ditto becomes the interpretation and sharing layer on top of standardized EU health data.

**Until then**: The AI input layer (recording + documents + voice) is the bridge. It's "good enough" for care understanding, and each new input type reduces the remaining gap.

---

## The Moat (Defensibility Stack)

Listed in order of strength:

| Layer | What it is | Switching cost | Competitive advantage |
|---|---|---|---|
| **1. Care graph** | Who cares about whom, what they know, what they need. | Very high — you can't export your family's care coordination. | Nobody else has this. Big Tech has social graphs but not CARE graphs. |
| **2. Care journey history** | Longitudinal record of summaries, documents, decisions, symptoms across months/years. | Very high — accumulated context can't be recreated. | Gets more valuable over time. Every new data point enriches everything before it. |
| **3. Trust** | Earned during the most vulnerable moments of people's lives. | Extremely high — you don't switch health tools mid-crisis. | Trust earned at the bedside > trust bought with ads. |
| **4. EHDS first-mover** | First to integrate patient-portable health data across EU. | Medium-high — regulatory navigation takes years. | Regulatory moat. The compliance cost IS the barrier. |
| **5. Network density** | Each patient → 3-7 circle members. Each circle member → future patient connections. | Increasing with density — hard to leave when your whole family is on it. | Cross-journey network effects: the sibling following dad's dementia journey later brings their own pregnancy journey. |

**Why Big Tech can't easily replicate this:**
- Apple/Google/OpenAI build for individuals. The care graph is fundamentally multi-user with asymmetric information needs.
- They optimize for engagement. Ditto optimizes for reducing burden — the best outcome is the circle member who doesn't need to open the app because they already know what's happening.
- They can't build trust at the bedside through a general-purpose assistant. Trust in healthcare is earned through specificity, not capability.

---

## Business Model at Scale

### Revenue streams (layered, not exclusive)

| Stream | Model | When | Size potential |
|---|---|---|---|
| **B2C Subscription** | Freemium: record + summarize free. Premium: full circle, document understanding, journey overview, advanced AI features. | Now | €5-15/month. 10M paying users = €600M-1.8B ARR. |
| **B2B2C (Insurers)** | Insurers pay for member access (like Menzis today, scaled EU-wide). Ditto reduces readmissions, improves adherence, enables value-based care. | Now-Next | Per-member-per-month. 50M insured lives × €1-3/month = €600M-1.8B. |
| **EHDS data services** | With patient consent, aggregate anonymized care journey data for research, pharma, policy. Secondary use under EHDS Article 33+. | 2028+ | Significant but regulatory-dependent. |
| **Provider partnerships** | Hospitals/clinics offer Ditto to patients as part of care. Improves patient experience scores, reduces follow-up call volume. | Next | Per-patient or site license. |

### The insurer angle is the EU growth accelerator

Unlike the US, EU healthcare runs through insurers/national health systems. In the Netherlands, Germany, France — if you partner with a major insurer, you get distribution to millions overnight. Menzis (2M members) is the proof case. Scale to 3-5 major EU insurers and you have 20-50M potential users with zero acquisition cost.

The pitch to insurers: "Your members who use Ditto have higher treatment adherence, fewer unnecessary follow-up calls, better self-reported outcomes, and lower readmission rates. Pay us €2/member/month."

---

## GTM: How to Get from 35K to 10M

### Phase 1: Own cancer + cardiology in the Netherlands (Now → 12 months)
**Goal**: Become the standard tool for serious care journeys in NL

- Two proven domains: cancer (oncology) and cardiology already generate most summaries — go deep here first
- Deepen product for these journeys (beyond recording: document explanation already works, add symptoms, journey overview, appointment prep)
- Menzis partnership: activate cancer and cardiology patients specifically within their 2M member base
- Hospital partnerships: 5 major oncology/cardiology departments distribute Ditto at diagnosis
- Care circle flywheel: every patient brings 3-5 circle members
- NL cancer population: ~120K new diagnoses/year. Cardiology adds significant volume. With circle: ~500K+ potential users/year.
- Target: 50-100K active users (patients + circle)

### Phase 2: Expand life moments + first EU markets (12-36 months)
**Goal**: Prove the model works across life moments and languages

- Add serious chronic conditions + cognitive decline
- Launch in Germany (largest EU market, strong insurance system, cultural similarity)
- Launch in France or Belgium (francophone, strong insurer ecosystem)
- EHDS preparation: build the data portability infrastructure before mandate
- Target: 500K-1M active users across 3 markets

### Phase 3: EU-wide + EHDS integration (36-60 months)
**Goal**: Become the consumer health layer for the EU

- EHDS goes live for priority categories (2029): Ditto is ready to ingest patient summaries, prescriptions
- Major insurer partnerships in 5+ countries
- Platform expansion: third-party integrations, specialized care journey modules
- Target: 5-10M active users, operating in 10+ EU markets

### The network effect math

```
Year 1: 1 cancer patient → 4 circle members = 5 users
         10K patients = 50K users (NL only)

Year 2: 50K users. Some circle members become patients (pregnancy, own health).
         20% of circle members create own journey = 10K new patients.
         10K × 4 circle = 40K new users.
         Total: ~90K users (compound growth begins)

Year 3: Cross-market. 3 countries. Insurer distribution.
         500K users, growing 3-4x annually.

Year 5: EHDS live. 10+ markets. 5M+ users.
         At 5M users: ~€50-100M ARR (mixed B2C + B2B2C)
         Growth rate: 2-3x annually
         Unicorn valuation: 10-20x ARR = €500M-2B
```

---

## Key Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| **Big Tech builds the care graph** | High | Speed. Big Tech moves slowly in healthcare due to regulation and trust. Ditto has 2-3 year head start on the care graph. Also: Big Tech builds for billions, not for the nuances of Dutch/German/French healthcare. |
| **EHDS delayed or watered down** | Medium | Don't depend on it for Phase 1-2. Build the AI input layer (recording, documents, voice) as the data source. EHDS is an accelerator, not a prerequisite. |
| **Insurers are slow to adopt** | Medium | Prove with Menzis first. Hospital partnerships as parallel channel. B2C growth creates pull ("your members are already using this"). |
| **Care graph doesn't create switching costs** | Medium | The graph alone isn't sticky — the journey HISTORY is. Once you have 18 months of cancer treatment context in Ditto, you can't recreate that elsewhere. |
| **Regulatory complexity across EU** | High | Start with NL/DE/FR — similar regulatory frameworks. Build compliance infrastructure once, adapt per market. Regulatory expertise becomes part of the moat. |
| **AI commoditization** | Near-certain | This is WHY the moat is the graph, not the AI. Use best-available AI (swap models as they improve), differentiate on what the AI operates ON (your data) and FOR (the care graph). |
| **Data completeness / input burden** | High | Care understanding ≠ clinical completeness. Recording + documents + voice captures ~80% of what circles need. Care circle members contribute as input sources. Smart prompting reduces friction. EHDS resolves the rest by 2029. |
| **50+ audience limits AI feature adoption** | Medium | Flip the constraint: compete on AI that feels human and safe, not sophisticated. Voice input + visual output. Every AI feature is a wow moment for this audience — lower bar, higher delight. |

---

## What Makes This a Unicorn, Not Just a Good Business

A good business solves a problem for a defined audience. A unicorn creates a new category with compounding network effects.

**Ditto's unicorn ingredients:**

1. **Massive TAM**: 250-400M people in the EU are in or adjacent to a care journey at any time. Not "total addressable" in theory — people with real, acute need.

2. **Network effects**: Every patient brings 3-7 circle members. Circle members bring their own journeys. The care graph compounds.

3. **Regulatory tailwind**: EHDS is the EU actively building the infrastructure Ditto needs. This is government-mandated interoperability creating a new market.

4. **Moat that deepens with time**: Care journey history + care graph + trust. More users = more data = better AI = more value = more users. Classic data flywheel, but with the added stickiness of life-moment trust.

5. **Multiple revenue streams**: Not dependent on a single model. B2C + B2B2C + data + provider = diversified and resilient.

6. **The emotional hook**: People don't switch health tools mid-cancer-treatment. The emotional cost of leaving is enormous. This creates LTV that SaaS companies dream of.

7. **Timing**: Big Tech just entered consumer health AI (Q1 2026). They're building general-purpose tools. There's a 2-3 year window to build the care-specific social layer before they figure out it matters.

---

## The One-Line Pitch

**To a VC**: "Ditto is building the consumer layer for healthcare in Europe — the care graph that connects patients and families through serious health journeys. We start with AI-powered understanding and expand through the social graph of care, timed with EHDS making health data portable across the EU."

**To a patient**: "When healthcare gets serious, Ditto makes sure you understand what's happening and the people around you can help."

**To an insurer**: "Your members who use Ditto stay informed, share with family, and navigate care more effectively — reducing your support costs and improving outcomes."

---

## Open Strategic Questions

1. **How fast can the care graph grow organically?** The 1-patient-to-4-circle math only works if circle members actually onboard. What's the realistic conversion rate?

2. **Is the insurer channel a growth engine or a dependency?** If 80% of users come through insurers, Ditto becomes a B2B2C company — different valuation dynamics than a true consumer company.

3. **When to expand beyond care journeys?** The "consumer health OS" is the long-term vision, but premature expansion kills focus. What's the signal that cancer/serious illness is "owned" enough to expand?

4. **Language and localization**: Healthcare is deeply local. Dutch oncology terminology, German insurance structures, French patient rights. How to scale without losing the specificity that builds trust?

5. **Funding path**: EU health tech Series A is typically €5-15M. Is there enough traction at 50-100K users to raise a strong Series A, or does Ditto need to reach Phase 2 milestones first?

---

## Sources

- [European Health Data Space Regulation - EC](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)
- [EHDS Implementation Timeline - EHTEL](https://ehtel.eu/activities/ehtel-on-the-ehds/european-health-data-space-regulation-a-brief-overview-of-timelines.html)
- [OpenAI launches ChatGPT Health - Fortune](https://fortune.com/2026/01/07/openai-launches-chatgpt-health-in-a-push-to-become-a-hub-for-personal-health-data/)
- [Apple Health+ AI Coach 2026](https://apple.gadgethacks.com/news/apple-health-ai-coach-launches-2026-what-to-expect/)
- [Microsoft Copilot Health - Fortune](https://fortune.com/2026/03/12/microsoft-copilot-health-ai-medical-personal-health-data/)
- [Europe's potential HealthTech Unicorns 2026](https://www.healthcare.digital/single-post/europe-s-potential-healthtech-and-medtech-unicorns-in-2026)
- [The 2026 Convergence: Big Tech + Healthcare](https://www.healthcare.digital/single-post/the-2026-convergence-big-tech-agentic-ai-and-the-restructuring-of-the-global-healthtech-ecosystem)
- [Where's Europe's next digital health unicorn? - Sifted](https://sifted.eu/articles/europe-digital-health-unicorn-hlth)
- [Care Coordination Software Market - Verified Market Research](https://www.verifiedmarketresearch.com/product/care-coordination-software-market/)
