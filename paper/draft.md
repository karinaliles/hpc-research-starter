# Whose Standard? Community-Led Evaluation of Generative AI for HBCU Communities

**Karina Liles, PhD** — Claflin University
Working draft · 2026 · Target venue: *AI and Ethics* (Springer)

> **STATUS — WORKING DRAFT.** Sections drawn from the research brief, methodology, and
> literature are filled in. Sections that depend on data collection (Results, parts of the
> Discussion, final Abstract numbers) are marked **[PENDING]** — they must NOT be written until
> the community-validation and model-evaluation steps are complete. Author lists for a few
> citations are flagged to verify before submission.

---

## Abstract

Generative AI systems are increasingly deployed in educational and community settings, yet the
benchmarks used to judge them are authored almost entirely by researchers external to the
communities those systems affect. We ask whether a *community-led* evaluation framework — one in
which an HBCU community defines and applies the criteria for "effective," "equitable," and
"trustworthy" AI — measures something that standard, generic benchmarks miss. We co-design a
three-dimension rubric with members of an HBCU community, assemble a community-grounded prompt
set, run a sweep of open generative models against it, and score every response both with the
community rubric and with a standard bias benchmark (BBQ). We then quantify the **divergence**
between community and standard judgments. **[PENDING: headline results — magnitude and direction
of divergence, reliability, and the domains where the gap is largest.]** Our contribution is the
framework and the community-authored prompt set, together with evidence on whether community-led
evaluation surfaces strengths and harms invisible to generic benchmarks.

---

## 1. Introduction

Large generative models are now used by students for advising, writing, coding help, financial-aid
navigation, and more. The dominant way we judge these systems — leaderboards and general-purpose
benchmarks — frames quality around a broad, "average" user [Raji et al. 2021; Liang et al. 2022].
This framing has a blind spot: it cannot tell us whether a system serves a *specific* community
well, because the community whose needs are at stake had no hand in defining what "well" means.

Historically Black Colleges and Universities (HBCUs) are exactly such a community — central to the
education of Black students, yet largely absent as authors of the criteria by which AI is assessed.
Where bias and fairness are measured at all, the measurement is typically defined and run by
researchers outside the community [Blodgett et al. 2020; Birhane et al. 2022]. The result is that
the very definition of "good" AI continues to be set by those outside the communities most affected.

This paper asks: **How can a community-grounded, participatory evaluation framework measure whether
a generative AI system is effective, equitable, and trustworthy for HBCU communities — and how do
its judgments differ from those of standard, generic AI benchmarks?**

We make three contributions:
1. A **community-led evaluation framework** — three dimensions (effectiveness, equity,
   trustworthiness) decomposed into community-authored sub-criteria.
2. A **community-grounded prompt set** rooted in the real needs of an HBCU community.
3. An **empirical comparison** quantifying how community judgments diverge from a standard
   benchmark, and where.

## 2. Background and Related Work

**The limits of general benchmarks.** Raji et al. [2021] argue that "general" benchmarks present a
false premise — that evaluation can exist independent of context and scope. HELM [Liang et al. 2022]
broadened evaluation across many metrics and scenarios but remains a researcher-defined, general
instrument. Bender et al. [2021] warn that scale without attention to whom a system serves
reproduces and amplifies harm.

**Bias, positionality, and language.** Blodgett et al. [2020] show that NLP "bias" work is often
disconnected from the lived experience of affected communities and call for centering those
communities. Santy et al. [2023] find datasets and models align most closely with "WEIRD"
populations. Ziems et al. [2022] demonstrate measurable performance drops on African American
English — directly relevant to HBCU community language. Durmus et al. [2023] offer a quantitative
template for asking *whose* opinions a model reflects. BBQ [Parrish et al. 2022] provides a
hand-built benchmark for social bias in question answering, which we adopt as our standard
comparison.

