"""Decode the dorse (P1, 8 run-over lines) of no. 24 with key R4755: our first-pass transcription by agent E
(targets/siena1421/transcripts/no24.txt, its own sign legend) mapped onto the key sheet by sign shape.
The submitted reading does not cover the dorse. Writes decode_no24_dorse.txt and prints an LM score with a
shuffled-key control. Run from the repository root with PYTHONUTF8=1."""
import re, sys, random, pathlib
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT)); from lang import lm
# agent E's label -> key R4755 value (by shape against the key sheet; '.' = null or unknown)
K = {'W': 'r', 'O': 'a', 'C': 'n', 'E': 'n', 'CE': 'u', 'SQ': 't', 'Q': 'i', 'G': 'i', 'VEN': 'e', 'PHI': 'm',
     'PHX': 'm', 'Z3': 'e', 'Z2': 'b', 'S5': 'a', 'S': 'o', 'EIGHT': 'o', 'SEV': 'o', 'X': 'i', 'T': 'o', 'TT': 'o',
     'H': 'u', 'B': 'a', 'SIX': 'e', 'SIXL': 'e', 'D': 'a', 'DX': 'c', 'M+': 's', 'ETA': 'g', 'U': 'a', 'FO': 'l',
     'SS': 'p', 'Y': 'i', 'TH': 'd'}
t = (ROOT / 'targets/siena1421/transcripts/no24.txt').read_text(encoding='utf8')
rows = []
for n, l in re.findall(r'^(L0\d) (.*)$', t, re.M):
    toks = re.sub(r'\{.*?\}', '', l).split(); out = []; i = 0
    while i < len(toks):
        s = toks[i].rstrip('?')
        if s == 'P' and i + 1 < len(toks) and toks[i + 1].rstrip('?') == 'P': out.append('e'); i += 2; continue
        out.append(K.get(s, '.')); i += 1
    rows.append((n, ''.join(out)))
m = lm.load('it-cinquecento', spaces=False)
sc = lambda s: m.per_char(lm.norm(s.replace('.', ''), 'early', spaces=False))
alltxt = ''.join(r for _, r in rows)
ctl = []
for r in range(20):
    v = list(K.values()); random.Random(r).shuffle(v); k2 = dict(zip(K, v))
    ctl.append(sc(''.join(k2.get(s.rstrip('?'), '') for _, l in re.findall(r'^(L0\d) (.*)$', t, re.M)
                          for s in re.sub(r'\{.*?\}', '', l).split())))
print(f'dorse: {len(alltxt)} decoded positions, {alltxt.count(".")} without value; LM {sc(alltxt):.3f}; '
      f'shuffled control mean {sum(ctl)/len(ctl):.3f}, best {max(ctl):.3f}')
(HERE / 'decode_no24_dorse.txt').write_text(
    '# No. 24 (DECODE R4812) dorse P1, 8 run-over lines, decoded here with key R4755 from our first-pass transcription\n'
    '# (agent E, targets/siena1421/transcripts/no24.txt). Not covered by the submitted reading. "." = no value; "pp"\n'
    '# counted as one e. No word division. Readable stretches are marked in NOTES.md.\n'
    + '\n'.join(f'{n} {r}' for n, r in rows) + '\n', encoding='utf8')
for n, r in rows: print(n, r)
