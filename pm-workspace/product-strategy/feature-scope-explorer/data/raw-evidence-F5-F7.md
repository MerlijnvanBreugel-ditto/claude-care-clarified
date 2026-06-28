# Raw evidence — F5 (care coordination), F7 (social networks)
_Extracted 2026-06-25. Raw material for features.json._

## SHARING (F7 + F5)

### Shareable health updates
- **Players**: CaringBridge (300k+ people/day, 1,600+ msgs/hr; donation nonprofit; 25-yr brand; CORE; no EU equivalent at scale); WhatsApp family group (Meta, 2B+; the actual default incumbent; health-update is incidental, lacks medical context); Caren/Nedap Ons (NL family/client portal tethered to Ons EHR, MedMij-compliant; care org pays; CORE but EHR-bundled); Belong.Life (IL, ~200k cancer patients; sharing is part of community surface).
- **Retention**: Crisis-episodic — high during crisis, decays on recovery/death. A plain update competing with WhatsApp on its turf is "a broadcast, not a network."
- **Reimbursement**: None.
- **Who pays**: Nobody directly. CaringBridge = donations because "loved ones don't pay; the patient is too overwhelmed to."
- **Takeaway**: A bare health update is a worse WhatsApp. Only defensible if the update carries medical comprehension WhatsApp can't replicate (plain-language summary of scan/meds/next steps).

### Light, frequent care updates
- **Players**: Strava (precedent — Kudos one-tap; 14B+ kudos in 2025 +20% YoY; group activities 95-121% more kudos; social streaks 5.69 vs 4.25 days; ~150M registered, ~50M MAU, ~1.2M paying, ~$500M ARR target, $2.2B val; CORE mechanic); Flo (daily log is habit core, community amplifies; ~70-77M MAU, ~5M paying, ~$157.6M ARR, $1B+ val); CaringBridge (reactions; crisis-episodic).
- **Retention**: THE retention engine. Strava "witnessing loop" (effort acknowledgement, zero composition) made a solitary activity a daily habit. **Caveat**: the kudos loop does NOT transfer to the patient's grim activity ("chemo round 4 done" is not a kudos moment); it transfers only to the *circle side* (one-tap 💚, "thinking of you"). Engineer frequency on the circle side, not from the patient.
- **Who pays**: In precedents users pay (Strava ~$79.99/yr, Flo Premium) — but for fitness/cycle utility. No user-pay precedent for care updates.
- **Takeaway**: Copy the mechanic but flip direction: frequency from loved ones' low-effort presence. Metric = "how many people are actively present, how often?" not "did the patient share?"

### Public sharing of updates
- Not covered as a distinct feature. Sharing is treated as circle-scoped (CaringBridge, WhatsApp) or anonymous/stranger (Flo Secret Chats, Belong anonymous, Inspire). No named player offers public (open-web, identified) sharing.
- **Signal**: anonymity (not publicity) unlocks participation — "people share what they'd never post under their name."
- **Takeaway**: Evidence points AWAY from public identified sharing for serious illness. Treat as unsupported.

### Peer finding
- **Players**: PatientsLikeMe (~830k members, 2,900+ conditions; never charged users; sold de-identified data to pharma; → UnitedHealth/Optum 2019; CORE); Inspire (10M+ annual visitors, 3,000+ conditions; 100% pharma-funded; → CorEvitas/Thermo Fisher; CORE); HealthUnlocked (UK, NHS/condition; research-monetized; → CorEvitas 2020); Belong.Life (largest cancer social network; anonymous peer chat + trial matching; ~200k; B2B i-Belong sells to pharma/payers; CORE); Peanut (life-stage matching TTC/pregnancy/menopause; ~1.6M users, only ~$21.8M raised, monetization "still evolving"; cautionary); Smart Patients (curated cancer forums; never scaled); Kanker.nl (NL national cancer info+community+clinician contact for patients AND loved ones; KWF/NFK/IKNL-funded; NL incumbent for the exact "patient + loved ones" framing).
- **Retention**: Episodic, diagnosis-spike then decay — "'am I normal?' spikes at diagnosis, decays. Strangers won't pay for episodic reassurance."
- **Who pays**: Pharma and payers pay for the DATA, not users. Every durable stranger-community got acqui-hired by a data buyer.
- **Takeaway**: Ditto is right to anchor on family circle, not stranger peer-finding. If built, monetizes only as data/RWD (oncology overlap with Belong) — never consumer subscription.

### Community building
- Same roster as peer finding + Flo Secret Chats (anonymous community as retention amplifier) + Peanut (group chats + expert Q&A).
- **Retention**: Community is a loyalty amplifier, not a frequency source (Flo: "community deepened loyalty but did not create the habit"). Anonymity drives participation.
- **Who pays**: Pharma/payer data businesses, charity (Kanker.nl), or under-monetized (Peanut). No durable consumer-paid community business exists.
- **Takeaway**: Don't monetize the social layer directly — monetize what it produces (B2B2C/data). Kanker.nl already occupies the NL "patient + loved ones" framing.

## MANAGEMENT / coordination (F5)

