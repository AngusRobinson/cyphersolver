"""Pull open cipher records from Cryptoole (Satoru's index) as catalogue candidates.

Cryptoole (https://cryptoole.satoru.net/) merges DECODE, Cryptiana, CryptoCellar, Rosson's
cipher-readings and our own catalogue (source 'cyphersolver') into one index with a JSON API
(api.html). This script pages through the API and keeps the rows that could become
catalogue.json entries:

  - type 'cipher', status 'open' (including 'partly' and 'key_only');
  - not already from us (no 'cyphersolver' among its sources);
  - no CryptoCellar rows or other Enigma messages (WWII machine traffic, outside the paper's scope);
  - dated 1950 or earlier, and not one of the famous ciphers (FAMOUS in docs/_check_writeup.py).

Each candidate is checked against what the repository already knows: DECODE R-numbers and
Cryptoole IDs found in catalogue.json, the ledgers, targets/ and research/. Matches are
reported, not dropped, so a near-duplicate can be checked by eye.

Outputs (in this folder):
  candidates.json  draft catalogue entries + match info, for triage (never written into catalogue.json)
  candidates.md    the same as a table
  state.json       cid -> status/sources at the last run; the next run reports what is new or changed
  snapshot.json    the raw API rows (git-ignored)

It also lists Cryptoole rows now marked solved or partly solved that share an R-number with an
open catalogue.json entry: the "check prior solutions first" rule, run automatically.

Usage:  python research/cryptoole/pull.py [--offline]   (--offline reuses snapshot.json)

API terms: free, CORS, no key; cite each item's own source (kept in 'url' and 'source' below);
page with limit=200 and do not flood the server.
"""
import argparse
import datetime
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
API = 'https://cryptoole.satoru.net/api.cgi'
UA = 'cyphersolver-catalogue-puller (https://dbourdeau.github.io/cyphersolver/)'
PAGE = 200
PAUSE = 1.5  # seconds between pages

sys.path.insert(0, str(ROOT / 'docs'))
from _check_writeup import FAMOUS  # noqa: E402

FAMOUS_WORDS = FAMOUS | {'z408', 'z32', 'rohonc', 'shugborough', 'somerton', 'tamam shud',
                         'linear a', 'phaistos', 'beale', 'voynich', 'dorabella', 'kryptos'}

LANG = {'pt': 'Portuguese', 'el': 'Greek', 'fr': 'French', 'it': 'Italian', 'es': 'Spanish',
        'en': 'English', 'de': 'German', 'la': 'Latin', 'nl': 'Dutch', 'sv': 'Swedish',
        'pl': 'Polish', 'hu': 'Hungarian', 'ja': 'Japanese'}
REGION = {'fr': 'France', 'it': 'Italy', 'es': 'Spain', 'gb': 'England', 'de': 'Germany',
          'nl': 'Low Countries', 'sc': 'Scandinavia', 'us': 'Other', 'as': 'Other', 'ot': 'Other'}
PERIODS = [(1496, '15th century'), (1559, '1497-1559'), (1589, '1560-1589'), (1598, '1589-1598'),
           (1610, '1598-1610'), (1650, '1611-1650'), (1700, '1651-1700'), (1800, '1701-1800'),
           (1900, '1801-1900')]

# Where to look for what we already hold. 'strong' = the catalogue, ledgers and targets;
# 'harvest' = research/ sweeps (looked at, not necessarily catalogued).
STRONG = ['catalogue.json', 'SOLVED_CATALOGUE.md', 'SOLVED_RANKING.md', 'README.md', 'CATALOGUE.md',
          'targets/**/NOTES.md', 'targets/**/profile.json', 'targets/**/*.md']
HARVEST = ['research/**/*.md', 'research/**/*.json']
R_RE = re.compile(r'\bR ?(\d{1,5})\b')
CID_RE = re.compile(r'\b[A-Z]{2}1[3-9][0-9X]{2}-\d+\b')


