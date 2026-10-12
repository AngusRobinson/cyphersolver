"""Decode a Michell number file (R1957_tx.txt, R1955_tx.txt, fagel5177/*.txt) with a key table.

usage: python decode.py <key.tsv> <cipher.txt>     (paths relative to the current directory)

Key formats: the cabinet keys in this folder (code<TAB>value<TAB>grade...; a code cell may hold several codes
'a b c' with values 'x|y|z') and the envoy table rebuilt by envoy_key.py (code<TAB>value<TAB>count...).
Lookup: code with its underline mark first, then the bare code (flagged '~' when the mark differs).
Fractions (40+1/2) are separate codes and never fall back to the integer. Unknown groups print as '·'.
This is the decoder used for the frozen blind run of 11 Oct 2026 (there called blind_decode.py), unchanged
except that it prints instead of writing a timestamped file."""
import sys, re


def clean_value(v):
    v = v.strip()
    if v.startswith('(opening'):
        return '<OPEN>'
    v = re.sub(r'\s*\((?:plural ending.*|stem|marked variant\?|Hanovre)\)', '', v)
    return v.replace(' / ', '/').strip()


def load_key(path):
    key = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or l.startswith('code\t') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        codes, val = p[0].split(), clean_value(p[1])
        conf = p[2] if len(p) > 2 else ''
        if val.startswith('(opening') or val == '':
            val = '<OPEN>'
        parts = val.split('|') if len(codes) > 1 and '|' in val else None
        for k, c in enumerate(codes):
            v = parts[k] if parts and k < len(parts) else (val if len(codes) == 1 else val + f'[{k + 1}/{len(codes)}]')
            key[c] = (v, conf)
    return key


def load_cipher(path):
    """Tokens (code, mark) from a transcription; '||' marks a page break. Clear text in "...", notes in {...} and
    struck groups [del:...] are dropped."""
    toks = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#'):
            continue
        if line.startswith('||'):
            toks.append(('||', '')); continue
        line = re.sub(r'"[^"]*"', ' ', line)
        line = re.sub(r'\{[^}]*\}', '', line)
        for t in line.split():
            t = t.strip(',.')
            if t.startswith('[del:'):
                continue
            m = re.match(r'^([0-9?]+)([_=#!~]*)((?:\+\d/\d)?)([_=#!~]*)$', t)
            if m:
                toks.append((m.group(1), m.group(2) + m.group(4) + m.group(3)))
    return toks


def decode(key, toks):
    out = []
    for code, mark in toks:
        if code == '||':
            out.append(('||', '', '', '')); continue
        full = code + mark
        if full in key:
            v, conf = key[full]; flag = ''
        elif code in key and '+' not in mark:
            v, conf = key[code]; flag = '~' if mark else ''
        else:
            v, conf, flag = '·', '', ''
        out.append((full, v, conf, flag))
    return out


if __name__ == '__main__':
    key = load_key(sys.argv[1])
    dec = [d for d in decode(key, load_cipher(sys.argv[2])) if d[0] != '||']
    hit = sum(1 for d in dec if d[1] != '·')
    print(f'# {sys.argv[2]} with {sys.argv[1]} ({len(key)} entries): groups {len(dec)}, '
          f'with a value {hit} ({hit / max(len(dec), 1):.1%})')
    print(' '.join(f'{d[0]}={d[1]}' + (f'[{d[2]}]' if d[2] else '') + d[3] for d in dec))
    print('\n# values only:')
    print(' '.join(d[1] for d in dec))
