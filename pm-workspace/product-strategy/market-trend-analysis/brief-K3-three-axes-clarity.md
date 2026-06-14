# Brief K3 — The Three Axes: Clarity, Connection, Convenience

**For:** CEO market framing | **Author:** Mewtwo (PM co-pilot) | **Date:** 2026-05-31
**Scope:** Map the market on three axes (Clarity / Connection / Convenience), go deep on Clarity, and answer the strategic moat question.

> **Reading convention.** Every claim carries a clickable source URL inline. Each source's publication date is flagged. The brief separates **[FACT]** (sourced), **[INFERENCE]** (my reasoning from facts), and **[RECOMMENDATION]** (what I'd do). Contrarian evidence is called out explicitly.

---

## 1) Executive summary

The CEO's three-axis framing is sound and maps cleanly onto the market: each axis already has well-funded incumbents, but **no one owns all three for the oncology patient + family in NL/EU**. That gap is real. The question is whether Clarity is a defensible place to stand.

- **Convenience** (access/scheduling/logistics) is **consolidated and won** in NL/EU by Doctolib (€348m+ ARR, 80m patient accounts, ~€5.8bn valuation) on the consumer-facing side, with ZorgDomein owning the B2B referral rail. [FACT] This is a network-effects, supply-side game. Not where a small player wins, and not Ditto's fight. ([Sifted, Mar 2025](https://sifted.eu/articles/doctolib-results-2024); [ZorgDomein/LLCP, n.d.](https://www.llcp.com/portfolio/zorgdomein/))
- **Connection** (family/care circle/community) is **fragmented and mostly low-tech**: CaringBridge and Lotsa (US, journaling/logistics), Caren/Carenzorgt (NL, tethered to care-provider EHRs via Nedap Ons), Kanker.nl (NL oncology info/community), Belong.Life (oncology community + AI mentor), and WhatsApp as the de-facto default. [FACT] No one has nailed the oncology family care circle as a product. This is Ditto's adjacent wedge, covered in prior work — kept short here.
- **Clarity** (understanding your care via AI) is **the most contested and fastest-moving axis**, and the one where the strategic bet must be made carefully. Three sub-markets: (a) curated/citation-grounded health chat — dominated for *physicians* by OpenEvidence ($12bn valuation, 40%+ of US doctors), with **no strong consumer-facing, citation-grounded oncology equivalent yet**; (b) symptom tracking & visualization — a crowded but UX-differentiated field (Bearable, Visible, Guava, MyTherapy, Vinehealth); (c) AI summaries/explainers — Ditto's home turf, overlapping clinical-scribe players (Abridge, Nabla).

