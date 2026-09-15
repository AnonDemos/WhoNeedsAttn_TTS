#!/usr/bin/env python3
"""Generates index.md's sample table from texts.tsv.
Re-run this after adding/editing samples in texts.tsv.
"""
import csv

MODELS = [
    ("conv", "Conv"),
    ("lstm", "LSTM"),
    ("mamba-attn", "Mamba-Attn"),
    ("mamba-mamba", "Mamba-Mamba"),
    ("transformer", "Transformer"),
]

with open("texts.tsv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
    rows = list(reader)

header_cells = "".join(f"<th>{name}</th>" for _, name in MODELS)
thead = f"<tr>\n                <th>#</th>\n                <th>Text</th>\n                {header_cells}\n            </tr>"

body_rows = []
for row in rows:
    sample = row["sample"]
    text = (
        row["text"]
        .replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    cells = []
    for folder, _ in MODELS:
        cells.append(
            f'<td><audio controls preload="none"><source src="resources/audios/{folder}/{sample}.wav" '
            f'type="audio/wav">Your browser does not support the audio element.</audio></td>'
        )
    cells_html = "\n                    ".join(cells)
    body_rows.append(
        f"""                <tr>
                    <td>{sample}</td>
                    <td class="text-cell">{text}</td>
                    {cells_html}
                </tr>"""
    )

table = f"""    <table>
        <thead>
            {thead}
        </thead>
        <tbody>
{chr(10).join(body_rows)}
        </tbody>
    </table>"""

with open("_table_include.html", "w", encoding="utf-8") as f:
    f.write(table)

print(f"Wrote table with {len(rows)} rows and {len(MODELS)} model columns to _table_include.html")
