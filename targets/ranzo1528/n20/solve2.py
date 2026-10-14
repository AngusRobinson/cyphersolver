import sys,math,random,collections,json,re
seed=int(sys.argv[1]); ITER=int(sys.argv[2]); random.seed(seed)
JUNK={'google','digitized','by','fe','eh','sig','ec','hic','hac','hoc','hzc','ut','ii','iii'}
MODE=sys.argv[3] if len(sys.argv)>3 else 'real'
_c=[w.replace('j','i') for w in open('ita/cast_fixed.txt').read().split()]
HO=(200000,204200)
words=_c[:HO[0]]+_c[HO[1]:] if MODE=='ctrl' else _c
words+= [w.replace('j','i') for w in open('ita/guicc_norm.txt').read().split()[:400000]]
words=[w for w in words if w not in JUNK and (len(w)>1 or w in ('e','a','o'))]
uni=collections.Counter(words); N=sum(uni.values()); V=len(uni)
bi=collections.Counter(zip(words,words[1:])); nd=collections.Counter(a for a,b in bi)
D=0.8
def pu(w): return (uni[w]+0.5)/(N+0.5*V)
cache={}
def lp(a,b):
    k=(a,b)
    r=cache.get(k)
    if r is None:
        if a is None or uni[a]==0: r=math.log(pu(b))
        else: r=math.log(max(bi[(a,b)]-D,0)/uni[a]+D*nd[a]/uni[a]*pu(b))
        cache[k]=r
    return r
def ik(w): return 'v' if w[0]=='u' else w[0]
bylet=collections.defaultdict(list)
for w,c in uni.most_common(12000): bylet[ik(w)].append(w)
if MODE=='ctrl':
    held=[w for w in _c[HO[0]:HO[1]] if w not in JUNK and (len(w)>1 or w in ('e','a','o'))][:3900]
    rng=random.Random(99); code={}; used=collections.defaultdict(set); toks=[]; truth=[]
    for w in held:
        if w not in code:
            L=w[0] if w[0]!='u' else 'v'
            while True:
                n=rng.randint(1,400)
                if n not in used[L]: used[L].add(n); break
            code[w]=L+str(n)
        toks.append(code[w]); truth.append(w)
else:
    toks=open('n20/all_tokens.txt').read().split()
# normalisation
cnt=collections.Counter(toks)
def norm(t):
    if t=='|' or '?' in t or not t[1:].isdigit(): return '|' if t=='|' else None
    L,n=t[0],t[1:]
    if L=='g' and cnt['s'+n]>=cnt[t]: L='s'
    if L=='b' and cnt['h'+n]>=cnt[t]: L='h'
    return L+n
seq=[]
for t in toks:
    x=norm(t)
    seq.append(None if x in (None,'|') else x)
types=sorted(set(x for x in seq if x)); occ=collections.defaultdict(list)
for i,x in enumerate(seq):
    if x: occ[x].append(i)
freq=collections.Counter(x for x in seq if x)
anyw=[w for w,c in uni.most_common(1500)]
def candlist(ty):
    L=ty[0]
    if L=='z': return ['<null>']+anyw[:300]
    if L=='y' or L=='x': return anyw
    if L=='Q': return bylet['q']
    if L=='D': return bylet['d']
    if L=='L': return bylet['l']
    return bylet[L]
C={t:candlist(t) for t in types}
assign={}; owner={}
for L in sorted(set(t[0] for t in types)):
    tl=sorted([t for t in types if t[0]==L],key=lambda t:-freq[t])
    for t in tl:
        for w in C[t]:
            if w=='<null>' or w not in owner:
                assign[t]=w
                if w!='<null>': owner[w]=t
                break
def nxt(j):
    k=j+1
    while k<len(seq) and seq[k] is not None and assign[seq[k]]=='<null>': k+=1
    return k if k<len(seq) and seq[k] is not None else None
def prv(j):
    k=j-1
    while k>=0 and seq[k] is not None and assign[seq[k]]=='<null>': k-=1
    return None if k<0 or seq[k] is None else assign[seq[k]]
def contrib(pos):
    s=0; done=set()
    for i in pos:
        for j in (i,nxt(i)):
            if j is None or j in done: continue
            done.add(j); w=assign[seq[j]]
            if w=='<null>': continue
            s+=lp(prv(j),w)
    return s
for it in range(ITER):
    T=1.2*(1-it/ITER)+0.02
    ty=random.choice(types); old=assign[ty]; Cl=C[ty]
    new=Cl[min(len(Cl)-1,int(random.expovariate(1/40)))] if random.random()<0.7 else random.choice(Cl)
    if new==old: continue
    other=owner.get(new) if new!='<null>' else None
    if other is not None and old not in C[other]: continue
    pos=occ[ty]+(occ[other] if other else [])
    b=contrib(pos); assign[ty]=new
    if other: assign[other]=old
    a=contrib(pos)
    if a>=b or random.random()<math.exp((a-b)/T):
        if old!='<null>':
            if other: owner[old]=other
            else: owner.pop(old,None)
        if new!='<null>': owner[new]=ty
    else:
        assign[ty]=old
        if other: assign[other]=new
tot=sum(lp(prv(j),assign[seq[j]]) for j in range(len(seq)) if seq[j] and assign[seq[j]]!='<null>')
print('SCORE',tot)
out=[]
for x in seq: out.append('\n' if x is None else assign[x])
print(' '.join(out))
if MODE=='ctrl':
    ok=sum(1 for x,w in zip(seq,truth) if x and assign[x]==w); print('CTRL token acc',ok/len(truth))
    tc=collections.Counter(truth); inv={v:k for k,v in code.items()}
    ty_ok=sum(1 for t in types if assign[t]==inv[t]); print('CTRL type acc',ty_ok/len(types),len(types))
json.dump(assign,open(f'n20/s2key_{seed}.json','w'),indent=0)
