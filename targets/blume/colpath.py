"""Single columnar (rows written, columns read) for a complete rectangle: order the CT segments as P-columns
by maximising row-aligned bigram scores (path search by annealing), then score the reading by quadgrams."""
import numpy as np, random, math, sys, re, struct
from collections import Counter
txt=re.sub('[^a-z]','',open('corpus/es2000.txt',encoding='utf8',errors='ignore').read().lower())
bg=Counter(txt[i:i+2] for i in range(len(txt)-1)); T=sum(bg.values())
B=np.full((26,26),math.log10(0.5/T))
for k,v in bg.items(): B[ord(k[0])-97,ord(k[1])-97]=math.log10(v/T)
q=np.fromfile('q4_es.bin',dtype=np.float32)
def q4(s):
    a=[ord(c)-97 for c in s]; return sum(q[a[i]*17576+a[i+1]*676+a[i+2]*26+a[i+3]] for i in range(len(a)-3))/(len(a)-3)
def solve(ct,w,iters=200000,restarts=8,seed=1):
    n=len(ct); r=n//w; assert n%w==0
    seg=np.array([[ord(c)-97 for c in ct[k*r:(k+1)*r]] for k in range(w)])
    S=np.array([[B[seg[a],seg[b]].sum() if a!=b else -1e9 for b in range(w)] for a in range(w)])
    rnd=random.Random(seed); best=None
    for rs in range(restarts):
        p=list(range(w)); rnd.shuffle(p); cur=sum(S[p[i],p[i+1]] for i in range(w-1))
        for it in range(iters):
            T0=20*(1-it/iters)+0.05
            i,j=sorted(rnd.sample(range(w),2)); m=rnd.random()
            if m<0.5: q2=p[:i]+p[i:j+1][::-1]+p[j+1:]
            else:
                blk=p[i:j+1]; rest=p[:i]+p[j+1:]; k=rnd.randrange(len(rest)+1); q2=rest[:k]+blk+rest[k:]
            v=sum(S[q2[t],q2[t+1]] for t in range(w-1))
            if v>=cur or rnd.random()<math.exp((v-cur)/T0): p,cur=q2,v
        pt=''.join(ct[p[c]*r+t] for t in range(r) for c in range(w))
        sc=q4(pt)
        if best is None or sc>best[0]: best=(sc,cur,p,pt)
    return best
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='plant':
        w=int(sys.argv[2]); pt=txt[int(sys.argv[3]):int(sys.argv[3])+615]; k=list(range(w)); random.Random(9).shuffle(k)
        r=615//w; ct=''.join(pt[t*w+c] for c in k for t in range(r))
        b=solve(ct,w); print('plant w=%d q4 %.3f path %.0f'%(w,b[0],b[1]),b[3][:100]); print('true    ',pt[:100])
    else:
        ct=open('ct1.txt').read().strip().lower(); w=int(sys.argv[2])
        b=solve(ct,w); print('telegram w=%d q4 %.3f path %.0f'%(w,b[0],b[1]),b[3][:150])
