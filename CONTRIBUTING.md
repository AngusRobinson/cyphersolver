# Contributing

This repository is a shared ledger of historical ciphers: what has been deciphered, by whom, and how. The site is
<https://dbourdeau.github.io/cyphersolver/>; the page for contributors is
[contribute.html](https://dbourdeau.github.io/cyphersolver/contribute.html), and everyone credited so far is on
[contributors.html](https://dbourdeau.github.io/cyphersolver/contributors.html).

## Four kinds of contribution

| Kind | What to send | Issue form |
|---|---|---|
| A solution to a cipher in the ledger | target, documents covered, key, decipherment against the ciphertext, how the key was obtained, prior publication | [Solution](https://github.com/dbourdeau/cyphersolver/issues/new?template=solution.yml) |
| A new unsolved cipher | archive, shelfmark, folio, image link, date and correspondents if known, what you know of its status | [New cipher](https://github.com/dbourdeau/cyphersolver/issues/new?template=new-cipher.yml) |
| A new cipher with its solution | both of the above; say whether an unpublished result may be shown in full | [New cipher with solution](https://github.com/dbourdeau/cyphersolver/issues/new?template=new-cipher-solved.yml) |
| A verification of a reading here | the passage and images you worked from, where your reading agrees and where it does not | [Verification](https://github.com/dbourdeau/cyphersolver/issues/new?template=verification.yml) |

Not on GitHub? Email dnbourdeau@gmail.com with the same details. The entry is made for you and credited the same way.

## Pull requests

A pull request is welcome for any of the above. The layout is in [README.md](README.md) (Repository layout,
Conventions). In short:

- One folder per target under `targets/<folder>/`, with a `NOTES.md` (what the document is, the system, the key, the
  reading, what is open and why) and the files the work used: transcription, key, decipherment, scripts.
- Large images stay out of git; link them (Gallica, DECODE, the archive's viewer) or describe where they are.
- Leave the generated files alone (`docs/*.html` built by `docs/_build_site.py`, `docs/search.json`,
  `docs/pages.json`, `docs/writeups.html`). They are rebuilt when the contribution is merged.
- Say in the description how you want to be credited (full name, initials or a handle, and a link if you like).

## How credit is recorded

Each target's `profile.json` carries `outcome.credits`: who contributed and in what role (solution, new cipher, new
cipher with solution, verification, key or decipherment used, prior solution, key corrected, transcription,
identification, pointer). The ids are in [contributors.json](contributors.json). `outcome.provenance` says whose result
it is: `project`, `contributed` or `mixed`. The write-up's credits line, the contributors page and the front page's
top contributors are all built from these fields. `docs/_check_profile.py` checks them.

Results contributed from outside are marked as such and are kept out of the figures for the study of how language
models perform against historical ciphers (`docs/_export_profiles.py` leaves out `contributed`, flags `mixed`).

## Tools

Use any tools you like, AI included. Say what you used, and check the reading against the images before sending it.
