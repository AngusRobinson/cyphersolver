from pathlib import Path
import json,re,hashlib,collections,csv
P=Path(__file__).resolve().parent
def load(n):return json.loads((P/n).read_text(encoding='utf-8'))
def fail(ok,msg):
 if not ok:raise SystemExit(msg)
k=load('key.json')['key'];corpus=load('transcription.json');ct=load('counts.json');src=load('source.json')
for name,digest in src['bundled_sha256'].items():fail(hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,'Hash mismatch: '+name)
lines={r['line_id']:r for m in corpus['messages'] for r in m['lines'] if r['line_id']}
f=collections.Counter(t for m in corpus['messages'] for r in m['lines'] for t in r['tokens']);fail(sum(f.values())==ct['cipher_occurrences']==6428,'Cipher count')
fail(len(k)==ct['observed_mapped_codes']==871,'Key count');fail(all(f[t]==r['count'] for t,r in k.items()),'Key frequencies')
null=lambda t:1<=int(t[1:])<=5
value=lambda t:k[t]['value'] if t in k else '' if null(t) else '{'+t+'}'
fail(sum(n for t,n in f.items() if null(t))==207,'Null count');fail(sum(n for t,n in f.items() if t in k)==5967,'Assignment count')
got={l.split('\t',1)[0]:l.split('\t',1)[1] for l in (P/'decode.txt').read_text(encoding='utf-8').splitlines() if '\t' in l and re.match(r'^\d+:',l)}
pat=re.compile(r'(?<![A-Za-z0-9])[A-Za-z]\d+(?![A-Za-z0-9])')
for lid,r in lines.items():
 expected=re.sub(' +',' ',pat.sub(lambda m:value(m[0]),r['content'])).strip();fail(got.get(lid)==expected,'Decryption mismatch: '+lid)
with (P/'alignment.tsv').open(encoding='utf-8',newline='') as stream:
 aligned=list(csv.DictReader(stream,delimiter='\t'))
fail(len(aligned)==6428,'Alignment count')
for r in aligned:fail(r['reading']==value(r['code']),'Alignment value')
for e in load('excerpts.json'):
 for r in e['lines']:
  expected=lines[r['line_id']]['tokens'][r['start_token']-1:r['end_token']]
  fail(expected==r['codes'],'Excerpt boundaries');fail(all(t in k or null(t) for t in expected),'Unresolved excerpt code')
  fail(r['literal_reading']==' '.join(value(t) for t in expected if value(t)),'Excerpt literal reading')
 fail(e['cipher_occurrences']==sum(len(r['codes']) for r in e['lines']),'Excerpt count')
print('OK: 871 mappings; 6,428 cipher occurrences; 541 reproduced lines; 2 excerpts with exact token boundaries. Coverage is not accuracy.')