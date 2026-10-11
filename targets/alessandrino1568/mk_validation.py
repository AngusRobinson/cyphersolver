"""Build validation.tsv: the beam-search reading of decrypt.py, kept per cipher item.

Same files, key and beam as `python decrypt.py`; only the backtrack keeps the item each output came from.
Letter digit -> its chosen letter; 0 -> null '-'; X0Y0 nomenclator -> one token (the four digits) with its word;
dotted pair -> token 'D<pair>' (its value, '-' for 00 comma, '?' if not in Lasry's list); unreadable '?' left out.
"""
import os, re, glob, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decrypt as D


def decode_items(items, beam=300):
    start = 0
    for x in D.enc('ente'):
        start = (start * D.A + x) % D.MOD
    n = len(items)
    states = [dict() for _ in range(n + 1)]
    states[0][start] = (0.0, None)
    for p in range(n):
        if not states[p]:
            continue
        best = sorted(states[p].items(), key=lambda kv: -kv[1][0])[:beam]
        for ctx, (sc, _) in best:
            it = items[p]
            moves = []
            if isinstance(it, tuple):
                g = D.DOTTED.get(it[1])
                moves.append((1, ('D' + it[1], '-' if g == '' else g if g is not None else '?'),
                              D.enc(g) if g else [], 0.0 if g is not None else -4.0))
            elif it == '?':
                moves.append((1, None, [], -3.0))
            elif it == '0':
                moves.append((1, ('0', '-'), [], D.NULL_COST))
            else:
                for ch in D.POLY[it]:
                    moves.append((1, (it, ch), D.enc(ch), 0.0))
                seg = items[p:p + 4]
                if len(seg) == 4 and all(isinstance(x, str) for x in seg):
                    code = ''.join(seg)
                    if code in D.NOM:
                        pt = D.NOM[code]
                        moves.append((4, (code, pt.replace(' ', '')), D.enc(pt), D.NOM_BONUS))
            for L, pair, chars, pen in moves:
                nctx, s = D.step(ctx, chars)
                ns = sc + s + pen
                q = p + L
                old = states[q].get(nctx)
                if old is None or ns > old[0]:
                    states[q][nctx] = (ns, (p, ctx, pair))
    end = max(states[n].items(), key=lambda kv: kv[1][0])
    out, q, ctx = [], n, end[0]
    while states[q][ctx][1] is not None:
        p, pctx, pair = states[q][ctx][1]
        if pair:
            out.append(pair)
        q, ctx = p, pctx
    return list(reversed(out))


files = sorted(glob.glob(os.path.join(HERE, 'decode', 'DOC_R*_D1[6]*.txt')) +
               glob.glob(os.path.join(HERE, 'decode', 'DOC_R100_D2342_2342.txt')) +
               glob.glob(os.path.join(HERE, 'decode', 'DOC_R115_D1*.txt')),
               key=lambda f: int(re.search(r'DOC_R(\d+)', f).group(1)))
lines = ['# model: it-cinquecento',
         '# source: decode/DOC_R*_D16xx (+R100 D2342, R115) transcriptions, Lasry key, beam search of decrypt.py (mk_validation.py)',
         '# note: polyphonic key (each digit two letters, chosen by the beam with it-cinquecento); 0 = null; X0Y0 codes one token; dotted pairs D<nn>']
for f in files:
    for img, items in D.parse(f):
        for tok, val in decode_items(items):
            lines.append(f'{tok}\t{val}')
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(len(lines))
