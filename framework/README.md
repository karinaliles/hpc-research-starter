# Framework — community evaluation rubric + prompt set

This folder holds the artifacts the evaluation pipeline reads:

- `scoring-rubric.md` — the three dimensions (effectiveness, equity, trustworthiness) and their
  12 sub-criteria, scored 1–5.
- `community-prompts.csv` — authored evaluation prompts (60 seed prompts, 10 domains).
- `bbq-seeded-prompts.csv` — real BBQ items (CC-BY 4.0) seeded as benchmark-linked, dual-scoreable prompts.
- `data-spec.md` — the three linked tables (prompts → responses → scores), provenance, and IRB notes.

## ⚠️ Status: expert-drafted starter — not yet community-validated

Both files are an **AI-assisted draft scaffold**, created to unblock the pipeline. They are
**not** the community's authored criteria. The participatory step — having Claflin / HBCU
community members review, revise, cut, add, and approve these — is what makes the framework
valid and is the heart of the contribution. Treat everything here as a first draft to react to.

## Decisions made (Step 1)

- **Prompt-gathering method:** expert-drafted starter set (this file), then **community-validated**
  via a Claflin focus group / short survey. Chosen because it lets the build proceed now while
  preserving community ownership of the final criteria.
- **Standard benchmark (comparison baseline):** **BBQ** (Bias Benchmark for Question Answering,
  Parrish et al. 2022). Chosen over HELM because it is equity-focused, hand-built, QA-formatted
  (pairs cleanly with prompts), and tractable for a one-week pilot. HELM's fairness/bias metrics
  remain an optional broader comparison.

## Current draft contents

- 60 seed prompts across 10 community-relevant domains: academic advising, financial aid,
  grad school & career, writing support, STEM/coding, health & wellness, identity/culture/history,
  local community (Orangeburg, SC), civic/legal, and mental health.
- High-stakes domains (financial aid, health, civic/legal, mental health) are flagged
  `high_stakes=yes`; the rubric weights trustworthiness/safety more heavily there.

## To reach the methodology target (~150 prompts)

Expand during community validation: ask community members to (1) add prompts from their own
experience, (2) flag any that feel off or stereotyping, and (3) confirm domain coverage. Aim
for ~15 validated prompts per domain.

## Pipeline contract

`scripts/build_dataset.py` should read `community-prompts.csv`; the inference step runs each
prompt through the open models; the scoring step applies `scoring-rubric.md` (via LLM-as-judge)
plus the BBQ baseline. See `templates/methodology.md` for the full plan.
