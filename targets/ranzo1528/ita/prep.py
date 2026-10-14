import re,unicodedata,collections
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    t=t.replace('ſ','s').replace('j','i').replace("'",' ').replace('’',' ')
    return re.sub(r'[^a-z]+',' ',t)
g=norm(open('guicc.txt',encoding='utf8').read()).split()
gv=collections.Counter(g)
print('guicc words',len(g),len(gv))
cast=[]
for f in ['bub_gb_CbcpV2IS7C8C.txt','bub_gb_laRnTtJmsDAC.txt']:
    t=open(f,encoding='utf8',errors='replace').read()
    t=re.sub(r'-\s*\n\s*','',t)  # dehyphenate
    cast+=norm(t).split()
fixed=[]; nfix=0
cv=collections.Counter(cast)
for w in cast:
    if 'f' in w and gv[w]<3:
        # try replacing each f with s (all combos up to 3 f's)
        idx=[i for i,ch in enumerate(w) if ch=='f']
        best=w; bc=gv[w]
        if len(idx)<=4:
            for m in range(1,1<<len(idx)):
                ww=list(w)
                for k,i in enumerate(idx):
                    if m>>k&1: ww[i]='s'
                ww=''.join(ww)
                if gv[ww]>bc: best,bc=ww,gv[ww]
        if best!=w: nfix+=1
        w=best
    fixed.append(w)
print('cast words',len(fixed),'fixed',nfix)
open('cast_fixed.txt','w').write(' '.join(fixed))
open('guicc_norm.txt','w').write(' '.join(g))
c=collections.Counter(fixed); print(c.most_common(80))
