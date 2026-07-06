#!/usr/bin/env python3
"""
Split africa-dpi-redteam.csv into small batch files for the dpi-verifier subagent.

Batches are grouped by priority -> chapter -> country so each subagent handles a
coherent, manageable slice (one country's rows within one chapter and priority).
High-priority batches sort first. Run from the project root:

    python split_batches.py

Output: data/batches/<priority>__<chapter>__<country>.csv
"""
import pandas as pd, os, re

SRC = "africa-dpi-redteam.csv"
OUT = "data/batches"
os.makedirs(OUT, exist_ok=True)

d = pd.read_csv(SRC, encoding="utf-8-sig", dtype=str).fillna("")

def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

prio_order = {"High": 0, "Medium": 1, "Low": 2, "OK": 3}
n = 0
manifest = []
for (prio, chapter, country), grp in d.groupby(
    ["redteam_priority", "Chapter", "Country"], sort=False
):
    fname = f"{prio_order.get(prio,9)}_{prio}__{slug(chapter)}__{country}.csv"
    grp.to_csv(os.path.join(OUT, fname), index=False, encoding="utf-8-sig")
    manifest.append((prio, chapter, country, len(grp), fname))
    n += 1

man = pd.DataFrame(manifest, columns=["priority","chapter","country","rows","file"])
man = man.sort_values(["priority","chapter","country"])
man.to_csv("data/batch_manifest.csv", index=False)

print(f"Wrote {n} batch files to {OUT}/")
print(man.groupby("priority")["rows"].agg(["count","sum"]).rename(
    columns={"count":"batches","sum":"rows"}).to_string())
print("\nStart with the High batches (prefix 0_High). See data/batch_manifest.csv.")
