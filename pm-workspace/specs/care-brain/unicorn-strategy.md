# The Unicorn Play: Ditto's Path from Summarization Tool to Billion-Dollar Care Intelligence Platform

**Date**: 2026-04-12
**Status**: Strategic draft
**Author**: Mewtwo (PM Co-Pilot)
**Method**: Virtual founding team stress-test + synthesis
**Parent**: [Care Brain Strategy](care-brain-strategy.md) (approved)

---

## The Thesis in One Sentence

AI is crude oil. Everyone has access to it. The companies that win are the refineries that turn raw intelligence into a specific, invisible, indispensable product for a specific person in a specific moment. Ditto's refinery turns medical conversations into shared understanding across care circles. No one else is building this.

---

## The Virtual Founding Team

Six personas, each modeled on a founder whose company crossed $1B+ by solving a specific product-market truth. They're here to stress-test the Care Brain strategy, identify what's missing, and chart the path from 35K users to unicorn.

| Seat | Persona | Modeled After | What They Bring |
|---|---|---|---|
| **Product Vision** | Kevin | Kevin Systrom (Instagram) | Radical simplification, emotional design, three-tap product thinking |
| **Domain & Trust** | Andy | Andy Puddicombe (Headspace) | Making an intimidating domain feel safe, voice/persona, habit formation |
| **Engineering Philosophy** | Jan | Jan Koum (WhatsApp) | Privacy-first architecture, zero friction, anti-bloat, extreme efficiency |
| **Platform & Growth** | Daniel | Daniel Ek (Spotify) | Invisible AI, data-driven personalization, freemium economics, network effects |
| **AI-Native Builder** | Anton | Anton Osika (Lovable) | AI as primary builder, rapid shipping, non-technical user focus, build-in-public |
| **Capital Strategy** | Sarah | Composite healthcare VC (Rock Health / a16z Bio / General Catalyst) | Investment thesis, milestone sequencing, moat validation, Series A readiness |

---

## Round 1: Each Founder's Diagnosis

### Kevin (Product Vision)

**What Instagram taught me**: We launched as Burbn, a bloated check-in app. It failed. We cut everything except photos, likes, and comments. Instagram took off when we made one thing magical, not ten things functional.

**Diagnosis of Ditto**: You have a strong core action (record appointment, get summary). That's your "photo." But your strategy doc lists 6 pipelines, 7 interface surfaces, 91 tickets across 12 weeks. That's Burbn energy.

**The hard question**: What is Ditto's "filter moment"? Instagram's filters turned bad phone photos into art. They gave people a reason to share. What's the equivalent? It's not the summary. It's what happens AFTER the summary. The moment where a patient taps a suggestion and gets an answer that references what their doctor said three months ago, and they think: "Ditto actually knows me." That's the emotional unlock.

**My prescription**:
1. Kill the 7-surface strategy for launch. Ship ONE magical surface first: the summary that anticipates your questions.
2. The "share" button is your cross-post to Twitter. When a patient can send a one-tap adapted update to their daughter, that's your distribution moment. Prioritize it ruthlessly.
3. Square crop thinking: constrain the interface so severely that there's nothing to be confused by. One column. One action per screen. The Corrie test is your compass.

---

### Andy (Domain & Trust)

**What Headspace taught me**: Meditation had an image problem. Too mystical, too hard, too weird. We made it feel like a gym membership. The breakthrough was making the first experience so simple and non-threatening that people who'd never meditated would try it. "Take 10" (10 minutes, 10 days) was the onboarding breakthrough.

**Diagnosis of Ditto**: Healthcare AI has the same image problem meditation had. People hear "AI" and think either "robot making medical decisions" or "ChatGPT giving me wrong health advice." You need to erase both associations entirely.

**The hard question**: What's Ditto's "Take 10"? You need a first experience so simple and trustworthy that the most skeptical 70-year-old cancer patient thinks: "Oh. This is just... helpful." Not "this is AI." Not "this is technology." Just: helpful.

