# Ditto — Long-term Product Vision

_Working narrative, June 2026. Up for debate. The point is to get us aligned enough to make better daily decisions, not to lock a ten-year plan._

## Why we exist

I want to start with the why, because the strategy will change, but I think the reason why we're doing this is/should be steadier. Mission so far: **clarify and connect care journeys for you and your loved ones.** 

This sits on the belief we started from: The patient is massively underserved, and the patient is the unlock for a healthcare system that is otherwise stuck. Scribes took off because the technology finally caught up, but the real gap was never the doctor's note. It was the person walking out of the room with a failing memory, a notepad, and a letter full of Latin that tells them they have cancer. EHRs have not fixed that. They gave us clunky software, fragmentation, and portals that store data without ever explaining it. AI assistants are individualistic yet generic, and omni-potent yet unreliable.  

## Summaries cannot be the goal
Summary tools are a commodity now and they keep getting more reliable. On the business side they are becoming standard for every conversation.

- Better summaries are only defensible if you have something no one else has: proprietary models, unique validation data, a sharp niche. We do not truly have that yet. We get the most we can out of the underlying models.

- EHRs and scribes are catching up. Within about a year, patient summaries are native. When ChatGPT or Gemini ship dedicated conversation summaries, that attacks us directly. Saying "doctors will never allow it" is stretching reality.

- A summary is relevant around the appointment and maybe the day after. Even when you are severely ill, that is a reason to open Ditto weekly at most. Unless we deliver something incredible in that moment, we are a convenient function, not something people grow attached to.

- Low frequency is hard to monetize. Consumers do not pay easily for health apps, and insurers want activity before they reimburse.

- Pushing frequency or growth features for their own sake is a dead end. Unless we solve real problems, we can only nudge so far in the direction *we* want.

The good part:

- Our summaries are genuinely better, and people trust them. That trust is key, and we have to keep measuring it instead of assuming it.

- We are roughly 10x better than the alternative, which is forgetting.

- Summaries and recordings hold far more potential than we unlock today.

- The summary is the way in. We have to squeeze the most value out of that episodic moment.

- From there the list is long: auto-update your health profile, nudge follow-up actions and help

# The long-term what

I feel like we leave the future vision open and vague. Also I don't know what Ditto will precisely be in 5 years time, but 
## Six potential product end states
These are the futures we have been circling. I want them all on the table, then synthesized.

1. **Care Companion.** Ditto supports you along every step of your care journey. Core focus: understanding, making sense of what is happening, knowing what to expect. This is where we are today, and the base of the spine.
    
2. **Trusted Health Assistant.** Ditto pro-actively guides and helps you in your treatment and gets you recovered as well as possible. Core focus: agency, advice and nudges on the medical behaviour you can control. This is a dedicated end state, and when you combine end states it is also the top of the intelligence ladder, what the companion becomes when you keep adding intelligence.
    
3. **Patient-Owned Record.** You own and understand all your healthcare data in Ditto. Core focus: ingest everything and make it understandable and shareable. Data alone is low value and we would be fighting governments and EHRs, so I do not see this as a stand-alone destination.
    
4. **Care Coordination.** Families manage the disease and arrange practical support inside Ditto. Core focus: tasks, agendas, keeping the core care group aligned. There is a real market here if you do it extremely well.
    
5. **Social Care Platform.** The place for shared understanding among loved ones and peers. Core focus: connection, not being alone, support gestures, updates, peers.
    
6. **The Front Door of European healthcare**: The go-to digital solution that does it all, basically. The first digital solution that comes to mind when you are a patient. Probably including a lot of operational things: scheduling, planning appointments, getting a second opinion, finding your data, messaging health professionals. And then probably an intelligence and comprehension layer and social connection side as well.

## The synthesis: two layers, plus leans

I think these potential 'visions' are actually layers that extend the product over various axes:

