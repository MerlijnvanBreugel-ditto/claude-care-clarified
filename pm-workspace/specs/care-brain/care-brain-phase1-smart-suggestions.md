# Smart Suggestions: Contextual Q&A on Summaries

**Author**: Merlijn van Breugel / Mewtwo
**Date**: 2026-04-04
**Status**: Draft
**Priority**: P1
**Parent**: [Care Brain Strategy](ideas/health-agent/care-brain-strategy.md) — Phase 1
**Classification**: Explore

---

## Problem

After reading a summary, patients have follow-up questions they can't get answered. "What did the doctor mean by 'we'll monitor the markers'?" "Is this medication change related to my last scan?" "What should I prepare for the next appointment?" These questions arise at 11pm, on the weekend, in moments of anxiety. Currently, users have no way to get answers without calling someone or searching the internet for generic information that doesn't match their situation.

**Who has this problem:**
- **Primary**: Patients who just received a summary (especially oncology, cardiology)
- **Secondary**: Care Circle members reading a shared summary who want to understand what it means for their loved one

**Current workarounds:**
- Google generic medical terms (no personal context, often alarming)
- Call family member who was at the appointment
- Wait until next appointment to ask
- Send message to doctor via patient portal (slow, often ignored)
- Ask ChatGPT (no knowledge of YOUR conversation or journey)

**Evidence:**
- Heavily requested feature across user feedback channels
- Common pattern in health apps (Torch Health, ChatGPT Health all building toward this)
- 40M people already ask ChatGPT health questions daily. They want answers. Ditto can give BETTER answers because it has the actual conversation context.

---

## Solution

### The concept: Smart Suggestions

After every summary, the brain generates 2-3 contextual suggestion chips specific to what was discussed. Users tap a suggestion to see an answer that's grounded in their actual conversation and journey history. No typing required. No chat interface. AI suggests, user taps, understanding deepens.

This is NOT a chatbot. It's contextual intelligence surfaced at the right moment.

### Key capabilities

1. **Auto-generated contextual suggestions**: The brain reads the summary and generates 2-3 questions a patient would likely want answered. These are specific: "What does watchful waiting mean for your situation?" not "What is watchful waiting?"

2. **Grounded answers**: Every answer references the actual conversation. "Dr. van der Berg mentioned [quote]. In the context of your [condition], this means..." Never general medical knowledge. Always YOUR data.

3. **Journey-aware**: If the patient has previous summaries, suggestions can bridge across appointments. "How does today's medication change compare to what was discussed in January?"

4. **Circle member suggestions**: When a circle member views a shared summary, they see different suggestions tailored to their perspective. "What does this mean for daily care?" vs. "What are the next steps?"

### User flow

```
Patient records appointment
    → Summary generated (existing flow)
    → Brain generates 2-3 contextual suggestions (new)
    → Patient sees summary with suggestion chips below

Patient taps a suggestion
    → Answer expands inline below the chip
    → Answer is grounded in conversation transcript + journey context
    → Patient can tap another suggestion or ask their own question

(Optional) Patient taps "Ask something else"
    → Text input appears
    → Patient types their question
    → Answer generated from same grounded context
```

### Out of scope (Phase 1)

- General health Q&A not tied to a summary (that's a chatbot, we're not building a chatbot)
- Voice-based Q&A (Phase 3)
- Proactive suggestions pushed via notifications (Phase 5)
- Cross-summary reasoning ("What changed across my last 5 appointments?") unless the patient has previous summaries loaded in context
- Medication interaction checking (requires verified database, Phase 4+)

---

## Interface Design

### The suggestion chips

Positioned below the summary content. Visually distinct but not aggressive. Part of the summary experience, not a separate feature.

```
┌─────────────────────────────────────────┐
│                                         │
│         [ Summary content ]             │
│                                         │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
│                                         │
│  💡 Suggestions for you                 │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ What does "watchful waiting"    │    │
│  │ mean for my situation?          │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ How is this different from      │    │
│  │ what we discussed in January?   │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ What should I prepare for       │    │
│  │ the follow-up appointment?      │    │
│  └─────────────────────────────────┘    │
│                                         │
│     Ask something else...               │
│                                         │
└─────────────────────────────────────────┘
```

### The expanded answer

When a suggestion is tapped, the answer expands inline. Collapsible. The answer should feel like a knowledgeable friend explaining, not a medical textbook.

