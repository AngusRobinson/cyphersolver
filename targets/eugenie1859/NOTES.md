# Napoleon III / Empress Eugénie (both directions) → Empress Eugénie / Napoleon III (both directions), June 1859, BnF NAF 11355 — Emperor–Empress code

Status: no write-up (result by George Lasry, summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
- Ciphertext-only: Yes
- Sender: Napoleon III / Empress Eugénie (both directions)
- Recipient: Empress Eugénie / Napoleon III (both directions)
- Date: June 1859
- Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
- Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
- Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the Italian campaign; private family news exchanged with Empress Eugénie.
- Method category (our classification): key recovered from ciphertext-only; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
NAF 11355 — Emperor–Empress code
Contents: Napoleon III’s policy toward the Pope, his criticism of diplomatic speculation, and reports from the
Italian campaign; private family news exchanged with Empress Eugénie.
15/15 pages transcribed; 9/11 cipher pages deciphered; 2 more in part
Ciphertext-only: Yes
Sender: Napoleon III / Empress Eugénie (both directions)
Recipient: Empress Eugénie / Napoleon III (both directions)
Year: June 1859
Key: 233 codes, 12 letter signs, 220 in nomenclature, 1 separator
Ciphertext: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?
Literal plaintext: f35r: L’ennemi s’est retiré cette nuit. — One ciphered sentence only; fatigue passage not
printed. · L’Écho saumurois, 28 June 1859, p. 1 ·
Gallica ff3r–5r
Gallica f9r
Gallica ff14r–15r
Gallica ff17r–19r
Gallica f27r
Gallica ff29r–30r
Gallica ff32r–35r

Excerpt and Translation
Excerpt
f19r — the Pope and diplomacy
Je suis bien peiné au milieu de mes travaux d’avoir à répondre à toutes les sotte[s] suppositions de
la diplomatie. Je maintiens le pape à Rome avec mon armée. Je ne me mêle en rien du reste de
ses États.
Translation
I am very distressed, amid my work, to have to answer all the foolish suppositions of diplomacy. I keep the
Pope in Rome with my army. I do not interfere in any way with the rest of his States.

Excerpt
f35r — the battle and the Austrian emperor’s room
Impossible de donner des détails sur la bataille d’hier. Tout [le] monde était mort de fatigue. L’ennemi
s’est retiré cette nuit. J’ignore le nombre précis de canons, de drapeaux et de prisonniers. J’ai couché
cette nuit dans la chambre où l’Empereur d’Autriche a déjeuné hier matin. Niel est nommé Maréchal. La
bataille prendra le nom de Solférino.
Translation
It is impossible to give details of yesterday’s battle. Everyone was dead tired; the enemy withdrew during the
night. I do not know the exact number of cannon, flags and prisoners. I slept last night in the room where the
Emperor of Austria had breakfast yesterday morning. Niel has been appointed Marshal. The battle will be
named Solferino.

Excerpt
f27r — Eugénie’s message
Je suis désolée de vous avoir fait de la peine, ce n’était? pas mon intention. Ne vous inquiétez
pas du petit, il va à merveille. J’écris aujourd’hui par la poste.
Translation
I am sorry to have caused you sorrow; that was not? my intention. Do not worry about the little one; he is
doing wonderfully. I am writing today by post.
```

## Links

- <https://archives.ville-saumur.fr/_depot_amsaumur/_depot_arko/fonds/echo_saumurois/pdf/1859/FRAC049328_ECHSAU_1859_06_28.pdf>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f11.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f23.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f33.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f39.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f57.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f61.item>
- <https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item>

## Images

- `lasry_p027_2.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p026_1.png, p028_3.png, p029_4.png, p030_5.png.

## Spot-check (13 Oct 2026)

- Batch A. Image checked: https://gallica.bnf.fr/ark:/12148/btv1b52517729k/f67.item
- Folio matches the report: yes; cipher present: yes
- What we checked: f32r = Solferino telegram "Cavriana 24 juin 1859, Empereur a Imperatrice", clear text + code "941 325 274 1155 / 163 1142 1162"; his key gives 274=connais, 163=ble, 1142=s (fragmentary, no excerpt covers this run); f19r/f35r excerpts not image-checked
- Verdict: **partly confirmed** (method key recovered from ciphertext-only, extent partial). The check is a sample, not a re-solution.
- Notes: 84.1% identified, 50 ?; 2 cipher pages only in part. Telegrams of 1859 were partly printed in the press (he cites L Echo saumurois 28 June 1859) - external plaintext available for f35r.
