# Cryptoole candidates

[Cryptoole](https://cryptoole.satoru.net/) is Satoru's open index of historical cipher records. It merges DECODE,
Cryptiana (Tomokiyo), CryptoCellar (Weierud), Rosson's cipher-readings and our own `catalogue.json` (source
`cyphersolver`), and serves them through a free JSON API ([api.html](https://cryptoole.satoru.net/api.html)).
`pull.py` uses it as a feed of catalogue candidates.

```bash
PYTHONUTF8=1 python research/cryptoole/pull.py
```

Re-run with `--offline` to rebuild the outputs from `snapshot.json` without calling the API.

## What it keeps

Rows of type `cipher`, open on Cryptoole (including partly solved and key-only), not already from us, dated 1950 or
earlier, and not a famous cipher (`FAMOUS` in `docs/_check_writeup.py`). CryptoCellar rows and every other Enigma
message are dropped as outside the paper's scope.

Each candidate's DECODE R-numbers (its own and its group members') and its Cryptoole ID are looked up in the repository:

- **known**: found in `catalogue.json`, the ledgers, the README or `targets/`. Probably a duplicate or a finished
  target; check before adding.
- **harvested**: found only in `research/` sweeps. Looked at before, never catalogued.

Cryptiana and Rosson rows have no R-numbers, so they get no automatic match. Check those by title.

## Outputs

| File | What |
|---|---|
| `candidates.md` | the table to triage, unmatched rows first, by date |
| `candidates.json` | draft `catalogue.json` entries (fields filled from Cryptoole; `id`, `cls` and the three scores left empty) plus a `cryptoole` block with the IDs, and the match info |
| `state.json` | Cryptoole ID → status and sources at the last pull; the next run prints new rows and status changes |
| `snapshot.json` | raw API rows (git-ignored) |

The run also prints **alerts**: rows that Cryptoole marks solved and that share an R-number with an entry still open
in `catalogue.json`. This applies the check-prior-solutions rule automatically. Partly-solved rows are not alerted,
because on merged rows that status is usually our own partial reading reflected back.

## Adding a candidate to the catalogue

Candidates never go into `catalogue.json` automatically. For each one: view the leaves (`verify` holds the source
link), give it the next unused `id`, set `cls`, `seen` and the three scores, write `why`, delete the `cryptoole` and
`match` blocks, keep `source: "Cryptoole (…)"` and the Cryptoole ID in `status`, then regenerate the page.

## Terms

The API is free, needs no key and allows cross-origin calls. Cite each item's own source (the `url`, DECODE, Cryptiana …)
and credit "Cryptoole (satoru.net)". The script fetches 200 rows per page with a pause between pages. DECODE images
are not part of the API.