**My prescription**:
1. The first summary a patient ever sees defines the entire relationship. It must be perfect. Not just accurate. Warm. Clear. Attributed to THEIR doctor by name. Invest disproportionately in this moment.
2. Create your own Andy Puddicombe. Headspace IS Andy's voice. Ditto needs a consistent voice/persona. Not a chatbot persona. A tone. A way of speaking. Like a trusted friend who was there at the appointment and explains things clearly. This voice must be consistent across every surface.
3. "Take 10" for Ditto: one recording, one summary, one suggestion tapped, one "oh wow" moment. If that sequence doesn't happen in the first session, nothing else matters.
4. The word "AI" should never appear in the user-facing product. Not once. It's "Ditto prepared this for you." It's "Based on your conversation with Dr. de Jong on April 4." The intelligence is invisible.

---

### Jan (Engineering Philosophy)

**What WhatsApp taught me**: We served 450 million users with 55 engineers. No ads, no gimmicks, no dark patterns. The product was fast, private, and reliable. That's it. When you focus on that, you win.

**Diagnosis of Ditto**: Your architecture spec is solid but ambitious for a 10-person team. Event bus, worker framework, 6 pipelines, profile store with versioning and audit logging. I see the skeleton of a product that could serve 50 million users. But you don't have 50 million users. You have 35,000.

**The hard question**: What's the minimum architecture that makes ONE pipeline feel like magic? Because if the recording pipeline is flawless, the rest follows. If you build all six and they're all 80% quality, you lose trust forever. One hallucinated medication change destroys more trust than six months of good summaries build.

**My prescription**:
1. GDPR is your moat, not your constraint. WhatsApp won because SMS was expensive and carrier-controlled. You win because European health data is regulated and most US competitors won't invest in compliance. Lean into it. "Your data never leaves the EU. Your doctor's words stay between you and the people you choose to share them with." That's not a compliance checkbox. That's a marketing message.
2. Phone number signup was WhatsApp's zero-friction play. What's yours? The recording. No account creation, no profile filling, no onboarding tutorial. Record your next appointment. See what happens. Signup can come after the first summary.
3. Build for reliability, not features. 10 seconds to summary, 100% grounded answers, zero hallucinations. Those three numbers are your entire engineering culture. Everything else is nice-to-have.
4. 55 engineers for 450M users. You have 10 people. Act like it. One pipeline, perfect. Not six pipelines, okay.

---

### Daniel (Platform & Growth)

**What Spotify taught me**: We spent two years negotiating with labels before writing a line of code. The product wasn't the technology. It was the business model that made labels and users both win. And then we made AI invisible: Discover Weekly drives 20% of all streams, and users think they just "have good taste."

**Diagnosis of Ditto**: Your care graph is the platform play. Each patient who joins brings 3-7 circle members. Each circle member is a potential patient. That's network effects. But 50 invitations/day is a seed, not a harvest. The question is: what makes circle members become patients?

**The hard question**: Where's Ditto's Discover Weekly? A feature so good it's the reason people come back, and they don't even know it's AI. Summaries are useful but episodic (you only record when you have an appointment). What brings someone back between appointments?

**My prescription**:
1. **The "Ditto Knows" moment**: After 3+ recordings, the Health Profile should surface something the patient didn't explicitly tell Ditto. "Based on your last three appointments, Ditto noticed your oncologist adjusted your medication twice. Here's your current medication overview." The patient thinks: "Ditto is paying attention, even when I'm not." That's Discover Weekly for healthcare.
2. **Freemium must work like Spotify Free**: Good enough to hook, limited enough to convert. Free tier: record + summarize (3/month). Premium: unlimited recordings, Q&A, health profile, circle sharing, appointment prep. The free tier has to be genuinely useful. Three summaries per month is enough for most patients. The ones who need more (chronic conditions, active treatment) are your premium users.
3. **Circle members as top-of-funnel**: When a patient shares an adapted summary with their daughter, the daughter sees a version specifically crafted for her. She's impressed. She signs up. She records her own appointment. Now SHE shares with HER partner. That's the viral loop. The adapted summary IS the growth engine.
4. **Insurer distribution is your label deal**: Menzis is your Universal Music. Prove it works with one, then sign the other three majors. The B2B2C model is how you get to millions without spending millions on acquisition.

