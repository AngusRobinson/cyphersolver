import re,glob,collections
def load():
    toks=[]
    for f in ['n20/f44r.txt','n20/f44v.txt','n20/f45r.txt','n20/f45v.txt','n20/f46r.txt','n20/f46v.txt']:
        try: L=open(f,encoding='utf8').read().splitlines()
        except FileNotFoundError: continue
        for l in L:
            if l.startswith('#'): continue
            if l.startswith('|'): toks.append('|'); continue
            l=re.sub(r'\[[^\]]*\]','',l)
            for t in l.split():
                if t=='·': continue
                toks.append(t)
    return toks