```
┌─────────────────────────────────────────┐
│  ┌─────────────────────────────────┐    │
│  │ What does "watchful waiting"  ▼ │    │
│  │ mean for my situation?          │    │
│  │                                 │    │
│  │ Dr. van der Berg mentioned      │    │
│  │ "watchful waiting" as the next  │    │
│  │ step for your condition. This   │    │
│  │ means they'll monitor your      │    │
│  │ [specific markers] through      │    │
│  │ regular check-ups rather than   │    │
│  │ starting treatment right away.  │    │
│  │                                 │    │
│  │ Based on your conversation,     │    │
│  │ your next check-up is in 8      │    │
│  │ weeks where they'll repeat the  │    │
│  │ [specific test].                │    │
│  │                                 │    │
│  │ ⚕️ This is based on your        │    │
│  │ conversation with Dr. van der   │    │
│  │ Berg. For medical advice,       │    │
│  │ contact your care team.         │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ How is this different from      │    │
│  │ what we discussed in January?   │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### Design principles

| Principle | What it means |
|---|---|
| **Guided, not open** | Suggestions come from the brain. User doesn't need to know what to ask. |
| **Grounded, not generic** | Every answer references the actual conversation. Source attribution always visible. |
| **Inline, not modal** | Answers expand within the summary. No new screen. No navigation. |
| **Safe** | Medical disclaimer on every answer. Never prescriptive. Always "based on your conversation with [doctor]." |
| **Natural** | Feels like "Ditto understood my appointment and can explain more." Not like "I'm querying an AI database." |

---

## Technical Approach

### Suggestion generation (async, on summary creation)

When a summary is generated, add a parallel LLM call:

**Input**: Conversation transcript + generated summary + (if available) previous summary titles/dates
**Prompt**: Generate 2-3 questions a patient would likely want answered after reading this summary. Questions must be specific to THIS conversation, not generic. If previous appointments exist, include at least one cross-appointment question.
**Output**: Array of 2-3 question strings
**Storage**: Store alongside summary record

### Answer generation (on-demand, on tap)

When user taps a suggestion:

**Input**: Conversation transcript + full summary + question + (if available) previous summaries as context
**Model**: Best available for long-context reasoning (route via orchestration layer)
**Prompt**: Answer this question using ONLY information from the conversation and patient's journey. Quote the doctor where relevant. Never provide medical advice. Always attribute to the specific conversation.
**Output**: Answer string (200-400 words)
**Cache**: Cache answer per suggestion per summary (same question always returns same answer)
**Latency target**: <3 seconds for answer to start streaming

### Custom questions (on-demand)

Same as answer generation, but with user-provided question instead of auto-generated one. Store custom questions + answers for analytics.

### For Care Circle members

When a circle member views a shared summary, generate different suggestions:
- Patient context available (via sharing permissions)
- Questions framed from circle member perspective: "What does this mean day-to-day?" "What should we prepare?"
- Same grounding principle: always based on the actual conversation

### Model costs (rough estimate)

| Action | Tokens (est.) | Cost per call | Frequency |
|---|---|---|---|
| Suggestion generation | ~2K in, ~200 out | ~$0.003 | 1x per summary |
| Answer generation | ~5K in, ~500 out | ~$0.008 | ~2x per summary view (est.) |
| Custom Q&A | ~5K in, ~500 out | ~$0.008 | ~0.3x per summary view (est.) |

At 35K users, ~5K summaries/month: ~$150-250/month for Q&A feature. At 100K users: ~$500-800/month. Negligible.

---

## Edge Cases & Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Medical hallucination** | 🔴 Critical | Strict grounding: answer ONLY from conversation context. If the question can't be answered from available data, say so. Never fill gaps with general knowledge. |
| **Over-reliance** | 🟡 Medium | Every answer includes source attribution ("Based on your conversation with Dr. X on [date]") and medical disclaimer. |
| **Irrelevant suggestions** | 🟡 Medium | Quality eval: review generated suggestions for first 100 summaries. Tune prompt if suggestions are too generic. |
| **Dutch medical terms** | 🟡 Medium | Test suggestion quality on Dutch conversations specifically. Medical terminology extraction must handle Dutch abbreviations and code-switching. |
| **Empty context** | 🟡 Low | If user has only 1 summary, skip cross-appointment suggestions. If summary is very short, generate fewer suggestions. |
| **Latency** | 🟡 Medium | Suggestions pre-generated. Answers streamed. Target <3s to first token. Use fastest capable model for answers. |

---

## Success Metrics

| Metric | Baseline | Target | Measurement |
|---|---|---|---|
| **Primary: Suggestion tap rate** | 0% (new) | 20%+ of summary viewers tap at least 1 suggestion | Mixpanel |
| **Frequency lift** | Current summary revisit rate | 10%+ increase in summary revisits within 7 days | Mixpanel |
| **Custom question usage** | 0% (new) | 5%+ of suggestion users also use "Ask something else" | Mixpanel |
| **Circle engagement** | Current CNIS | Measurable CNIS uplift from circle members engaging with suggestions | Mixpanel |
| **Answer quality (internal)** | N/A | 95%+ of answers grounded in conversation data (manual review of 50 sample) | Internal eval |

### Guardrails (must not decrease)

- Summary generation quality score (98%+ target)
- Summary generation latency
- App performance (suggestion generation is async, should not slow down summary display)

---

## Experimentation

**Cheapest test**: Before building the full feature, generate suggestions for 50 existing summaries offline. Review with Merlijn + team:
- Are the suggestions specific and relevant?
- Would a patient actually want to know this?
- Is the answer grounded in the conversation?

If offline quality is strong, proceed to in-app build. If not, tune prompts before shipping.

**A/B approach**: Feature flag. 50% of new summaries get suggestions. Compare:
- Summary engagement (time on page, scroll depth)
- Revisit rate within 7 days
- Circle sharing rate (does deeper understanding drive more sharing?)

---

## Phasing

### P1: Core suggestions (4-5 weeks dev)

- Suggestion generation on summary creation (2-3 suggestions)
- Inline answer expansion on tap
- Source attribution + medical disclaimer
- Tracking events for all interactions
- A/B test setup

### P1.5: Circle suggestions (2 weeks dev, after P1 ships)

- Different suggestion set for circle members viewing shared summaries
- Circle-perspective framing

### P2: "Ask something else" (2 weeks dev, after P1 validated)

- Free-text input for custom questions
- Same grounding principles
- Rate limiting (prevent abuse)

---

## Tracking Plan

| Event | Trigger | Properties |
|---|---|---|
| Smart Suggestions - Displayed | Suggestions visible on summary | `summary_id`, `suggestion_count`, `has_previous_summaries`, `is_circle_member` |
| Smart Suggestions - Tapped | User taps a suggestion | `summary_id`, `suggestion_index`, `suggestion_text_preview`, `is_circle_member` |
| Smart Suggestions - Answer Viewed | Answer fully loaded | `summary_id`, `suggestion_index`, `answer_length`, `load_time_ms` |
| Smart Suggestions - Answer Collapsed | User collapses answer | `summary_id`, `suggestion_index`, `time_open_ms` |
| Smart Suggestions - Ask Custom | User taps "Ask something else" | `summary_id`, `suggestion_count_viewed` |
| Smart Suggestions - Custom Answer | Custom question answered | `summary_id`, `question_length`, `answer_length`, `load_time_ms` |

---

## Multi-Perspective Review

| Perspective | Verdict | Assessment |
|---|---|---|
| **User** | 🟢 | High-value. Addresses real pain (questions after appointment). Smart suggestions remove the "how do I use AI" barrier. Grounded answers are meaningfully different from Googling. |
| **Mobile Dev** | 🟢 | Moderate complexity. Summary UI extension (not new screen). LLM call on tap (async, streamable). Caching straightforward. No new external dependencies. Suggestion generation piggybacks on existing summary pipeline. |
| **CPO/Strategy** | 🟢 | Directly serves frequency (#1 priority). Proves the "brain" concept without building the full architecture. First step toward care intelligence platform. Differentiates from commoditized summarization. |
| **Growth** | 🟢 | Drives retention (reason to revisit summaries). Circle member engagement increases when they can ask questions about shared summaries. Potential activation lever: "Your summary has answers waiting." |
| **Business** | 🟢 | Low incremental cost (~$150-800/month at current-to-3x scale). Premium feature candidate for future monetization. Deepens product value beyond free-tier competitors. |
| **Privacy/GDPR** | 🟡 | Same data already processed for summaries (conversation transcripts sent to LLM). Q&A uses same pipeline with same data processing agreement. Circle member Q&A must respect sharing permissions (only answer from data the patient shared with them). Custom questions stored alongside summary data, same retention policy. **One concern**: custom question text could contain sensitive info not in the original conversation. Store with same protections as conversation data. |

No 🔴 blockers. Privacy concern is manageable within existing data handling framework.

---

## References

- [Care Brain Strategy](ideas/health-agent/care-brain-strategy.md)
- [ZeroClaw JTBD Discovery](ideas/health-agent/zeroclaw-jtbd-discovery.md) — Jobs #8, #9, #11
- [Activation & Audience Brainstorm](ideas/activation-and-audience/)
- [Unicorn Thesis](ideas/activation-and-audience/unicorn-thesis-consumer-layer-healthcare.md) — "AI as connective tissue" positioning
