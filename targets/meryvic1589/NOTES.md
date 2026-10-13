# Méry de Vic → Henri IV, 28 August 1589, BnF Dupuy 61 — Méry de Vic, f43r

Status: no write-up (result by George Lasry, summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 6/6 pages transcribed; Partly deciphered
- Ciphertext-only: Yes
- Sender: Méry de Vic
- Recipient: Henri IV
- Date: 28 August 1589
- Key: 81 symbols: 50 alphabet signs, 8 nomenclature signs, 3 nulls, 20 unidentified types
- Ciphertext: 545 elements, 523 identified (96.0%)
- Contents: Méry de Vic writes after the assassination of Henri III and the accession of Henri IV. The opening cleartext reports the arrival of the news and local allegiances. The cipher reports troops near Limoges and divided loyalties; later cleartext discusses expenses, elections, intercepted dispatches and cannon for rebel forts.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Dupuy 61 — Méry de Vic, f43r
Contents: Méry de Vic writes after the assassination of Henri III and the accession of Henri IV. The opening
cleartext reports the arrival of the news and local allegiances. The cipher reports troops near Limoges and
divided loyalties; later cleartext discusses expenses, elections, intercepted dispatches and cannon for rebel
forts.
6/6 pages transcribed; Partly deciphered
Ciphertext-only: Yes
Sender: Méry de Vic
Recipient: Henri IV
Year: 28 August 1589
Key: 81 symbols: 50 alphabet signs, 8 nomenclature signs, 3 nulls, 20 unidentified types
Ciphertext: 545 elements, 523 identified (96.0%)
Gallica f40r
Gallica f43r
Ciphertext-only

Excerpt and Translation
Excerpt
f43r
? assembler à huict lieues de ceste ville. Leur troupe ? au plus de douze cents hommes? de
pied? et deux cents chevaux et doivent meiner deux ou trois pieces.
Translation
? to assemble eight leagues from this town. Their force ? at most twelve hundred men? on foot? and two
hundred horsemen, and they must bring two or three guns.
Excerpt
f43r
? qui avoit tenu le feu Roy en esperance de le servir, s’est déclaré comme plusieurs du ? m’ont
asseuré. Il ? amas d’homes et se delibere de
Translation
?, who had kept the late King hoping to serve him, has declared himself, as several of ? have assured me. He
? a gathering of men and intends to
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b103164206/f89.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b103164206/f95.item>

## Images

- `lasry_p004_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p005_2.png, p005_3.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b103164206/f95.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f43r: cleartext opening (Pompadour, Clermont Vertillac) + cipher block match his description; clear words between cipher runs read "...= roy q2 change come on ma asseure ... assemble aussi" whereas his excerpt gives "s est declare comme plusieurs du ? m ont asseure"; symbol-level decode not completed
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: Excerpt clear-text words do not exactly match the MS clear words (change come on ma asseure); 96% identified, status Partly deciphered; worth rechecking that excerpt line.

## Notes and corrections

One excerpt line disagrees with the manuscript. Lasry gives "s'est déclaré comme plusieurs du ? m'ont asseuré"; the clear words on f43r read "… roy q2 change come on ma asseure". The other clear words and the cipher block match. That line should be checked again.
