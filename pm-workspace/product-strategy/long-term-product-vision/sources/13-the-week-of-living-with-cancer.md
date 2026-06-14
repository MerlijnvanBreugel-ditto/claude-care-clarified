# 13 — The Week of Living with Cancer (and the AI-Native Daily Evidence)

**Status:** synthesis of a 10-finder + critic deep-research sweep (2026-06-05), answering two questions: *what do people with cancer deal with daily and weekly (emotional, practical, cognitive, social)?* and *is there published evidence that AI-native daily mechanics retain?* Raw data: [`research/core-action-evidence-sweep/daily-life-sweep.json`](../../../research/core-action-evidence-sweep/daily-life-sweep.json). Verbatim quotes throughout; unlike sources 12/14, the load-bearing numbers here are flagged but NOT yet 3-vote verified (see §7).

## Bottom line (my read)

1. **The week is forecastable.** The chemo cycle has a stable per-patient architecture (steroid buffer days 0–2, crash days 3–5, the turn at day 7, a near-normal third week shadowed by dread), and the day has one too (mid-morning is the good window, fatigue peaks at bedtime, night is the hardest emotional hour). Patients already run this model in their heads ("chemo Wednesday, sick till Sunday"). A companion that knows your cycle day can *predict your day*, which is what patients say their diaries are actually for.
2. **The heaviest loads are not medical.** A median ~7 hours/week of cancer admin (it has a clinical name now: "logistic toxicity"), 2 hours of travel/waiting per hour of treatment, the social labor of updates and deflecting pity, and the nights. The product surface area is mostly *life*, not symptoms.
3. **The worst phase comes after treatment, and the triggers never stop.** The Dutch "zwarte gat": help evaporates the day treatment ends, the ward number you could always call is gone, and scanxiety does not habituate ("86 times and I still get scanxiety"). This is a years-long, episodic, lifelong product surface.
4. **On Merlijn's three mechanics, the evidence splits cleanly:** daily check-in with synthesis has the strongest retention signal in the AI era (10×+ the pre-AI baseline, with a morning ritual as the single biggest driver) but decays to ~2×/week by week 4 and hits a month-3 cliff; context-grounded Q&A is already proven behavior at planetary scale (40M people ask ChatGPT health questions *daily*, with no streaks and no persona — pure on-demand utility); and voice symptom capture works only as **input convenience** (the signal lives in the words, not the acoustics — the voice-biomarker category just died, and Dutch elderly speech breaks off-the-shelf ASR until fine-tuned).
5. **Design rules from products with real numbers:** win the habit in the first two weeks; deliver value before asking for input (pregnancy apps' zero-entry weekly reward; Oura's wake-up score); a weekly anchor beats daily logging (Noom's best users weighed in once a week); proactive system-triggered outreach over fixed calendars (Virta, 83% retention at 1 year); never punish a missed day (streaks backfire catastrophically in illness); and the strongest retention multiplier is an accountability partner — which for Ditto is the care circle we already have.

---

## 1. The architecture of the week (21-day infusion cycle)

| Cycle days | What it's like | In their words |
|---|---|---|
| **Day 0 (infusion)** | A full workday consumed (7am pickup, home after 3pm), but sedated, not active: wired 1–2h on steroids, then dozing through a 6–8h drip | "Loaded up with Benadryl and mostly doze for the next 6 hours" |
| **Days 1–2** | The steroid buffer: deceptively okay, manically energetic, and sleepless (~45% moderate-severe insomnia on dexamethasone) | "I went crazy with the housework... physically I am feeling fine, mentally I am broken into pieces" |
| **Days 3–5** | The crash: steroids gone, sickness peaks, stairs become the limiting activity | "Days 4 and 5 were the worst, the steroids had worn off but the sickness was there"; "zelfs de trap op lopen ging bijna niet" |
| **Days 6–7** | The turn: "two steps forward" (NL diary), non-linear | "Vanaf zaterdag ging het ietsje beter, 2 stapjes vooruit" |
| **Week 2** | Recovering; rationed 90-minute upright windows | |
| **Week 3** | Near-normal, and dreading the next round | "The first they felt almost normal, yet they were absolutely dreading the next treatment" |

Modifiers: take-home pump regimens carve a dead Monday–Wednesday block plus one usable week; toxicity is cumulative (the same hill takes 3× longer by the last cycle); the hardest month can be **after the final infusion**. And one NL-specific texture: the chemo pump travels in the handbag via thuiszorg — treatment literally walks through daily life ("met mijn chemopomp in mijn handtas").

## 2. The architecture of the day

- **Mid-morning is the reliable window**; patients schedule anything demanding there. Exception: parents, whose mornings are spent on the school run while "quickly winded."
- **Fatigue rises through the day and peaks at bedtime**, not mid-afternoon. Evening fatigue is more prevalent and more persistent than morning fatigue (~80% vs ~67%, statistically distinct phenotypes — US data, verify before relying). Thinking and mood degrade in the same afternoon/evening window.
- **Energy is counted in spoons, and a day buys one of three:** "I typically had enough energy to do one thing each day — take a shower, or go to Target, or go to lunch with a friend — but I couldn't do all three."
- **Night is the hardest hour.** "After I turn off the lights, my thoughts go immediately to my cancer and possibly dying from it." Sleep arrives in 2–3 hour fragments; ~half wake early; some vomit on a clock (midnight and 3am); steroid nights are write-offs filled with "quiet busywork." The 3am awake-and-afraid hour is the single most product-relevant uncovered window (see §6).
- **The night before infusion is a leverage point:** poor pre-chemo sleep (~55% of one sample) predicted worse fatigue and mood across the *entire* 3-week cycle (verify; if it holds, one well-timed intervention shapes 21 days).

## 3. What fills the week

**Practical/admin — a part-time job.** Median 400 minutes (~7 hours) per week managing cancer; at least one care task at home on 80% of days; ~2 hours travel/wait per 1 hour of treatment; for 35% it disrupts normal life on most days. NL specifics: the bedrijfsarts re-integration track is slow and rated 4.6/10 by patients; the eigen risico is consumed annually by routine controls; for half of 2,391 NFK respondents the financial damage had **not recovered after five years**; the weekly machine includes regiotaxi reimbursements, hospital bags, helper rosters, online groceries. Childcare silently drives *missed treatment*: nearly half of parents rescheduled oncology appointments over childcare; 1 in 7 radiotherapy patients missed sessions.

**Social — labor, loss, and the pity tax.** 47% find it hard to ask for help; the #1 reason is fear of pity (43%), and it's sharply gendered (58% of women vs 36% of men; women take 10 days to even tell loved ones, men 6). "Cancer ghosting" is majority-experienced; friends withdraw because "I reminded them of death," without explanation. Loneliness lives *inside* the full house ("there could be everybody home in my house and I still feel really alone") and inside the couple (partners present for logistics, absent emotionally). The distinctly Dutch friction is linguistic: "hoe gaat het?" has no good answer ("eigenlijk maar 1 ding: slecht"), and "wat zie je er nog goed uit" cuts ("waarom dan het woordje 'nog'?"). Patients prefer clumsy words over avoidance. Caregivers hit their own wall: "Ik ben er zó klaar mee. Ik kan en wíl hem even niet horen" — and explicitly want practical help, not check-in questions.

**Emotional — a rhythm, not a state.** Dexamethasone runs a named weekly cycle families brace for ("Dex Day!", the bear barking orders, the crash ~40 hours later). Identity loss recurs daily ("Me gewoon even Deborah voelen in plaats van dat zieke, vermoeide hoopje mens"). Numbness and autopilot at appointments. Anger that needs permission. Scanxiety peaks in the ~6 days *before* a scan ("like a death row prisoner hoping for a stay of execution") and costs functional weeks. Post-treatment brings the gratitude burden: "I'm living, and I should be grateful, but I just want to cry... What's wrong with me?" — which actively suppresses help-seeking exactly when support has evaporated. Moments of normalcy exist and are fragile: hands in warm dishwater, "the illusion of normalcy."

**Cognitive/physical micro-reality.** Chemo brain (~75% during treatment) fires as discrete, nameable failure events: the 2.5-hour grocery trip (wallet, then bag, then keys, then list), the car lost for an hour, the word "salt" gone at the dinner table. The dominant workaround is external memory (pocket lists, one fixed daily alarm). Taste is a *daily roulette*, not a stable deficit ("elke dag was mijn smaak anders") — cold, sweet, acidic survives when hot and savory doesn't; cooking smells are a barrier before taste even starts. Eating becomes clock-driven defense ("I have to eat every two hours or the shit hits the fan"). And one direct design constraint: **neuropathy degrades the phone itself** — numb, painfully cold fingers make patients limit phone use. Voice input and big touch targets are accessibility requirements here, not novelties.

## 4. Phase contrast

| Phase | Dominant reality | Sharpest signal |
|---|---|---|
| **Limbo (diagnosis → start)** | Fighting intrusive thoughts; a single ambiguous clinician word becomes the rumination object | A *fast* hospital callback reads as bad news; proactive "no results yet" calls measurably reduce distress |
| **Active treatment** | The cycle clock above; life re-engineered around symptom timing, not taken off | "Never took a full day off" but no early calls |
| **Off-weeks** | Near-normal week shadowed by countdown | The least documented, most product-critical window (§6) |
| **First year after** | The zwarte gat: structure and reassurance vanish at once; offers of help don't convert | "When I was in treatment, I could ring the ward... now what do I do if I'm worried?" |
| **Metastatic/chronic (years)** | Scan-to-scan time; no plans beyond the next result; energy economy; deliberate compartmentalization ("I entered the grief room when my boys were at school") | "Take your tablets, turn up for appointments, and between those times find things that make you happy." The 5 working days between scan and uitslag are the heaviest (NL) |

## 5. The AI-native daily evidence (Merlijn's three mechanics, scored)

**Daily check-in + smart synthesis — strongest signal, with a shape.** Youper held 42.7% of subscribers active at week 4 against a 3.3% industry 30-day median (10×+), but cadence decayed from 6.5 conversations/week to ~2 by week 4. Woebot ran near-daily for two weeks with 9% attrition vs 31% control. The single biggest retention driver found anywhere: **Wysa's morning check-in ritual** (HR 0.89, p=.001 — small effect, vendor-affiliated, verify). The cliff is month 3: automated nudges retain 30–60 days; beyond that, human accountability outperforms pure app — and 2–3× higher 90-day retention comes from having an accountability partner. **Our care circle is a built-in accountability partner no solo app has.** Anti-pattern with hard numbers: streaks. Fewer than 1% of users who break a 2–3 day streak ever return (weak source, but Lally's habit science agrees: missing a day doesn't hurt habit formation — punishing it does). Cancer patients *will* miss crash days; the design must treat that as expected, never as failure.

**Context-aware Q&A / explainers — proven behavior, wrong to make it a persona.** 40M+ people ask ChatGPT health questions daily; ~200M weekly. No streaks, no companion character: pure on-demand utility at the moment of need. Character.AI's 93 min/day proves AI *can* be obsessive, but that's parasocial entertainment; Slingshot's Ash (a16z, $93M) explicitly designs for "healthy disengagement." In NHS deployment, AI support increased therapy session attendance 42% (Limbic). Verdict: build the grounded ask-anything as an always-available utility woven into the companion, not a chatty friend. Telling detail: Belong's Dave, the closest oncology analog, publishes *zero* engagement numbers after years — assume the numbers are unflattering.

**Voice/automatic symptom capture — yes as input, no as biomarker.** The signal lives in the **words**: top LLMs exceed 90% F1 extracting symptoms/mood from patient *text*, while adding audio features *under*performs text-only by 2–4%. The acoustic-biomarker category just collapsed: Kintsugi (the flagship) shut down Feb 2026 and open-sourced its tech; field-wide, 1 of 308 models ever approached clinical implementation. The one study testing exactly our use case (extracting palliative-care symptoms from conversational patient speech) failed across the board (all F1 < 0.5), driven by 55.6% transcription accuracy on patient speech. And the home-market kicker: **Whisper hits 28.7% word-error-rate on elderly Dutch speech out of the box** (~9% after fine-tuning on the JASMIN corpus). Verdict: voice as a low-friction input channel (transcribe → LLM extracts from words) is right, *requires Dutch fine-tuning*, and outputs must stay non-diagnostic. Acoustic mood-detection: don't.

**Design rules from products with real retention numbers:**
1. **Win the habit in the first 14 days** (Hinge Health: 6 sessions in 2 weeks = the "habit point").
2. **Reciprocity before input**: deliver something before asking anything. Pregnancy apps are the only consumer category with genuine daily health habits, and their hook needs zero data entry (this week your baby is the size of a lime); Oura/Whoop deliver a wake-up score for free. The Ditto analog: "here's what today likely looks like (cycle day 4), here's what your circle asked."
3. **A weekly anchor beats daily logging**: Noom's most successful users weighed in once a week; weigh-ins, not meal logs, best predicted outcomes.
4. **Proactive and system-triggered, not calendar-fixed** (Virta's Spark flags who needs outreach; 83% retention at 1 year; Livongo replies at the decision moment, 1.8 checks/day).
5. **Fit their rhythm**: 42% of Sword sessions happen outside working hours, 23% on weekends.
6. **≤2 notifications/day, <60-second loop, and decay is universal** — front-load value, don't fight the curve.

## 6. What even this sweep couldn't see (the critic's holes → interview targets)

1. **The caregiver's hour-by-hour day** — we have time totals (NL eQuiPe: median 15h/week; US: 33h/week), zero clock texture. For a circle-led growth thesis, the entire B-side of every day is a hole.
2. **The near-normal week (days 14–20)** — richly lived, barely documented. If there's no symptom to manage, what is the daily hook? This is where a companion earns its keep or gets deleted.
3. **Weekends** — clinic closed, helpline gone, partner home, no school anchor. Never studied.
4. **The 3am awake hour** — we know they're awake; we don't know what would be wanted vs resented then.
5. **Oral-therapy regimens** — no infusion anchor, flat-but-grinding daily profile, growing share of oncology. The whole cycle map above doesn't apply.
6. **The structurally empty mid-cycle Wednesday** — no event, no crash, no scan. Retention lives or dies here.
7. **Mealtimes on good days** — eating is a 3×/day natural anchor; we only see it broken.
8. **The within-day medication clock** — the most obvious companion hook, still fragmentary in texture.

All eight go into the interview discussion guide.

## 7. Verification flags (unlike sources 12/14, not yet adversarially verified)

| Claim | Why it matters | Status |
|---|---|---|
| Morning/evening fatigue are distinct phenotypes (80%/67%) | Dictates check-in timing | US cohort; verify before design relies on it |
| Wysa morning check-in HR 0.89 | The most decision-relevant retention number | Small effect, vendor-affiliated, no control |
| Streak-break return rates (0.90%) | Hard anti-streak constraint | Single vendor blog; directionally backed by Lally |
| Replika ~20% D90 / Character.AI 93 min/day | Retention ceiling/floor anchors | Secondary aggregators, low confidence |
| Pre-chemo sleep shapes the whole cycle | A single high-leverage intervention point | One study; verify cohort and effect window |
