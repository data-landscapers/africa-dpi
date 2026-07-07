"""Merge the OK/stale verified batches back into africa-dpi-verified.csv.

Only the batches listed in data/ok_stale_manifest.csv (no priority prefix in
data/verified/) are merged here. Matches master rows by (Country, Variable Id)
and overwrites only the revision/publishing columns, preserving row order and
every original column. Prints a summary and leaves a .bak of the master.
"""
import csv, os, sys, shutil

MASTER = "africa-dpi-verified.csv"
VERIFIED_DIR = "data/verified"
MANIFEST = "data/ok_stale_manifest.csv"

REVISION_COLS = [
    "revised_value_code", "revised_source_urls", "revision_notes",
    "revised_year", "revised_year_confidence", "revised_comments", "status",
]

def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)

# batch file names to merge (from manifest)
with open(MANIFEST, encoding="utf-8-sig", newline="") as f:
    batch_files = [row["file"] for row in csv.DictReader(f)]

# collect verified rows keyed by (Country, Variable Id)
verified = {}
missing, empty = [], []
for bf in batch_files:
    p = os.path.join(VERIFIED_DIR, bf)
    if not os.path.exists(p):
        missing.append(bf)
        continue
    _, rows = read_csv(p)
    if not rows:
        empty.append(bf)
        continue
    for row in rows:
        verified[(row["Country"], row["Variable Id"])] = row

fields, master = read_csv(MASTER)

matched = changed = confirmed = unknown_lc = human = 0
for row in master:
    key = (row["Country"], row["Variable Id"])
    v = verified.get(key)
    if not v:
        continue
    matched += 1
    for c in REVISION_COLS:
        row[c] = v.get(c, "")
    if v.get("revised_value_code", "").strip():
        changed += 1
    else:
        confirmed += 1
    st = v.get("status", "").strip()
    if st == "unknown_lightcheck":
        unknown_lc += 1
    elif st == "human_review":
        human += 1

shutil.copy2(MASTER, MASTER + ".premerge_okstale.bak")
with open(MASTER, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(master)

print(f"verified rows collected : {len(verified)}")
print(f"master rows matched     : {matched}")
print(f"  value code revised    : {changed}")
print(f"  confirmed unchanged   : {confirmed}")
print(f"  unknown (lightcheck)  : {unknown_lc}")
print(f"  human_review flagged  : {human}")
if missing:
    print(f"MISSING verified files ({len(missing)}): {', '.join(missing)}", file=sys.stderr)
if empty:
    print(f"EMPTY verified files ({len(empty)}): {', '.join(empty)}", file=sys.stderr)
