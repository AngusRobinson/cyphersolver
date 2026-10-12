"""Per-group check of the frozen blind decode of R1957 (key v1) against the post-hoc alignment with PC 5263.

The alignment (align_R1957.txt) was made AFTER the blind run; positions graded A/B there were fixed by context, so
confirmations at those positions are partly circular. The unbiased statistic is lcs_test.py; this script only
classifies each decoded group:
  CONFIRMED     blind value = aligned unit
  PARTIAL       blind value is part of the aligned unit ('le roi' for 'le roi de Sardaigne', '-s' for s')
  CONTRADICTED  aligned unit (grade A/B) differs
  UNVERIFIABLE  aligned unit '?' or grade C
usage: python scripts/eval_blind.py [--rows]     (from targets/michell1751/key1751/)"""
import os, sys, re, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode as b
from common import DATA


def nz(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r"[^a-z' ]", '', s).strip()


def load_align(p):
    A = {}
    for l in open(p, encoding='utf8'):
        if l.startswith('#') or l.startswith('idx') or not l.strip():
            continue
        f = l.rstrip('\n').split('\t')
        A[int(f[0])] = (f[1], f[2])
    return A


def compare(bv, au):
    x, y = nz(bv.split('/')[0]), nz(au.replace('!', ''))
    alts = [nz(v) for v in bv.split('/')]
    if not y:
        return None
    if x == y or y in alts:
        return 'CONFIRMED'
    if (x and (x in y or y in x)) or (x == 's' and y in ("s'", 's')) or (x == 'd' and y.startswith('d')):
        return 'PARTIAL'
    return 'CONTRADICTED'


if __name__ == '__main__':
    key = b.load_key(os.path.join(DATA, 'key_cabinet_v1_frozen.tsv'))
    toks = [t for t in b.load_cipher(os.path.join(DATA, 'R1957_tx.txt')) if t[0] != '||']
    dec = b.decode(key, toks)
    A = load_align(os.path.join(DATA, 'align_R1957.txt'))
    res = collections.Counter(); rows = []
    for i, d in enumerate(dec):
        if d[1] == '·':
            continue
        au, conf = A.get(i, ('?', 'C'))
        cls = 'UNVERIFIABLE' if au == '?' or conf == 'C' else (compare(d[1], au) or 'UNVERIFIABLE')
        res[cls] += 1
        rows.append((i, d[0], d[1], au, conf, cls))
    if '--rows' in sys.argv:
        print('idx\tcode\tblind_value\taligned_unit\talign_conf\tclass')
        for r in rows:
            print(*r, sep='\t')
    else:
        for r in rows:
            if r[5] in ('CONTRADICTED', 'PARTIAL'):
                print(*r, sep='\t')
    print('groups', len(dec), 'decoded', len(rows), dict(res))
