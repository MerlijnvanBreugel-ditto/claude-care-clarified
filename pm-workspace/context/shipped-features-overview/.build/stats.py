import csv, collections
rows=list(csv.DictReader(open('shipped_features.csv')))
proj_url={}
import json
for p in json.load(open('prod_projects.json'))['projects']:
    proj_url[p['name']]=p.get('url','')

n=len(rows)
print("TOTAL shipped:",n)
print("MONTH:",dict(sorted(collections.Counter(r['Completed'][:7] for r in rows).items())))

print("\n=== PILLAR (count | % | effort L/M/S/XS) ===")
for pil in ["Clarity","Connection","Convenience","Fundamentals"]:
    sub=[r for r in rows if r['Pillar']==pil]
    eff=collections.Counter(r['Effort'] for r in sub)
    print(f"  {pil:13} {len(sub):3} ({100*len(sub)//n:2}%)  L{eff['L']} M{eff['M']} S{eff['S']} XS{eff['XS']}")

print("\n=== OKR primary (count | linked/projmap/inferred/BAU) ===")
for okr in ["O2-KR2","O2-KR3","O2-KR4","O2-KR1","O1-KR2","O1-KR3","O1-KR4","—"]:
    sub=[r for r in rows if r['OKR_primary']==okr]
    src=collections.Counter(r['OKR_link'] for r in sub)
    print(f"  {okr:7} {len(sub):3}  linked:{src['Linear-linked']} projmap:{src['Project-mapped']} inferred:{src['Inferred']} bau:{src['None (BAU/foundational)']}")

print("\n=== INVESTMENT ===")
for k,v in sorted(collections.Counter(r['Investment'] for r in rows).items(), key=lambda x:-x[1]):
    print(f"  {v:3}  {k}")

print("\n=== PROJECT ROLLUP (shipped issues per project) ===")
byproj=collections.defaultdict(list)
for r in rows: byproj[r['Project']].append(r)
def keyfn(kv):
    return -len(kv[1])
for proj,sub in sorted(byproj.items(), key=keyfn):
    if proj=="(none)": continue
    pil=sub[0]['Pillar']; 
    okrs=collections.Counter(r['OKR_primary'] for r in sub).most_common(1)[0][0]
    link=collections.Counter(r['OKR_link'] for r in sub).most_common(1)[0][0]
    dmin=min(r['Completed'] for r in sub); dmax=max(r['Completed'] for r in sub)
    url=proj_url.get(proj,'')
    print(f"  {len(sub):3} | {pil:12} | {okrs:6}({link[:4]}) | {dmin}..{dmax} | {proj[:42]:42} | {url}")
print("\n  (none/loose issues):", len(byproj['(none)']))
loose_inv=collections.Counter(r['Investment'] for r in byproj['(none)'])
for k,v in loose_inv.most_common(): print(f"      {v:3} {k}")

print("\n=== AI STACK items (Investment in AI quality / AI agents) ===")
for r in rows:
    if r['Investment'] in ("AI quality","AI agents") and r['Effort'] in ("L","M"):
        print(f"  {r['ID']:8} {r['Effort']} | {r['Title'][:60]}")
