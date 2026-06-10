import json, csv, re, collections, datetime
from classify import investment_type, pillar_kw, okr_kw

WIN_START, WIN_END = "2026-03-01", "2026-05-31"
comp = json.load(open('prod_completed.json'))['issues']
projects = json.load(open('prod_projects.json'))['projects']

AGI = [("AGI-26","Draft email — David Chaney, Diabetes UK","draft-email-david-chaney-diabetes-uk"),
 ("AGI-27","Draft email — Matt McGill, Aviva","draft-email-matt-mcgill-aviva"),
 ("AGI-25","Draft email — Carla Belcher, ACME ACO","draft-email-carla-belcher-acme-aco"),
 ("AGI-24","Research — Matt McGill, Aviva","research-matt-mcgill-aviva"),
 ("AGI-23","Research — David Chaney, Diabetes UK","research-david-chaney-diabetes-uk"),
 ("AGI-22","Research — Richard Simcock, Macmillan Cancer Support","research-richard-simcock-macmillan-cancer-support"),
 ("AGI-21","Research — Carla Belcher, ACME ACO","research-carla-belcher-acme-aco"),
 ("AGI-19","Discovery — Aviva","discovery-aviva"),("AGI-20","Discovery — Diabetes UK","discovery-diabetes-uk"),
 ("AGI-16","Discovery — Acme","discovery-acme"),
 ("AGI-14","Draft email — Gemma Peters, Macmillan Cancer Support","draft-email-gemma-peters-macmillan-cancer-support"),
 ("AGI-13","Research — Gemma Peters, Macmillan Cancer Support","research-gemma-peters-macmillan-cancer-support"),
 ("AGI-12","Discovery — Macmillan Cancer Support","discovery-macmillan-cancer-support"),
 ("AGI-7","B2B Outreach — Ditto Care B.V.","b2b-outreach-ditto-care-bv"),
 ("AGI-10","Draft email — Tobias Polak, Ditto Care B.V.","draft-email-tobias-polak-ditto-care-bv"),
 ("AGI-9","Research — Tobias Polak, Ditto Care B.V.","research-tobias-polak-ditto-care-bv"),
 ("AGI-3","Discovery — Bupa","discovery-bupa"),("AGI-8","Discovery — Ditto Care B.V.","discovery-ditto-care-bv")]
agi_rows=[{"id":i,"title":t,"url":f"https://linear.app/ditto-care/issue/{i}/{s}","completedAt":"2026-05-22T00:00:00.000Z",
 "project":"B2B Outreach POC","projectMilestone":None,"priority":{"name":"No priority"},
 "labels":["agent:outreach"],"team":"Agents","startedAt":"2026-05-22T00:00:00.000Z"} for i,t,s in AGI]

def kr_from_inits(inits):
    codes=[]
    for it in (inits or []):
        codes+=re.findall(r"O\d-KR\d", it.get('name',''))
    return codes
proj_kr={p['name']:kr_from_inits(p.get('initiatives')) for p in projects}

PMAP={
 "Care Circle 3.0":("Connection","O2-KR4"),"Care Circle V2":("Connection","O2-KR4"),
 "Remove confirmation from Care Circle invite flow":("Connection","O2-KR2"),
 "Multi-profile / Managed accounts":("Connection","O2-KR4"),
 "Calendar Integration":("Convenience","O2-KR4"),"Calendar Pull":("Convenience","O2-KR4"),
 "Customer.io — Marketing Automation & Push Notifications":("Convenience","O2-KR4"),
 "Customer.io Welcome Series (1a + 1d)":("Convenience","O2-KR4"),
 "Customer.io Appointment Preparation Flow":("Convenience","O2-KR4"),
 "Customer.io Post-Summary Flow":("Convenience","O2-KR4"),
 "Customer.io Profile Completion Flow":("Convenience","O2-KR4"),
 "Growth: Customer.io":("Convenience","O2-KR2"),"Dedicated Discover Tab":("Convenience","O2-KR2"),
 "Appointment Preparation":("Clarity","O2-KR2"),
 "AI Quality — Tune Evals and Guardrails":("Clarity","O1-KR4"),
 "Conversation Explainer AI Improvements":("Clarity","O1-KR2"),
 "AI Answer Suggestions":("Clarity","O2-KR2"),
 "Improved analytics data on personas and life moment audiences":("Fundamentals","O2-KR2"),
 "Analytics Foundations":("Fundamentals","O2-KR4"),"Implement Survicate":("Fundamentals","O1-KR4"),
 "Migrate Away from Auth0":("Fundamentals","O1-KR4"),"Move to Liquid Glass UI (iOS 26+)":("Fundamentals",""),
 "UI / LEGO maintenance":("Fundamentals",""),"Security Improvements":("Fundamentals",""),
 "Staging Backend Environment":("Fundamentals",""),"Website | lead generation pages":("Convenience","O2-KR1"),
 "Triage Intelligence (Linear AI)":("Fundamentals","O1-KR2"),"Triage RISCE Scoring (Linear AI)":("Fundamentals","O1-KR2"),
 "Triage Cleanup":("Fundamentals",""),"Proposal Flow (Slack #propose)":("Fundamentals",""),
 "Post-Ship Evaluation & Verdict Ritual":("Fundamentals",""),"Concurrent Experiment Operations":("Fundamentals",""),
 "Ship at 80%: Experiment Velocity Engine":("Fundamentals",""),"Experimentation Engine":("Fundamentals",""),
 "15 FTE AI agents":("Fundamentals",""),"15ftes: Person Research":("Fundamentals",""),
 "Growth: Team Way of Working (WoW)":("Fundamentals",""),
 "Beyond Appointments: Expanding Activation Paths":("Convenience",""),
 "Create an aha moment during onboarding":("Convenience",""),"HCP Persona Experience":("Convenience","O2-KR2"),
 "UK launch":("Fundamentals",""),"Language Expansion":("Convenience",""),"B2B Outreach POC":("Fundamentals",""),
}
for nm in set(i.get('project') for i in comp if i.get('project') and i['project'].startswith("EXP-B2B")):
    PMAP[nm]=("Fundamentals","O1-KR2")

