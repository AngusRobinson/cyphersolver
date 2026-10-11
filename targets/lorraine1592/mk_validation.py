"""Build validation.tsv from ct/no97_reread.txt (reading of record, 5 Oct pass) with the pair key of
measure_reread.py. One line per cipher token. The token type is the transcription token with its override
('c:t' = the secretary e, a different glyph from 'c'); figures are '<n>'. Words graded H or C are read
(as measure_reread.py counts them); M and I words are '?'. A read word whose mechanical decode differs from its
stated plain text (an emendation) is assigned letter by letter only when lengths allow, otherwise '?'."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import measure_reread as M

def tokval(t):
    base, colon, ov = t.partition(':')
    if colon: return ov
    if base in M.UNKNOWN or base not in M.KEY: return None
    return M.KEY[base]

out = ['# model: fr-1600-letters', '# source: ct/no97_reread.txt (5 Oct 2026) + pair key of measure_reread.py (mk_validation.py)',
       '# note: H/C words read, M/I words unread; token = transcription token incl. override (glyph split)']
stats = {'ok': 0, 'emend_aligned': 0, 'emend_unread': 0}
for line in open(os.path.join(HERE, 'ct', 'no97_reread.txt'), encoding='utf-8'):
    if not re.match(r'L\d\d:', line): continue
    for w in line.split()[1:]:
        m = re.match(r'(.*)=(.*)/([HCMI])$', w)
        if not m: continue
        toks, plain, g = m.groups()
        if toks.startswith('<'):
            out.append(f'{toks}\t{M.norm(plain) if g in "HC" and plain not in ("?", "") else "?"}'); continue
        tl = toks.split('.')
        if g not in 'HC' or '?' in plain:
            out += [f'{t}\t?' for t in tl]; continue
        vals = [tokval(t) for t in tl]
        p = M.norm(plain)
        if None not in vals and M.norm(''.join(vals)) == p:
            stats['ok'] += 1
            out += [f'{t}\t{M.norm(v) or "-"}' for t, v in zip(tl, vals)]
        else:
            # emendation: keep per-token letter counts of the key where they sum to the plain length
            lens = [len(M.norm(v)) if v is not None else 1 for v in vals]
            if sum(lens) == len(p):
                stats['emend_aligned'] += 1; i = 0; r = []
                for t, L in zip(tl, lens):
                    r.append(f'{t}\t{p[i:i+L] or "-"}'); i += L
                out += r
            else:
                stats['emend_unread'] += 1
                out += [f'{t}\t?' for t in tl]
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, stats)
