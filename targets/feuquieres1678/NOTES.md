# Louis XIV → Marquis de Feuquières, 9 December 1678, BnF NAF 22738

Status: no write-up (result by George Lasry, summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 4/4 pages transcribed; 4/4 pages deciphered in part
- Ciphertext-only: No
- Sender: Louis XIV
- Recipient: Marquis de Feuquières
- Date: 9 December 1678
- Key: 67 codes: 18 letter signs, 49 in nomenclature
- Ciphertext: 1,920 elements, 1,169 identified (60.9%)
- Contents: Louis XIV's instructions to Feuquières discuss Sweden's military plans and the risk of sending a fleet into the Baltic.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
NAF 22738
Contents: Louis XIV's instructions to Feuquières discuss Sweden's military plans and the risk of sending a
fleet into the Baltic.
4/4 pages transcribed; 4/4 pages deciphered in part
Ciphertext-only: No
Sender: Louis XIV
Recipient: Marquis de Feuquières
Year: 9 December 1678
Key: 67 codes: 18 letter signs, 49 in nomenclature
Ciphertext: 1,920 elements, 1,169 identified (60.9%)
Interlinear plaintext: Interlinear plaintext on ff156r–157v.
Plaintext in the margin or below: Marginal plaintext on f157r.
Gallica ff156r–157v

Excerpt and Translation
Excerpt
f156r, lines6–8
pouvoir reduire entierement les ennemis de la Suede par la force, que je crois important de
profiter des dispositions où ils paroissent de s’accommoder avec cette Couronne,
Translation
to overcome Sweden’s enemies completely by force; I consider it important to take advantage of their
apparent willingness to reach an accommodation with that Crown.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b10027843q/f294.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10027843q/f294/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p097_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p098_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10027843q/f294/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f156r lines 6-8: contemporary interlinear "pouvoir reduire entierement les Ennemis de la Suede par la force, que je crois important de profiter des dispositions ou ils paroissent de saccommoder avec cette Couronne" = his excerpt; docket "Louis XIV a M. le marquis de Feuquieres ... 9 xbre 1678"
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Full interlinear decipherment on the pages, yet only 60.9% of number codes mapped in his key; the text itself is fully read from the interlinear.

## Notes and corrections

A different item from [targets/feuquieres](../feuquieres/NOTES.md).
