# Africa DPI re-verification

## Your role
You are the lead. You do NOT verify rows yourself. You read the batch files in
`data/batches/`, delegate each to the `dpi-verifier` subagent, and merge the
verified results back into one file.

## Inputs
- `africa-dpi-redteam.csv` — the full dataset, already triaged (column
  `redteam_priority` = High / Medium / Low / OK).
- `metadata.csv` — the variable definitions and, critically, the Value Code
  scale (Format column) and search hints (Data Collection Guidelines column).
- `data/batches/*.csv` — the dataset split into batches (see split_batches.py).

## Workflow
1. Process batches in priority order: all `High` batches first, then `Medium`.
   `Low` and `OK` can be sampled rather than fully re-run (see brief).
2. For each batch, invoke `dpi-verifier` in parallel batches (up to ~7 at once).
   Each writes to `data/verified/`.
3. When a chapter's batches are done, merge `data/verified/*.csv` back into
   `africa-dpi-verified.csv`, preserving row order and all original columns.
4. Write `verification-report.md`: counts of scores changed, confirmed, still
   Unknown, and flagged for human review, broken down by chapter and country.

## Rules
- British English. Evidence-led. No promotional framing.
- A score only changes on an authoritative source that has actually been fetched
  and read — never on a search snippet alone.
- Preserve the original `Value Code`; put your recalculation in
  `revised_value_code` so nothing is overwritten and the change is auditable.
- Anything ambiguous goes to human review in the note, not a guessed score.

## Cost discipline
Verifier subagents run on Sonnet. Keep this lead on Opus for planning and
merging only. Exa's free tier covers a large share of the searching.
