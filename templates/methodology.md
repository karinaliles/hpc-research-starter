# Methodology Document

**Name:**
**Date:**
**Research Question:** _(copy from Research Brief)_

This is your project's plan. Your AI tools read it to help you build, so be specific. It works for any kind of HPC computation, not only machine learning.

---

## 1. What Is Your Computation?

What kind of computation does your research need? Check the one that fits best (you can combine):

- [ ] **Machine learning / predictive model** — predict or classify an outcome from data
- [ ] **Simulation or numerical model** — model how a system behaves over time or under conditions
- [ ] **Large-scale data processing / pipeline** — clean, join, or transform data too big for a laptop
- [ ] **Statistical analysis** — test relationships or differences at scale (regression, Bayesian, bootstrapping)
- [ ] **Optimization / parameter sweep** — search many configurations for the best one
- [ ] **Other / domain-specific:** _______________

**In one sentence, what will your computation do?**



---

## 2. What Goes In?

**Unit of analysis:** Each row or record represents a _______________

**Data sources:**

| Dataset | Source | Key Variables Used | Join Key |
|---------|--------|--------------------|----------|
| | | | |
| | | | |

**Approximate size:** ~______ records x ______ variables

**Data quality notes:** _(missing values, gaps, alignment issues)_



---

## 3. What Comes Out?

**What does your computation produce?** _(a prediction, a simulated dataset, a processed table, a statistical result, an optimal configuration, etc.)_



**Form of the output:**
- [ ] A number (continuous)
- [ ] A category or label
- [ ] A time series
- [ ] Clusters or patterns
- [ ] A simulated or processed dataset
- [ ] A statistical result (effect size, interval, posterior, etc.)
- [ ] Other: _______________

---

## 4. What Is Your Method?

**The approach you will use:** _________________________________

**Why this approach over alternatives:** _________________________________

**Your baseline or point of comparison:** _(the simpler result you compare against)_



### If your computation is machine learning

_Skip this block if you are not training a model._

**Standard features (from raw data):**

| Feature | Source Dataset | Type |
|---------|---------------|------|
| | | Continuous / Categorical |
| | | Continuous / Categorical |

**Engineered features (created from raw data):**

| Feature | How It's Computed | Why It Matters |
|---------|-------------------|----------------|
| | | |

**Which features are novel?** _(often the publishable contribution)_

**Baseline model:** ____________   **Primary model:** ____________

**Interpretability approach:** SHAP / built-in feature importance / partial dependence / other: ____________

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
| | |
| | |

**What does a "good" result look like for your question?**



**Would a negative or null result still be worth reporting?**



---

## Data Pipeline Diagram

_Draw or describe the flow from inputs to results. Show each source, how they combine, where the heavy compute happens, and what comes out._

```
[Input A] ---\
              \
[Input B] -----> [Combine / process] --> [Your computation] --> [Results]
              /
[Input C] ---/
```

---

## Computational Plan

| Step | What Happens | Where | Queue | Estimated Time |
|------|-------------|-------|-------|----------------|
| Data download | | Laptop / Login node | N/A | |
| Preprocessing | | | | |
| Main computation | | Vista | gh | |
| Evaluation / analysis | | | | |
| Visualization | | Laptop / Jupyter | N/A | |

**Total estimated allocation usage:** ______ node-hours

---

## Self-Check

Before moving to Compute, confirm:

- [ ] I have named what kind of computation this is
- [ ] My method is specific enough that someone else could run this study
- [ ] I have identified how my data sources connect
- [ ] I have a clear way to tell whether the result is good
- [ ] I know which steps need HPC and which do not
- [ ] My plan fits the time I have on Vista this week
