# Compute Log

**Name:**
**Date:**
**Project directory on Vista:** /scratch/_______________/project/

---

## 1. Data Staging

| Dataset | Source URL | File on Vista | Size | Status |
|---------|-----------|---------------|------|--------|
| | | /scratch/.../data/raw/ | | Downloaded / Pending / Error |
| | | /scratch/.../data/raw/ | | Downloaded / Pending / Error |
| | | /scratch/.../data/raw/ | | Downloaded / Pending / Error |

**Data cleaning notes:** _(what was removed, how missing values were handled, how datasets were joined)_



**Processed data file:** /scratch/_______________/data/processed/_______________

**Rows in final table:** _______________
**Columns in final table:** _______________

---

## 2. Pipeline Scripts

| Script | Purpose | Location on Vista | Status |
|--------|---------|-------------------|--------|
| | Data download | /scratch/.../scripts/ | Working / In progress / Error |
| | Data cleaning and joining | /scratch/.../scripts/ | Working / In progress / Error |
| | Feature engineering | /scratch/.../scripts/ | Working / In progress / Error |
| | Model training | /scratch/.../scripts/ | Working / In progress / Error |
| | Evaluation | /scratch/.../scripts/ | Working / In progress / Error |

**AI tools used to generate code:**
- [ ] Claude Code
- [ ] Cursor
- [ ] Antigravity
- [ ] VS Code + Copilot
- [ ] Codex
- [ ] Other: _______________

---

## 3. Jobs Submitted

| Job Name | Queue | Nodes | Time Requested | Job UUID | Status | Output Location |
|----------|-------|-------|----------------|----------|--------|-----------------|
| | gh-dev / gh / gg | | | | Finished / Failed / Running | /scratch/.../ |
| | gh-dev / gh / gg | | | | Finished / Failed / Running | /scratch/.../ |
| | gh-dev / gh / gg | | | | Finished / Failed / Running | /scratch/.../ |
| | gh-dev / gh / gg | | | | Finished / Failed / Running | /scratch/.../ |

---

## 4. Raw Output

| Output File | What It Contains | Location on Vista |
|-------------|------------------|-------------------|
| | Trained model | /scratch/.../results/ |
| | Metrics (RMSE, R-squared, etc.) | /scratch/.../results/ |
| | Predictions | /scratch/.../results/ |
| | SHAP values | /scratch/.../results/ |

**Key metrics from raw output:**

| Metric | Baseline Model | Primary Model |
|--------|---------------|---------------|
| | | |
| | | |
| | | |

---

## 5. Issues and Debugging Log

| Issue | Error Message | How It Was Resolved |
|-------|---------------|---------------------|
| | | |
| | | |
| | | |

---

## Self-Check

Before moving to Stage 4 (Analysis), confirm:

- [ ] All datasets are downloaded and staged in $SCRATCH
- [ ] Data joins are clean (no duplicated rows, no mismatched keys)
- [ ] Train/test split does not leak information
- [ ] Baseline model ran and produced reasonable results
- [ ] Primary model ran without errors
- [ ] All output files are saved and readable
- [ ] I can explain what each script does (even if AI wrote it)
