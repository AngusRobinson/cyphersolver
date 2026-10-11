"""Build validation.tsv for sessa1523 from reading_r9660.txt (both parts) and reading_r9665.txt.
Each (a) cipher line is paired with its (b) reading line; clear quotes, parenthetical notes, '/' and the f~ switch
are dropped; v db / v:db / ▷db (the null opener) is one token, read '¶' (null, '-'). The reading line is split into
words and hyphenated letters; a piece wholly in [ ] is unread, supplied letters [x] inside a piece are dropped.
A line is used only when its reading pieces match its cipher tokens one for one; otherwise its tokens are written
as unread ('?'), never re-aligned by hand. The script prints the share of lines that matched."""
import re, pathlib
H = pathlib.Path(__file__).resolve().parent

def unquote(s):
    s = re.sub(r'"[^"]*"', ' ', s)
    return s.split('"')[0]          # an unclosed quote runs to the end of the line

def ctoks(s):
    s = unquote(s).replace('—', ' ')
    s = re.sub(r'\([^()]*\)|\[[^\]]*\]', ' ', s)      # notes such as (interl. tto), [struck word]
    s = re.sub(r'\bv:db\b|▷db|\bv db\b', ' NULLOPEN ', s)
    return [t for t in s.split() if t not in ('f~', '/', '¶', '...', '…')]

def rpieces(s):
    s = unquote(s)
    s = re.sub(r'\([^()]*\)', ' ', s)
    s = s.replace('¶', ' NULLOPEN ')
    out = []
    for w in s.split():
        if w in ('/', '...', '…', '->'): continue
        if w == 'NULLOPEN': out.append('-'); continue
        depth = 0
        for p in w.split('-'):
            if not p: continue
            whole = (p.startswith('[') and p.endswith(']')) or (depth > 0) or (p.startswith('[') and ']' not in p) or (p.endswith(']') and '[' not in p)
            depth += p.count('[') - p.count(']')
            if whole:
                out.append('?')
            else:
                v = re.sub(r'\[[^\]]*\]', '', p).strip('.,;:?')
                out.append(v if re.search(r'[A-Za-zñçáéíóú]', v) else '?')
    return out

def pairs(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    for i, l in enumerate(lines):
        m = re.match(r'^\s*(\d+)\s?a\s(.*)$', l)
        if not m or i + 1 >= len(lines): continue
        n = re.match(r'^\s*(?:\d+\s?)?b\s(.*)$', lines[i + 1])
        if n: yield m.group(2), n.group(1)

out = ['# model: es-golden-age', '# source: reading_r9660.txt (parts 1-2) + reading_r9665.txt, (a)/(b) line pairs, mk_validation.py',
       '# note: Spanish 1523; lines whose reading pieces do not match the cipher tokens one for one are written unread (?); '
       'NULLOPEN = the v db null opener']
ok = bad = 0
for f in ('reading_r9660.txt', 'reading_r9665.txt'):
    for a, b in pairs(H / f):
        c, r = ctoks(a), rpieces(b)
        if not c: continue
        if len(c) == len(r):
            ok += 1; out += [f'{t}\t{v}' for t, v in zip(c, r)]
        else:
            bad += 1; out += [f'{t}\t?' for t in c]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'lines matched {ok}, not matched {bad}; tokens {len(out) - 3}')
