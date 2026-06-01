# Methodology Document

**Name:** Karina Liles, PhD
**Date:** 2026-06-01
**Research Question:** How can a community-grounded, participatory evaluation framework
measure whether a generative AI system is "effective," "equitable," and "trustworthy" for
historically underserved communities (specifically HBCU communities) — and how do its
judgments differ from those of standard, generic AI benchmarks?

This is your project's plan. Your AI tools read it to help you build, so be specific. It works for any kind of HPC computation, not only machine learning.

---

## 1. What Is Your Computation?

What kind of computation does your research need? Check the one that fits best (you can combine):

- [x] **Machine learning / predictive model** — predict or classify an outcome from data
- [ ] **Simulation or numerical model** — model how a system behaves over time or under conditions
- [x] **Large-scale data processing / pipeline** — clean, join, or transform data too big for a laptop
- [x] **Statistical analysis** — test relationships or differences at scale (regression, Bayesian, bootstrapping)
- [ ] **Optimization / parameter sweep** — search many configurations for the best one
- [x] **Other / domain-specific:** Large-scale generative-model inference + scoring (LLM evaluation pipeline)

**In one sentence, what will your computation do?**

Run open generative AI models at scale against a community-grounded prompt set, score every
response along community-defined dimensions (effectiveness, equity, trustworthiness) and
along standard benchmarks, and statistically compare the two sets of judgments.



---

## 2. What Goes In?

**Unit of analysis:** Each row or record represents a __single model response__ (one prompt,
run through one model, one repetition).

**Data sources:**

| Dataset | Source | Key Variables Used | Join Key |
|---------|--------|--------------------|----------|
| Community-grounded prompt set | Built with the HBCU community (participatory; TBD method) | prompt text, scenario/topic, target dimension | prompt_id |
| Open generative models | Open weights (e.g., Llama, Mistral/Mixtral, Qwen, Gemma) via Hugging Face | model name, size, generated response text | model_id |
| Standard benchmark | Existing public eval set (specific set TBD) | benchmark items + reference scores | prompt_id / item_id |

**Approximate size:** ~2,250 records (150 prompts x 5 models x 3 repetitions) x ~10-15
variables (ids, prompt, response, the three community-dimension scores + sub-criteria,
standard-benchmark scores, sampling settings).

**Data quality notes:** _(missing values, gaps, alignment issues)_

- Prompt set is newly authored and small (~150) — needs validation that it covers the
  intended community dimensions; risk of author bias until community-reviewed.
- Model outputs vary with sampling temperature/seed — fix and log these so runs are
  reproducible; the 3 repetitions capture this variance.
- Aligning community prompts with a standard benchmark for a fair comparison is non-trivial
  — define the mapping explicitly.
- Some models may refuse or truncate responses — log and handle empty/refused outputs.



---

## 3. What Comes Out?

**What does your computation produce?** _(a prediction, a simulated dataset, a processed table, a statistical result, an optimal configuration, etc.)_

Three things: (1) a scored response corpus — every model response with its community-dimension
scores (effectiveness, equity, trustworthiness) and its standard-benchmark scores; (2) a
statistical comparison quantifying how the community framework's judgments diverge from
standard benchmarks; and (3) the validated framework itself — the documented community-defined
criteria and scoring procedure.

**Form of the output:**
- [x] A number (continuous)
- [ ] A category or label
- [ ] A time series
- [x] Clusters or patterns
- [x] A simulated or processed dataset
- [x] A statistical result (effect size, interval, posterior, etc.)
- [x] Other: A documented, reusable evaluation framework (criteria + scoring rubric)

---

## 4. What Is Your Method?

**The approach you will use:** A participatory, community-led evaluation framework operationalized
as a large-scale scoring pipeline: HBCU community members define the criteria; open models generate
responses to the community prompt set on Vista; each response is scored on the community dimensions
(via a rubric + LLM-as-judge, with human community validation on a sample) and on standard
benchmarks; the two score sets are compared statistically.

**Why this approach over alternatives:** Generic benchmarks and expert-only rubrics do not center the
community whose needs are at stake — they measure an "average" user. Community authorship of the
criteria is the entire point and the novel contribution; no existing framework lets an HBCU community
define and drive the evaluation.

**Your baseline or point of comparison:** _(the simpler result you compare against)_

Standard, generic AI benchmark scores serve as the baseline. The community framework's scores are
compared against this baseline; the divergence between them is the finding.

### If your computation is machine learning

_Skip this block if you are not training a model._

_Note: this project does not train a supervised model. It runs inference with pretrained open models
and scores their outputs. The "features" below are reframed as the scoring dimensions._

**Standard features (from raw data):**

| Feature | Source Dataset | Type |
|---------|---------------|------|
| Standard-benchmark dimension scores (e.g., accuracy, helpfulness, harmlessness) | Standard benchmark | Continuous |
| Model identity / size | Open models | Categorical |

