# Care Brain: Competitive Analysis

**Date**: 2026-04-05
**Status**: Internal draft

---

## Competitive Landscape Overview

The consumer health AI market exploded in Q1 2026. Big Tech entered aggressively. Startups raised record amounts. But the field is fragmenting into distinct categories, and most players are building the same thing: individual health AI. Nobody is building the social layer of care.

### Market Categories

| Category | What it means | Key players | Ditto's relevance |
|---|---|---|---|
| **Personal Health AI** | Individual + AI chatbot about their health | ChatGPT Health, Copilot Health, Apple Health AI | Adjacent threat. Same user, different product. |
| **Ambient Documentation** | Provider-facing clinical note generation | Ambience, Abridge, Nuance DAX | Indirect. Commoditizes the transcription layer Ditto uses. |
| **Care Coordination** | Logistics of caregiving (who's driving, meal schedules) | Lotsa Helping Hands, CaringBridge | Adjacent. Solves coordination, not understanding. |
| **Health Data Infrastructure** | Aggregation and interoperability of health records | b.well, Torch Health (now OpenAI), Galen | Enabling layer. Could be partner or competitor. |
| **Care Intelligence** (proposed) | AI that transforms health moments into shared understanding across care circles | **Ditto (planned)** | The category we're creating. |

---

## Head-to-Head Analysis

### ChatGPT Health (OpenAI)

**What it is**: Health-focused features within ChatGPT, enhanced by the Torch Health acquisition (Jan 2026). Aims to be a "unified medical memory" aggregating patient data from hospitals, labs, wearables, and consumer apps.

**Current capabilities**:
- Health-specific Q&A with improved medical reasoning
- Medical record integration (via Torch Health's interoperability layer)
- 40M users already ask ChatGPT health questions daily
- General-purpose. Not a dedicated health product.

**Strengths**:
- Massive distribution (hundreds of millions of users)
- Best AI model capability (GPT-5.x)
- Torch acquisition gives data infrastructure
- Brand recognition and user trust in AI

**Weaknesses**:
- General-purpose. Health is a feature, not the product.
- No care circle, no social layer, no audience adaptation
- US-centric data integrations
- No European health data compliance positioning
- User trust is in "AI that knows things," not "AI that helped me through cancer"
- Can't build bedside trust from a general-purpose chatbot

**Ditto's advantage**: ChatGPT Health answers questions about YOUR health. Ditto helps your FAMILY understand your health. Different product. Different moat. ChatGPT Health is Ditto's biggest competitor for individual Q&A, but Ditto's care graph is unreachable from ChatGPT's architecture.

**Threat level**: Medium-high for individual Q&A. Low for care circle features.

---

### Microsoft Copilot Health

**What it is**: Dedicated health space within Microsoft Copilot, launched March 2026. Aggregates health records from 50K+ US providers + 50 types of wearables.

**Current capabilities**:
- Health record aggregation (US providers only)
- Wearable data integration
- AI-powered health insights
- Separate secure space within Copilot
- US English-speaking adults only

**Strengths**:
- Massive provider network (50K+ US)
- Enterprise distribution (hundreds of millions of Microsoft users)
- Integration with existing Microsoft health infrastructure

**Weaknesses**:
- US-only launch. No European presence.
- Enterprise-adjacent positioning (not consumer-first)
- No social/sharing features
- No care circle concept
- Not designed for serious health journeys (more wellness/monitoring)

**Ditto's advantage**: Copilot Health is Microsoft's answer to ChatGPT Health, not to Ditto. It's US-focused, individual-focused, enterprise-adjacent. Ditto is European, family-focused, patient-first.

**Threat level**: Low for current product. Medium if they expand to EU.

---

### Apple Health AI

**What it is**: Apple's Project Mulberry (Health+ AI Coach) was a planned subscription health AI service. Scaled back in February 2026. Now shipping AI features individually into the Health app.

**Current capabilities**:
- Individual features being added to Health app (spring 2026)
- Wearable integration (Apple Watch is the best health wearable)
- On-device processing for privacy
- Scaled-down AI Health Agent (not the full coaching service)

**Strengths**:
- Best health wearable ecosystem
- On-device processing (unmatched privacy)
- Billions of devices
- Trust in Apple's privacy stance

**Weaknesses**:
- Retreated from full health AI service
- Wearable-first, not care-journey-first
- No social/sharing features
- No European health system integration
- On-device limits AI capability

**Ditto's advantage**: Apple's retreat is Ditto's opportunity. Apple builds for wellness. Ditto builds for care journeys. Apple's privacy moat (on-device) is also a constraint. Care Brain features require cloud processing with full context.

**Threat level**: Low-medium. Could change if Apple re-enters.

---

### Hippocratic AI ($3.5B valuation)

**What it is**: Patient-facing AI agents for chronic care and post-discharge follow-up. Raised $126M Series C at $3.5B valuation (Nov 2025).

**Current capabilities**:
- Voice-based patient agents (call patients after discharge)
- Chronic care management via AI conversations
- Provider-facing (sold to health systems, not direct to patients)
- US-focused

**Strengths**:
- Massive funding and valuation
- Patient-facing AI agents in production
- Focus on outcomes (readmission reduction)
- Voice-first approach

**Weaknesses**:
- Provider-facing (hospitals buy it, patients don't choose it)
- US healthcare system only
- No consumer brand
- No care circle
- Transactional (post-discharge check-in), not longitudinal (care journey)

**Ditto's advantage**: Hippocratic AI is provider-led. Patients don't choose it. Ditto is patient-led. Patients choose it because it helps them. Different go-to-market, different moat (Hippocratic's moat is health system contracts; Ditto's is patient trust + care graph).

**Threat level**: Low for consumer. Could become partner (Hippocratic does post-discharge, Ditto does patient understanding).

---

### b.well bailey (White-Label Health AI)

**What it is**: White-label AI assistant that organizations embed in their own apps. Launched February 2026. 350+ health data sources. Used by OpenAI and Samsung for their health AI features.

**Current capabilities**:
- Provider search, medication management, benefits navigation, appointment scheduling
- Integrates 350+ health data sources into single longitudinal record
- Health AI SDK for organizations to deploy in weeks
- White-label (invisible to end user)

**Strengths**:
- Infrastructure play (powers others' health AI)
- Massive data integration (350+ sources)
- Fast deployment for partners
- Used by OpenAI and Samsung

**Weaknesses**:
- No consumer brand
- White-label means no direct patient relationship
- No care circle or social features
- US health data sources primarily
- Functional (scheduling, navigation), not emotional (understanding, sharing)

**Ditto's advantage**: b.well is infrastructure. Ditto is product. b.well could actually be a PARTNER. Their data integration layer + Ditto's care intelligence and care graph = powerful combination. Worth exploring.

**Threat level**: Low as competitor. Medium-high as potential partner.

---

### Ambience Healthcare ($3B+ valuation)

**What it is**: Ambient clinical documentation + AI coding + chart awareness. Raised $243M Series C. Provider-facing.

**Current capabilities**:
- Ambient documentation (auto-generates clinical notes from conversations)
- Chart Awareness (AI interprets full longitudinal record)
- Automated medical coding
- 40% reduction in documentation time reported

**Strengths**:
- Best ambient documentation product
- Massive funding
- Strong provider adoption
- Full longitudinal record awareness

**Weaknesses**:
- Provider-facing only. Patients never see it.
- No patient-facing product
- No care circle
- Optimized for clinician workflow, not patient understanding

**Ditto's advantage**: Ambience commoditizes the supply side (clinical documentation). Ditto owns the demand side (patient understanding). They'll never compete directly. But Ambience's success proves the market values AI processing of medical conversations.

**Threat level**: None as competitor. Validates the market.

---

### CaringBridge

**What it is**: Health journey blog + support coordination. ~900K patients. The closest existing product to the "care circle" concept.

**Current capabilities**:
- Patient blog (post updates about health journey)
- Support coordination (meal schedules, visit scheduling)
- Community features
- Non-profit

**Strengths**:
- Existing care circle concept (rare)
- Emotional connection with users
- Non-profit mission alignment

**Weaknesses**:
- Not AI-native. No intelligence.
- Blog format (broadcast, not adapted)
- One post to everyone (no audience adaptation)
- No health data integration
- No European presence
- Outdated platform, limited investment

**Ditto's advantage**: CaringBridge proved the need. Patients WANT to share health updates with their circle. But CaringBridge is broadcast (same post to everyone). Ditto is adapted sharing (different version for each person). That's the fundamental upgrade.

**Threat level**: None. Validates the need, doesn't compete on capability.

---

## The Unique Position: Audience-Adapted Health Sharing

### Is it actually unique?

After comprehensive market research: **yes.**

| Product | Individual health AI | Care circle/social | Audience-adapted sharing |
|---|---|---|---|
| ChatGPT Health | Yes | No | No |
| Copilot Health | Yes | No | No |
| Apple Health AI | Yes | No | No |
| Hippocratic AI | Yes (voice) | No | No |
| b.well bailey | Yes (infrastructure) | No | No |
| Ambience | No (provider-facing) | No | No |
| CaringBridge | No | Yes (broadcast) | No |
| Lotsa Helping Hands | No | Yes (logistics) | No |
| Patient portals | Partially | No | No |
| **Ditto Care Brain** | **Yes** | **Yes** | **Yes (planned)** |

Nobody else is building the intersection of: AI intelligence + care circle social layer + audience-adapted sharing. This is the gap. The question is whether the gap exists because no one thought of it, or because it's not valuable enough to build. The evidence (35K users, 50 invitations/day, Menzis partnership, user research) suggests it's the former.

---

## Strategic Implications

### What we must NOT do

1. **Don't compete on individual health Q&A.** ChatGPT Health has 40M daily health queries and the best AI. We lose that fight. Our Q&A must be care-graph-native (useless without Ditto's data).

2. **Don't build a general health chatbot.** That's what everyone else is building. Our interface should be guided intelligence (smart suggestions), not open-ended chat.

3. **Don't try to aggregate health records.** b.well, Torch Health, and Microsoft are spending hundreds of millions on data interoperability. We use recording + documents + voice as our input layer. EHDS handles the rest eventually.

4. **Don't position as "AI-powered."** The 50+ audience doesn't care about AI. Position as "Ditto understands your health and helps the people who love you understand it too."

### What we must DO

1. **Build the care graph fast.** This is the moat. Every feature should grow the graph (more circle members, more connections, more sharing). CC V2 soft launch shows 50 invitations/day. Accelerate.

2. **Make sharing magical.** Audience-adapted sharing is the unicorn feature. One recording, everyone understands. Ship this before anyone else realizes it matters.

3. **Own the European market.** US is a war zone (ChatGPT, Copilot, Ambience, Hippocratic). Europe has fewer competitors and EHDS as a structural advantage. Be the EU care intelligence platform.

4. **Ground everything in patient data.** Our Q&A is different because it answers questions about YOUR conversation, not about medicine in general. Grounding is the feature AND the safety mechanism.

5. **Lock in Menzis, then replicate.** The insurer model is the EU growth accelerator. Prove it works with Menzis, then pitch to other EU insurers with data.

---

## Timeline Sensitivity

### The window

Big Tech entered consumer health AI in Q1 2026. Currently focused on individual health Q&A and record aggregation. They haven't noticed the care circle gap.

**Estimated window before Big Tech adds care circle features: 18-24 months.**

Why?
- Big Tech moves slowly in healthcare (regulation, risk aversion)
- Their architecture is individual-first (adding social is a fundamental product change)
- EU is not their primary market (US first, EU later)
- They're competing with each other on the same surface area

**Ditto's advantage**: 18-24 months to build the care graph and make it sticky before anyone else enters this space.

### If we're too slow

If Ditto doesn't ship the Care Brain by Q3 2026:
- Summarization continues to commoditize
- ChatGPT Health captures the "health Q&A" positioning
- A well-funded European startup could enter the care circle space
- Insurer interest wanes if Ditto can't show innovation beyond current product

The clock is ticking. Not because of panic, but because the window is real and finite.
