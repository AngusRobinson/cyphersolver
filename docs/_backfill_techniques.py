"""One-off backfill of solution[].technique from the text of each step (October 2026).

George Lasry asked that the paper say which techniques the model used: simulated annealing, hill climbing, crib
testing, hypotheses about the structure of the key, and so on. Until then the technique lived only in the free
text of each step (`what`) and in `conditions.tools`. This script reads that text with keyword rules and writes a
`technique` list on every step of kind solver, hypothesis, crib or statistics that has none yet.

New steps get their technique when they are recorded (the /profile skill); this script is kept so the backfill
can be reproduced and audited. The paper reports the backfilled labels as rule-assigned from the step text.

  python docs/_backfill_techniques.py            dry run: counts per technique and the steps left as 'other'
  python docs/_backfill_techniques.py --write    insert the field (the kind line gains a "technique" key; the rest
                                                 of each file is left byte for byte, whatever its indentation)
"""
import sys, re, json, pathlib, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ROOT = pathlib.Path(__file__).resolve().parent.parent
NEEDS = ('solver', 'hypothesis', 'crib', 'statistics')

# order matters only for display; a step may carry several techniques
RULES = [
    ('simulated annealing', r'anneal|\bSA\b|tempering|metropolis'),
    ('hill climbing', r'hill[- ]?climb|climb|local search|\bIDP\b|greedy|swap search|coordinate ascent|iterated local'
                      r'|permutation search|block[- ]edit|optimi[sz]er|polish pass|free-cell search'),
    ('EM alignment', r'\bEM\b|hard-EM|expectation|aligner|alignment|\bHMM\b|forward-backward'),
    ('beam/DP decoding', r'beam|viterbi|depth-first|dynamic programming|segment(?:ation|er)|word-aware decoder'
                         r'|\bdecod(?:er|ing)\b|rescoring'),
    ('SAT/constraint solving', r'\bSAT\b|z3|constraint|backtrack|integer program|\bILP\b|pysat|solver for the equations'),
    ('exhaustive search', r'exhaustive|lexicon search|wordmatch|dictionary|all grid orientations|all line lengths|enumerat|brute|every (?:width|offset|period|shift|key|order|combination)|all (?:widths|offsets|periods|shifts|keys|orders|permutations)|scan(?:ned)? (?:all|every)|grid search'),
    ('crib testing', r'(?<!without )(?<!no )\bcrib|known[- ]plaintext|probable word|dragg'),
    ('key-structure hypothesis', r'structure|syllab|nomenclator|homophon|one-part|two-part|alphabetical|monoalphab|polyalphab|vigen|transposi|columnar|playfair|code ?book|null|digraph|grille|design|system|bigram cipher|polyphon|superscript|diacritic|vowel'),
    ('frequency analysis', r'frequenc|\bIC\b|index of coincidence|chi-?squared|entropy|distribution|\bKS\b|histogram|kappa|mass|share of|counts?\b|top group'),
    ('repeat/pattern analysis', r'repeat|isomorph|pattern|recurr|chain|periodic|kasiski|position|line-end|word-?length|run[s]?\b'),
    ('language-model scoring', r'n-?gram|\bLM\b|language model|per char|per letter|log-?prob|quadgram|trigram|5-gram|perplex|de-1500s|fr-1|it-c|es-|la\b model'),
    ('key matching', r'sibling key|key R\d|R\d+ key|applied the|with the .* key|existing key|archive key|published key|Lasry\'?s key|tomokiyo|known key|keys? (?:of|from) the (?:same|volume)|every .* key|tried .* keys?'),
    ('plaintext matching', r'clear copy|decipherment|interlinear|gloss|marginal|margin|decifrat|register copy|in print|printed|edition|calendar'),
    ('contextual inference', r'context|attribut|identif|by sense|historical|date[ds]?\b|signature|docket|sender|recipient|names?\b'),
    ('statistical test', r'permutation test|p ?[<=]|significan|random (?:key|numbering|control)|shuffl|null model|percentile|z-?score|control'),
]
RX = [(t, re.compile(p, re.I)) for t, p in RULES]
ENUM = [t for t, _ in RULES] + ['manual reconstruction', 'automated search (unspecified)', 'other']

# a solver step whose text names only a script (hsolve.py, solve2.py) is recorded as an unspecified search
DEFAULT = {'crib': 'crib testing', 'statistics': 'frequency analysis', 'hypothesis': 'key-structure hypothesis',
           'solver': 'automated search (unspecified)'}

def classify(kind, what):
    got = [t for t, rx in RX if rx.search(what or '')]
    if kind != 'hypothesis' and 'key-structure hypothesis' in got: got.remove('key-structure hypothesis')
    if kind == 'crib' and 'crib testing' not in got: got.insert(0, 'crib testing')
    if kind == 'solver':
        # a solver step that names no search is usually a hand/scripted reconstruction
        if not any(t in got for t in ('simulated annealing', 'hill climbing', 'EM alignment', 'SAT/constraint solving',
                                      'exhaustive search')):
            if re.search(r'by hand|manual|hand-|rebuilt|reconstruct|fixed .*=|set .*=', what or '', re.I):
                got.append('manual reconstruction')
    if not got: got = [DEFAULT[kind]]
    return got

KIND_RX = re.compile(r'("kind"\s*:\s*"(?:solver|hypothesis|crib|statistics)")')

def backfill(path, write=False):
    text = path.read_text(encoding='utf-8')
    prof = json.loads(text)
    steps = prof.get('solution', [])
    if not isinstance(steps, list): return []
    # the n-th "kind" key in the file text is the n-th step that has a kind (no other field is named "kind")
    kinds = [m for m in re.finditer(r'"kind"\s*:\s*"([^"]*)"', text)]
    with_kind = [s for s in steps if isinstance(s, dict) and 'kind' in s]
    if len(kinds) != len(with_kind): return [('SKIP', path.parent.name, 'kind count mismatch')]
    out, pieces, last = [], [], 0
    for m, s in zip(kinds, with_kind):
        if s['kind'] not in NEEDS or 'technique' in s: continue
        tech = classify(s['kind'], s.get('what', ''))
        out.append((tech, path.parent.name, s.get('what', '')))
        pieces.append(text[last:m.end()])
        pieces.append(', "technique": ' + json.dumps(tech, ensure_ascii=False))
        last = m.end()
    if write and out:
        new = ''.join(pieces) + text[last:]
        chk = json.loads(new)                                 # the insert must not change anything else
        for s in chk['solution']: s.pop('technique', None)
        ref = json.loads(text)
        for s in ref['solution']: s.pop('technique', None)
        assert chk == ref, path
        path.write_text(new, encoding='utf-8', newline='')
    return out

if __name__ == '__main__':
    write = '--write' in sys.argv
    sys.path.insert(0, str(ROOT / 'docs'))
    import _check_writeup as cw
    tally, other, skips = collections.Counter(), [], []
    for p in sorted([*(ROOT / 'targets').glob('*/profile.json'), *(ROOT / 'research').glob('**/profile.json')]):
        if p.parent.name in cw.FAMOUS: continue
        for tech, name, what in backfill(p, write):
            if tech == 'SKIP': skips.append(name); continue
            tally.update(tech)
            if tech in (['other'],): other.append((name, what))
    for t, n in tally.most_common(): print(f'{n:5}  {t}')
    print(f'{len(other)} step(s) left as other')
    for n, w in other: print(f'  {n}: {w[:150]}')
    if skips: print('skipped (kind count mismatch):', ', '.join(skips))
