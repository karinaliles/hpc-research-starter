# Data Specification

The three linked tables the pipeline produces, plus provenance and ethics notes.

## Table 1 — Prompt set (input)

Union of `community-prompts.csv` (authored) + `bbq-seeded-prompts.csv` (benchmark-seeded),
plus any community-contributed prompts. Unified schema `build_dataset.py` should emit:

| Field | Required | Notes |
|-------|----------|-------|
| `prompt_id` | yes | Unique key joining all tables |
| `prompt_text` | yes | The text sent to the models |
| `domain` | yes | Coverage analysis |
| `primary_dimension` | yes | effectiveness / equity / trustworthiness |
| `high_stakes` | yes | yes/no — weights trust & safety more heavily |
| `source` | yes | `authored`, `bbq-seeded`, or `community-contributed` |
| `community_validated` | yes | yes/no — has the community reviewed/approved it |
| `bbq_example_id`, `bbq_category`, `unbiased_answer` | for seeded | Links to BBQ gold data for the standard score |

## Table 2 — Model responses (generated)

| Field | Notes |
|-------|-------|
| `prompt_id`, `model_id`, `repetition` | Composite key |
| `response_text` | The generation |
| `sampling_settings`, `seed` | Reproducibility — fix and log these |
| `refused`, `truncated` | Flags for empty/blocked/cut-off outputs |

## Table 3 — Scores (analysis)

| Field | Notes |
|-------|-------|
| `prompt_id`, `model_id` | Join key |
| `E1..E4`, `Q1..Q4`, `T1..T4` | 12 rubric sub-criteria (1–5) |
| `effectiveness`, `equity`, `trustworthiness` | Dimension means |
| `judge_rationale` | Short per-dimension justification |
| `human_score_*` | On the validation sample only |
| `bbq_standard_score` | Standard benchmark score for the comparison |
| `divergence` | community − standard, per dimension |

## Standard benchmark linkage (BBQ)

- Source: https://github.com/nyu-mll/BBQ — 11 jsonl files, ~58k items, **CC-BY 4.0**.
- For **ambiguous** contexts the unbiased correct answer is always the "unknown" option; a model
  picking a named group reflects bias. This is what makes BBQ items dual-scoreable (BBQ bias score
  + your equity/trust rubric).
- To seed more at scale, sample from `data/Race_ethnicity.jsonl` (and other categories) in
  `build_dataset.py` rather than copying by hand — keep `example_id` for traceability.

## Ethics / IRB

- **Authored + BBQ-seeded prompts (current):** no human subjects — no IRB needed.
- **Real community data (interviews, surveys, student questions):** human-subjects research —
  obtain **Claflin IRB approval + informed consent before collecting**. Document under the
  prompt set's "datasheet" (motivation, collection, consent, uses).
