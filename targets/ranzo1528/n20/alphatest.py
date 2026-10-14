import sys,collections,random,math
sys.path.insert(0,'n20'); from load import load
words=open('ita/cast_fixed.txt').read().split(); uni=collections.Counter(w.replace('j','i') for w in words)
LS={'a':326,'b':156,'c':326,'d':307,'e':217,'f':227,'g':214,'h':105,'i':321,'l':144,'m':269,'n':150,'o':176,'p':399,'q':80,'r':335,'s':393,'t':196,'v':250}
def ik(w): return 'v' if w[0]=='u' else w[0]
B=10
wprof={}
for X,S in LS.items():
    ws=[w for w,c in uni.most_common() if ik(w)==X and len(w)>1][:S]
    ws=sorted(ws,key=lambda w:w.replace('u','v'))
    prof=[0]*B
    for i,w in enumerate(ws): prof[min(B-1,i*B//len(ws))]+=uni[w]
    s=sum(prof); wprof[X]=[p/s for p in prof]
toks=[t for t in load() if t!='|' and t[0] not in 'zy' and t[1:].isdigit()]
bylet=collections.defaultdict(list)
for t in toks:
    L='l' if t[0]=='L' else t[0]; bylet[L].append(int(t[1:]))
def stat(bl):
    tot=0
    for X,nums in bl.items():
        if X not in LS or len(nums)<10: continue
        prof=[0]*B
        for n in nums: prof[min(B-1,n*B//LS[X])]+=1
        s=sum(prof); prof=[p/s for p in prof]
        # overlap (Bhattacharyya)
        tot+=len(nums)*sum(math.sqrt(a*b) for a,b in zip(prof,wprof[X]))
    return tot
obs=stat(bylet)
# null: remap each distinct number within its letter to a random number (random codebook order), preserving token freq
null=[]
for r in range(500):
    bl={}
    for X,nums in bylet.items():
        if X not in LS: continue
        d=sorted(set(nums)); perm=random.sample(range(1,LS[X]+1),len(d)); m=dict(zip(d,perm))
        bl[X]=[m[n] for n in nums]
    null.append(stat(bl))
import statistics
print('obs',obs,'null mean',statistics.mean(null),'sd',statistics.pstdev(null),'z',(obs-statistics.mean(null))/statistics.pstdev(null), 'p',sum(n>=obs for n in null)/len(null))

# power check: simulate alphabetical code on real text
codes={}
for X,S in LS.items():
    ws=[w for w,c in uni.most_common() if ik(w)==X and len(w)>1][:S]
    ws=sorted(ws,key=lambda w:w.replace('u','v'))
    for i,w in enumerate(ws): codes[w]=(X,i+1)
for trial in range(3):
    st=random.randint(0,len(words)-5000)
    sim=collections.defaultdict(list); n=0
    for w in words[st:]:
        w=w.replace('j','i')
        if w in codes: X,i=codes[w]; sim[X].append(i); n+=1
        if n>=1100: break
    o=stat(sim); nl=[]
    for r in range(200):
        bl={}
        for X,nums in sim.items():
            d=sorted(set(nums)); perm=random.sample(range(1,LS[X]+1),len(d)); m=dict(zip(d,perm)); bl[X]=[m[x] for x in nums]
        nl.append(stat(bl))
    print('SIM obs',o,'z',(o-statistics.mean(nl))/statistics.pstdev(nl))
