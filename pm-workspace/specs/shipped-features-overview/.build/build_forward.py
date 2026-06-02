import json, csv, re, collections, datetime
from classify import investment_type, pillar_kw, okr_kw

started = json.load(open('prod_started.json'))['issues']
projects = json.load(open('prod_projects.json'))['projects']

def kr_from_inits(inits):
    c=[]
    for it in (inits or []): c+=re.findall(r"O\d-KR\d", it.get('name',''))
    return c
proj_kr={p['name']:kr_from_inits(p.get('initiatives')) for p in projects}
proj_url={p['name']:p.get('url','') for p in projects}

# reuse PMAP pillars from build2 logic (inline minimal: pillar by project via pillar_kw on name, override known)
PILLAR_OVR={"Care Circle 3.0":"Connection","Care Circle V2":"Connection","Remove confirmation from Care Circle invite flow":"Connection",
 "Multi-profile / Managed accounts":"Connection","Calendar Integration":"Convenience","Calendar Pull":"Convenience",
 "Appointment Preparation":"Clarity","AI Quality — Tune Evals and Guardrails":"Clarity","Conversation Explainer AI Improvements":"Clarity",
 "AI Answer Suggestions":"Clarity","Dedicated Discover Tab":"Convenience","Beyond Appointments: Expanding Activation Paths":"Convenience",
 "Create an aha moment during onboarding":"Convenience","HCP Persona Experience":"Convenience","Care journeys (mobile visualization)":"Connection",
 "Personalized Discovery page":"Convenience","Medical Data Vault":"Fundamentals","Geofencing":"Convenience","Wearable Integration":"Convenience",
 "Language Expansion":"Convenience","Multi-profile / Managed accounts":"Connection"}
def proj_pillar(nm):
    if nm in PILLAR_OVR: return PILLAR_OVR[nm]
    return pillar_kw(nm, [])
def proj_okr(nm):
    linked=proj_kr.get(nm) or []
    if linked: return linked[0],"Linear-linked"
    p=proj_pillar(nm); o,s=okr_kw(nm,[],p); return o,("Inferred" if o!="—" else "None (BAU/foundational)")

def effort(it):
    t=it['title'].lower(); L=[x.lower() for x in it.get('labels',[])]
    sa,ca=it.get('startedAt'),it.get('updatedAt'); lead=None
    if sa and ca:
        try: lead=(datetime.datetime.fromisoformat(ca.replace('Z','+00:00'))-datetime.datetime.fromisoformat(sa.replace('Z','+00:00'))).days
        except: pass
    big=("feature" in L) or ("[implement" in t)
    if big or (lead is not None and lead>=14): return "L"
    if lead is not None and lead>=5: return "M"
    return "S"

# ---- planned ISSUES (in progress) ----
prows=[]
for it in started:
    proj=it.get('project') or ""
    pillar=proj_pillar(proj) if proj else pillar_kw(it['title'],it.get('labels',[]))
    if proj: okrp,src=proj_okr(proj)
    else: okrp,src=okr_kw(it['title'],it.get('labels',[]),pillar)
    labels=it.get('labels',[]) or []
    prows.append({"ID":it['id'],"Title":it['title'].replace("\n"," ").strip(),"Status":it.get('status',''),
      "Project":proj or "(none)","Pillar":pillar,"OKR_primary":okrp,"OKR_link":src,
      "Investment":investment_type(it['title'],labels),"Effort":effort(it),
      "Priority":(it.get('priority') or {}).get('name',''),"Link":it['url']})
prows.sort(key=lambda r:(r['Project'],r['ID']))
with open('planned_issues.csv','w',newline='') as f:
    c=["ID","Title","Link","Status","Project","Pillar","OKR_primary","OKR_link","Investment","Effort","Priority"]
    w=csv.DictWriter(f,fieldnames=c); w.writeheader(); [w.writerow(r) for r in prows]

# ---- planned PROJECTS (active/planned, with dates) ----
def parse(d): return d[:10] if d else ""
pjrows=[]
for p in projects:
    st=p.get('status',{}).get('name','')
    if st in ("Completed","Canceled"): continue
    sd,td=parse(p.get('startDate')),parse(p.get('targetDate'))
    nm=p['name']; okrp,src=proj_okr(nm)
    # "next 2 months" flag: any date in Jun-Jul 2026 OR currently In Progress
    near = st=="In Progress" or any(x and ("2026-06" in x or "2026-07" in x) for x in [sd,td]) or st=="Planned"
    pjrows.append({"Project":nm,"Status":st,"Pillar":proj_pillar(nm),"OKR_primary":okrp,"OKR_link":src,
      "Start":sd,"Target":td,"Near2mo":"Y" if near else "","Link":proj_url.get(nm,'')})
order={"In Progress":0,"Planned":1,"Backlog":2}
pjrows.sort(key=lambda r:(order.get(r['Status'],9), r['Target'] or "9999", r['Project']))
with open('planned_projects.csv','w',newline='') as f:
    c=["Project","Status","Pillar","OKR_primary","OKR_link","Start","Target","Near2mo","Link"]
    w=csv.DictWriter(f,fieldnames=c); w.writeheader(); [w.writerow(r) for r in pjrows]

print("PLANNED in-progress issues:",len(prows))
print("  by pillar:",dict(collections.Counter(r['Pillar'] for r in prows)))
print("  by OKR:",dict(sorted(collections.Counter(r['OKR_primary'] for r in prows).items())))
print("\nFORWARD projects (active/planned):",len(pjrows))
print("  near-2mo (Jun-Jul / In Progress / Planned):",sum(1 for r in pjrows if r['Near2mo']))
print("\n--- Forward project list (status | pillar | OKR | start->target) ---")
for r in pjrows:
    print(f"  [{r['Status']:11}] {r['Project'][:46]:46} | {r['Pillar']:12} | {r['OKR_primary']:7} | {r['Start'] or '—'} -> {r['Target'] or '—'}")
