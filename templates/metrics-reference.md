# Metrics Reference Card

Keep this open while reviewing your results.

---

## Regression Metrics (predicting a number)

### R-squared (R2)

**What it is:** The percentage of variation in your outcome that your model explains.

**Range:** 0 to 1 (can be negative for very bad models)

**How to read it:**
- 0.80 = your model explains 80% of the variation
- 0.50 = your model explains half, misses half
- 0.10 = your model barely explains anything

**Rough benchmarks:**
- Above 0.7: strong model for most social/health science applications
- 0.4 - 0.7: moderate, may still be publishable depending on the field
- Below 0.3: weak, reconsider your features or approach

**Compare to:** Your baseline model AND published work in your area.

---

### RMSE (Root Mean Squared Error)

**What it is:** The average size of your prediction errors, in the same units as your outcome. Larger errors are penalized more.

**How to read it:** If your outcome is "mortality rate per 100,000" and your RMSE is 5.2, your predictions are off by about 5.2 per 100,000 on average.

**Is it good?** Compare RMSE to the mean and standard deviation of your outcome variable.
- RMSE much smaller than the standard deviation = good
- RMSE close to the standard deviation = model is barely better than guessing the average
- RMSE larger than the standard deviation = something is wrong

---

### MAE (Mean Absolute Error)

**What it is:** The average absolute error. Unlike RMSE, it does not penalize large errors extra.

**When to use:** When you care about all errors equally, not just the big ones.

**How to compare to RMSE:** If MAE is much smaller than RMSE, you have some very large outlier errors.

---

## Classification Metrics (predicting a category)

### Accuracy

**What it is:** The percentage of predictions that are correct.

**The trap:** If 90% of your data is one class, a model that always predicts that class gets 90% accuracy. That does not mean it works.

**When to use:** Only when your classes are roughly balanced.

**When NOT to use:** Imbalanced datasets (use F1 or AUC instead).

---

### Precision

**What it is:** Of all the things your model predicted as positive, how many actually are?

**Plain language:** "When the model says yes, how often is it right?"

**High precision means:** Few false alarms.

**Low precision means:** The model cries wolf too often.

---

### Recall (Sensitivity)

**What it is:** Of all the actual positives, how many did your model catch?

**Plain language:** "Of all the real cases, how many did the model find?"

**High recall means:** You catch most of the real cases.

**Low recall means:** You are missing real cases.

---

### F1 Score

**What it is:** The balance between precision and recall. The harmonic mean of both.

**Range:** 0 to 1

**When to use:** When you care about both false positives AND false negatives.

**Rough benchmarks:**
- Above 0.75: strong
- 0.5 - 0.75: moderate
- Below 0.5: weak

---

### AUC-ROC

**What it is:** How well your model separates the two classes across all possible thresholds.

**Range:** 0.5 (random guessing) to 1.0 (perfect separation)

**Rough benchmarks:**
- Above 0.9: excellent
- 0.8 - 0.9: good
- 0.7 - 0.8: fair
- Below 0.7: poor

**Always report this** for binary classification problems.

---

## Reading SHAP Plots

### Summary Plot (beeswarm)

This is the most common SHAP visualization. Each row is a feature. Each dot is one observation.

- **Position (left/right):** How much this feature pushed the prediction down (left) or up (right) for that observation
- **Color (blue/red):** The actual value of the feature for that observation. Red = high value, blue = low value.
- **Top to bottom ordering:** Features at the top matter most overall

**What to look for:**
- Feature at the top = most important predictor
- Red dots on the right = high values of this feature increase the prediction
- Blue dots on the right = low values increase the prediction (inverse relationship)
- Wide spread = this feature has a strong, variable effect
- Tight cluster near zero = this feature does not matter much

### Dependence Plot

Shows how one feature affects predictions across its range.

- **X-axis:** Value of the feature
- **Y-axis:** SHAP value (how much it pushed the prediction)
- **Color:** Often shows interaction with another feature

**What to look for:**
- Upward trend = higher values of this feature increase predictions
- Flat line = this feature does not matter
- Nonlinear pattern = the effect changes at certain thresholds

---

## Quick Decision Guide

| I want to know... | Look at... |
|---|---|
| Is my model any good overall? | R-squared (regression) or AUC (classification) |
| How big are my errors? | RMSE or MAE |
| Which features matter most? | SHAP summary plot |
| Is my model better than the baseline? | Compare metrics side by side |
| Is my model overfitting? | Compare train vs. test metrics (big gap = overfitting) |
| Are my results publishable? | Compare to published work in your area |

---

## Red Flags

| What You See | What It Means |
|---|---|
| R-squared of 0.99 | Almost certainly data leakage or a bug. Real-world data is never this clean. |
| Accuracy of 95% on imbalanced data | The model is probably just predicting the majority class. Check F1 and recall. |
| Train accuracy 98%, test accuracy 60% | Overfitting. Your model memorized the training data. Simplify or add regularization. |
| All SHAP values near zero | Your features do not predict the outcome. Reconsider your question or data. |
| One feature dominates everything | Check if that feature is a proxy for the outcome (leakage) or if it is genuinely important. |
