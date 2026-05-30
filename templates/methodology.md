# Methodology Document

**Name:**
**Date:**
**Research Question:** _(copy from Research Brief)_

---

## 1. What Goes In?

**Unit of analysis:** Each row in my final table represents a _______________

**Datasets:**

| Dataset | Source | Key Variables Used | Join Key |
|---------|--------|--------------------|----------|
| | | | |
| | | | |
| | | | |

**Final table dimensions:** ~______ rows x ______ columns

**Data quality notes:** _(missing values, suppressed cells, temporal/spatial alignment issues)_



---

## 2. What Comes Out?

**I am predicting/classifying:** _________________________________

**Outcome variable name:** _________________________________

**Outcome type:**
- [ ] Continuous (a number)
- [ ] Binary (yes/no, high/low)
- [ ] Multi-class (3+ categories)
- [ ] Time series
- [ ] Clusters/patterns

---

## 3. What Features Matter?

**Standard features (from raw data):**

| Feature | Source Dataset | Type |
|---------|---------------|------|
| | | Continuous / Categorical |
| | | Continuous / Categorical |
| | | Continuous / Categorical |
| | | Continuous / Categorical |
| | | Continuous / Categorical |

**Engineered features (created from raw data):**

| Feature | How It's Computed | Why It Matters |
|---------|-------------------|----------------|
| | | |
| | | |
| | | |

**Which features are novel?** _(These are often the publishable contribution)_



---

## 4. What Models and Why?

**Baseline model:** _________________________________

**Why:** _________________________________

**Primary model:** _________________________________

**Why this over alternatives:** _________________________________

**Additional model(s) (if time allows):** _________________________________

**Interpretability approach:** 
- [ ] SHAP values
- [ ] Feature importance (built-in)
- [ ] Partial dependence plots
- [ ] Other: _________________________________

---

## 5. How Do You Know It Worked?

**Train/test split strategy:**
- [ ] 80/20 random split
- [ ] K-fold cross-validation (k = ___)
- [ ] Temporal split (train on years ___, test on years ___)
- [ ] Other: _________________________________

**Evaluation metrics:**

| Metric | Why This Metric |
|--------|-----------------|
| | |
| | |

**What does a "good" result look like?** _(What R-squared, accuracy, or F1 would be worth publishing?)_



**What would a "bad" result tell you?** _(Would it still be publishable as a negative finding?)_



---

## Data Pipeline Diagram

_Draw or describe the flow from raw data to final results. Show each dataset, how they join, where features are engineered, and where the model runs._

```
[Dataset A] ---\
                \
[Dataset B] -----> [JOIN on ___] --> [Feature Engineering] --> [Model] --> [Results]
                /
[Dataset C] ---/
```

---

## Computational Plan

| Step | What Happens | Where | Queue | Estimated Time |
|------|-------------|-------|-------|----------------|
| Data download | | Laptop / Login node | N/A | |
| Data cleaning | | | | |
| Feature engineering | | | | |
| Model training | | | | |
| Evaluation / SHAP | | | | |
| Visualization | | | | |

**Total estimated allocation usage:** ______ node-hours

---

## Self-Check

Before moving to Stage 3 (Compute), confirm:

- [ ] My methodology is specific enough that someone else would know exactly how to run this study
- [ ] I have identified the join keys between my datasets
- [ ] I have chosen models with a clear justification (not just "it's popular")
- [ ] I have an evaluation plan with specific metrics
- [ ] I know which steps need HPC and which don't
- [ ] My computational plan accounts for the time I have on Vista this week
