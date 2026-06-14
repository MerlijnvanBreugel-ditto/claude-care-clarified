import json, csv, re, collections

WIN_START, WIN_END = "2026-03-01", "2026-05-31"

comp = json.load(open('prod_completed.json'))['issues']
started = json.load(open('prod_started.json'))['issues']
projects = json.load(open('prod_projects.json'))['projects']

# ---- Agents completed (from live Linear pull, embedded) ----
AGI = [
 ("AGI-26","Draft email — David Chaney, Diabetes UK","draft-email-david-chaney-diabetes-uk"),
 ("AGI-27","Draft email — Matt McGill, Aviva","draft-email-matt-mcgill-aviva"),
 ("AGI-25","Draft email — Carla Belcher, ACME ACO","draft-email-carla-belcher-acme-aco"),
 ("AGI-24","Research — Matt McGill, Aviva","research-matt-mcgill-aviva"),
 ("AGI-23","Research — David Chaney, Diabetes UK","research-david-chaney-diabetes-uk"),
 ("AGI-22","Research — Richard Simcock, Macmillan Cancer Support","research-richard-simcock-macmillan-cancer-support"),
 ("AGI-21","Research — Carla Belcher, ACME ACO","research-carla-belcher-acme-aco"),
 ("AGI-19","Discovery — Aviva","discovery-aviva"),
 ("AGI-20","Discovery — Diabetes UK","discovery-diabetes-uk"),
 ("AGI-16","Discovery — Acme","discovery-acme"),
 ("AGI-14","Draft email — Gemma Peters, Macmillan Cancer Support","draft-email-gemma-peters-macmillan-cancer-support"),
 ("AGI-13","Research — Gemma Peters, Macmillan Cancer Support","research-gemma-peters-macmillan-cancer-support"),
 ("AGI-12","Discovery — Macmillan Cancer Support","discovery-macmillan-cancer-support"),
 ("AGI-7","B2B Outreach — Ditto Care B.V.","b2b-outreach-ditto-care-bv"),
 ("AGI-10","Draft email — Tobias Polak, Ditto Care B.V.","draft-email-tobias-polak-ditto-care-bv"),
 ("AGI-9","Research — Tobias Polak, Ditto Care B.V.","research-tobias-polak-ditto-care-bv"),
 ("AGI-3","Discovery — Bupa","discovery-bupa"),
 ("AGI-8","Discovery — Ditto Care B.V.","discovery-ditto-care-bv"),
]
agi_rows = [{"id":i,"title":t,"url":f"https://linear.app/ditto-care/issue/{i}/{s}",
             "completedAt":"2026-05-22T00:00:00.000Z","project":"B2B Outreach POC",
             "projectMilestone":None,"priority":{"name":"No priority"},
             "labels":["agent:outreach"],"team":"Agents","startedAt":"2026-05-22T00:00:00.000Z"} for i,t,s in AGI]

# ---- KR code extraction from project initiatives ----
def kr_from_inits(inits):
    codes=[]
    for it in (inits or []):
        m=re.findall(r"O\d-KR\d", it.get('name',''))
        codes+=m
    return codes

proj_kr = {}
for p in projects:
    proj_kr[p['name']] = kr_from_inits(p.get('initiatives'))

