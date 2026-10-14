import collections
words=open('ita/cast_fixed.txt').read().split()
uni=collections.Counter(w.replace('j','i') for w in words)
LS={'a':326,'b':156,'c':326,'d':307,'e':217,'f':227,'g':214,'h':105,'i':321,'l':144,'m':269,'o':176,'p':399,'r':335,'s':393,'t':196,'v':250}
def key(w): return w.replace('u','v')
for X,S in LS.items():
    ws=[w for w,c in uni.most_common() if (w[0] if w[0]!='u' else 'v')==X and len(w)>1][:S]
    ws=sorted(ws,key=key)
    show=[f'{w}:{i}' for i,w in enumerate(ws) if uni[w]>250]
    print(X,S,' '.join(show))
