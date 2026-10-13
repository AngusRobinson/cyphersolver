# Châtillon → Servien, 3 août 1635, BnF Français 3758 — Châtillon, 3 August 1635

Status: no write-up (result by George Lasry, summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 10/10 pages transcribed; 4/4 cipher pages deciphered
- Ciphertext-only: No
- Sender: Châtillon
- Recipient: Servien
- Date: 3 août 1635
- Key: 78 signs: 56 letter signs, 20 in nomenclature, 2 repeat controls.
- Ciphertext: 666 written positions, 624 identified (93.7%); one group boundary uncertain.
- Contents: Châtillon criticizes the army’s condition and discusses withdrawal across the Rhine for greater safety.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3758 — Châtillon, 3 August 1635
Contents: Châtillon criticizes the army’s condition and discusses withdrawal across the Rhine for greater
safety.
10/10 pages transcribed; 4/4 cipher pages deciphered
Ciphertext-only: No
Sender: Châtillon
Recipient: Servien
Year: 3 août 1635
Key: 78 signs: 56 letter signs, 20 in nomenclature, 2 repeat controls.
Ciphertext: 666 written positions, 624 identified (93.7%); one group boundary uncertain.
Plaintext in another folio of the same volume: Plaintext in the same volume: f123v for f124r; f126r
for f126v–127r; f127r for f127v.

Excerpt and Translation
Excerpt
f127v, cipher continuation
Cette consideration les pourra empescher de s’engager si avant, mais Je Vous respon que nous
ne jouons point de ruse cete fois, mais nous passons le Rhin pour nostre plus grande seurete
afin d’avoir se grand fleuve entre les ennemis et nous.
Translation
This consideration may prevent them from advancing so far; but I assure you that we are playing no trick this
time. We cross the Rhine for our greater safety, in order to have this great river between the enemy and
ourselves.
```

## Links

- No link in the report.

## Images

- `lasry_p087_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p086_1.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: none (no Gallica link in dossier; fr. 3758 ark not found offline, gallica.bnf.fr behind Cloudflare)
- Folio matches the report: unclear; cipher present: yes
- What we checked: his f127v crop: clear "mais Je Vous respon que" then 95(nous)...46(ennemi)...33(de)... codes consistent with his table, but sign-level read of 8+ symbols from the small crop was not reliable
- Verdict: **partly confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Plaintext of the same letters elsewhere in the volume (f123v, f126r, f127r). 93.7% identified. Repo CATALOGUE lists Chatillon-Servien fr. 3758 nos.100,104 (ark btv1b9059471x?).

## Notes and corrections

Fr. 3758 is also part of [targets/rohan1636](../rohan1636/NOTES.md).
