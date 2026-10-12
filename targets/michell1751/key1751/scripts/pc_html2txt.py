"""Plain text of a Politische Correspondenz volume from the Trier digital edition, for circular.py.

Save the page https://friedrich.uni-trier.de/de/politKorr/<vol>/text/ (vol 8 and 9) as HTML, then
usage: python scripts/pc_html2txt.py <saved.html> <out.txt>
Footnote reference numbers are dropped; block elements become line breaks; page numbers stay as <NNN>."""
import re, sys, html

h = open(sys.argv[1], encoding='utf8', errors='replace').read()
h = re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<!--.*?-->', '', h)
h = re.sub(r'<span class="noteRef">[^<]*</span>', '', h)
h = re.sub(r'(?i)<(br|/p|/h\d|/div|/li|/tr|/td|/table|/ul)\b[^>]*>', '\n', h)
h = re.sub(r'<[^>]+>', '', h)
open(sys.argv[2], 'w', encoding='utf8').write(html.unescape(h))
