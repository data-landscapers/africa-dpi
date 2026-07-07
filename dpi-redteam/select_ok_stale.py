#!/usr/bin/env python3
"""
Select OK-priority rows dated before 2024 and write them as batch files for the
dpi-verifier subagent. Everything else (recent OK rows, already-verified rows) is
skipped. Run from the project root:

    python select_ok_stale.py

Output: data/batches_ok_stale/<chapter>__<country>.csv
Point SRC at whatever file currently holds your latest merged data.
"""
import pandas as pd, os, re

SRC = "africa-dpi-verified.csv"   # your current working/merged file
OUT = "data/batches_ok_stale"
CUTOFF = 2024                      # keep rows with Year strictly before this
os.makedirs(OUT, exist_ok=True)

d = pd.read_csv(SRC, encoding="utf-8-sig", dtype=str).fillna("")
year = pd.to_numeric(d["Year"], errors="coerce")

mask = (d["redteam_priority"] == "OK") & (year < CUTOFF)
# idempotent: skip anything already verified in a previous run
if "revised_value_code" in d.columns:
    mask &= (d["revised_value_code"].str.strip() == "")

sel = d[mask].copy()
print(f"Source rows: {len(d)}")
print(f"OK & Year < {CUTOFF} & not yet verified: {len(sel)}")

def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

n = 0
manifest = []
for (chapter, country), grp in sel.groupby(["Chapter", "Country"], sort=True):
    fname = f"{slug(chapter)}__{country}.csv"
    grp.to_csv(os.path.join(OUT, fname), index=False, encoding="utf-8-sig")
    manifest.append((chapter, country, len(grp), fname))
    n += 1

pd.DataFrame(manifest, columns=["chapter","country","rows","file"]).to_csv(
    "data/ok_stale_manifest.csv", index=False)
print(f"Wrote {n} batch files to {OUT}/  (see data/ok_stale_manifest.csv)")
if len(sel):
    print("\nOldest rows in the selection:")
    print(sel.assign(_y=year[mask]).nsmallest(5, "_y")[
        ["Country","Chapter","Variable Name","Year"]].to_string(index=False))