**Engineered features (created from raw data):**

| Feature | How It's Computed | Why It Matters |
|---------|-------------------|----------------|
| Effectiveness score | Rubric + LLM-as-judge over response, validated against community ratings | Community-defined dimension |
| Equity score | Same, on community equity sub-criteria | Community-defined dimension |
| Trustworthiness score | Same, on community trust sub-criteria | Community-defined dimension |
| Divergence (community − standard) | Difference between community and benchmark scores per response | The publishable signal |

**Which features are novel?** The three community-authored dimensions and their sub-criteria — defined
by the HBCU community rather than imported from a generic benchmark. This is the publishable contribution.

**Baseline model:** Standard benchmark scoring   **Primary model:** Community-led framework scoring (rubric + LLM-as-judge + human validation)

**Interpretability approach:** Per-dimension score breakdowns, qualitative analysis of high-divergence
responses, and clustering of failure patterns by community dimension. (other: ___)

---

## 5. How Do You Know It Worked?

Match your evaluation to your method:

- **Machine learning:** train/test split, metrics (RMSE, accuracy, F1, AUC), comparison to baseline
- **Simulation:** validation against known cases, convergence, sensitivity analysis
- **Data pipeline:** correctness and completeness checks, reproducibility
- **Statistics:** significance, effect size, model fit, assumptions checked
- **Optimization:** objective value, comparison to the baseline configuration

**Your evaluation plan:**

| What you check | Why |
|--------|-----------------|
| Inter-rater agreement between LLM-as-judge and human community raters (on a sample) | Validates that the automated scoring reflects real community judgment |
| Score reliability across the 3 repetitions (variance, consistency) | Confirms scores are stable, not sampling noise |
| Statistical significance + effect size of community-vs-standard divergence | Shows the framework captures something benchmarks miss, and how much |
| Pipeline correctness + completeness (no dropped/empty responses; reproducible from logged seeds) | Ensures results are trustworthy and reproducible |
| Coverage check: do the prompts span the intended community dimensions? | Guards against a biased or incomplete prompt set |

**What does a "good" result look like for your question?**

The framework produces reliable scores (high human–judge agreement, low repetition variance) and its
judgments diverge significantly from standard benchmarks on equity- and trust-sensitive prompts —
demonstrating that community-led evaluation surfaces strengths/harms that generic benchmarks miss.

**Would a negative or null result still be worth reporting?**

Yes. If community scores closely track standard benchmarks, that itself is a meaningful, publishable
finding — it would suggest generic benchmarks are more aligned with HBCU community needs than expected,
and the validated framework + community-authored prompt set remain contributions regardless.



---

## Data Pipeline Diagram

_Draw or describe the flow from inputs to results. Show each source, how they combine, where the heavy compute happens, and what comes out._

```
[Community prompt set] ----\
  (participatory, HBCU)      \
                              \
[Open models] -------------> [Run inference on Vista] --> [Response corpus] --\
  (Llama, Mistral, ...)       (150 prompts x 5 models                          \
                               x 3 reps ~= 2,250 responses)                     \
                                                                                 \
                                                            [Score 2 ways] --> [Compare community
[Standard benchmark] ------------------------------------>  - community rubric    vs. standard]
  (existing public set)                                       + LLM-as-judge   --> [Stats + figures
                                                            - standard benchmark      + validated
                                                              (human validation         framework]
                                                               on a sample)
```

---

## Computational Plan

| Step | What Happens | Where | Queue | Estimated Time |
|------|-------------|-------|-------|----------------|
| Data download | Download open model weights + the standard benchmark set | Login node / Vista `$SCRATCH` | N/A | ~1 hr |
| Preprocessing | Assemble + clean the community prompt set; format prompts for batch inference | Laptop / Login node | N/A | ~1-2 hr |
| Main computation | Run 5 open models over 150 prompts x 3 reps (~2,250 generations) | Vista (GPU) | gh | ~2-4 hr (est.) |
| Evaluation / analysis | Score responses (rubric + LLM-as-judge), run human-validation sample, compute divergence stats | Vista (GPU for judge) + Laptop | gh | ~2-3 hr |
| Visualization | Figures: score distributions, community-vs-standard divergence, failure-pattern clusters | Laptop / Jupyter | N/A | ~2 hr |

**Total estimated allocation usage:** ~8-15 node-hours (refine after a small pilot run; depends on model sizes)

---

## Self-Check

Before moving to Compute, confirm:

- [x] I have named what kind of computation this is
- [x] My method is specific enough that someone else could run this study
- [x] I have identified how my data sources connect
- [x] I have a clear way to tell whether the result is good
- [x] I know which steps need HPC and which do not
- [x] My plan fits the time I have on Vista this week
