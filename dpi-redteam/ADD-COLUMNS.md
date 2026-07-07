# Adding revised_year and revised_comments to the verifier

Two changes so the REMAINING batches produce these columns natively (better than
retrofitting, because the verifier still has the sources in context), plus a
one-off retrofit for the High/Medium batches already done.

## 1. For remaining batches — edit .claude/agents/dpi-verifier.md

In the "write the revised row" step, add these output fields alongside the
existing ones:

- **revised_year** — the year the revised evidence pertains to (the vintage of
  the newest authoritative source the score now rests on). If you find the
  original Year was mislabelled, use the corrected year. Add
  **revised_year_confidence** (high / medium / low).
- **revised_comments** — a clean, standalone statement of the current evidence
  for the score: present tense, British English, sourced in substance, readable
  on its own. It must NOT mention the previous data, prior errors, mislabelled
  sources, score changes ("revised from X to Y"), or review flags. Write it as if
  authoring the cell fresh. Keep the error/bookkeeping detail in revision_notes,
  where it belongs.

Nothing else changes. revision_notes stays as the audit trail; revised_comments
is the publishable version of the same finding with the criticism stripped out.

## 2. For the High/Medium batches already processed — one retrofit run

These already have revision_notes, so they need no re-searching. Use the
retrofit-columns subagent (no web access, pure text):

    Split the already-verified rows (those with a revised_value_code) into
    batches, then run the retrofit-columns subagent over them to add
    revised_year, revised_year_confidence and revised_comments. Merge back into
    africa-dpi-verified.csv.

Because it does no searching, this run is fast and draws almost nothing from your
usage — it is just reading two columns and writing two more. Review the rows
where revised_year_confidence is medium or low first.