**Participatory approaches — and their pitfalls.** Bondi et al. [2021] propose that affected
communities define "social good" and act as partners (the PACT framework). Birhane et al. [2022]
examine who actually benefits from participatory AI. Sloane et al. [2020] caution against
"participation-washing" — extractive or token involvement. Johnson et al. [2026] — our nearest
neighbor — engage marginalized communities to design rubrics that are then operationalized in
automated evaluation pipelines, and surface the tension between automation and community expertise.
We extend this line of work from images to text, and specifically to the HBCU context.

**Documentation as method.** We document our prompt set and framework following the norms of
Datasheets [Gebru et al. 2021] and Model Cards [Mitchell et al. 2019], and situate our impact
categories alongside Solaiman et al. [2023].

**The gap.** No validated, community-led framework exists in which an HBCU community defines, drives,
and applies the criteria for effective, equitable, and trustworthy generative AI. This paper builds
and tests one.

## 3. Methodology

### 3.1 Overview
The framework is operationalized as a large-scale scoring pipeline: community members define the
criteria; open models generate responses to a community-grounded prompt set; each response is scored
on the community dimensions (rubric + LLM-as-judge, with human community validation on a sample) and
on a standard benchmark; the two score sets are compared statistically.

### 3.2 Community-defined dimensions and rubric
Three top-level dimensions — **effectiveness, equity, trustworthiness** — each decomposed into four
sub-criteria scored 1–5 (12 sub-criteria total). The rubric is an expert-drafted starter that is
**reviewed, revised, and approved by the HBCU community** before use; the community step is what
makes the criteria valid. **[PENDING: report the community-finalized rubric and any
added/renamed/re-weighted criteria.]**

### 3.3 Community-grounded prompt set
Prompts span ten domains relevant to HBCU community needs: academic advising, financial aid, grad
school/career, writing support, STEM/coding, health and wellness, identity/culture/history, local
community context, civic/legal, and mental health. High-stakes domains (financial aid, health,
civic/legal, mental health) are flagged, and the rubric weights trustworthiness and safety more
heavily there. The set is seeded with authored prompts and a subset of BBQ items, then expanded to
~150 through community validation. **[PENDING: final prompt count and per-domain coverage.]**

### 3.4 Models and generation
A sweep of open generative models (e.g., Llama-3, Mixtral, Qwen, Gemma; sizes to be finalized) is run
on HPC (TACC Vista). Each (prompt × model × repetition) generation uses a fixed seed and logged
sampling settings for reproducibility; planned scale is ~150 prompts × 5 models × 3 repetitions
≈ 2,250 generations. **[PENDING: final model list and generation counts.]**

### 3.5 Scoring
Each response is scored two ways: (1) the community rubric via an LLM-as-judge that returns the 12
sub-criteria plus a rationale, validated against human community ratings on a stratified ~10–15%
sample; and (2) the standard benchmark (BBQ): for ambiguous-context items, selecting any named group
over the "unknown" option indicates bias. We report judge–human agreement as a reliability check.

### 3.6 Analysis
We compute, per response and per dimension, the **divergence** between community and standard scores,
with significance and effect size, plus reliability across repetitions and per-domain breakdowns.

## 4. Results

**[PENDING — DATA NOT YET COLLECTED. Do not write until the pipeline has run.]**
Planned reporting:
- Reliability: judge–human inter-rater agreement; variance across repetitions.
- Divergence: magnitude/direction of community-vs-standard differences, overall and by dimension.
- Where the gap is largest: which domains and which dimensions (expected: equity- and
  trust-sensitive, high-stakes prompts).
- Per-model comparison: do community-framework model rankings differ from benchmark rankings?

## 5. Discussion

**[PARTIAL — finalize after Results.]** If community scores diverge significantly from the standard
benchmark, it demonstrates that community-led evaluation captures strengths and harms generic
benchmarks miss — supporting the case that affected communities should author the criteria. If
scores closely track the benchmark, that is itself a meaningful finding about alignment, and the
validated framework and community-authored prompt set remain contributions either way.

