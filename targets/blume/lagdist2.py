import random,io,contextlib,math
src=open('lagscan.py').read().split("random.seed(5); pt")[0].replace("/corpus/es_2000.txt","/corpus/es2000.txt").replace("HERE = os.path.dirname(os.path.abspath(__file__))","HERE = '.'")
with contextlib.redirect_stdout(io.StringIO()): exec(src)
def scan2(s):  # baseline from this text's own shuffles
    l=list(s); v=[]
    for _ in range(200): random.shuffle(l); v.append(bscore(''.join(l),1))
    m=sum(v)/len(v); sd=(sum((x-m)**2 for x in v)/len(v))**.5; n=len(s)
    return max(max(bscore(s,lag),bscore(s[::-1],lag))-m for lag in range(1,600) for _ in [0]) if False else max(
        (max(bscore(s,lag),bscore(s[::-1],lag))-m)/(sd*math.sqrt((n-1)/(n-lag))) for lag in range(1,600))
def rk(w): k=list(range(w)); random.shuffle(k); return k
random.seed(7)
print('telegram %.1f'%scan2(ct))
fams={'random perm':lambda pt:''.join(random.sample(pt,len(pt))),
 'F,F 13-25':lambda pt: encF(encF(pt,rk(a:=random.randint(13,25)),a),rk(b:=random.randint(13,25)),b),
 'G,F 13-25':lambda pt: encF(undoF(pt,rk(a:=random.randint(13,25)),a),rk(b:=random.randint(13,25)),b),
 'F,G 13-25':lambda pt: undoF(encF(pt,rk(a:=random.randint(13,25)),a),rk(b:=random.randint(13,25)),b),
 'single F 13-25':lambda pt: encF(pt,rk(a:=random.randint(13,25)),a)}
for name,f in fams.items():
    v=sorted(scan2(f(txt[(o:=random.randrange(0,len(txt)-700)):o+615])) for _ in range(12))
    print(name,'min %.1f median %.1f max %.1f'%(v[0],v[len(v)//2],v[-1]),flush=True)