---

### Anton (AI-Native Builder)

**What Lovable taught me**: We validated with open source (gpt-engineer, 50K+ GitHub stars) before building the product. We targeted non-technical users, not developers. And we ship fast because the AI IS the product, not a feature bolted onto a product.

**Diagnosis of Ditto**: You're building the AI as a backend system (event bus, workers, orchestrator). That's fine engineering. But you're not thinking AI-natively. The AI shouldn't just power the features. The AI should define the product surface.

**The hard question**: What if the entire Ditto experience was generated, not designed? Not a chatbot. But every screen the patient sees is composed by the brain for that specific patient at that specific moment. The summary isn't a template filled in. It's a document the brain writes. The health profile isn't a form. It's a living page the brain maintains. The prep screen isn't a feature. It's a briefing the brain generates.

**My prescription**:
1. **AI-native means the brain writes the UI, not just the content.** The summary's structure, the order of information, the emphasis, which suggestions appear, all of that should be brain-determined based on the patient's context. A cancer patient seeing medication changes gets a different layout than a diabetes patient seeing routine bloodwork.
2. **Ship weekly. Validate daily.** Your 12-week plan with gates is responsible engineering. But it's also slow. Build the eval harness in week 1. Ship to 100 internal users in week 2. Get real feedback in week 3. The synthetic personas are good, but real patients reacting to real summaries are better.
3. **"AI as raw oil" means you're the refinery.** GPT-5, Claude, Gemini are all crude. Your prompts, your extraction logic, your confirmation flows, your audience adaptation rules: THAT'S the refinery. The refinery is the moat. Not the model. Invest in prompt engineering and eval infrastructure disproportionately. That's your IP.
4. **Build in public.** Share anonymized examples of what Ditto does. "Patient records oncology appointment. Here's what their partner received." The demo IS the marketing. Lovable grew because the demos were shareable. Ditto's demos would be even more powerful because the problem is universal and emotional.

---

### Sarah (Capital Strategy)

**What healthcare VCs look for**: Category-defining companies solving measurable problems with defensible moats, clear unit economics, and a path to $100M+ ARR. In health-tech specifically: regulatory moats, network effects, and proof that patients actually use the product (not just download it).

**Diagnosis of Ditto**: The raw ingredients are strong. 35K users (proof of demand), Menzis partnership (proof of B2B2C viability), Care Circle invitations at 50/day (proof of network effects), and a commoditizing core product forcing a pivot (urgency). The business case math works. But you're pre-revenue with a strategy deck, not a shipped Care Brain.

**The hard question**: What milestones, in what order, make this a $5-10M Series A within 12 months?

**My prescription**:

**The Series A narrative in one sentence**: "Ditto is building the consumer layer for healthcare in Europe, where one recording creates shared understanding across everyone who cares about the patient."

**Milestone sequence (the VC staircase)**:

| Quarter | Milestone | What It Proves | Valuation Signal |
|---|---|---|---|
| Q2 2026 | Care Brain Phase 1 shipped (Q&A + suggestions) | Brain > summarizer. AI adds value beyond core. | Product evolution |
| Q2 2026 | 20%+ suggestion engagement rate | Users WANT contextual intelligence | Product-market fit signal |
| Q3 2026 | Living Health Profile + Voice Input | Switching costs. Data gravity. Multiple input modalities. | Platform, not feature |
| Q3 2026 | 100K active users (patients + circle) | Growth trajectory | Scale signal |
| Q3 2026 | Circle-to-patient conversion rate measured | Network effects are real, not theoretical | Network effects |
| Q4 2026 | Adapted sharing shipped + circle engagement (CNIS) at 40%+ | The care graph produces measurable value | Unicorn feature validated |
| Q4 2026 | Menzis upsell or second insurer LOI | B2B2C model replicable | Revenue model validation |
| Q1 2027 | First non-NL market pilot (BE or DE) | Cross-border viability | TAM expansion |

