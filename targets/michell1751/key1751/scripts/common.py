"""Shared helpers: word normalisation, PC texts, longest common subsequence."""
import os, re, json, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..')


def norm(s):
    """Lower case, accents stripped, a-z and apostrophes; l'annee -> l' annee."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').lower()
    s = s.replace('’', "'")
    s = re.sub(r"[^a-z' ]+", ' ', s)
    s = re.sub(r"'", "' ", s)
    return s.split()


def nz(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def pc_letters():
    return json.load(open(os.path.join(DATA, 'pc_michell.json'), encoding='utf8'))


def pc_words(PC, num):
    """Words of a PC letter after the heading and date line, before the signature; page numbers dropped."""
    t = PC[num]['text'].split('\n', 2)[2].split('Federic')[0]
    t = re.sub(r'<\d+>', ' ', t)
    return [nz(w) for w in norm(t)]


def lcs(a, b):
    """Length of the longest common subsequence of two word lists (bit-parallel, Hyyrö 2004)."""
    if not a or not b:
        return 0
    masks = {}
    for j, y in enumerate(b):
        masks[y] = masks.get(y, 0) | (1 << j)
    full = (1 << len(b)) - 1
    v = full
    for x in a:
        u = v & masks.get(x, 0)
        v = ((v + u) | (v - u)) & full
    return len(b) - bin(v).count('1')
