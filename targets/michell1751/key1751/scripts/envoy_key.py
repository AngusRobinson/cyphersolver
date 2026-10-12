"""Rebuild the table of Michell's envoy code from the DECODE transcriptions of R1050 and R1051.

R1050 (Michell to Frederick II, London 5 Sep 1752) and R1051 (12 Nov 1751) are Hague copies of Michell's own reports
with the contemporary Dutch decipherment written over the numbers. DECODE's transcriptions (transcriber XZ, March 2020)
give each line of that decipherment as '<PLAINTEXT FR ...>' followed by the cipher line, one group per plaintext token.
This script pairs them token by token. Lines whose token counts disagree are listed and skipped, not guessed.

The table is derived from DECODE's transcriptions, so neither the transcriptions nor the table are committed here
(envoy_key_lyonet.tsv and envoy_pairs.tsv are git-ignored). Download DOC_R1050_*.txt and DOC_R1051_*.txt from
DECODE (login needed) into one folder and run:

usage: python scripts/envoy_key.py <folder with DOC_R1050_*.txt and DOC_R1051_*.txt>   (from key1751/)
expected (11 Oct 2026): 512 pairs, 271 codes, 5 lines skipped; sha256 of the table with LF line ends 301391c6...
(frozen_keys.sha256); 40 codes in both reports, 32 with the same commonest value."""
import re, os, sys, glob, collections, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..')


def parse_cipher(line):
    line = line.strip().rstrip('.').strip()
    chunks = [c for c in re.split(r'\s*,\s*|\s{2,}', line) if c.strip()]
    out = []
    for c in chunks:
        mark = '_' if '_' in c else ''
        s = c.replace('_', '').replace(' ', '')
        frac = ''
        m = re.match(r'^(.*?)(1/2|1/4|3/4)$', s)
        if m:
            s, frac = m.group(1), '+' + m.group(2)
        out.append(s + mark + frac)
    return out


if __name__ == '__main__':
    src = sys.argv[1]
    pairs, skipped = [], []
    for rec in ('1050', '1051'):
        fs = glob.glob(os.path.join(src, f'DOC_R{rec}_*.txt'))
        if not fs:
            sys.exit(f'no DOC_R{rec}_*.txt in {src}')
        for f in fs:
            L = open(f, encoding='utf8', errors='replace').read().split('\n')
            for i, l in enumerate(L):
                m = re.match(r'<PLAINTEXT FR (.*)>\s*$', l)
                if not m or i + 1 >= len(L):
                    continue
                plain = m.group(1).replace('<ABBR', ' ').split()
                ciph = parse_cipher(L[i + 1])
                if len(plain) != len(ciph):
                    skipped.append((rec, i + 1, len(plain), len(ciph)))
                    continue
                for p, c in zip(plain, ciph):
                    pairs.append((rec, i + 1, c, p))
    with open(os.path.join(OUT, 'envoy_pairs.tsv'), 'w', encoding='utf8') as fo:
        fo.write('rec\tline\tcode\tplain\n')
        for r in pairs:
            fo.write('\t'.join(map(str, r)) + '\n')
    key = collections.defaultdict(collections.Counter)
    for rec, ln, c, p in pairs:
        key[c.replace('_', '')][p.lower()] += 1
    kp = os.path.join(OUT, 'envoy_key_lyonet.tsv')
    with open(kp, 'w', encoding='utf8') as fo:
        fo.write('# Michell envoy code, values from Lyonet\'s solutions as transcribed in DECODE R1050 (5 Sep 1752) and R1051 (12 Nov 1751)\n')
        fo.write('code\tvalue\tcount\talternatives\n')
        for code in sorted(key, key=lambda x: (len(x), x)):
            v, n = key[code].most_common(1)[0]
            alt = '; '.join(f'{a}:{b}' for a, b in key[code].most_common()[1:])
            fo.write(f'{code}\t{v}\t{sum(key[code].values())}\t{alt}\n')
    print('pairs', len(pairs), 'codes', len(key), 'skipped lines', len(skipped))
    for s in skipped:
        print('skipped: R%s line %d, %d plaintext tokens vs %d groups' % s)
    raw = open(kp, 'rb').read()
    print('sha256 (LF line ends)', hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest())
    # stability of the code between the two reports (Nov 1751, Sep 1752): codes seen in both, same commonest value?
    by = {r: collections.defaultdict(collections.Counter) for r in ('1050', '1051')}
    for rec, ln, c, p in pairs:
        by[rec][c.replace('_', '')][p.lower()] += 1
    both = sorted(set(by['1050']) & set(by['1051']), key=lambda x: (len(x), x))
    same = [c for c in both if by['1050'][c].most_common(1)[0][0] == by['1051'][c].most_common(1)[0][0]]
    print('codes in both reports', len(both), 'same commonest value', len(same))
    for c in both:
        if c not in same:
            print('  differs:', c, dict(by['1050'][c]), dict(by['1051'][c]))