**The moat verdict (preview).** [INFERENCE] You cannot win Clarity by out-intelligence-ing ChatGPT — and the evidence that this is impossible got *stronger* in April 2026 when OpenAI launched citation-grounded "ChatGPT for Clinicians." [FACT] ([OpenAI, Apr 2026](https://openai.com/index/making-chatgpt-better-for-clinicians/)) But there is a credible, *narrower* moat: **healthcare-specific UX (structuring/visualizing a patient's own longitudinal data) + verifiable trust (doctor-credible, EU-compliant, grounded in the patient's actual visit), localized for NL/EU.** The single strongest signal for this thesis is that OpenEvidence **withdrew entirely from the EU and UK in May 2026** over AI Act uncertainty — vacating the regulated-market high ground that a focused EU player is structurally positioned to hold. [FACT] ([Lancet Regional Health Europe, 2026](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(26)00130-4/fulltext))

---

## 2) The three axes mapped (who owns each)

| Axis | What it means | Who owns it | Structure | Ditto's position |
|---|---|---|---|---|
| **Convenience** | Access, scheduling, logistics, pharmacy/booking | **Doctolib** (consumer EU); **ZorgDomein** (NL B2B referral rail); Doctena, Spaarne/Epic MyChart locally | Network effects, supply-side lock-in. Won/consolidating. | Not Ditto's fight. Integrate, don't compete. |
| **Connection** | Family/care circle, community, updates | Fragmented: CaringBridge, Lotsa (US); Caren/Carenzorgt (NL, EHR-tethered); Kanker.nl, Belong.Life (oncology); **WhatsApp** (default) | Low-tech, fragmented, no oncology-family winner | Adjacent wedge; "care circle" is differentiated white space. |
| **Clarity** | Understanding your care via AI | OpenEvidence (physicians); ChatGPT (consumers, by default); no grounded consumer oncology winner | Fast-moving, contested, big-tech-adjacent | **The contested bet. See §3–5.** |

### Convenience — winning by bundling supply [brief]
- **Doctolib** is the EU consumer-facing winner: ~€348m ARR for 2024 (one source cites $402.6m / ~€5.8bn valuation), **80m patient accounts and ~400k healthcare-professional subscribers** across France, Germany, Italy and the Netherlands; ~€115m R&D in 2024, much of it on AI. [FACT, 2024–2025] ([Sifted, Mar 2025](https://sifted.eu/articles/doctolib-results-2024); [GetLatka, n.d.](https://getlatka.com/companies/doctolib)) It entered NL via acquisition (inherited team of ~50). [FACT] ([Sifted, n.d.](https://sifted.eu/articles/doctolib-france-europe-healthcare-startup)) **What it bundles:** booking + practice-management software + (increasingly) AI scribe/consultation tools — i.e. it is moving *toward* Clarity from the Convenience base.
- **ZorgDomein** (NL, founded 2000, PE-owned by Levine Leichtman) is the dominant **B2B e-referral / diagnostic-request rail** between GPs, hospitals and labs; patient-facing portal is thin. [FACT] ([ZorgDomein patient support, n.d.](https://patienten-support.zorgdomein.com/hc/nl/articles/10985640987538-What-is-ZorgDomein); [LLCP, n.d.](https://www.llcp.com/portfolio/zorgdomein/)) Hospital portals (e.g. MijnSpaarneGasthuis on **Epic MyChart**, DigiD login) own the patient-record access layer. [FACT] ([Spaarne Gasthuis, n.d.](https://www.spaarnegasthuis.nl/verwijzers/verwijzen-via-zorgdomein))
- [INFERENCE] Convenience is a solved, capital-intensive, network-effects game. A 10-person startup does not win here. The strategic move is **interoperability** (read appointments/records, don't rebuild booking).

### Connection — fragmented, low-tech, no oncology-family winner [brief]
- **CaringBridge** (US): private journaling/update hub so families stop repeating news to everyone. **Lotsa Helping Hands** (US): volunteer/task coordination (meals, rides). [FACT] ([Caring.com, 2024](https://www.caring.com/resources/best-caregiving-apps))
- **Caren / Carenzorgt** (NL, by **Nedap**): a "digital care map" for clients, family and mantelzorgers — but **tethered to the care provider's Nedap Ons EHR**; the patient/family experience depends on the institution enabling it. Renewed Nov 2025. [FACT] ([caren.nl, n.d.](https://caren.nl/); [Nedap support, 2025](https://support.nedap-ons.nl/support/solutions/articles/103000307341-informatiepagina-caren-3-0))
- **Kanker.nl** (NL): the national oncology info + community platform, run by IKNL, KWF and NFK — statistics, side-effect reviews, referral guide, patient community. [FACT] ([IKNL, n.d.](https://iknl.nl/over-iknl/wat-we-doen)) This is the credible NL oncology *content/community* incumbent and a likely partner, not a product competitor.
- **Belong.Life**: world's largest oncology social network + "Dave," an LLM oncology mentor trained on 7 years of patient interactions; ~$30m raised (Series B led by IQVIA). [FACT, 2023] ([Fierce Healthcare, 2023](https://www.fiercehealthcare.com/digital-health/belonglife-maker-social-network-cancer-patients-launches-ai-mentor)) Note: this player straddles Connection *and* Clarity.
- [INFERENCE] **WhatsApp is the real incumbent.** The connection job is mostly done badly in group chats. The opportunity is a purpose-built oncology care circle — but Connection alone is a thin, hard-to-monetize wedge. It is strongest as a *distribution and retention layer on top of Clarity*, not a standalone product.

---

## 3) Clarity deep-dive (a): curated-source health chat, incl. OpenEvidence

### OpenEvidence — the category-defining player (for physicians)
**[FACT]** OpenEvidence is a citation-grounded medical search/chat engine — a "brain extender" for clinicians, generating answers **exclusively from trusted, peer-reviewed sources** (NEJM, JAMA Network, FDA, CDC, PubMed) via exclusive licensing deals, explicitly to avoid the "Reddit forums" problem of general LLMs. ([healthcare.digital, 2026](https://www.healthcare.digital/single-post/openevidence-chatgpt-for-doctors-2026-plans-and-strategic-outlook))

Scale and traction (flag: numbers move fast):
- **$12bn valuation**, $250m Series D (Jan 2026), ~$700m raised since 2021, backers Thrive/DST/Sequoia/Kleiner/GV/Coatue. [FACT, Jan 2026] ([Crunchbase News, Jan 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/))
- **760,000 registered US physicians, ~18m clinical consultations/month, used daily by 40%+ of US physicians across 10,000+ hospitals; ~$100m ARR.** [FACT, Dec 2025–Jan 2026] ([CNBC, Jan 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html))
- Free to doctors, **ad-supported** (pharma). [FACT] ([Crunchbase News, Jan 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/))

**Consumer ambition?** [FACT] **No.** OpenEvidence is "direct-to-prosumer" — targeting physicians, nurses (5.2m), pharmacists, med students. No patient/consumer-facing product or stated plan. ([healthcare.digital, 2026](https://www.healthcare.digital/single-post/openevidence-chatgpt-for-doctors-2026-plans-and-strategic-outlook); [STAT, Jan 2026](https://www.statnews.com/2026/01/12/openevidence-medical-super-intelligence-jpm-conference/))

**The EU/UK exit — the single most important fact in this brief.** [FACT] In May 2026 OpenEvidence **geoblocked and withdrew its platform from the EU and UK**, citing EU AI Act uncertainty — specifically that classification as "high-risk AI" would require constant audits, algorithmic transparency and bias evaluations. ([Lancet Regional Health Europe, 2026](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(26)00130-4/fulltext); [Distilled Post, 2026](https://www.distilledpost.com/post/openevidence-withdraws-clinical-ai-platform-from-uk-and-europe-over-regulatory-uncertainty)) [INFERENCE] The best-capitalized clarity player just *vacated Ditto's home market* because regulated-market compliance is hard. A native EU player that treats AI Act / MDR / GDPR compliance as a feature, not a tax, inherits high ground the giants are fleeing.

### Consumer-facing, citation-grounded / trusted health Q&A
There is **no consumer equivalent of OpenEvidence with comparable scale.** The closest players:

| Player | What it does | Traction | Source (date) |
|---|---|---|---|
| **Ada Health** (Berlin) | AI symptom-assessment chat, probabilistic clinical reasoning over a curated medical knowledge base; freemium + enterprise/pharma (Bayer partner) | **11m+ users, 25m+ assessments**; $120m Series B | [Fierce Biotech, n.d.](https://www.fiercebiotech.com/medtech/ada-health-hits-120m-series-b-top-up-for-symptom-assessment-ai-app) |
| **Healthily** (ex-Your.MD, London/Oslo) | AI symptom checker + self-care content + tracking; English-first | ~**30m users / 12 months**; ~$139m raised over 9 rounds (last Sep 2022) | [Sifted, n.d.](https://sifted.eu/articles/healthtech-healthily-raises-20m); [pharmaphorum, n.d.](https://pharmaphorum.com/news/your-md-secures-30m-to-expand-self-care-app-healthily) |
| **Wysa** | Clinically-validated mental-health chatbot; FDA Breakthrough Device designation; NHS deployments | **4.5m users / 65 countries** (2022); £5.3m Wellcome grant (2025); 300k+ via Wysa Gateway | [TechCrunch, 2022](https://techcrunch.com/2022/07/14/wysa-20-million-series-b-funding-expand-therapist-chatbot-wider-mental-health-services/); [BusinessWire, Jun 2025](https://www.businesswire.com/news/home/20250611949498/en/Wysa-Launches-AI-Powered-Chatbot-to-Streamline-Mental-Health-Patient-Intake-in-the-US) |
| **Belong.Life ("Dave")** | Conversational AI oncology mentor on a cancer community, trained on 7 yrs of patient interactions | Tested by 10k+ patients; ~$30m raised | [Fierce Healthcare, 2023](https://www.fiercehealthcare.com/digital-health/belonglife-maker-social-network-cancer-patients-launches-ai-mentor) |

[INFERENCE] Note the pattern: symptom-checkers (Ada, Healthily) ground in a *curated clinical knowledge base* but are **triage/pre-visit** tools — they don't ground in *your* visit. Belong is the only oncology-specific conversational player, but its grounding is community data, not your medical record or peer-reviewed literature. **The white space: citation-grounded, oncology-specific, consumer-facing Q&A that is grounded in the patient's own care (their visit, their record) — not generic triage.** Nobody owns this in NL/EU.

---

## 4) Clarity deep-dive (b): symptom tracking & visualization

This is the most *executable* part of Clarity, because the moat here is **product craft (structuring + visualizing longitudinal data)**, which compounds with proprietary user data and is hard to copy quickly — unlike raw chat intelligence.

| Player | What it does well | Traction | Source (date) |
|---|---|---|---|
| **Bearable** (UK) | Best-in-class **correlation engine**: auto-correlates symptoms with sleep, diet, weather, meds, habits; surfaces patterns after ~7 days. Built by people with chronic illness. | **900k+ users**; free + premium reports | [Bearable, n.d.](https://bearable.app/) |
| **Visible** (UK) | ME/CFS & Long-COVID **pacing**: bundled wearable, real-time PEM/illness-specific metrics; deep condition focus | **100k+ users**; investors with "skin in the game" | [TechCrunch, 2022](https://techcrunch.com/2022/11/22/visible-launches-activity-tracking-platform-to-tackle-long-covid/); [ME Association, Apr 2024](https://meassociation.org.uk/2024/04/visible-the-pacing-app-for-people-with-me-cfs-and-long-covid/) |
| **Guava Health** (US) | **Aggregation + visualization**: pulls records from 50k+ US providers (MyChart/Cerner), AI-extracts labs from PDFs/DICOM/CCDA, **body heat map**, symptom co-occurrence, treatment comparison. HIPAA, no ads, no data sale. | App-store scale, exact MAU not public | [guavahealth.com, n.d.](https://guavahealth.com/) |
| **Vinehealth** (UK) | **Oncology-specific** symptom + med tracking, care-team comms; closest direct comparable to Ditto's space | $6.99m raised; **acquired by Sciensus Jan 2024** (for the data asset) | [MobiHealthNews, n.d.](https://www.mobihealthnews.com/news/emea/digital-health-startup-vinehealth-lands-55m-oncology-platform); [Medical Device Network, 2024](https://www.medicaldevice-network.com/news/sciensus-acquires-oncology-symptom-tracker-app-vinehealth/) |
| **MyTherapy** (Germany, smartpatient) | Med-reminder + symptom/measurement diary + adherence; "always free"; pharma-funded | "hundreds of thousands" of users; German Health Award 2023 | [mytherapyapp.com, n.d.](https://www.mytherapyapp.com/) |

[INFERENCE — three takeaways]
1. **Visualization is the differentiator, not tracking.** Bearable's correlations and Guava's body heat map are what users praise — the *structuring of messy data into legible insight*. That craft is Ditto-shaped.
2. **Oncology-specific tracking is a thin, acquirable market.** Vinehealth, the clearest comparable, was acqui-hired by a pharma supply company for its data, not scaled as a consumer brand. [FACT] [INFERENCE] This is a signal that *tracking alone* doesn't reach venture scale — it needs to be part of a larger value loop (which is exactly the three-axis bundle argument).
3. **The data asset is the prize.** Sciensus bought Vinehealth, IQVIA backed Belong, Bayer backed Ada — pharma/data buyers value the **longitudinal real-world patient data**, not the app UI. [INFERENCE] Ditto's tracking/visualization, grounded in actual visit summaries, could produce uniquely structured oncology RWD — a second business model beneath the consumer product.

### Clarity deep-dive (c): AI summaries/explainers [brief — overlaps prior work]
- **Abridge**: generative AI scribe; patients leave with a **plain-English after-visit summary** + care plan. [FACT] ([abridge.com, n.d.](https://www.abridge.com/)) **Nabla**: scribe with pre-visit context summaries. [FACT] ([nabla.com, n.d.](https://www.nabla.com/blog/ai-medical-scribes))
- [INFERENCE] These are **clinician-side, enterprise-sold** tools where the patient summary is a by-product. Ditto's distinction is **patient-first** summaries (consumer-owned, family-shareable), not a hospital IT sale. Different buyer, different wedge — but watch Abridge: if it pushes its patient summary into a consumer/family layer, it converges on Ditto from the enterprise side, the way Doctolib converges from Convenience.

---

## 5) The moat question: healthcare UX + trust vs. raw intelligence

**The hypothesis:** A focused player can win Clarity not by being smarter than ChatGPT (impossible; big tech moves fast on raw intelligence; consumers under-value privacy), but via **(1) superior healthcare-focused UX** (tracking, visualization, structuring) **+ (2) trust/verification** (doctor-credible, curated/grounded sources, EU-compliant).

### Evidence FOR the moat
- **[FACT] Big tech does not yet own the structured, longitudinal, patient-owned data layer.** ChatGPT answers questions; it does not maintain *your* visit history, *your* symptom timeline, *your* care circle. The 2025 Rock Health survey shows consumers want "the ease and actionability of ChatGPT… in every step of their care journey" — i.e. demand for *integration into a journey*, not just answers. ([Rock Health, Dec 2025](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/))
- **[FACT] Trust still routes through clinicians.** 40% of AI-health users consulted a provider *after* a chatbot interaction; clinicians remain the most-trusted source (85–88%). ([Rock Health, Dec 2025](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)) [INFERENCE] A product positioned *with/beside* the clinician (grounded in the real visit) inherits trust that a standalone chatbot cannot.
- **[FACT] The EU regulatory moat is now demonstrated, not theoretical.** OpenEvidence ($12bn) abandoned the EU/UK over AI Act risk. ([Lancet, 2026](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(26)00130-4/fulltext)) [INFERENCE] A Rotterdam company built EU-native (GDPR, MDR, AI Act) holds ground that better-funded US players are *actively retreating from*. This is the strongest single piece of pro-moat evidence.
- **[FACT] Condition-specific UX wins where generalists don't.** Visible (ME/CFS pacing), Bearable (correlations), Belong (oncology) all show durable engagement from *depth* in a condition. Generic ChatGPT cannot replicate a PEM-aware pacing UI or an oncology-tuned care timeline.
- **[FACT] Pharma/data buyers reward proprietary RWD.** Vinehealth→Sciensus, Belong←IQVIA, Ada←Bayer. The defensible asset is the **structured longitudinal dataset**, which compounds and is not commoditized by foundation-model progress.

### Contrarian evidence AGAINST the moat (read this carefully)
- **🔴 [FACT] Big tech is invading the "trusted/grounded" position directly.** In **April 2026 OpenAI launched "ChatGPT for Clinicians"** — citation-grounded answers from PubMed, FDA and medical societies, built with 260+ physicians, 99.6% rated safe/accurate, and in one test it cited ground-truth sources *more often than human physicians*. ([OpenAI, Apr 2026](https://openai.com/index/making-chatgpt-better-for-clinicians/); [HIT Consultant, Apr 2026](https://hitconsultant.net/2026/04/23/chatgpt-for-clinicians-openai-launch-gpt-5-4/)) [INFERENCE] "Citation-grounded trust" is **not** a durable moat on its own — OpenAI just shipped it for free. Trust-via-citations is becoming table stakes.
- **🔴 [FACT] Consumers are already defaulting to ChatGPT for the exact jobs Ditto targets.** 40m people/day ask ChatGPT health questions; 1 in 4 of 800m+ weekly users asks a health prompt; **55% use it to check symptoms, 48% to understand medical terms/instructions, 44% to understand treatment options.** ([Fierce Healthcare, n.d.](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says); [eMarketer, n.d.](https://www.emarketer.com/content/1-4-chatgpt-users-submit-prompts-about-healthcare-weekly)) "Understanding your care" is *already* one of ChatGPT's highest-volume use cases. Ditto is not entering empty space; it is entering ChatGPT's busiest room.
- **🟡 [FACT] Consumers under-value privacy, undercutting the GDPR/trust pitch as a *consumer* differentiator.** AI-health users are *more* willing to share data with tech firms (23%) and consumer-tech (15%) than non-users, despite weaker protections. ([Rock Health, Dec 2025](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)) [INFERENCE] "We're more private/compliant" wins with *regulators, hospitals and partners* — not necessarily with the end consumer choosing an app. Sell trust B2B/B2B2C; sell UX/usefulness B2C.
- **🟡 [FACT] Tracking-only oncology products don't reach scale alone** (Vinehealth acqui-hired). [INFERENCE] UX craft is necessary but insufficient; it must sit inside a loop that creates compounding value (data + care circle + clinician trust).

### The synthesis [INFERENCE + RECOMMENDATION]
**The moat is not UX *or* trust *or* intelligence individually — each is being commoditized.** The defensible position is the **compound**: healthcare-specific UX **×** clinician-grounded trust **×** EU-native compliance **×** patient-owned longitudinal data **×** family care circle — *localized for NL/EU oncology*, where no global player is currently competing.

- Raw intelligence: **rent it** (foundation models), don't try to win it. You will lose.
- Citation-grounding alone: **table stakes** post-ChatGPT-for-Clinicians. Necessary, not sufficient.
- The durable edges, ranked:
  1. **Grounding in the patient's *actual* care** (their visit, their record) — ChatGPT grounds in literature, not in *you*. This is the sharpest differentiator and the hardest for a generalist to copy.
  2. **EU-native trust/compliance** — a demonstrated vacancy (OpenEvidence exit). Strongest as a B2B2C / hospital / regulator wedge.
  3. **Oncology-specific UX + visualization** — compounds into proprietary RWD; defensible via depth and data, not cleverness.
  4. **Family care circle** — the retention/virality layer that none of the Clarity players have, and the bridge to the Connection axis.

[RECOMMENDATION] Frame Clarity as **"understanding *your* care," not "understanding *health*."** The moment Ditto competes on generic medical Q&A it loses to ChatGPT. The moment it competes on *making your specific oncology journey legible, trustworthy, and shareable with your family*, it is in a room big tech is not in — and that OpenEvidence just left.

---

## 6) Sources

**Convenience**
- Doctolib 2024 results / ARR / valuation — [Sifted, Mar 2025](https://sifted.eu/articles/doctolib-results-2024); [GetLatka](https://getlatka.com/companies/doctolib); [Sifted, Europe expansion](https://sifted.eu/articles/doctolib-france-europe-healthcare-startup)
- ZorgDomein — [Patient support](https://patienten-support.zorgdomein.com/hc/nl/articles/10985640987538-What-is-ZorgDomein); [LLCP portfolio](https://www.llcp.com/portfolio/zorgdomein/); [Spaarne Gasthuis referrals](https://www.spaarnegasthuis.nl/verwijzers/verwijzen-via-zorgdomein)

**Connection**
- Caregiving apps overview (CaringBridge, Lotsa) — [Caring.com, 2024](https://www.caring.com/resources/best-caregiving-apps)
- Caren/Carenzorgt (Nedap) — [caren.nl](https://caren.nl/); [Nedap support, Nov 2025](https://support.nedap-ons.nl/support/solutions/articles/103000307341-informatiepagina-caren-3-0)
- Kanker.nl / IKNL — [IKNL](https://iknl.nl/over-iknl/wat-we-doen)
- Belong.Life "Dave" + funding — [Fierce Healthcare, 2023](https://www.fiercehealthcare.com/digital-health/belonglife-maker-social-network-cancer-patients-launches-ai-mentor); [PR Newswire, 2023](https://www.prnewswire.com/news-releases/belonglife-launches-dave-worlds-first-real-time-conversational-ai-oncology-mentor-for-cancer-patients-301820795.html)

**Clarity — curated-source chat**
- OpenEvidence valuation/traction — [Crunchbase News, Jan 2026](https://news.crunchbase.com/venture/openevidence-ai-doctors-doubles-valuation-seriesd/); [CNBC, Jan 2026](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html); [BusinessWire, Jan 2026](https://www.businesswire.com/news/home/20260121029132/en/OpenEvidence-Raises-$250-Million-to-Build-Medical-Superintelligence-for-Doctors)
- OpenEvidence strategy / sources / no-consumer-plan — [healthcare.digital, 2026](https://www.healthcare.digital/single-post/openevidence-chatgpt-for-doctors-2026-plans-and-strategic-outlook); [STAT, Jan 2026](https://www.statnews.com/2026/01/12/openevidence-medical-super-intelligence-jpm-conference/)
- OpenEvidence EU/UK withdrawal — [Lancet Regional Health Europe, 2026](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(26)00130-4/fulltext); [Distilled Post, 2026](https://www.distilledpost.com/post/openevidence-withdraws-clinical-ai-platform-from-uk-and-europe-over-regulatory-uncertainty); [Telehealth.org, 2026](https://telehealth.org/news/openevidence-exits-europe-highlighting-divide-in-health-ai-rules/)
- Ada Health — [Fierce Biotech](https://www.fiercebiotech.com/medtech/ada-health-hits-120m-series-b-top-up-for-symptom-assessment-ai-app); [Wikipedia](https://en.wikipedia.org/wiki/Ada_Health)
- Healthily / Your.MD — [Sifted](https://sifted.eu/articles/healthtech-healthily-raises-20m); [pharmaphorum](https://pharmaphorum.com/news/your-md-secures-30m-to-expand-self-care-app-healthily); [Wikipedia](https://en.wikipedia.org/wiki/Your.MD)
- Wysa — [TechCrunch, 2022](https://techcrunch.com/2022/07/14/wysa-20-million-series-b-funding-expand-therapist-chatbot-wider-mental-health-services/); [BusinessWire, Jun 2025](https://www.businesswire.com/news/home/20250611949498/en/Wysa-Launches-AI-Powered-Chatbot-to-Streamline-Mental-Health-Patient-Intake-in-the-US)

**Clarity — symptom tracking & visualization**
- Bearable — [bearable.app](https://bearable.app/)
- Visible — [TechCrunch, 2022](https://techcrunch.com/2022/11/22/visible-launches-activity-tracking-platform-to-tackle-long-covid/); [ME Association, Apr 2024](https://meassociation.org.uk/2024/04/visible-the-pacing-app-for-people-with-me-cfs-and-long-covid/)
- Guava Health — [guavahealth.com](https://guavahealth.com/)
- Vinehealth (+ Sciensus acquisition) — [MobiHealthNews](https://www.mobihealthnews.com/news/emea/digital-health-startup-vinehealth-lands-55m-oncology-platform); [Medical Device Network, 2024](https://www.medicaldevice-network.com/news/sciensus-acquires-oncology-symptom-tracker-app-vinehealth/)
- MyTherapy — [mytherapyapp.com](https://www.mytherapyapp.com/)

**Clarity — AI summaries/explainers**
- Abridge — [abridge.com](https://www.abridge.com/)
- Nabla — [nabla.com](https://www.nabla.com/blog/ai-medical-scribes)

**Moat — consumer behavior & big-tech invasion**
- ChatGPT health usage (40m/day, 1-in-4 weekly, symptom/term/treatment use) — [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/40m-people-use-chatgpt-answer-healthcare-questions-openai-says); [eMarketer](https://www.emarketer.com/content/1-4-chatgpt-users-submit-prompts-about-healthcare-weekly)
- ChatGPT for Clinicians (citation-grounded, Apr 2026) — [OpenAI, Apr 2026](https://openai.com/index/making-chatgpt-better-for-clinicians/); [HIT Consultant, Apr 2026](https://hitconsultant.net/2026/04/23/chatgpt-for-clinicians-openai-launch-gpt-5-4/)
- Rock Health 2025 Consumer Adoption Survey (trust, privacy, post-query action) — [Rock Health, Dec 2025](https://rockhealth.com/insights/the-tortoise-and-the-hare-of-care-health-ai-insights-from-rock-healths-2025-consumer-adoption-survey/)

---

### Caveats & confidence
- Traction figures for fast-moving AI players (esp. OpenEvidence) are point-in-time (Dec 2025–Jan 2026) and will be stale within a quarter. Flagged inline.
- User counts for tracking apps (Bearable 900k, MyTherapy "hundreds of thousands") are self-reported on company sites; treat as directional, not audited.
- The OpenEvidence EU withdrawal is well-corroborated (Lancet + trade press) and is the load-bearing fact for the EU-moat thesis. High confidence.
- I did not find a strong, scaled, *Dutch-native* consumer Clarity player — itself a finding: the NL/EU consumer Clarity slot appears open.
