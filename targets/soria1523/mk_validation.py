"""Build validation.tsv for the key-A letters (June R9488-90 and the July R9492-93 body), the ciphertext-only break.
Units and their alignment to the reading follow measure/measure.py keyA(): transcription units (one glyph, or one
code group) decoded mechanically (measure/deca.py), aligned to r_june.txt / r_july.txt by difflib per line.
A unit's reading: the aligned reading characters where the alignment is equal or a same-length replacement
(homophone variant / slip as read); '?' where the alignment is uneven or the unit lies in a bracketed word;
'-' for null glyphs (decrypt empty) that the alignment skips. Key-B letters (key from the court decipherment of
R9844) are a different cipher and are left out."""
import os, re, sys, difflib
H = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(H, 'measure')
sys.path.insert(0, os.path.dirname(os.path.dirname(H))); sys.path.insert(0, M)
from deca import dec, toks, CODES
from lang import lm
OPEN_CODES = {'rip', 'qed', 'pur', 'dus', 'cop'}
N = lambda w: lm.norm(w, 'early').replace(' ', '')

def letter(trans, reading):
    rd = {}
    for l in open(reading, encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)', l)
        if m: rd[m.group(1)] = m.group(2)
    out = []
    for l in open(trans, encoding='utf-8'):
        m = re.match(r'\s*(L\d+):(.*)', l)
        if not m: continue
        ct = [t for t in toks(m.group(2)) if t != '.']
        rw = rd[m.group(1)].split()
        for w in rw:
            if w.startswith('{') and w[1:-1] in ct: ct.remove(w[1:-1])
        us = []
        for t in ct:
            if t in CODES: us.append((t, N(CODES[t])))
            elif t in OPEN_CODES: us.append((t, t))
            else:
                v = t.replace('cT', '\x01').replace('Lo', '\x02')
                for ch in v:
                    if ch == '?': continue
                    s = {'\x01': 'cT', '\x02': 'Lo'}.get(ch, ch); d = dec(s)
                    us.append((s, '' if d.startswith('_') or d == '?' else d))
        rch = []
        for w in rw:
            if w.startswith('{'): continue
            br = w.startswith('[')
            for c in N(w.strip('[]').strip('-')): rch.append((c, br))
        a = ''.join(u[1] or '#' for u in us); owner = []
        for k, u in enumerate(us): owner += [k] * max(1, len(u[1]))
        b = ''.join(c for c, _ in rch)
        got = [[] for _ in us]; bad = [False] * len(us)
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
                for k in range(i2 - i1):
                    c, br = rch[j1 + k]; got[owner[i1 + k]].append(c)
                    if br: bad[owner[i1 + k]] = True
            elif tag in ('replace', 'delete'):
                for i in range(i1, i2):
                    if us[owner[i]][1]: bad[owner[i]] = True
        for k, (s, d) in enumerate(us):
            if not d and not got[k]: out.append((s, '-'))
            elif bad[k] or len(got[k]) != max(1, len(d)): out.append((s, '?'))
            else: out.append((s, ''.join(got[k]).replace('#', '') or '-'))
    return out

rows = letter(os.path.join(H, 'keyA_june.txt'), os.path.join(M, 'r_june.txt')) + \
       letter(os.path.join(H, 'keyA_r9492_v2.txt'), os.path.join(M, 'r_july.txt'))
lines = ['# model: es-golden-age',
         '# source: keyA_june.txt + measure/r_june.txt, keyA_r9492_v2.txt + measure/r_july.txt, aligned as measure/measure.py keyA() (mk_validation.py)',
         '# note: key-A letters only (ciphertext-only break); key-B letters (external-plaintext key) not included; bracketed words unread']
lines += [f'{s}\t{v}' for s, v in rows]
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(len(rows))
