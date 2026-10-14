import re,sys,os,collections
R=sys.argv[1]
key={}
for l in open(R+'/key/table.tsv',encoding='utf8').read().split('\n')[1:]:
    f=l.split('\t')
    if len(f)>=3 and f[1]: key[f[0]]=(f[1],f[2])
cor={}
for l in open(R+'/evidence/transcription_corrections.tsv',encoding='utf8').read().split('\n')[1:]:
    f=l.split('\t')
    if len(f)==5: cor[(f[0],int(f[1]),f[3])]=f[4]
def toks(path):
    name=os.path.basename(path); out=[]; odd=collections.Counter()
    for n,l in enumerate(open(path,encoding='utf8'),1):
        l=l.rstrip('\n')
        if l.startswith('#') or l.startswith('|'): continue
        l=re.sub(r'\[[^\]]*\]','',l)
        for t in l.split():
            t=cor.get((name,n,t),t)
            if t=='(delete)': continue
            m=re.match(r'^([A-Za-z])(\d+)\??$',t)
            if m:
                L,N=m.group(1),int(m.group(2))
                if L=='L': L='l'
                if L=='g' and N>214: L='s'   # the g list has 214 entries: an 8-like s (decode.py)
                if L=='t' and N>196: L='r'   # the t list has 196 entries: a tau-like r
                out.append(L+str(N))
            else: odd[t]+=1
    return out,odd
def cls(t):
    if t in key: return key[t][1]
    return 'none'
files=sys.argv[2:]
tot=collections.Counter()
print('file tokens sure probable guess null none | typesnone | island-tokens(>=6 run sure/prob/null-free)')
for f in files:
    t,odd=toks(f); c=collections.Counter(cls(x) for x in t)
    # islands: runs of >=6 consecutive tokens with class sure/probable (null allowed? rule says value sure/probable; treat null as breaking? count nulls as neutral-inside)
    runs=0;cur=0
    for x in t:
        k=cls(x)
        if k in('sure','probable'): cur+=1
        else:
            if cur>=6: runs+=cur
            cur=0
    if cur>=6: runs+=cur
    print(os.path.basename(f),len(t),c['sure'],c['probable'],c['guess'],c['null'],c['none'],'| uniq-none',len({x for x in t if cls(x)=='none'}),'| island',runs, round(100*runs/len(t),1) if t else 0,'| odd',dict(odd))
    tot.update(c); tot['n']+=len(t); tot['isl']+=runs
print('TOTAL',dict(tot))