# ---- PROJECT MAP: name -> (pillar, okr_primary, okr_secondary) ----
# pillar judgment + OKR (prefer Linear-linked from proj_kr; else inferred marked with *)
PMAP = {
 "Care Circle 3.0":            ("Connection","O2-KR3","O2-KR4"),
 "Care Circle V2":             ("Connection","O2-KR3*","O2-KR4"),
 "Remove confirmation from Care Circle invite flow":("Connection","O2-KR3","O2-KR2"),
 "Multi-profile / Managed accounts":("Connection","O2-KR3","O2-KR4"),
 "Calendar Integration":       ("Convenience","O2-KR2","O2-KR4"),
 "Calendar Pull":              ("Convenience","O2-KR2*","O2-KR4"),
 "Customer.io — Marketing Automation & Push Notifications":("Convenience","O2-KR2*","O2-KR4"),
 "Customer.io Welcome Series (1a + 1d)":("Convenience","O2-KR2","O2-KR4"),
 "Customer.io Appointment Preparation Flow":("Convenience","O2-KR2","O2-KR4"),
 "Customer.io Post-Summary Flow":("Convenience","O2-KR2","O2-KR4"),
 "Customer.io Profile Completion Flow":("Convenience","O2-KR2","O2-KR4"),
 "Growth: Customer.io":        ("Convenience","O2-KR4","O2-KR2"),
 "Dedicated Discover Tab":     ("Convenience","O2-KR4*","O2-KR2"),
 "Appointment Preparation":    ("Clarity","O2-KR4","O2-KR2"),
 "AI Quality — Tune Evals and Guardrails":("Clarity","O2-KR4*","O1-KR4"),
 "Conversation Explainer AI Improvements":("Clarity","O2-KR4*","O1-KR2"),
 "AI Answer Suggestions":      ("Clarity","O2-KR4","O2-KR2"),
 "Improved analytics data on personas and life moment audiences":("Fundamentals","O2-KR4","O2-KR2"),
 "Analytics Foundations":      ("Fundamentals","O1-KR4","O2-KR4"),
 "Implement Survicate":        ("Fundamentals","O2-KR4","O1-KR4"),
 "Migrate Away from Auth0":    ("Fundamentals","O2-KR3","O1-KR4"),
 "Move to Liquid Glass UI (iOS 26+)":("Fundamentals","O1-KR4*",""),
 "UI / LEGO maintenance":      ("Fundamentals","O1-KR4*",""),
 "Security Improvements":      ("Fundamentals","O1-KR4*",""),
 "Staging Backend Environment":("Fundamentals","O1-KR4*",""),
 "Website | lead generation pages":("Convenience","O2-KR2","O2-KR1"),
 "Triage Intelligence (Linear AI)":("Fundamentals","O1-KR4","O1-KR2"),
 "Triage RISCE Scoring (Linear AI)":("Fundamentals","O1-KR4","O1-KR2"),
 "Triage Cleanup":             ("Fundamentals","O1-KR4",""),
 "Proposal Flow (Slack #propose)":("Fundamentals","O1-KR4",""),
 "Post-Ship Evaluation & Verdict Ritual":("Fundamentals","O1-KR4",""),
 "Concurrent Experiment Operations":("Fundamentals","O1-KR4",""),
 "Ship at 80%: Experiment Velocity Engine":("Fundamentals","O1-KR4",""),
 "Experimentation Engine":     ("Fundamentals","O1-KR4*",""),
 "15 FTE AI agents":           ("Fundamentals","O1-KR2",""),
 "15ftes: Person Research":    ("Fundamentals","O1-KR2",""),
 "Growth: Team Way of Working (WoW)":("Fundamentals","O1-KR4*",""),
 "Beyond Appointments: Expanding Activation Paths":("Convenience","O2-KR2",""),
 "Create an aha moment during onboarding":("Convenience","O2-KR2*",""),
 "HCP Persona Experience":     ("Convenience","O2-KR1","O2-KR2"),
 "UK launch":                  ("Fundamentals","O1-KR3*",""),
 "Language Expansion":         ("Convenience","O1-KR3*",""),
 "Staging Backend Environment":("Fundamentals","O1-KR4*",""),
 "B2B Outreach POC":           ("Fundamentals","O1-KR2",""),
}
# EXP-B2B experiment projects
for nm in set(i.get('project') for i in comp+started if i.get('project') and i['project'].startswith("EXP-B2B")):
    PMAP[nm]=("Fundamentals","O1-KR4","O1-KR2")

# ---- keyword fallback for no-project / unmapped ----
def classify_keyword(title, labels):
    t=title.lower(); L=set(labels)
    # pillar
    if any(k in t for k in ["summary","summaries","ai ","evals","guardrail","transcription","explainer","notes editor","question"]) or "ai" in L:
        pillar="Clarity"
    elif any(k in t for k in ["care circle","loved one","follower","invite","sharing","shared with you","reaction","carepath"]):
        pillar="Connection"
    elif any(k in t for k in ["privacy","consent","gdpr","deletion","delete user","auth0","supabase","terraform","staging","security","16 kb","16kb","domain map","repo","lego","glass","typography","shadow","dialog","toast","analytics","mixpanel","tracking","adjust","triage","proposal","risce","experiment","a/b","runbook","okr","kr","release","app store","linear","github","brand lead","onboarding wouter","onboarding jasper","skills"]):
        pillar="Fundamentals"
    elif any(k in t for k in ["calendar","activation","onboarding","intent","appointment","ftue","customer.io","cio","welcome series","discover","notification","reminder","recording","smiirl","geofenc","wearable","storefront","region","localization","uk app","uk launch"]):
        pillar="Convenience"
    else:
        pillar="Fundamentals"
    # okr (inferred -> *)
    okr={"Connection":"O2-KR3*","Clarity":"O2-KR4*","Convenience":"O2-KR2*","Fundamentals":"O1-KR4*"}[pillar]
    return pillar, okr, ""

