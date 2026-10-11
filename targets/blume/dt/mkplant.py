import sys,random
def order(k): return sorted(range(len(k)),key=lambda i:(k[i],i))
def enc(pt,k):
    w=len(k); n=len(pt); rows,rem=divmod(n,w); out=[]
    for c in order(k):
        L=rows+(1 if c<rem else 0)
        out+= [pt[r*w+c] for r in range(L)]
    return ''.join(out)
def encG(pt,k):  # columns written in key order, rows read: inverse of enc
    w=len(k); n=len(pt); rows,rem=divmod(n,w); m=[0]*n;pos=0
    for c in order(k):
        L=rows+(1 if c<rem else 0)
        for r in range(L): m[r*w+c]=pos; pos+=1
    return ''.join(pt[m[i]] for i in range(n))
if __name__=='__main__':
    src,off,n,k1,k2,conv,out=sys.argv[1:8]
    t=''.join(c for c in open(src,encoding='utf-8',errors='ignore').read().lower() if 'a'<=c<='z')
    pt=t[int(off):int(off)+int(n)]
    I=encG(pt,k1) if conv=='2' else enc(pt,k1)
    ct=encG(I,k2) if conv=='3' else enc(I,k2)
    open(out,'w').write(ct); print(pt[:60])
