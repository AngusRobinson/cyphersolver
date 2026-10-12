"""Build key1751/pc_michell.json (the printed letters to Michell used by the key reconstruction and the blind test)
from the plain-text volumes made by pc_html2txt.py, so that no Politische Correspondenz text is redistributed here.

usage: python scripts/pc_html2txt.py <saved vol-8 html> pc8.txt   (and the same for vol 9 -> pc9.txt)
       python scripts/build_pc_michell.py
Reads key1751/pc8.txt and key1751/pc9.txt; writes key1751/pc_michell.json."""
import json, os, re

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HEAD = re.compile(r'^\s*(\d{4})\.\s+([A-ZÀ-Ý][^\n]*)$', re.M)

out = {"_source": "Politische Correspondenz Friedrich's des Grossen, vols 8-9 (Berlin 1882), text of the digital "
       "edition of the Universitaetsbibliothek Trier (friedrich.uni-trier.de/de/politKorr/<vol>/text/); <NNN> = page "
       "number of the print. Letters to Michell used by the key reconstruction and the blind test. Built locally by "
       "scripts/build_pc_michell.py; not distributed."}
for vol in ('8', '9'):
    t = open(os.path.join(DATA, f'pc{vol}.txt'), encoding='utf8').read()
    heads = list(HEAD.finditer(t))
    for i, m in enumerate(heads):
        if 'MICHELL' not in m.group(2).upper():
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        out[m.group(1)] = {"vol": vol, "title": m.group(2).strip(), "text": t[m.start():end].strip()}
json.dump(out, open(os.path.join(DATA, 'pc_michell.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out) - 1, 'letters to Michell written to pc_michell.json')
