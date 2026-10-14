import os,time,urllib.request,sys
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
ark=sys.argv[1]; d=sys.argv[2]; sz=sys.argv[3]; idx=[int(x) for x in sys.argv[4].split(',')] if ',' in sys.argv[4] else range(int(sys.argv[4]),int(sys.argv[5])+1)
os.makedirs(d,exist_ok=True)
for i in idx:
    fn=f'{d}/c{i:03d}.jpg'
    if os.path.exists(fn) and os.path.getsize(fn)>8000: continue
    url=f'https://gallica.bnf.fr/iiif/ark:/12148/{ark}/f{i}/full/{sz}/0/native.jpg'
    for t in range(10):
        try:
            b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=180).read(); open(fn,'wb').write(b); print(d,i,len(b),flush=True); break
        except Exception as e:
            print(d,i,'fail',str(e)[:40],flush=True); time.sleep(60*(t+1))
    time.sleep(15)
print('DONE',d,flush=True)
