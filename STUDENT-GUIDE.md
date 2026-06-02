# Student Guide — Running the Study

A plain-language walkthrough for completing the research study. Each part says what to do,
the exact command (if any), and what "done" looks like.

**The one rule:** always test with a few questions (`--limit 10`) before running everything.
It catches most problems early.

---

## Part 1 — Get the criteria from the community  *(no computer needed)*
1. Sit down with HBCU community members (students, faculty). Show them the rubric in
   `framework/scoring-rubric.md` and the example questions in `framework/community-prompts.csv`.
2. Ask: *Are these the right things to measure? What's missing? Reword anything that doesn't sound right.*
3. Together, write more real questions people would actually ask an AI — aim for about 150 total.
   Save them in a new file, `framework/community-contributed.csv`.

✅ **Done when:** the community has approved the rubric and you have ~150 questions.

## Part 2 — Build the question list  *(on a laptop)*
4. Open a terminal in the project folder and run:
   ```
   python scripts/build_dataset.py
   ```

✅ **Done when:** it prints "Wrote ~150 prompts" and creates `data/processed/prompts.csv`.

## Part 3 — Get the AI models  *(on Vista — ask the compute guide for help)*
5. Log into Vista and run:
   ```
   python scripts/download_data.py
   ```

✅ **Done when:** the models and the BBQ comparison data finish downloading.

## Part 4 — Ask the AI models every question  *(on Vista)*
6. **Test first** with a few questions:
   ```
   python scripts/run_inference.py --limit 10
   ```
7. If that works, run them all (submit the job):
   ```
   sbatch jobs/run_inference.slurm
   ```

✅ **Done when:** `data/processed/responses.csv` is full of AI answers.

## Part 5 — Score the answers  *(on Vista, then laptop)*
8. Run:
   ```
   python scripts/evaluate.py
   ```
   This scores each answer two ways — by your community rubric and by the standard benchmark.
9. Have a few community members hand-score a small sample (about 1 in 10) to check the AI
   scorer agrees with real people.

✅ **Done when:** `results/scores.csv` exists and you have the human-check sample.

## Part 6 — See what you found  *(on laptop)*
10. Make charts comparing your community scores to the standard scores. Where do they disagree
    most? *That difference is your finding.*
11. Write it up and fill in `templates/analysis.md`.

## Part 7 — Share it
12. Draft the paper and submit to **AI and Ethics** (the target journal).

---

### Where things live
- Criteria & questions: `framework/`
- Pipeline scripts: `scripts/`  (each file's top comment says what it does and how to run it)
- Vista job: `jobs/run_inference.slurm`
- Results: `results/`  •  Figures: `figures/`
- Bigger-picture roadmap: `next-steps.md`  •  Full plan: `templates/methodology.md`
