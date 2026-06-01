# Research Brief

**Name:** Karina Liles, PhD
**Date:** 2026-06-01
**Institution:** Claflin University
**Discipline:** Computer Science / Data Science / Applied AI

---

## 1. Research Question

_State your research question in one sentence._

How can a community-grounded, participatory evaluation framework measure whether a
generative AI system is "effective," "equitable," and "trustworthy" for historically
underserved communities — and how do its judgments differ from those of standard,
generic AI benchmarks?

**Why does this question need HPC?**

Validating the framework means running many generative-model inferences at scale: the
same battery of community-grounded prompts across multiple models and many repetitions,
producing thousands of responses that then need to be scored both by the new framework
and by standard automated benchmarks for comparison. Running open models locally (rather
than paying per-call APIs), sweeping across models and prompt sets, and processing the
resulting large response corpus is what pushes this beyond a laptop and onto Vista.



---

## 2. Gap It Fills

**What has been well-studied in this area?**

Generic, general-purpose evaluation of generative AI is mature: standard benchmarks and
leaderboards (accuracy on academic tasks, helpfulness/harmlessness ratings, broad fairness
metrics) measure model quality for a broad, "average" user. There is also a growing body of
AI fairness and bias work, but it is largely defined and run by researchers external to the
communities being evaluated.

**What has NOT been done?**

There is no validated, community-led evaluation framework in which an HBCU community
defines, drives, and applies the criteria for what "effective," "equitable," and
"trustworthy" generative AI means for that community. HBCU students, faculty, and contexts
are typically absent as the *primary authors* of evaluation criteria — included, at best, as
a demographic category in someone else's benchmark rather than as the people setting the
terms of assessment.

**Why does this gap matter?**

Generative AI is already being deployed in HBCU classrooms, advising, and research, yet we
have no validated way to measure whether these systems actually serve HBCU communities.
Without community-led evaluation, mismatches and harms go undetected, and the definition of
"good" AI continues to be set by those outside these communities — reinforcing the very lack
of local relevance this work aims to correct.



**Key papers that define the current state (3-5):**

| # | Title | Authors | Year | Key Finding |
|---|-------|---------|------|-------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## 3. Data Sources

> _TO DO (Karina). Three data types identified; details to be filled in later:_
> 1. _Community-grounded prompt/criteria set — built with the HBCU community (novel, core contribution). Collection method TBD (focus group / survey / expert-drafted)._
> 2. _Generative model outputs — produced by running open models on Vista (generated, not downloaded)._
> 3. _Standard benchmark — an existing public eval set, for comparison. Specific set TBD._

**Primary dataset:**

| Field | Details |
|-------|---------|
| Name | |
| Source URL | |
| Format | |
| Size | |
| Key variables | |
| Geographic scope | |
| Temporal scope | |
| Access method | |
| Known limitations | |

**Supporting dataset(s):**

| Field | Dataset 2 | Dataset 3 |
|-------|-----------|-----------|
| Name | | |
| Source URL | | |
| Format | | |
| Key variables | | |
| Join key | | |

**How do the datasets connect?**

_Describe the join key (FIPS code, date, lat/lon, etc.) and any spatial or temporal alignment needed._



---

## 4. Target Venues

| # | Venue Name | Type | Next Deadline | Page Limit | Why It Fits |
|---|-----------|------|---------------|-----------|-------------|
| 1 | AI and Ethics (Springer) | Journal | Rolling (verify on site) | Verify on site | Directly about effective/equitable/trustworthy AI; receptive to a validated evaluation framework + benchmark comparison |
| 2 | AI & Society (Springer) | Journal | Rolling (verify on site) | Verify on site | Interdisciplinary; values participatory, community-centered AI work and societal impact |
| 3 | ACM Journal on Responsible Computing (JRC) | Journal | Rolling (verify on site) | Verify on site | Prestigious venue squarely on responsible/equitable computing; strong fit for community-led method |

---

## 5. Proposed Approach (brief)

**What method will you use?** (e.g., XGBoost, Random Forest, LSTM, etc.)

A participatory, community-led evaluation framework, validated empirically: run open
generative models at scale (on Vista) against a community-grounded prompt set, score the
outputs along community-defined dimensions, and compare those scores to standard automated
benchmarks.

**What is your outcome variable?**

Per-response scores on three community-defined, top-level dimensions for the HBCU context:
**effectiveness, equity, and trustworthiness.**

**What are your key features?**

The community-defined sub-criteria that make up the three dimensions (exact sub-criteria
come from the participatory step). The novel element: these criteria are authored by the
HBCU community, not imported from a generic benchmark.

**What does success look like?** (What result would be worth publishing?)

A working, documented framework that (a) produces consistent, meaningful scores across
models, and (b) demonstrably diverges from standard benchmarks — showing it captures
something generic evaluation misses. That divergence is the publishable finding.



---

## Self-Check

Before moving to Stage 2 (Design), confirm:

- [ ] My question is specific enough that someone else would know exactly what I'm studying
- [ ] The gap is real (not already addressed in published work)
- [ ] I have at least one dataset I can access this week
- [ ] I have identified at least one venue where this work fits
- [ ] This question benefits from HPC (not solvable on a laptop)
