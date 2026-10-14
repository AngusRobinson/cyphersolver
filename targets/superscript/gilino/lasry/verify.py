#!/usr/bin/env python3
"""Validate this static Gilino contribution with the Python standard library."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_text(name):
    raw = (ROOT / name).read_bytes()
    require(not raw.startswith(b"\xef\xbb\xbf"), f"{name}: UTF-8 BOM")
    text = raw.decode("utf-8")
    require("\r" not in text, f"{name}: expected LF newlines")
    require(all(line == line.rstrip() for line in text.splitlines()),
            f"{name}: trailing whitespace")
    require(not re.search(r"(?<![A-Za-z])[A-Za-z]:[\\/]|file:///", text),
            f"{name}: local absolute path")
    return text


def collect_counts():
    document = json.loads(read_text("key.json"))
    key = document["key"]
    rows = list(csv.DictReader(io.StringIO(read_text("alignment.tsv")), delimiter="\t"))
    transcribed_rows = []
    for line in read_text("transcription.txt").splitlines():
        match = re.fullmatch(r"(P[0-9]+\.C[0-9]+)\t(.+)", line)
        if match:
            transcribed_rows.append((match[1], match[2]))
    require(transcribed_rows == [(r["line_id"], r["cipher_groups"]) for r in rows],
            "transcription and alignment differ")
    require(len({r["line_id"] for r in rows}) == len(rows), "duplicate line ID")
    frequencies = Counter()
    doubtful = Counter()
    pages = {}
    encountered_order = []
    for row in rows:
        tokens = row["cipher_groups"].split(";")
        values = row["aligned_values_nulls_retained"].split(";")
        require(len(tokens) == len(values), f"{row['line_id']}: unequal token/value counts")
        match = re.fullmatch(r"P([0-9]+)\.C([0-9]+)", row["line_id"])
        require(match is not None, "malformed line ID")
        photo = int(match[1])
        if not encountered_order or photo != encountered_order[-1]:
            encountered_order.append(photo)
        page = pages.setdefault(str(photo), {"lines": 0, "transcribed_tokens": 0,
                                            "cipher_tokens": 0, "inline_cleartext_tokens": 0})
        page["lines"] += 1
        require(int(match[2]) == page["lines"], f"P{photo}: nonsequential line IDs")
        for index, (token, actual) in enumerate(zip(tokens, values), 1):
            canonical = token.rstrip("?")
            require(canonical in key, f"{row['line_id']}:{index}: missing {canonical}")
            entry = key[canonical]
            frequencies[canonical] += 1
            page["transcribed_tokens"] += 1
            if entry.get("kind") == "cleartext":
                page["inline_cleartext_tokens"] += 1
            else:
                page["cipher_tokens"] += 1
            expected = entry["value"]
            if token.endswith("?"):
                doubtful[canonical] += 1
            if expected == "":
                expected = "[null?]" if token.endswith("?") else "∅"
            elif token.endswith("?") and not expected.endswith(("?", "?]")):
                expected += "?"
            require(actual == expected,
                    f"{row['line_id']}:{index}: {token}: {actual!r} != {expected!r}")
    require(encountered_order == document["reading_order"], "unexpected photo order")
    require(set(frequencies) == set(key), "key and corpus labels differ")
    for name, entry in key.items():
        require(frequencies[name] == entry["count"], f"{name}: key frequency mismatch")
        require(doubtful[name] == entry["doubtful_glyph_occurrences"],
                f"{name}: doubtful-glyph frequency mismatch")
    clear = sorted(name for name, entry in key.items() if entry.get("kind") == "cleartext")
    nulls = sorted(name for name, entry in key.items() if entry["value"] == "")
    tentative = sorted(name for name, entry in key.items() if entry["value"].endswith("?"))
    separators = sorted(name for name, entry in key.items() if entry["status"] == "possible separator")
    def category(names):
        return {"label_count": len(names), "token_count": sum(frequencies[n] for n in names),
                "labels": {n: frequencies[n] for n in names}}
    return {
        "scope": "Assignment and transcription counts, not plaintext accuracy. Uncertainty categories may overlap.",
        "cipher_line_count": len(rows),
        "total_transcribed_tokens": sum(frequencies.values()),
        "cipher_tokens": sum(frequencies.values()) - sum(frequencies[n] for n in clear),
        "canonical_transcription_labels": len(frequencies),
        "cipher_labels": len(frequencies) - len(clear),
        "inline_cleartext": category(clear),
        "presumed_nulls": category(nulls),
        "tentative_values": category(tentative),
        "possible_separators": category(separators),
        "doubtful_glyphs": {"token_count": sum(doubtful.values()),
                            "labels": {n: doubtful[n] for n in sorted(doubtful)}},
        "unassigned_cipher_labels": [],
        "reading_order": encountered_order,
        "pages": pages,
    }


def main():
    observed = collect_counts()
    recorded = json.loads(read_text("counts.json"))
    require(observed == recorded, "counts.json differs from recomputed counts")
    sources = json.loads(read_text("source.json"))
    for item in sources["artifact_sources"]:
        name = item["bundled_name"]
        read_text(name)
        digest = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        require(digest == item["bundled_sha256"], f"{name}: bundled SHA-256 mismatch")
    read_text("NOTES.md")
    print(json.dumps({"status": "ok", "cipher_lines": observed["cipher_line_count"],
                      "transcribed_tokens": observed["total_transcribed_tokens"],
                      "cipher_tokens": observed["cipher_tokens"],
                      "cipher_labels": observed["cipher_labels"],
                      "inline_cleartext_tokens": observed["inline_cleartext"]["token_count"],
                      "doubtful_glyph_tokens": observed["doubtful_glyphs"]["token_count"]}, indent=2))


if __name__ == "__main__":
    main()
