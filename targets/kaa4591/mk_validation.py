"""Build validation.tsv for System A' (the German letters R9408, R9409, R9410 f.244, R9413, R9427; one system, keys
re-learned per letter). For each letter, sysA2/measure2.py (the project's own measure) is run on its .tok file and
hand reading; its final sign-letter alignment (DP, 0-3 letters per sign, scored by the letter's sign-value counts)
gives each sign its value. Lines with an unread stretch ({?}) are left wholly unread, since the aligner does not
know where the gap lies; signs aligned to no letter (dividers, nulls) are also left '?'. [F.G.] and [K] code signs
are not in the alignment and are omitted. The Latin letter R9410 ff.246-247 and the other systems are not included."""
import io, os, sys, runpy, contextlib, pathlib
H = pathlib.Path(__file__).parent; S = H / 'sysA2'
RECS = [('r9408', '../r9408/reading.txt'), ('r9409', '../r9409/reading.txt'), ('r9410', '../r9410/reading.txt'),
        ('r9413', '../r9413/reading.txt'), ('r9427', '../r9427/reading.txt')]
out = ['# model: de-1500s',
       "# source: sysA2/<rec>.tok + r94xx/reading.txt for R9408, R9409, R9410 f.244, R9413, R9427, aligned sign by sign with sysA2/measure2.py's DP (mk_validation.py)",
       "# note: System A' German letters only (keys re-learned per letter, pooled here); lines with {?} gaps and signs aligned to nothing left unread"]
os.chdir(S)
for rec, rf in RECS:
    sys.argv = ['measure2.py', f'{rec}.tok', rf]
    with contextlib.redirect_stdout(io.StringIO()):
        g = runpy.run_path('measure2.py')
    _, T, R = g['data'][0]
    n = k = 0
    for no in T:
        s = T[no]; r = R.get(no)
        if not s: continue
        real = [(w, d) for w, d in g['words_of'](r)] if r else []
        al = g['align'](s, [x for x in real if x[0]], g['P']) if r and '{?}' not in r and any(w for w, _ in real) else None
        if al is None:
            out += [f'{c}\t?' for c in s]; n += len(s); continue
        for c, v, wi in al:
            out.append(f"{c}\t{v if v else '?'}"); n += 1; k += bool(v)
    print(rec, n, k)
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
