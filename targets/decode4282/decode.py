"""Reapply Lasry's CTTS key; keep editorial Latin separate from literal output.

Run from any directory with Python3. Only derived files in this target are written.
No images, original transcription, source key, or editorial reading are modified.
"""
from pathlib import Path
from collections import Counter
import csv, json, re

HERE=Path(__file__).resolve().parent
key=json.loads((HERE/'key.json').read_text(encoding='utf-8'))
rows=[]; page=line_no=0
for line in (HERE/'transcription.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#'):
        page+=1;line_no=0;continue
    if not line.strip():continue
    line_no+=1
    toks=[t.strip() for t in line.split(';') if t.strip()]
    rows.append((page,line_no,toks))

records=[]; literal=[]; tokens=[]; validation=['# model: la','# source: transcription.txt + key.json','# note: literal values only; no editorial restorations or cleartext; nulls fixed; unknown codes omitted']
last=0
for p,n,toks in rows:
    if p!=last:literal.extend(['',f'# {p}.png']);last=p
    literal.append(' '.join('_' if t in key and key[t]=='' else '[name/title?]' if t in key and key[t] is None else key.get(t,t) for t in toks))
    line_records=[]
    for pos,t in enumerate(toks,1):
        if t not in key:continue
        value=key[t]
        rec={'page':p,'line':n,'position_in_line':pos,'sign':t,'value':'?' if value is None else '-' if value=='' else value,'status':'unresolved' if value is None else 'null' if value=='' else 'mapped'}
        line_records.append(rec);tokens.append(t)
        validation.append(t+'\t'+rec['value'])
    # Exclude entire known-but-imperfect words from the conservative coherence floor.
    wanted={(1,12):['simpir','aglo'],(1,13):['prsrsvs'],(1,16):['prsmitat'],(2,4):['it']}.get((p,n),[])
    chars=[];owners=[]
    for i,r in enumerate(line_records):
        if r['status']=='mapped':
            chars.extend(r['value']);owners.extend([i]*len(r['value']))
        elif r['status']=='unresolved':chars.append('?');owners.append(i)
    text=''.join(chars)
    for word in wanted:
        starts=[m.start() for m in re.finditer(re.escape(word),text)]
        assert len(starts)==1,(p,n,word,text,starts)
        for i in set(owners[starts[0]:starts[0]+len(word)]):line_records[i]['status']='editorial-word'
    records.extend(line_records)

# Confirm full original decryption is exactly reproduced, not merely counted.
def canonical(lines):
    return [' '.join(x.lower().split()) for x in lines if x.strip()]
assert canonical(literal)==canonical((HERE/'literal_decryption.txt').read_text(encoding='utf-8').splitlines())
counts=Counter(r['status'] for r in records)
assert counts=={'null':279,'mapped':773,'editorial-word':27,'unresolved':5},counts
assert len(tokens)==1084 and len(set(tokens))==39
with (HERE/'token_readings.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=records[0].keys(),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(records)
(HERE/'cipher_tokens.txt').write_text('\n'.join(' '.join(t for t in ts if t in key) for _,_,ts in rows)+'\n',encoding='utf-8')
(HERE/'validation.tsv').write_text('\n'.join(validation)+'\n',encoding='utf-8')
metrics={'cipher_elements':1084,'distinct_signs':39,'pages':2,'lines_by_page':{'1':25,'2':7},'non_null_elements':805,'mapped_non_null':800,'null_elements':279,'unresolved_elements':5,'unresolved_types':3,'editorial_word_elements':27,'key_assignment_non_null':800/805,'key_assignment_including_nulls':1079/1084,'conservative_coherence_floor':773/805,'coherence_rule':'Exclude all sign occurrences in five editorially restored words and all unresolved signs; this is a coverage lower bound, not probabilistic accuracy.'}
(HERE/'counts.json').write_text(json.dumps(metrics,indent=1,ensure_ascii=False),encoding='utf-8')
print(json.dumps(metrics,indent=1))