**The fundraise window**: Q4 2026 to Q1 2027. After shipping Care Brain Phases 1-3, with engagement data and a second insurer signal. Target: EUR 5-10M at EUR 40-80M pre-money.

**What kills the raise**:
- Shipping Care Brain but nobody uses Q&A (brain adds no value)
- Care Circle organic growth stalls (care graph thesis fails)
- Medical hallucination incident (trust destroyed, regulatory risk)
- Menzis partnership doesn't convert to active users (distribution channel doesn't work)

---

## Round 2: The Convergence (Where All Six Agree)

After each persona's solo take, the convergences are striking:

### 1. One Magical Moment Before Everything Else

Every founder said the same thing differently. Kevin: "What's your filter moment?" Andy: "What's your Take 10?" Jan: "One pipeline, perfect." Daniel: "Where's your Discover Weekly?" Anton: "Ship to 100 real users in week 2."

**The convergent answer**: The magical moment is when a patient records an appointment, sees a summary that mentions their history by name, taps a suggestion they were already wondering about, and gets an answer grounded in what THEIR doctor said. In under 30 seconds, they go from "I should probably write this down" to "Ditto already knows."

Everything else (voice input, document processing, appointment prep) is Phase 2+. Don't dilute the magic.

### 2. The Interface Is the Moat (Not the AI)

Everyone agreed: the AI is crude oil. ChatGPT, Claude, Gemini can all summarize a medical transcript. The interface, specifically HOW the intelligence surfaces, WHEN it appears, and WHO it adapts for, is the refinery.

**The convergent answer**: Ditto's interface innovation is "contextual intelligence surfaces." Not a chat. Not a dashboard. Not a feed. Instead: every screen the patient touches has been composed by intelligence that knows their full context, and the patient never thinks about AI once. Specifically:

| Interface Pattern | What It Replaces | Why It's Better |
|---|---|---|
| **Suggestion chips below content** | Chat input / "Ask anything" | User doesn't need to think of a question. Brain already anticipated it. |
| **Inline answer expansion** | Opening a chat thread | Information appears where you already are. No context switch. |
| **Adapted sharing preview** | Copy-paste into WhatsApp | One-tap preview of what each person will see. The brain writes it. |
| **Living health profile** | Manual forms / scattered notes | Auto-maintained, auto-sourced, patient-correctable. |
| **Prep briefing** | Scribbled notes in the waiting room | Brain generates a briefing from your full journey. |

This is the Oura model applied to healthcare: raw medical data in, one clear insight out, no conversation required.

### 3. The Care Graph Is the Only Real Moat

Sarah made it clearest: "AI is commoditizing. Regulatory compliance is a barrier, not a moat. The care graph, the map of who cares about whom and what each person needs to know, is the only thing that compounds over time and can't be replicated by adding an API call."

**The convergent answer**: Every feature decision should be evaluated by one question: does this grow the care graph? If it doesn't add a patient, a circle member, a connection, or a reason to share, deprioritize it.

| Feature | Grows Care Graph? | Priority |
|---|---|---|
| Smart suggestions / Q&A | Indirectly (retention → sharing) | High (proves brain value) |
| Living Health Profile | Yes (switching cost → retention) | High |
| Adapted sharing | Yes (directly adds circle members) | **Highest** |
| Voice input | No (convenience feature) | Medium |
| Document processing | Indirectly (more data → better brain) | Medium |
| Appointment prep | No (retention feature) | Lower |

### 4. Privacy Is a Feature, Not a Constraint

Jan was emphatic, and Sarah backed it: in a post-GDPR, post-AI-Act Europe, privacy isn't a compliance cost. It's a competitive advantage. Every US competitor (ChatGPT Health, Copilot Health) has to adapt to EU regulation. Ditto is born into it.

