import csv
import pathlib
import re

src = pathlib.Path(r"C:\Users\bill\Dropbox\Github\africa-dpi\manual\docs\csvs\digital-pay-metadata.csv")
out = pathlib.Path(r"C:\Users\bill\Dropbox\Github\africa-dpi\manual\docs\csvs\digital-pay-metadata.md")

def clean(text):
    if text is None:
        return ""
    s = str(text).strip()
    s = s.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.replace("|", "\\|")

with src.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames or []
    rows = list(reader)

lines = [
    "# Digital payment metadata",
    "",
    "Variable definitions and collection guidance for the digital payment module.",
    "",
]

last_section = None
for row in rows:
    section = clean(row.get("Section", ""))
    var_name = clean(row.get("Variable Name", ""))

    if section != last_section:
        lines.append(f"## {section}")
        lines.append("")
        last_section = section

    lines.append(f"### {var_name}")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")

    for h in fieldnames:
        if h in {"Section", "Variable Name"}:
            continue
        lines.append(f"| {clean(h)} | {clean(row.get(h, ''))} |")

    lines.append("")

out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"Wrote {len(rows)} entries to {out}")
