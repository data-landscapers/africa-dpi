#!/usr/bin/env python3
"""
Merge the verified rural rows into the main verified DPI file. Run after the
rural batches have been verified and merged into one file. From project root:

    python merge_rural.py

- Reads the target (africa-dpi-verified.csv) to learn its exact column set.
- Conforms the verified rural rows to that schema (missing columns added blank).
- Maps revised_year -> Year where Year is blank, so every rural row ends up dated.
- Appends and writes africa-dpi-verified-merged.csv (does NOT overwrite the input).
"""
import pandas as pd

TARGET = "africa-dpi-verified.csv"        # the main verified file
RURAL  = "data/verified_rural.csv"        # your merged, verified rural rows
OUT    = "africa-dpi-verified-merged.csv"

tgt = pd.read_csv(TARGET, encoding="utf-8-sig", dtype=str).fillna("")
rur = pd.read_csv(RURAL,  encoding="utf-8-sig", dtype=str).fillna("")

# Fill Year from revised_year where the original Year is blank
if "revised_year" in rur.columns:
    blank = rur["Year"].str.strip() == ""
    rur.loc[blank, "Year"] = rur.loc[blank, "revised_year"]
    still = (rur["Year"].str.strip() == "").sum()
    if still:
        print(f"WARNING: {still} rural rows still have no Year after mapping - review these.")

# Conform rural to the target's columns (add any missing as blank, drop extras)
for c in tgt.columns:
    if c not in rur.columns:
        rur[c] = ""
extra = [c for c in rur.columns if c not in tgt.columns]
if extra:
    print(f"Note: dropping rural-only columns not in target: {extra}")
rur = rur[tgt.columns]

merged = pd.concat([tgt, rur], ignore_index=True)
merged.to_csv(OUT, index=False, encoding="utf-8-sig")
print(f"Target rows: {len(tgt)} | rural rows added: {len(rur)} | total: {len(merged)}")
print(f"Wrote {OUT}. Original {TARGET} left untouched.")
