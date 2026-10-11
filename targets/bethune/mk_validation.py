"""Build validation.tsv for docs/_validate.py from the known-plaintext reading of corpus_v2.txt: f. 34 (10 Nov 1601)
against its clear minute f. 36, plus the glossed passages of 8 Nov (P1-P7) and 10 Dec (D1).
Alignment: em_align.py's own EM (40 iterations, run in memory; em_model_v2.json is not rewritten) and its Viterbi
path per block, token = unit. PH is already expanded by em_align.load to the previous symbol. Plaintext letters the
path skips (paraphrase) are dropped; tokens aligned to nothing are written '-' (null).
The 9 Nov letter (f. 33) is not included: its decode (decode_f33_v3.txt) is word-level LM output with no
token alignment and reads about half its words."""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.argv = [sys.argv[0]]
import em_align as E
data = E.load(os.path.join(HERE, 'corpus_v2.txt')); model = E.Model(data)
for it in range(40):
    newc = collections.defaultdict(lambda: collections.defaultdict(float)); newt = collections.defaultdict(float)
    for pid, ct, pt in data:
        Z, post = E.forward_backward(model, ct, pt)
        if post is None: continue
        for (tok, u), p in post.items(): newc[tok][u] += p; newt[tok] += p
    model.counts, model.tot = newc, newt
rows = []
for pid, ct, pt in data:
    path, sc = E.viterbi(model, ct, pt)
    rows.append(('#', f'block {pid}'))
    for t, u in path:
        if t == '~': continue
        rows.append((t, u or '-'))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8') as f:
    f.write('# model: fr-1600-letters\n# source: corpus_v2.txt (f. 34 vs minute f. 36; glosses P1-P7, D1), aligned by em_align.py EM + Viterbi (mk_validation.py)\n')
    f.write('# note: the reading is the clear minute / contemporary glosses; f. 33 (9 Nov) not included (no token alignment)\n')
    for t, u in rows: f.write(f'# {u}\n' if t == '#' else f'{t}\t{u}\n')
print(sum(t != '#' for t, u in rows))