**The convergent answer**: "Your health data never leaves Europe. Your doctor's words stay between you and the people you choose to share them with." This isn't a footnote in your privacy policy. It's your second tagline after "Care. Clarified."

### 5. Speed Is the Strategy

Anton and Sarah converged on this: the window before Big Tech adds care circle features is 18-24 months. The competitive analysis is clear: nobody is building audience-adapted health sharing for care circles. But the gap exists because nobody's shipped it yet, not because nobody's thought of it.

**The convergent answer**: The 12-week MVP timeline is right. But the sequencing matters. Ship the thing that's hardest to copy first (adapted sharing), not the thing that's most technically impressive (health profile versioning).

---

## The Unicorn Roadmap

### Phase 0: The Foundation (Now, Weeks 1-4)

**Goal**: Fix what's broken. Establish the base.

- AI quality to 98%+ (ongoing)
- Care Circle V2 adoption tracking (measure invitation-to-activation conversion)
- Define the "Ditto voice" (tone guide for all AI-generated content)
- Build eval harness (the infrastructure that protects against hallucination)

**Kevin's test**: Does the current summary make someone say "wow"? If not, fix that before adding anything.

### Phase 1: The Brain Proves Itself (Weeks 5-10)

**Goal**: Recording → summary + suggestions + grounded Q&A. One pipeline, perfect.

Ship the recording pipeline with:
- Patient-friendly summary (existing, upgraded with brain context)
- 3-5 contextual suggestion chips per summary
- Tap-to-expand grounded answers
- Source attribution on everything

**Metric that matters**: 20%+ of summary viewers tap a suggestion. If this fails, the entire brain thesis fails.

**Andy's test**: Would Corrie (81, cognitive decline) understand the summary and successfully tap a suggestion without help?

### Phase 2: The Brain Remembers (Weeks 8-14)

**Goal**: Health Profile auto-populates from recordings. The brain accumulates knowledge.

- Health Profile (medications, conditions, care team, action items)
- Cross-appointment context (Q&A references previous visits)
- Voice input ("Tell Ditto" for quick updates between appointments)

**Metric that matters**: 90%+ profile accuracy after 3+ recordings. This is the switching cost. Once Ditto knows your medication history across 6 oncology appointments, you can't leave.

**Jan's test**: Zero silent wrong updates. Every profile change is confirmed. Every source is attributed.

### Phase 3: The Care Graph Comes Alive (Weeks 14-20)

**Goal**: Adapted sharing. The unicorn feature. One recording, everyone understands.

- Patient taps "Share" on a summary
- Sees preview cards: "What your partner will see" / "What your daughter will see" / "What your friend will see"
- Each preview is audience-adapted (detail level, emotional tone, language)
- One-tap send

**This is the Spotify Discover Weekly moment**: the feature that makes Ditto unreplaceable and inherently viral.

**Metric that matters**: Circle engagement (CNIS) at 40%+. Circle-to-patient conversion rate measured.

**Daniel's test**: Does the adapted summary make the daughter think "I need this for MY health stuff too"?

### Phase 4: The Platform Emerges (Weeks 20-30)

**Goal**: Proactive intelligence + second market + insurer expansion.

- Appointment prep (brain generates briefing from journey context)
- Pattern detection v1 ("You've reported fatigue 3 weeks running")
- First non-NL market pilot (Belgium or Germany)
- Second insurer LOI

**Sarah's test**: Can you walk into a Series A meeting with: 100K users, 20%+ Q&A engagement, 40%+ circle engagement, Menzis proof case, second insurer signal?

### Phase 5: Series A and Scale (Month 8-12)

**Goal**: Raise EUR 5-10M. Expand team. Enter 2-3 EU markets.

- Engineering team 10 → 20
- Localization infrastructure for DE/BE/FR
- EHDS integration preparation (first elements go live Fall 2026)
- Insurer partnership playbook replication

---

## AI as Raw Oil: The Refinery Model

