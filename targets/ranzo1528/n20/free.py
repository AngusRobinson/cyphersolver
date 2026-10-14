import sys,math,random,collections,json
sys.path.insert(0,'n20'); from load import load
seed=int(sys.argv[1]); ITER=int(sys.argv[2]); random.seed(seed)
files=sys.argv[3].split(',') if len(sys.argv)>3 else None
words=open('ita/cast_fixed.txt').read().split()
words=[w.replace('j','i') for w in words if len(w)>1 or w in ('e','a','o')]
uni=collections.Counter(words); N=sum(uni.values())
bi=collections.Counter(zip(words,words[1:])); nd=collections.Counter(a for a,b in bi)
D=0.8; V=len(uni)
def pu(w): return (uni[w]+0.5)/(N+0.5*V)
cache={}
def lp(a,b):
    k=(a,b)
    if k in cache: return cache[k]
    if a is None or uni[a]==0: r=math.log(pu(b))
    else: r=math.log(max(bi[(a,b)]-D,0)/uni[a]+D*nd[a]/uni[a]*pu(b))
    cache[k]=r; return r
def ik(w): return 'v' if w[0]=='u' else w[0]
cands=collections.defaultdict(list)
for w,c in uni.most_common(6000):
    cands[ik(w)].append(w)
anyc=[w for w,c in uni.most_common(400)]
toks=load() if files is None else None
seq=[]
for t in toks:
    if t=='|': seq.append(None); continue
    L=t[0]; L='l' if L=='L' else L
    if not t[1:].isdigit(): seq.append(None); continue
    seq.append(t if L!='L' else t)
types=sorted(set(x for x in seq if x)); occ=collections.defaultdict(list)
for i,x in enumerate(seq):
    if x: occ[x].append(i)
def cl(ty):
    L=ty[0].lower()
    if L in 'zy': return ['<null>']+anyc
    return cands[L]
C={ty:cl(ty) for ty in types}
assign={ty:C[ty][0] if C[ty][0]!='<null>' else '<null>' for ty in types}
# init: most frequent types -> most frequent words in their letter
freq=collections.Counter(x for x in seq if x)
for L in set(t[0] for t in types):
    tl=sorted([t for t in types if t[0]==L],key=lambda t:-freq[t])
    for k,t in enumerate(tl): assign[t]=C[t][min(k,len(C[t])-1)]
def word(i):
    x=seq[i]
    if x is None: return None
    return assign[x]
def prevword(j):
    k=j-1
    while k>=0 and seq[k] is not None and assign[seq[k]]=='<null>': k-=1
    return None if k<0 or seq[k] is None else assign[seq[k]]
def nextidx(j):
    k=j+1
    while k<len(seq) and seq[k] is not None and assign[seq[k]]=='<null>': k+=1
    return k if k<len(seq) and seq[k] is not None else None
def contrib(positions):
    s=0; done=set()
    for i in positions:
        for j in (i, nextidx(i) if nextidx(i) is not None else -1):
            if j is None or j<0 or j in done: continue
            done.add(j)
            w=assign[seq[j]]
            if w=='<null>': continue
            s+=lp(prevword(j),w)
    return s
owner={}
for ty,w in assign.items():
    if w!='<null>': owner.setdefault(w,ty)
# fix initial duplicates
for ty in types:
    w=assign[ty]
    if w!='<null>' and owner[w]!=ty:
        for c in C[ty]:
            if c not in owner and c!='<null>': assign[ty]=c; owner[c]=ty; break
for it in range(ITER):
    T=1.5*(1-it/ITER)+0.03
    ty=random.choice(types); old=assign[ty]
    new=random.choice(C[ty][:80]) if random.random()<0.6 else random.choice(C[ty])
    if new==old: continue
    other=owner.get(new) if new!='<null>' else None
    if other is not None and old not in C[other]: continue
    pos=list(occ[ty])+(list(occ[other]) if other else [])
    b=contrib(pos)
    assign[ty]=new
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
out=[]
for t,x in zip(toks,seq):
    if t=='|': out.append('\n|'); continue
    out.append(assign[x] if x else f'<{t}>')
print(' '.join(out))
json.dump(assign,open(f'n20/fkey_{seed}.json','w'),indent=0)