### Shared, factual overview
- **Players**: Caren/Nedap Ons (NL family/client portal tethered to Ons EHR; care org pays; CORE — dominant NL pattern); OZOverbindzorg (NL independent non-profit; patient controls who joins; mantelzorg+professionals+municipality; municipality/insurer-funded, free to client; CORE); Thyme Care (US; shared clinical view integrated with 800+ oncologists, ADT/claims feeds).
- **Retention**: Stickiness in NL comes from EHR bundling, not engagement.
- **Who pays**: Care organizations (EHR seat) or municipalities/insurers. Never the family.
- **Takeaway**: Don't enter NL shared-overview head-on (fights Nedap's distribution + free-to-family economics). Ditto's wedge is patient-owned, conversation-derived understanding, not the institutional record.

### Agenda, tasks & allocation
- **Players**: Lotsa Helping Hands (US task coordination; CORE but graveyard); ianacare (US free Caregiver Organizer = the front door; "rally my circle" viral hook; ~50,000 caregivers served; CORE free tier); Jointly (UK); CaringBridge (meal trains).
- **Popularity**: "Crowded feature graveyard at the consumer layer."
- **Retention**: Circle-rallying / task pickup is the viral + frequency hook (low-effort pickup from many people). Strongest coordination retention signal; maps to "frequency from the circle side."
- **Who pays**: Nobody for the tasks layer — it's free acquisition. ianacare's paid layer (human Navigators) migrating toward CMS GUIDE dementia reimbursement.
- **Takeaway**: Tasks/allocation is a growth/virality feature, not a revenue line. Free organizer + circle network effect as front door, money made elsewhere.

### Managed accounts
- Not covered as a software feature. Closest: Wellthy/Cariloop/ianacare assign a named human (Care Coordinator/Navigator) who manages the family's "Care Project" — a human-concierge model, not a proxy-account feature.
- **Retention**: Wellthy — "a named human owns the family's Care Project — trust + offloaded work = stickiness. Software is the wrapper, the human is the moat."
- **Takeaway**: Briefs validate that the *human managing the case* gets paid for, not the account structure. Managed/proxy accounts = table-stakes plumbing, not a differentiator.

### Close & wider circle tiers
- **Players**: OZOverbindzorg (patient controls who joins — explicit permissioned tiering; CORE); CaringBridge (implicitly tiered).
- **Signal**: F7 care-graph names "permissions" as part of Ditto's unique asset (patient + conditions + meds + events + documents + circle + permissions).
- **Takeaway**: Permissioned tiering is a validated need + a component of the care-graph moat — but no evidence it monetizes alone. Build it as part of the graph.

### Family accounts & shared profiles
- **Players**: Familienet (NL/BE/DE/NO/UK family-communication for care homes since 2005; 1000+ orgs; €99/mo per location, care org pays; CORE); Caren/Nedap Ons (care org pays); CaringBridge (nonprofit).
- **Popularity**: Mature as a low-ticket B2B facility add-on (Familienet 1000+ orgs). Not a patient-owned consumer category at scale.
- **Who pays**: Care organizations/facilities. Familienet €99/mo per location.
- **Takeaway**: Monetizes only as a cheap B2B facility add-on; the "neutral family portal" position is already taken (Caren). Differentiation must be patient-owned + conversation-derived.

## Candidate missing features (from F5/F7)
- **One-tap acknowledgement / Kudos loop (circle → patient)**: Strava (14B+ kudos/yr, most transferable mechanic), CaringBridge reactions. THE identified frequency engine. The reaction/witnessing primitive (vs the broadcast/update primitive) is the load-bearing missing half.
- **Comprehension-attached sharing (share the *understood* summary, not chat)**: nobody owns it (WhatsApp can't, CaringBridge/Caren don't understand content, Kanker.nl is static). F7's only defensible "connect." Should be the substrate under every sharing feature, not a separate item.
- **Anonymity / Anonymous Mode as a feature**: Flo (Anonymous Mode, Secret Chats), Belong.Life (anonymous peer chat). Unlocks participation in sensitive contexts; GDPR/EU-aligned. The list has "public sharing" (unsupported) but not anonymous sharing (well-supported).
- **Recurring "interpreted signal" to manufacture daily return**: Flo (cycle), Strava (workout). Both built frequency on a recurring personal signal the app helps interpret. Ditto's candidate: the understanding of each appointment as the signal — a return ritual, currently absent.
- **Free "rally my circle" organizer as acquisition front door**: ianacare (~50,000 caregivers; viral hook before any paid layer). Reframe of agenda-tasks as top-of-funnel growth, not a coordination utility.
- **Clinical-trial / care-pathway matching**: Belong.Life (oncology-deep, ~200k), PatientsLikeMe. The one social-health capability with a clear pharma/RWD revenue line overlapping Ditto's oncology beachhead.

**Cross-cutting**: the social/coordination layer never monetizes directly (stranger-communities → data buyers; CaringBridge/Peanut → can't monetize; NL coordination → EHR-bundled/public-funded). All these features are growth/retention/distribution; money is made elsewhere (B2B2C, RWD).
