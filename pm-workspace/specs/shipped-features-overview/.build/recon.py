import json, collections, datetime

def load(p):
    return json.load(open(p))

proj = load('prod_projects.json')['projects']
comp = load('prod_completed.json')['issues']
start = load('prod_started.json')['issues']

print("### PRODUCT PROJECTS (count:", len(proj), ")")
for p in sorted(proj, key=lambda x: (x.get('status',{}).get('name',''), x['name'])):
    inits = ";".join(i.get('name','') for i in p.get('initiatives',[])) if p.get('initiatives') else "-"
    st = p.get('status',{}).get('name','')
    td = p.get('targetDate') or '-'
    sd = p.get('startDate') or '-'
    print(f"  [{st:12}] {p['name'][:45]:45} | KR:{inits[:40]:40} | start:{sd} target:{td}")

print("\n### COMPLETED ISSUES total:", len(comp))
# completedAt window check
def d(s):
    return s[:10] if s else None
cw = collections.Counter()
nowin=0
for i in comp:
    c = i.get('completedAt')
    if c:
        m = c[:7]
        cw[m]+=1
    else:
        nowin+=1
print("completedAt by month:", dict(sorted(cw.items())))
print("no completedAt:", nowin)

print("\n### COMPLETED issues by PROJECT:")
pc = collections.Counter(i.get('project') or '(none)' for i in comp)
for k,v in pc.most_common():
    print(f"  {v:3}  {k}")

print("\n### STARTED (in-progress) issues total:", len(start))
ps = collections.Counter(i.get('project') or '(none)' for i in start)
for k,v in ps.most_common():
    print(f"  {v:3}  {k}")
print("started statuses:", dict(collections.Counter(i.get('status') for i in start)))

# labels distribution on completed
print("\n### sample labels on completed:")
lab=collections.Counter()
for i in comp:
    for l in i.get('labels',[]):
        lab[l]+=1
for k,v in lab.most_common(20):
    print(f"  {v:3}  {k}")