def fetch_all():
    rows, offset = [], 0
    while True:
        q = urllib.parse.urlencode({'type': 'cipher', 'offset': offset, 'limit': PAGE, 'sort': 'date'})
        req = urllib.request.Request(f'{API}?{q}', headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        rows += d['items']
        offset += PAGE
        print(f'  fetched {len(rows)}/{d["total"]}', file=sys.stderr)
        if offset >= d['total']:
            return rows
        time.sleep(PAUSE)


def r_numbers(row):
    """DECODE R-numbers of a row and its group members."""
    out = {s['id'] for s in row.get('source_ids') or [] if s['source'] == 'decode'}
    for m in row.get('group_members') or []:
        if m['id'].startswith('decode:'):
            out.add('R' + m['id'].split(':', 1)[1])
    return {x if x.startswith('R') else 'R' + x for x in out}


def scan(patterns, skip):
    """Map R-number / Cryptoole ID -> set of repo files mentioning it."""
    hits = {}
    for pat in patterns:
        for p in ROOT.glob(pat):
            if not p.is_file() or HERE in p.parents or p.stat().st_size > 20_000_000:
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel in skip:
                continue
            try:
                text = p.read_text(encoding='utf-8', errors='ignore')
            except OSError:
                continue
            for n in R_RE.findall(text):
                hits.setdefault('R' + n, set()).add(rel)
            for c in CID_RE.findall(text):
                hits.setdefault(c, set()).add(rel)
    return hits


def year_of(row):
    m = re.match(r'(\d{4})', row.get('date_sort') or '')
    return int(m.group(1)) if m and m.group(1) != '0000' else None


def period(y):
    if y is None:
        return 'unknown'
    for top, name in PERIODS:
        if y <= top:
            return name
    return 'unknown'


def is_famous(row):
    t = (row.get('title_en') or '').lower() + ' ' + (row.get('details_en') or '').lower()
    return any(re.search(r'\b' + re.escape(w.replace('_', ' ')) + r'\b', t) for w in FAMOUS_WORDS)


def shelfmark(row):
    """details_en is 'shelfmark · language · region'; only DECODE/Rosson rows lead with a shelfmark."""
    first = (row.get('details_en') or '').split(' · ')[0]
    if re.match(r'(Solved|Partly solved|Key found)\b', first) or '(inferred' in first:
        return ''
    return first


def source_label(row):
    names = {'decode': 'DECODE', 'cryptiana': 'Cryptiana', 'rosson': 'Rosson cipher-readings'}
    return 'Cryptoole (' + ', '.join(names.get(s, s) for s in row['sources']) + ')'


def draft(row):
    y = year_of(row)
    langs = [LANG.get(c, c) for c in row.get('languages') or []]
    region = REGION.get(row.get('region'), 'Other')
    blob = (row.get('title_en', '') + row.get('details_en', '')).lower()
    if region == 'Italy' and any(w in blob for w in ('vatican', 'papal', 'nunzia', 'segreteria')):
        region = 'Papacy'
    status = {'partly': 'partly solved', 'key_only': 'key found, text unread'}.get(row.get('status_detail'), 'open')
    return {
        'id': None,  # assigned when the entry is accepted into catalogue.json (ids are never reused)
        'counted': False,
        'year': y,
        'date': row.get('date_en') or 'unknown',
        'title': row.get('title_en') or row.get('title_ja'),
        'correspondents': '',
        'place': '',
        'language': ', '.join(langs) or 'unknown',
        'region': region,
        'period': period(y),
        'shelfmark': shelfmark(row),
        'ark': '',
        'folio_note': '',
        'cls': None,
        'seen': 'catalogue',
        'source': source_label(row),
        'status': f"Cryptoole {row['cid']} ({status}): {row.get('details_en', '')}",
        'why': '',
        'importance': None, 'solvability': None, 'difficulty': None,
        'verify': f"View the leaves at {row['url']} (Cryptoole {row['case_page']}).",
        'cryptoole': {'cid': row['cid'], 'id': row['id'], 'url': row['url'], 'case_page': row['case_page'],
                      'sources': row['sources'], 'r_numbers': sorted(r_numbers(row), key=lambda r: int(r[1:])),
                      'members': len(row.get('group_members') or [])},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--offline', action='store_true', help='reuse snapshot.json instead of calling the API')
    args = ap.parse_args()

    snap = HERE / 'snapshot.json'
    if args.offline:
        rows = json.loads(snap.read_text(encoding='utf-8'))
    else:
        rows = fetch_all()
        snap.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')

    strong = scan(STRONG, skip=set())
    harvest = scan(HARVEST, skip=set())

    # 1. Candidates
    kept, dropped = [], {'ours': 0, 'cryptocellar': 0, 'not open': 0, 'after 1950': 0, 'famous': 0}
    for row in rows:
        y = year_of(row)
        if 'cyphersolver' in row['sources']:
            dropped['ours'] += 1
        elif 'cryptocellar' in row['sources'] or re.search(r'\b(enigma|cryptocellar)\b', row['title_en'] or '', re.I):
            dropped['cryptocellar'] += 1
        elif row['status'] != 'open':
            dropped['not open'] += 1
        elif y and y > 1950:
            dropped['after 1950'] += 1
        elif is_famous(row):
            dropped['famous'] += 1
        else:
            d = draft(row)
            keys = d['cryptoole']['r_numbers'] + [row['cid']]
            d['match'] = {
                'known': {k: sorted(strong[k])[:5] for k in keys if k in strong},
                'harvested': {k: sorted(harvest[k])[:5] for k in keys if k in harvest and k not in strong},
            }
            kept.append(d)
    kept.sort(key=lambda d: (bool(d['match']['known']), d['year'] or 9999))

    # 2. Solved elsewhere: Cryptoole rows (not ours) marked solved/partly that share an R-number
    #    with an entry still open in catalogue.json.
    cat = json.loads((ROOT / 'catalogue.json').read_text(encoding='utf-8'))['entries']
    open_r = {}
    for e in cat:
        for n in R_RE.findall(json.dumps(e, ensure_ascii=False)):
            open_r.setdefault('R' + n, set()).add(e['id'])
    # 'Partly' is left out: on merged rows it is usually our own partial reading reflected back.
    alerts = []
    for row in rows:
        if row['status'] != 'solved' or row['sources'] == ['cyphersolver']:
            continue
        shared = sorted((r for r in r_numbers(row) if r in open_r), key=lambda r: int(r[1:]))
        if shared:
            alerts.append({'catalogue_ids': sorted({i for r in shared for i in open_r[r]}), 'r': shared,
                           'cid': row['cid'], 'sources': row['sources'],
                           'status': row['status'] + (f"/{row['status_detail']}" if row.get('status_detail') else ''),
                           'title': row['title_en'], 'details': row['details_en'], 'url': row['url']})

    # 3. Changes since the last run
    state_p = HERE / 'state.json'
    old = json.loads(state_p.read_text(encoding='utf-8'))['rows'] if state_p.exists() else {}
    new = {r['cid']: {'status': r['status'] + (f"/{r['status_detail']}" if r.get('status_detail') else ''),
                      'sources': r['sources'], 'title': r['title_en']} for r in rows}
    added = [c for c in new if c not in old] if old else []
    changed = [(c, old[c]['status'], new[c]['status']) for c in new if c in old and old[c]['status'] != new[c]['status']]
    today = datetime.date.today().isoformat()
    state_p.write_text(json.dumps({'pulled': today, 'rows': new}, ensure_ascii=False, indent=1, sort_keys=True),
                       encoding='utf-8')

    (HERE / 'candidates.json').write_text(json.dumps(
        {'_about': 'Draft catalogue.json entries from Cryptoole (research/cryptoole/pull.py). Not catalogued: '
                   'score, class and view each one before moving it into catalogue.json. Cite each item\'s '
                   'own source (url) and credit Cryptoole (satoru.net).',
         'pulled': today, 'dropped': dropped, 'alerts': alerts, 'candidates': kept},
        ensure_ascii=False, indent=1), encoding='utf-8')
    write_md(kept, alerts, dropped, today)

    print(f'{len(rows)} Cryptoole cipher rows; {len(kept)} candidates '
          f'({sum(1 for d in kept if d["match"]["known"])} already mentioned in the repo); dropped {dropped}')
    if old:
        print(f'since last run: {len(added)} new rows, {len(changed)} status changes')
        for c, a, b in changed:
            print(f'  {c}: {a} -> {b}  {new[c]["title"]}')
    for a in alerts:
        print(f'ALERT catalogue {a["catalogue_ids"]} shares {", ".join(a["r"])} with {a["cid"]} ({a["status"]}): {a["title"]}')


def write_md(kept, alerts, dropped, today):
    L = [f'# Cryptoole candidates ({today})', '',
         'Generated by `research/cryptoole/pull.py`; do not edit by hand. Rows open on Cryptoole, not from '
         'our catalogue, CryptoCellar excluded. "Known" = an R-number or Cryptoole ID of the row already '
         'appears in the catalogue, ledgers or targets/; "harvested" = only in research/ sweeps.', '',
         f'Dropped: {", ".join(f"{k} {v}" for k, v in dropped.items())}.', '']
    if alerts:
        L += ['## Solved elsewhere? (shares an R-number with an open catalogue entry)', '',
              '| Catalogue | R | Cryptoole | Status | Title |', '|---|---|---|---|---|']
        L += [f"| {', '.join(map(str, a['catalogue_ids']))} | {', '.join(a['r'])} | [{a['cid']}]({a['url']}) | {a['status']} | "
              f"{a['title']} |" for a in alerts]
        L.append('')
    L += [f'## Candidates ({len(kept)})', '', '| Cryptoole | Year | Title | Source | Shelfmark | R | Already here |',
          '|---|---|---|---|---|---|---|']
    for d in kept:
        c, m = d['cryptoole'], d['match']
        rs = c['r_numbers']
        r = ', '.join(rs[:3]) + (f' +{len(rs) - 3}' if len(rs) > 3 else '')
        here = '; '.join(f'{k}: {", ".join(v[:2])}' for k, v in m['known'].items())
        if m['harvested']:
            here += (' · ' if here else '') + 'harvested: ' + ', '.join(m['harvested'])
        title = (d['title'] or '').replace('|', '/')
        L.append(f"| [{c['cid']}]({c['case_page']}) | {d['year'] or '?'} | [{title}]({c['url']}) | "
                 f"{d['source'][11:-1]} | {d['shelfmark'].replace('|', '/')[:60]} | {r} | {here[:120]} |")
    (HERE / 'candidates.md').write_text('\n'.join(L) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
