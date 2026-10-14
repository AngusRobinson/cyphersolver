import sys,math,random,collections,re,json
sys.path.insert(0,'n20'); from load import load
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
ITER=int(sys.argv[2]) if len(sys.argv)>2 else 300000
# corpus
words=open('ita/cast_fixed.txt').read().split()+open('ita/guicc_norm.txt').read().split()[:300000]
words=[w.replace('j','i') for w in words]
uni=collections.Counter(words); N=sum(uni.values())
bi=collections.Counter(zip(words,words[1:]))
fol=collections.Counter(a for a,b in bi)   # number of distinct continuations approx
ndist=collections.Counter(); 
for (a,b) in bi: ndist[a]+=1
D=0.75
def pu(w): return (uni[w]+0.1)/(N+0.1*50000)
def lp(a,b):
    if a is None: return math.log(pu(b))
    ca=uni[a]
    if ca==0: return math.log(pu(b))
    return math.log(max(bi[(a,b)]-D,0)/ca + D*ndist[a]/ca*pu(b))
LISTSIZE={'a':326,'b':156,'c':326,'d':307,'e':217,'f':227,'g':214,'h':105,'i':321,'l':144,'m':269,'n':150,'o':176,'p':399,'q':80,'r':335,'s':393,'t':196,'v':250}
def init_key(w): 
    c=w[0]; return 'v' if c=='u' else c
cands={}
for X,S in LISTSIZE.items():
    ws=[w for w,c in uni.most_common() if init_key(w)==X and c>=3 and len(w)>=1][:int(S*2.5)]
    ws=sorted(ws,key=lambda w:w.replace('u','v'))
    cands[X]=ws
toks=load()
seq=[]
for t in toks:
    if t=='|' : seq.append(None); continue
    L=t[0]; L='l' if L=='L' else L
    try: n=int(t[1:])
    except: seq.append(None); continue
    if L in ('z','y'): seq.append(None); continue   # unknown/null: break
    seq.append((L,n))
types=sorted(set(x for x in seq if x))
occ=collections.defaultdict(list)
for i,x in enumerate(seq):
    if x: occ[x].append(i)
bylet=collections.defaultdict(list)
for ty in types: bylet[ty[0]].append(ty)
for L in bylet: bylet[L].sort(key=lambda t:t[1])
# init: proportional position
assign={}
for L,tl in bylet.items():
    C=cands[L]; S=LISTSIZE[L]; prev=-1
    for k,ty in enumerate(tl):
        want=int(ty[1]/S*len(C)); want=max(prev+1,min(want,len(C)-(len(tl)-k)))
        assign[ty]=want; prev=want
def word(i):
    x=seq[i]
    return None if x is None else cands[x[0]][assign[x]]
SIG=0.12
def prior(ty,idx):
    C=cands[ty[0]]; d=idx/len(C)-ty[1]/LISTSIZE[ty[0]]
    return -0.5*(d/SIG)**2
def local(ty):
    s=prior(ty,assign[ty]); done=set()
    for i in occ[ty]:
        for j in (i,i+1):
            if 0<=j<len(seq) and j not in done and seq[j] is not None:
                done.add(j); s+=lp(word(j-1) if j>0 else None, word(j))
    return s
def total():
    s=sum(prior(t,assign[t]) for t in types)
    for j in range(len(seq)):
        if seq[j] is not None: s+=lp(word(j-1) if j>0 else None, word(j))
    return s
cur=total(); T0=3.0
for it in range(ITER):
    T=T0*(1-it/ITER)+0.05
    ty=random.choice(types); L=ty[0]; tl=bylet[L]; k=tl.index(ty)
    lo=assign[tl[k-1]]+1 if k>0 else 0
    hi=assign[tl[k+1]]-1 if k+1<len(tl) else len(cands[L])-1
    if hi<lo: continue
    if random.random()<0.5: new=random.randint(lo,hi)
    else: new=min(hi,max(lo,assign[ty]+random.randint(-3,3)))
    if new==assign[ty]: continue
    old=assign[ty]; b=local(ty); assign[ty]=new; a=local(ty)
    if a>=b or random.random()<math.exp((a-b)/T): cur+=a-b
    else: assign[ty]=old
print('score',total())
out=[]
for t,x in zip(toks,seq):
    if t=='|': out.append('\n|'); continue
    out.append(cands[x[0]][assign[x]] if x else f'<{t}>')
print(' '.join(out))
json.dump({f'{k[0]}{k[1]}':cands[k[0]][v] for k,v in assign.items()},open(f'n20/key_{sys.argv[1] if len(sys.argv)>1 else 1}.json','w'),indent=0)
