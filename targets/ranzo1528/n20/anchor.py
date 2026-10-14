import sys,math,random,collections,json
sys.path.insert(0,'n20'); from load import load
seed=int(sys.argv[1]); ITER=int(sys.argv[2]); random.seed(seed)
ANCH=json.load(open('n20/anchors.json'))
words=open('ita/cast_fixed.txt').read().split()+open('ita/guicc_norm.txt').read().split()[:200000]
words=[w.replace('j','i') for w in words]
uni=collections.Counter(words); N=sum(uni.values())
bi=collections.Counter(zip(words,words[1:])); nd=collections.Counter(a for a,b in bi)
D=0.75
def pu(w): return (uni[w]+0.1)/(N+5000)
def lp(a,b):
    if a is None or uni[a]==0: return math.log(pu(b))
    return math.log(max(bi[(a,b)]-D,0)/uni[a]+D*nd[a]/uni[a]*pu(b))
LS={'a':326,'b':156,'c':326,'d':307,'e':217,'f':227,'g':214,'h':105,'i':321,'l':144,'m':269,'n':150,'o':176,'p':399,'q':80,'r':335,'s':393,'t':196,'v':250}
def ik(w): return 'v' if w[0]=='u' else w[0]
cands={}
for X,S in LS.items():
    ws=[w for w,c in uni.most_common() if ik(w)==X and c>=2][:int(S*1.6)]
    for a,w in ANCH.items():
        if (a[0].lower() if a[0]!='L' else 'l')==X and w not in ws: ws.append(w)
    cands[X]=sorted(set(ws),key=lambda w:w.replace('u','v'))
# anchor positions -> piecewise-linear expected index
def expected(X,n):
    pts=[(0,0),(LS[X],len(cands[X])-1)]
    for a,w in ANCH.items():
        L=a[0] if a[0]!='L' else 'l'
        if L==X: pts.append((int(a[1:]),cands[X].index(w)))
    pts=sorted(set(pts))
    for (n0,i0),(n1,i1) in zip(pts,pts[1:]):
        if n0<=n<=n1: return i0+(i1-i0)*(n-n0)/max(1,n1-n0)
    return pts[-1][1]
toks=load(); seq=[]
for t in toks:
    if t=='|': seq.append(None); continue
    L=t[0]; L='l' if L=='L' else L
    try: n=int(t[1:])
    except: seq.append(None); continue
    if L in ('z','y'): seq.append(None); continue
    seq.append((L,n))
types=sorted(set(x for x in seq if x)); occ=collections.defaultdict(list)
for i,x in enumerate(seq):
    if x: occ[x].append(i)
bylet=collections.defaultdict(list)
for ty in types: bylet[ty[0]].append(ty)
for L in bylet: bylet[L].sort(key=lambda t:t[1])
fixed={}
for a,w in ANCH.items():
    L=a[0] if a[0]!='L' else 'l'; fixed[(L,int(a[1:]))]=cands[L].index(w)
assign={}
for L,tl in bylet.items():
    prev=-1
    for ty in tl:
        e=fixed.get(ty,int(expected(L,ty[1])))
        e=max(prev+1,e); assign[ty]=e; prev=e
SIG=float(sys.argv[3]) if len(sys.argv)>3 else 12
def prior(ty,idx): return -0.5*((idx-expected(ty[0],ty[1]))/SIG)**2
def word(i): x=seq[i]; return None if x is None else cands[x[0]][assign[x]]
def local(ty):
    s=prior(ty,assign[ty]); done=set()
    for i in occ[ty]:
        for j in (i,i+1):
            if 0<=j<len(seq) and j not in done and seq[j] is not None:
                done.add(j); s+=lp(word(j-1) if j>0 else None,word(j))
    return s
free=[t for t in types if t not in fixed]
for it in range(ITER):
    T=2.0*(1-it/ITER)+0.05
    ty=random.choice(free); L=ty[0]; tl=bylet[L]; k=tl.index(ty)
    lo=assign[tl[k-1]]+1 if k>0 else 0
    hi=assign[tl[k+1]]-1 if k+1<len(tl) else len(cands[L])-1
    if hi<lo: continue
    new=random.randint(lo,hi) if random.random()<0.3 else min(hi,max(lo,assign[ty]+random.randint(-4,4)))
    if new==assign[ty]: continue
    old=assign[ty]; b=local(ty); assign[ty]=new; a=local(ty)
    if not(a>=b or random.random()<math.exp((a-b)/T)): assign[ty]=old
out=[]
for t,x in zip(toks,seq):
    if t=='|': out.append('\n|'); continue
    out.append(cands[x[0]][assign[x]] if x else f'<{t}>')
print(' '.join(out))
json.dump({f'{k[0]}{k[1]}':cands[k[0]][v] for k,v in assign.items()},open(f'n20/akey_{seed}.json','w'),indent=0)