## 6. Limitations

- The prompt set begins as an expert-drafted starter; until community-validated it carries author
  bias, and even after validation it reflects one HBCU community, not all.
- LLM-as-judge scoring can be unreliable and varies across judge models; we mitigate with human
  validation but do not eliminate this risk.
- Aligning open-ended community prompts with a structured benchmark (BBQ) for a fair comparison
  involves design choices that bound the divergence claim.
- Results reflect the specific models and time period evaluated.

## 7. Ethics and Responsible Research

Human-subjects components (community focus groups/surveys, human scoring) require **Claflin IRB
approval and informed consent prior to data collection**. The community are partners and co-authors
of the criteria, not subjects of extraction [Sloane et al. 2020; Birhane et al. 2022]. The prompt
set and framework will be documented datasheet-style [Gebru et al. 2021]. High-stakes domains are
handled with added care in both prompting and scoring.

## 8. Conclusion

**[PENDING final Results.]** We present a community-led framework for evaluating generative AI in the
HBCU context and a method for quantifying how its judgments differ from standard benchmarks. The
framework and community-authored prompt set are contributions independent of the specific findings.

---

## References

- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *FAccT '21*, 610–623.
- Birhane, A., Isaac, W., Prabhakaran, V., Díaz, M., Elish, M. C., Gabriel, I., & Mohamed, S. (2022). Power to the People? Opportunities and Challenges for Participatory AI. *EAAMO '22*. arXiv:2209.07572.
- Blodgett, S. L., Barocas, S., Daumé III, H., & Wallach, H. (2020). Language (Technology) is Power: A Critical Survey of "Bias" in NLP. *ACL 2020*. arXiv:2005.14050.
- Bondi, E., Xu, L., Acosta-Navas, D., & Killian, J. A. (2021). Envisioning Communities: A Participatory Approach Towards AI for Social Good. *AIES 2021*. arXiv:2105.01774.
- Durmus, E., et al. (2023). Towards Measuring the Representation of Subjective Global Opinions in Language Models. arXiv:2306.16388. *[verify full author list]*
- Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for Datasets. *Communications of the ACM*, 64(12), 86–92.
- Johnson, N., Sudharsan, D., Hamna, Dalal, S., Holroyd, T., Thieme, A., Heidari, H., Massiceti, D., Wortman Vaughan, J., & Morrison, C. (2026). Evaluating AI-Generated Images of Cultural Artifacts with Community-Informed Rubrics. arXiv:2604.02406.
- Liang, P., et al. (2022). Holistic Evaluation of Language Models (HELM). arXiv:2211.09110. *[verify full author list]*
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model Cards for Model Reporting. *FAT* '19*. arXiv:1810.03993.
- Parrish, A., et al. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering. *Findings of ACL 2022*. arXiv:2110.08193. *[verify full author list]*
- Raji, I. D., Bender, E. M., Paullada, A., Denton, E., & Hanna, A. (2021). AI and the Everything in the Whole Wide World Benchmark. *NeurIPS 2021 Datasets & Benchmarks*. arXiv:2111.15366.
- Sambasivan, N., Kapania, S., Highfill, H., Akrong, D., Paritosh, P., & Aroyo, L. (2021). "Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI. *CHI 2021*.
- Santy, S., et al. (2023). NLPositionality: Characterizing Design Biases of Datasets and Models. *ACL 2023*. arXiv:2306.01943. *[verify full author list]*
- Sloane, M., Moss, E., Awomolo, O., & Forlano, L. (2020). Participation Is not a Design Fix for Machine Learning. *EAAMO 2020*. arXiv:2007.02423.
- Solaiman, I., Talat, Z., Agnew, W., et al. (2023). Evaluating the Social Impact of Generative AI Systems in Systems and Society. arXiv:2306.05949.
- Ziems, C., et al. (2022). VALUE: Understanding Dialect Disparity in NLU. *ACL 2022*. arXiv:2204.03031. *[verify full author list]*