The "AI as raw oil" thesis explained for Ditto:

```
CRUDE OIL (commodity)              REFINED PRODUCT (differentiated)
─────────────────────              ────────────────────────────────
GPT-5 / Claude / Gemini    →      "Ditto prepared this for you"
Generic medical summary     →      Summary referencing YOUR history with YOUR doctor
"Ask me anything about      →      3 suggestion chips the patient was already
 your health"                       wondering about
Raw transcript text         →      Adapted version for partner, daughter, friend
LLM structured extraction   →      Living health profile with source attribution
                                    and patient correction
```

**Where Ditto's refinery creates value**:

| Refinery Layer | What It Does | Why It Can't Be Copied Easily |
|---|---|---|
| **Extraction prompts** | Pull medications, conditions, care team from Dutch medical conversations | Tuned on NL medical terminology, dialect, code-switching |
| **Audience adaptation rules** | Different versions for different relationships | Requires care graph (who is this person to the patient?) |
| **Confirmation UX** | Patient verifies before profile updates | Trust architecture, not just AI |
| **Cross-appointment reasoning** | References previous visits in current answers | Requires accumulated journey data |
| **Voice/persona** | Consistent warm, clear tone across all surfaces | Brand asset, not model capability |
| **Eval harness** | Catches hallucinations before they reach patients | Continuous investment in quality infrastructure |

The model is replaceable. The refinery is not.

---

## Interface Innovation: Beyond Chat

The founding team unanimously rejected chat as the primary interface. Here's the alternative design philosophy:

### The Principle: Contextual Intelligence Surfaces

Instead of one general-purpose AI interface (chat), many specialized surfaces, each purpose-built for a specific moment:

**Pattern 1: Anticipatory Suggestions**
The brain predicts what the patient will want to know and surfaces it as tappable chips directly below the relevant content. The patient doesn't search, doesn't type, doesn't "talk to AI." They just tap.

```
┌──────────────────────────────────────┐
│  Your summary from Dr. de Jong       │
│  April 4, 2026                       │
│                                      │
│  "Dr. de Jong discussed switching    │
│  from capecitabine to oxaliplatin    │
│  due to the scan results from..."    │
│                                      │
│  ┌──────────────────────────────┐    │
│  │ Why is the medication        │    │
│  │ changing?                    │    │
│  └──────────────────────────────┘    │
│  ┌──────────────────────────────┐    │
│  │ What are the side effects    │    │
│  │ of oxaliplatin?              │    │
│  └──────────────────────────────┘    │
│  ┌──────────────────────────────┐    │
│  │ When does the new treatment  │    │
│  │ start?                       │    │
│  └──────────────────────────────┘    │
│                                      │
│  Ask something else...               │
└──────────────────────────────────────┘
```

The "ask something else" is the escape hatch, not the primary interaction. Like WHOOP Coach: the card is the interface, conversation is the backup.

**Pattern 2: Adaptive Sharing Previews**
When a patient taps "Share," they don't fill a form or pick from a list. The brain generates preview cards showing exactly what each person will receive:

```
┌──────────────────────────────────────┐
│  Share your update                    │
│                                      │
│  ┌─ Hans (partner) ────────────┐    │
│  │ Full summary with action    │    │
│  │ items and medication change  │    │
│  │ details.                     │    │
│  │              [Preview] [Send]│    │
│  └──────────────────────────────┘    │
│                                      │
│  ┌─ Sanne (daughter) ──────────┐    │
│  │ Key updates: medication     │    │
│  │ changed, next appointment   │    │
│  │ May 2. Dad is doing okay.   │    │
│  │              [Preview] [Send]│    │
│  └──────────────────────────────┘    │
│                                      │
│  ┌─ Mehmet (friend) ───────────┐    │
│  │ "Treatment is going well,   │    │
│  │ some changes to medication. │    │
│  │ Next check-up in 4 weeks."  │    │
│  │              [Preview] [Send]│    │
│  └──────────────────────────────┘    │
└──────────────────────────────────────┘
```

