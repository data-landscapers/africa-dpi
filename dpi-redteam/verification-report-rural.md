# Rural Digitalisation — verification report

Re-verification of the Rural Digitalisation chapter (`data/batches_rural/`), the
rows that carried **no Year** (`redteam_flag = no_year`). Every row was routed
down the full path (all cited sources and carried a substantive score) and
delegated to the `dpi-verifier` subagent, one invocation per country. Merged
output: `data/verified_rural.csv`.

## Coverage

- **54 country batches**, **216 rows** (Clinic, Police, Registry, School per
  country).
- **Year populated on every row** — 0 rows left undated. This was the primary
  objective. `revised_year_confidence`: 86 high, 124 medium, 6 low.
- Vintage of the evidence the scores now rest on: 2025 (95 rows) and 2024 (52)
  dominate; 44 rows carry 2026 evidence. A small tail is older (one 2012 Mauritius
  registry figure, one 2019 Cabo Verde school figure) and is confidence-flagged
  accordingly.

## Scores

- **47 rows changed**, 169 confirmed unchanged.
- Direction: almost all changes are single-step upgrades reflecting digital
  pilots now reaching facility level (e.g. DHIS2/EMR at rural clinics, civil-
  registry point-of-service capture). Three are **downgrades** on stronger
  evidence: RWA Clinic 3→2 (2024 study: EMR at only ~33% of health centres),
  SYC School 3→2 (OpenEMIS not yet live in schools), TZA Clinic 3→2.
- By section: Clinic 16, Registry 14, School 13, Police 4.
- Several changes corrected an internal inconsistency in the original data where
  the `Comments` text argued one score but the `Value Code` cell held another.

## Flagged for human review (8)

No row reached the top of the 0–4 scale (`4 = Entirely digital`), so none was
escalated on that basis. The 8 `human_review` flags mark rows where the evidence
is strong but thin, indirect, or contested:

| Country | Section | Note |
|---|---|---|
| CIV | Registry | 2→3 rests on a single self-reported ONECI figure |
| GIN | Registry | 1→2 on emerging rollout evidence, uptake unconfirmed |
| MRT | Registry | two-step 1→3; verify facility-level digital capture |
| SDN | Registry | 1→2, but pre-war biometric evidence may not survive post-2023 conflict |
| COM | School | held at 1, but e-Msomo/e-Shiyo rollout may soon understate it |
| MUS | Registry | confirmed 2, but evidence base ~13 years old (2012) |
| LBY | Police | confirmed 1 on national-level, not rural-specific, evidence |
| TGO | Police | confirmed 1; emerging digitisation evidence inconclusive |

## Auditability

Original `Value Code` and `Year` are preserved untouched; recalculations live in
`revised_value_code`, dates in `revised_year` / `revised_year_confidence`,
rationale in `revision_notes`, and clean standalone cells in `revised_comments`.
Per-country outputs are retained under `data/verified_rural_batches/`.

## Notes for the next cycle

- A few originally cited sources were dead or inaccessible on fetch (STP Police
  403s, SWZ PDFs timing out, BWA school case-study URL now a marketing page);
  the verifier replaced or corroborated these and logged it in `revision_notes`.
- Live initiatives worth re-checking as they reach rural facilities: BDI
  biometric civil-registry platform (decree pending), and the CIV/GIN/MRT/SDN/NER
  registry rollouts behind the flags above.
