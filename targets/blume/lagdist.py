import random,io,contextlib,sys
src=open('lagscan.py').read().split("random.seed(5); pt")[0].replace("/corpus/es_2000.txt","/corpus/es2000.txt").replace("HERE = os.path.dirname(os.path.abspath(__file__))","HERE = '.'")
with contextlib.redirect_stdout(io.StringIO()): exec(src)
def rk(w): k=list(range(w)); random.shuffle(k); return k
def grille(pt,m):  # Fleissner turning grille 2m x 2m, blocks
    N=2*m; out=[]
    for b in range(0,len(pt),N*N):
        blk=pt[b:b+N*N].ljust(N*N,'x'); g=[[None]*N for _ in range(N)]
        holes=[]
        for i in range(m):
            for j in range(m):
                r=random.randrange(4); p=(i,j)
                for _ in range(r): p=(p[1],N-1-p[0])
                holes.append(p)
        k=0
        for rot in range(4):
            for (i,j) in sorted(holes):
                g[i][j]=blk[k]; k+=1
            holes=[(j,N-1-i) for (i,j) in holes]
        out.append(''.join(''.join(r) for r in g))
    return ''.join(out)[:len(pt)]
fams={
 'F,F 26-40': lambda pt: encF(encF(pt,rk(a:=random.randint(26,40)),a),rk(b:=random.randint(26,40)),b),
 'F,F 8-12':  lambda pt: encF(encF(pt,rk(a:=random.randint(8,12)),a),rk(b:=random.randint(8,12)),b),
 'triple F 13-25': lambda pt: encF(encF(encF(pt,rk(a:=random.randint(13,25)),a),rk(b:=random.randint(13,25)),b),rk(c:=random.randint(13,25)),c),
 'grille 10x10': lambda pt: grille(pt,5),
 'random perm': lambda pt: ''.join(random.sample(pt,len(pt))),
}
random.seed(3)
for name,f in fams.items():
    v=[]
    for t in range(15):
        off=random.randrange(0,len(txt)-700); v.append(scan(f(txt[off:off+615]))[0][0])
    v.sort(); print(name,'min %.1f median %.1f max %.1f'%(v[0],v[len(v)//2],v[-1]),flush=True)
