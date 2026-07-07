#!/usr/bin/env python3
"""
Prepare rural_digitalisation.csv for the same verification pipeline as the DPI
data, and write it out as batches. Run from the project root:

    python prep_rural.py

Produces:
  rural-prepped.csv                 normalised, triaged, ready to verify
  data/batches_rural/<country>.csv  one batch per country
Also appends the 4 rural variables to metadata.csv if they are not already there.
"""
import pandas as pd, os, re

SRC   = "rural_digitalisation.csv"
META  = "metadata.csv"
RMETA = "rural_metadata.csv"
OUT   = "data/batches_rural"
os.makedirs(OUT, exist_ok=True)

d = pd.read_csv(SRC, encoding="utf-8-sig", dtype=str).fillna("")

# 1. Rename columns to the canonical (DPI) schema
d = d.rename(columns={
    "Country ISO-3 Code": "Country",
    "Variable":           "Variable Name",
    "Source URLs":        "Source urls",
})

# 2. Derive Variable Id from Section (data column is empty)
section_to_id = {
    "Clinic":   "rural-clinic-status",
    "Police":   "rural-police-status",
    "School":   "rural-school-status",
    "Registry": "rural-registry-status",
}
d["Variable Id"] = d["Section"].map(section_to_id).fillna(d["Variable Id"])
missing = d[d["Variable Id"].str.strip() == ""]
if len(missing):
    print(f"WARNING: {len(missing)} rows have a Section not in the map: "
          f"{sorted(missing['Section'].unique())}")

# 3. Variable Sort — keep if present, else order by section
if (d["Variable Sort"].str.strip() == "").all():
    order = {k: i+1 for i, k in enumerate(section_to_id)}
    d["Variable Sort"] = d["Section"].map(order).astype(str)

# 4. Flatten markdown [title](url) sources to bare URLs (semicolon-separated),
#    matching the DPI Source urls format, then count them.
def flatten_urls(s):
    seen = []
    for u in re.findall(r"https?://[^\s)\]]+", s):
        u = u.rstrip(".,;")               # strip stray trailing punctuation
        if u not in seen:
            seen.append(u)
    return ";".join(seen)
d["Source urls"] = d["Source urls"].apply(flatten_urls)
d["n_sources"]   = d["Source urls"].apply(lambda s: 0 if not s else len(s.split(";")))

# 5. Same structural triage as the DPI red-team (adapted: scale max is 3)
d["_vc"] = pd.to_numeric(d["Value Code"], errors="coerce")
def triage(r):
    fl = []
    if r["n_sources"] == 0:               fl.append("claim_no_source" if r["_vc"] not in (0, None) else "unknown_no_source")
    if r["n_sources"] == 1 and (r["_vc"] or 0) >= 2: fl.append("single_source")
    if str(r["Year"]).strip() == "":      fl.append("no_year")
    if any(f in fl for f in ["claim_no_source"]):        p = "High"
    elif any(f in fl for f in ["single_source"]):        p = "Medium"
    elif fl:                                             p = "Low"
    else:                                               p = "OK"
    return p, ";".join(fl)
tr = d.apply(triage, axis=1)
d["redteam_priority"] = [x[0] for x in tr]
d["redteam_flags"]    = [x[1] for x in tr]
d["redteam_note"]     = d["redteam_flags"].apply(
    lambda f: "No data year recorded - must be populated during verification."
              if "no_year" in f else "")
d = d.drop(columns=["_vc"])

# Reorder to the DPI column order (plus the triage columns)
base = ["Country","Country Name","Chapter","Chapter Details","Section","Variable Name",
        "Definition","Value Code","Value Name","Year","Comments","Variable Id",
        "Variable Sort","Source urls","n_sources","redteam_priority","redteam_flags","redteam_note"]
d = d[base]
d.to_csv("rural-prepped.csv", index=False, encoding="utf-8-sig")
print(f"Wrote rural-prepped.csv ({len(d)} rows). Priority mix:")
print(d["redteam_priority"].value_counts().to_string())

# 6. One batch per country
n = 0
for country, grp in d.groupby("Country", sort=True):
    grp.to_csv(os.path.join(OUT, f"{country}.csv"), index=False, encoding="utf-8-sig")
    n += 1
print(f"Wrote {n} country batches to {OUT}/")

# 7. Ensure metadata.csv contains the 4 rural variables
if os.path.exists(META) and os.path.exists(RMETA):
    mm = pd.read_csv(META, encoding="utf-8-sig", dtype=str).fillna("")
    rm = pd.read_csv(RMETA, encoding="utf-8-sig", dtype=str).fillna("")
    have = set(mm["Variable"]) if "Variable" in mm.columns else set()
    add = rm[~rm["Variable"].isin(have)]
    if len(add):
        pd.concat([mm, add], ignore_index=True).to_csv(META, index=False, encoding="utf-8-sig")
        print(f"Appended {len(add)} rural variables to {META}.")
    else:
        print("metadata.csv already contains the rural variables.")
else:
    print("NOTE: metadata.csv or rural_metadata.csv not found here - append the 4 "
          "rural rows to your metadata.csv manually before verifying.")