**The intelligence layer is the spine, and it is our contrarian core.** It runs understanding (Care Companion) to advising to agency (Trusted Health Assistant), and it grows in two directions: up the intelligence ladder, and outward into the day-to-day and weekly needs between appointments where frequency and attachment actually live. The **Patient-Owned Record is not a goal here, it is a multiplier.** If we can integrate it, the assistant finally sees the full picture and every rung of the ladder gets better. So we chase the record as an enabler, not a destination.

**The operational layer is the front door.** Scheduling, prescriptions, messaging, data access. This is not intelligence, it is operations, and it is where Doctolib and the portals live. It stacks under or beside the spine: it brings reach and data, and being the front door is itself a defensible position. I think being honest that some of this is operational and some is intelligence is what was missing before. It makes the whole thing buildable instead of one vague tower.

**Coordination and social are leans, not the spine.** We take the parts of coordination and social that make the companion a more complete experience, we can experiment where there is a real market, but neither becomes the foundation.

One tension to name honestly. The rung where the money is, individualised advising, is also the rung where regulation bites hardest. Advising is the MDR and AI-Act device rung. The companies that survive there route around it by keeping a human or the care circle in the loop, rather than having the AI act alone. That is the line we have to respect as we climb.

## Two ways of reasoning

We keep confusing ourselves because we mix two ways of reasoning. Both are valid, and I want to run them at the same time.

**Backwards from a vision.** Imagine the Ditto that should exist in a few years and reason back to what we build now. This keeps us coherent and stops us becoming a pile of features. We don't know the precise route, but we have directionality.

**Forwards from jobs to be done.** Watch how people actually struggle in healthcare today and solve one job, then the next, so Ditto solves more and more real problems over time. The care-management jobs people already do badly are concrete. This keeps us useful and grounded in how people already behave.

Over both sits one hard filter: **monetization.** What actually becomes a business is a real constraint, not an afterthought, and it excludes options no matter how nice the vision or how real the job. The uncomfortable truth is that almost nothing in this space monetizes on patient-pay directly. At least, I haven't found it. Fitness: easy. Wellness: doable. Longevity: easy. Healthcare: hard. I think we would benefit from a stronger awareness in how we take monetization into account when deciding strategy. Uncomfortable  question: can a reimbursed app be a unicorn?

## The how for product
Having more focus on critical care moments (oncology) is helpful for the mid-term. It scopes down the infinite amount of options and makes decision-making based on intuition easier. For product, I believe the following will be key to move fast(er) in the right direction
1. Creating more clarity on where we want to be in a few year helps prioritize product in the short-term. e.g. we want to be an intelligent assistance, we should have interactive AI chat over task management in circle circles
2. We should make bigger bets in shorter cycles and learn fast. Anthropic spends 70% of time on big bets. The rest is polish and maintenance and low-hanging fruits
3. If the strategic priorities are clear, we can seriously consider buy-options as well, to directly buy distribution, scale, etc. 
4. We should be very careful with the perspective of 'what would be good for Ditto;s growth'. On the product side, we should address actual (or potentially unaware) problems or needs. 
5. At the same time: just solving the straightforward practical issues people face will probably not create a new market category 
5. Not committing on any direction might leave our options open, but it could just as well lead to a frankenstein product and some windows closing. E.g. if we invest heavily in data integrations and anticipating EHDS, we slow down on adding real intelligence to the data users already put into Ditto. 

## What we need to decide
I would love to try to answer the following:

0. **Why do we exist?** --> Miss
1. **What does Ditto solve or improve?**
2. **Who are we building for primarily?**
3. **What is/will be our moat?**
4. **How do we monetize it?**

## Appendix A: Market dynamics
- Core market trends in 2026
- Where our product competes, can integrate, is under threat

## Appendix B: Oncology deepdive
- The underlying needs
- Core use cases we are not yet addressing

## Appendix C: Monetization hard truths
- Examples of success cases in consumer healthcare
- Failure cases/graveyards
- What this likely means for Ditto

