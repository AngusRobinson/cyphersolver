import json,urllib.request,urllib.parse,re,html,time,sys
UA={'User-Agent':'cypher-research/0.1 (dnbourdeau@gmail.com)'}
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
out=open('guicc.txt','w',encoding='utf8')
for prefix in ["Storia d'Italia/","Istorie fiorentine/"]:
    cont=''; titles=[]
    while True:
        u="https://it.wikisource.org/w/api.php?action=query&list=allpages&apnamespace=0&aplimit=500&format=json&apprefix="+urllib.parse.quote(prefix)+cont
        d=get(u); titles+= [p['title'] for p in d['query']['allpages']]
        if 'continue' in d: cont='&apcontinue='+urllib.parse.quote(d['continue']['apcontinue'])
        else: break
    titles=[t for t in titles if 'Capitolo' in t]
    print(prefix,len(titles),flush=True)
    for t in titles:
        try:
            d=get("https://it.wikisource.org/w/api.php?action=parse&prop=text&format=json&page="+urllib.parse.quote(t))
            h=d['parse']['text']['*']
            h=re.sub(r'<(style|script)[^>]*>.*?</\1>','',h,flags=re.S)
            tx=html.unescape(re.sub(r'<[^>]+>',' ',h)); out.write(tx+'\n'); out.flush()
        except Exception as e: print('fail',t,e,flush=True)
        time.sleep(0.3)
print('DONE')