def effort(it):
    t=it['title'].lower(); L=[x.lower() for x in it.get('labels',[])]
    sa,ca=it.get('startedAt'),it.get('completedAt'); lead=None
    if sa and ca:
        try: lead=(datetime.datetime.fromisoformat(ca.replace('Z','+00:00'))-datetime.datetime.fromisoformat(sa.replace('Z','+00:00'))).days
        except: pass
    big=("feature" in L) or ("[implement" in t) or ("[implementation]" in t)
    triv=any(w in t for w in ["copy","grammar","typo","icon"," color","spacing","alignment","thumbnail","comment","walk ","prep ","review handwritten","reactive google","schedule thursday","meeting rhythm","onboarding wouter","onboarding jasper","walk tobias"])
    if big or (lead is not None and lead>=14): return "L"
    if triv and (lead is None or lead<3): return "XS"
    if any(x in L for x in ["bug","design-polish","maintenance"]): return "S" if (lead is None or lead<7) else "M"
    if lead is not None and lead>=7: return "M"
    if lead is not None and lead>=2: return "M"
    return "S"

def norm(it,team):
    proj=it.get('project') or ""; pm=it.get('projectMilestone') or {}
    mile=pm.get('name','') if isinstance(pm,dict) else ""
    labels=it.get('labels',[]) or []
    rel=";".join([l for l in labels if re.match(r"^\d\.\d",l)])
    if proj in PMAP:
        pillar,okrs=PMAP[proj]; linked=proj_kr.get(proj) or []
        if linked:
            okrp=linked[0]; src="Linear-linked"
            if len(linked)>1 and not okrs: okrs=linked[1]
        else:
            okrp,src=okr_kw(it['title'],labels,pillar)
            if okrp=="—": src="None (BAU/foundational)"
            else: src="Project-mapped"
    else:
        pillar=pillar_kw(it['title'],labels); okrp,src=okr_kw(it['title'],labels,pillar); okrs=""
    inv=investment_type(it['title'],labels)
    if inv in ("AI quality","AI agents"): pillar="Clarity"   # AI set -> Clarity (per Merlijn 2026-05-30)
    return {"ID":it['id'],"Title":it['title'].replace("\n"," ").strip(),"Team":team,
      "Project":proj or "(none)","Milestone":mile,"Release":rel,"Completed":(it.get('completedAt') or "")[:10],
      "Pillar":pillar,"OKR_primary":okrp,"OKR_link":src,"OKR_secondary":okrs,
      "Investment":inv,"Effort":effort(it),
      "Priority":(it.get('priority') or {}).get('name',''),"Labels":";".join(labels),"Link":it['url']}

rows=[norm(it,"Product") for it in comp if it.get('completedAt') and WIN_START<=it['completedAt'][:10]<=WIN_END]
rows+=[norm(it,"Agents") for it in agi_rows]
rows.sort(key=lambda r:(r['Completed'],r['ID']))
cols=["ID","Title","Link","Team","Project","Milestone","Release","Completed","Pillar","OKR_primary","OKR_link","OKR_secondary","Investment","Effort","Priority","Labels"]
with open('shipped_features.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); [w.writerow(r) for r in rows]
print("SHIPPED rows:",len(rows))
print("PILLAR:",dict(collections.Counter(r['Pillar'] for r in rows)))
print("OKR primary:",dict(sorted(collections.Counter(r['OKR_primary'] for r in rows).items())))
print("OKR link src:",dict(collections.Counter(r['OKR_link'] for r in rows)))
print("INVESTMENT:",dict(sorted(collections.Counter(r['Investment'] for r in rows).items())))
print("EFFORT:",dict(collections.Counter(r['Effort'] for r in rows)))
leftover=[r for r in rows if r['Investment']=="Team/internal ops"]
print("\nTeam/internal ops bucket (",len(leftover),"):")
for r in leftover: print(f"  {r['ID']:9}| {r['Title'][:62]}")