One recording. Three taps. Everyone understands. THAT is the unicorn feature.

**Pattern 3: The Living Profile (Not a Form)**
The health profile isn't something the patient fills in. It's a document the brain maintains and the patient oversees:

```
┌──────────────────────────────────────┐
│  What Ditto knows about you          │
│                                      │
│  Medications                         │
│  ┌──────────────────────────────┐    │
│  │ Oxaliplatin                  │    │
│  │ From: Dr. de Jong, Apr 4    │    │
│  │ Replaced: Capecitabine      │    │
│  │                  [Correct ✏️] │    │
│  └──────────────────────────────┘    │
│  ┌──────────────────────────────┐    │
│  │ Metformin 500mg              │    │
│  │ From: Dr. Bakker, Feb 12    │    │
│  │                  [Correct ✏️] │    │
│  └──────────────────────────────┘    │
│                                      │
│  Conditions                          │
│  ┌──────────────────────────────┐    │
│  │ Colon cancer (stage 3b)      │    │
│  │ From: Dr. de Jong, Jan 8    │    │
│  │                  [Correct ✏️] │    │
│  └──────────────────────────────┘    │
│                                      │
│  Last updated: April 4, 2026        │
│  Based on 6 recorded appointments    │
└──────────────────────────────────────┘
```

Every item sourced. Every item correctable. The brain maintains it. The patient trusts it because they can see where everything came from.

---

## Market Differentiation: The Position No One Occupies

```
                    Individual ◄────────────────────► Social/Circle
                         │                                  │
          ┌──────────────┤                                  │
          │              │                                  │
    AI-Powered   ChatGPT Health                             │
          │      Copilot Health                             │
          │      Apple Health AI                            │
          │              │                                  │
          │              │                                  │
          │              │           CaringBridge           │
   Not AI │              │           (broadcast, no AI)     │
          │              │                                  │
          │              │                 ★ DITTO          │
          │              │           (AI-powered +          │
          │              │            audience-adapted +    │
          │              │            care circle)          │
          │              │                                  │
          └──────────────┤                                  │
                         │                                  │
                   Individual                          Social/Circle
```

Ditto occupies the only empty quadrant: AI-powered AND social/circle. Everyone else is building individual health AI. CaringBridge has the social layer but no intelligence. Ditto has both.

**The 18-24 month window**: Big Tech hasn't noticed this quadrant yet. They're competing with each other on individual health Q&A. By the time they realize the care circle matters, Ditto needs to have built the care graph that makes it sticky.

---

## The Numbers That Make It a Unicorn

### The Path

| Year | Users (active) | ARR | Valuation (10-20x) |
|---|---|---|---|
| End 2026 | 100K | EUR 1-3M (Menzis + early premium) | EUR 40-80M (Series A) |
| End 2027 | 500K (3 EU markets) | EUR 10-25M | EUR 100-250M (Series B) |
| End 2028 | 2M (5+ EU markets) | EUR 30-50M | EUR 300-500M |
| End 2029 | 5-10M (EU-wide) | EUR 50-100M | EUR 500M-2B |

### What Makes Each Jump Possible

**35K → 100K** (now → end 2026): Care Brain engagement + Menzis activation + organic circle growth. No new market needed.

**100K → 500K** (2027): Second and third insurer partnerships (DE, BE). Each insurer deal adds 1-2M addressable members. Convert at 5-10%.

**500K → 2M** (2028): EHDS first elements go live. First consumer app to ingest Patient Summaries wins the land grab. Platform effects: care graph makes every new user more valuable.

**2M → 10M** (2029): EU-wide insurer network. "Ditto" becomes the verb for sharing health updates, the way "WhatsApp" became the verb for messaging.

### Unit Economics at Scale

