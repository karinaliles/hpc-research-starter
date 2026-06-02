# Next Steps — Karina

From setup → submitted paper. Checked items are done; work top-down.

## ✅ Done — Setup (Stage 1–2)
- [x] Research brief — question, gap, 5 key papers, venues, approach
- [x] Methodology — full pipeline, validation plan, compute estimate
- [x] Literature — 15 papers organized in `literature/` + 16 items in Zotero
- [x] Git/GitHub — working and backed up

## Step 1 — Close the two open decisions *(mine; ~30 min each, no Vista needed)*
- [ ] Choose the **prompt-gathering method** (focus group / survey of Claflin students & faculty / expert-drafted starter set)
- [ ] Pick the **standard benchmark** to compare against (HELM / BBQ / a slice of one)
- [ ] Fill in the parked data-source details in `templates/research-brief.md` (section 3)

## Step 2 — Build the community prompt set + scoring rubric *(mine + community)*
- [ ] Draft ~150 prompts grounded in HBCU community needs
- [ ] Turn the three dimensions (effectiveness, equity, trustworthiness) into concrete, scorable sub-criteria — a rubric
- [ ] Document the prompt set like a "datasheet" (template: Gebru et al., in `literature/04-documentation-standards/`)

## Step 3 — Set up on Vista *(mid-week compute guide helps)*
- [ ] Confirm allocation/login; move data to `$SCRATCH`
- [ ] Download open model weights + the chosen benchmark
- [ ] Write Slurm scripts in `jobs/` (inference sweep, then scoring)

## Step 4 — Run the pipeline *(compute guide helps)*
- [ ] Inference: 5 models × 150 prompts × 3 reps ≈ 2,250 responses
- [ ] Score two ways: community rubric (LLM-as-judge) + standard benchmark
- [ ] Validate: human-rate a sample to check judge agreement with community raters
- [ ] Log runs + seeds in `templates/compute-log.md` (reproducible)

## Step 5 — Analyze & visualize (Stage 4)
- [ ] Compute community-vs-standard divergence + significance / effect size
- [ ] Make figures at 300 DPI: score distributions, divergence, failure clusters
- [ ] Fill in `templates/analysis.md`

## Step 6 — Write & submit (Stage 5)
- [ ] Draft the paper (intro/gap → method → results → discussion)
- [ ] Peer review (`templates/peer-review.md`) → submission plan (`templates/submission-plan.md`)
- [ ] Submit to **AI and Ethics** (primary venue; backups: AI & Society, ACM JRC)

## Small open threads (from setup)
- [ ] Verify full author lists in Zotero for HELM, BBQ, VALUE, NLPositionality, Durmus, and the LLMs-as-Judges survey (flagged in each item's Extra field)
- [ ] Add the MDPI 2025 paper to Zotero by DOI `10.3390/bs15060808`
- [ ] Grab the Solaiman 2023 PDF manually: https://arxiv.org/abs/2306.05949

---
**Best next session (no Vista needed):** Step 1 + the rubric in Step 2. Everything downstream waits on the prompt set and rubric.