def investment_type(title, labels, pillar):
    t=title.lower(); L=set(labels)
    if "Bug" in L: return "Bug fix"
    if "agent:outreach" in " ".join(labels) or "agent:" in " ".join(labels): return "AI agents"
    if any(k in t for k in ["privacy","consent","gdpr","deletion","delete user","policy"]): return "Compliance/privacy"
    if "maintenance" in L: return "Maintenance"
    if "Research" in L or "research:" in t or t.startswith("research") or "lyssna" in t or "survey" in t: return "Research/discovery"
    if "ai" in L or any(k in t for k in ["evals","guardrail","explainer","transcription"]): return "AI quality"
    if "Feature" in L or "[implement" in t or "[implementation]" in t: return "New feature"
    if "Improvement" in L: return "Improvement"
    if "design-polish" in L: return "Design polish"
    if any(k in t for k in ["auth0","supabase","terraform","staging","domain map","16 kb","16kb","repo","architecture"]): return "Infra/platform"
    if any(k in t for k in ["customer.io","cio","welcome series","broadcast","campaign"]): return "Lifecycle/CRM"
    if any(k in t for k in ["mixpanel","analytics","tracking","adjust","dashboard","smiirl","porygon"]): return "Analytics/tracking"
    if any(k in t for k in ["experiment","proposal","triage","risce","runbook","okr","ship at 80","a/b","pilot"]): return "Process/tooling"
    if any(k in t for k in ["lego","glass","typography","shadow","dialog","colors","toast"]): return "Design system"
    if any(k in t for k in ["release","app store","linear release"]): return "Release ops"
    return "Other/ops"

def effort(it):
    t=it['title'].lower(); L=set(it.get('labels',[]))
    sa=it.get('startedAt'); ca=it.get('completedAt')
    import datetime
    lead=None
    if sa and ca:
        try:
            d1=datetime.datetime.fromisoformat(sa.replace('Z','+00:00'))
            d2=datetime.datetime.fromisoformat(ca.replace('Z','+00:00'))
            lead=(d2-d1).days
        except: pass
    big = ("Feature" in L) or ("[implement" in t) or ("[implementation]" in t)
    trivialwords=["copy","grammar","typo","icon","color","spacing","alignment","thumbnail","comment","walk ","prep ","review handwritten","onboarding wouter","onboarding jasper","reactive google"]
    triv = any(w in t for w in trivialwords)
    if big or (lead is not None and lead>=14): return "L"
    if triv and (lead is None or lead<3): return "XS"
    if "Bug" in L or "design-polish" in L or "maintenance" in L:
        return "S" if (lead is None or lead<7) else "M"
    if lead is not None and lead>=7: return "M"
    if lead is not None and lead>=2: return "M"
    return "S"

def norm(it, team="Product"):
    proj = it.get('project') or ""
    pm = it.get('projectMilestone') or {}
    mile = pm.get('name','') if isinstance(pm,dict) else ""
    labels = it.get('labels',[]) or []
    rel = ";".join([l for l in labels if re.match(r"^\d\.\d",l)])
    # pillar/okr
    if proj in PMAP:
        pillar, okrp, okrs = PMAP[proj]
        # override okr with Linear-linked KR if available
        linked = proj_kr.get(proj) or []
        if linked:
            okrp = linked[0]
            if len(linked)>1 and not okrs: okrs=linked[1]
            okr_src="Linear-linked"
        else:
            okr_src="Inferred" if okrp.endswith("*") else "Project-mapped"
    else:
        pillar, okrp, okrs = classify_keyword(it['title'], labels)
        okr_src="Inferred"
    inv = investment_type(it['title'], labels, pillar)
    return {
      "ID":it['id'],"Title":it['title'].replace("\n"," ").strip(),
      "Team":team,"Project":proj or "(none)","Milestone":mile,"Release":rel,
      "Completed":(it.get('completedAt') or "")[:10],
      "Pillar":pillar,"OKR_primary":okrp.replace("*",""),
      "OKR_link":okr_src,"OKR_secondary":okrs,
      "Investment":inv,"Effort":effort(it),
      "Priority":(it.get('priority') or {}).get('name',''),
      "Labels":";".join(labels),"Link":it['url'],
    }

# filter completed window
rows=[]
for it in comp:
    c=it.get('completedAt','')
    if c and WIN_START<=c[:10]<=WIN_END:
        rows.append(norm(it,"Product"))
for it in agi_rows:
    rows.append(norm(it,"Agents"))

rows.sort(key=lambda r:(r['Completed'], r['ID']))

cols=["ID","Title","Link","Team","Project","Milestone","Release","Completed","Pillar","OKR_primary","OKR_link","OKR_secondary","Investment","Effort","Priority","Labels"]
with open('shipped_features.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow(r)

print("SHIPPED rows:",len(rows))
print("\nBy PILLAR:",dict(collections.Counter(r['Pillar'] for r in rows)))
print("By OKR primary:",dict(sorted(collections.Counter(r['OKR_primary'] for r in rows).items())))
print("By OKR link source:",dict(collections.Counter(r['OKR_link'] for r in rows)))
print("By Investment:",dict(sorted(collections.Counter(r['Investment'] for r in rows).items())))
print("By Effort:",dict(collections.Counter(r['Effort'] for r in rows)))
print("\nResidual 'Other/ops' (rules fell through):")
for r in rows:
    if r['Investment']=="Other/ops":
        print(f"  {r['ID']:9} | {r['Pillar']:12} | {r['Title'][:60]}")