| Metric | Value | Source |
|---|---|---|
| AI cost per recording | EUR 0.07 | Business case model |
| AI cost per user per month | EUR 0.15-0.30 | 2 recordings + Q&A + adaptations |
| B2C premium price | EUR 7.99/month | Consumer pricing |
| B2B2C PMPM | EUR 0.50-1.00 | Insurer pricing |
| Gross margin | 85-90% | SaaS economics with negligible AI costs |
| LTV (premium user, 18mo avg) | EUR 144 | EUR 7.99 × 18 |
| CAC (organic/circle) | EUR 5-15 | Network-driven acquisition |
| LTV:CAC ratio | 10-30x | Best-in-class SaaS territory |

---

## The 10 Moves (Prioritized)

What must happen, in order, for this to work:

| # | Move | Owner | Timeline | Why This Order |
|---|---|---|---|---|
| 1 | Fix AI quality to 98%+ | Engineering | Now | Nothing works if summaries are wrong |
| 2 | Ship Smart Suggestions (Q&A) | Engineering + Prompt | Weeks 5-10 | Proves the brain adds value |
| 3 | Measure suggestion engagement | Product | Week 10 | Go/no-go for everything after |
| 4 | Define and implement "Ditto voice" | Product + Design | Weeks 5-8 | Consistent persona across all surfaces |
| 5 | Ship Living Health Profile | Engineering | Weeks 8-14 | Creates switching costs |
| 6 | Ship Adapted Sharing | Engineering + Design | Weeks 14-20 | The unicorn feature. Grows care graph. |
| 7 | Measure circle engagement + conversion | Product + Growth | Week 20 | Validates network effects |
| 8 | Activate Menzis user base | Partnerships | Q3-Q4 2026 | Scale from 35K to 100K |
| 9 | Secure second insurer signal | Partnerships | Q4 2026 | Proves B2B2C model is replicable |
| 10 | Raise Series A | CEO | Q4 2026 - Q1 2027 | Fund EU expansion |

---

## What Could Kill This

The founding team's honest assessment of existential risks:

| Risk | Probability | Who Flagged It | The Kill Scenario |
|---|---|---|---|
| **Medical hallucination** | Medium | Andy, Jan | One wrong medication suggestion shared to a care circle. Media picks it up. "AI gives cancer patient wrong drug info." Trust destroyed overnight. |
| **Care graph doesn't compound** | Medium | Daniel, Sarah | Circle members receive adapted summaries but don't become patients. Network effects stay theoretical. Growth is linear, not exponential. |
| **Big Tech adds circle features** | Low (18-24mo) | Sarah | Apple or Google adds "Share your health summary with family" to their health apps. Commoditizes the unicorn feature before Ditto scales. |
| **Menzis activation fails** | Medium | Sarah | 2M addressable members, but conversion to active users is <1%. Distribution channel exists but doesn't convert. |
| **Team burns out** | Medium-high | Kevin, Jan | 10 people, 12-week sprint, 91 tickets. Ambitious timeline with a small team. If Phase 1 takes 16 weeks instead of 10, everything slides. |
| **Over-engineering** | Medium | Kevin, Anton | Building 6 pipelines, 7 surfaces, versioned profile store when you need 1 magical pipeline first. Architecture astronaut syndrome. |

**The biggest risk nobody mentions**: Ditto ships Care Brain, it works, but it doesn't FEEL different enough. The summary is better. The Q&A is useful. But users say "it's nice" instead of "I can't live without this." The difference between a good product and a unicorn is the emotional response. Build for "wow," not "useful."

---

## Final Synthesis: The One Thing

If this document is too long, here's the one thing:

**Ditto's unicorn thesis is not about AI. It's about the care graph.**

AI is the crude oil that powers the refinery. The refinery turns medical conversations into shared understanding. The care graph, who cares about whom and what each person needs to know, is the asset that compounds over time. Build the graph. Make it sticky. Make it grow. Everything else (the summaries, the Q&A, the health profile, the prep) is fuel for the graph.

One recording. Everyone understands. That's the product. That's the pitch. That's the unicorn.

---

*Generated by Mewtwo's virtual founding team. Not a real board meeting, but the questions are real.*
