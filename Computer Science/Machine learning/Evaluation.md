---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Evaluation
- to determine which model is the most suitable for a task
- to estimate how the model will perform

| Target      | Evaluation                                                                      |
| ----------- | ------------------------------------------------------------------------------- |
| Categorical | [[Confusion matrix]]<br>[[Average class accuracy]]<br>[[Profit and loss]]       |
| Continuous  | [[Error function]]<br>[[R2 coefficient]]                                        |
| Prediction  | [[Prediction score]]<br>[[ROC curve]]<br>[[K-S statistic]]<br>[[Gain and lift]] |

## Misclassification rate
| T P | +   | -   |
| --- | --- | --- |
| +   | TP  | FN  |
| -   | FP  | TN  |

$$\text{class accuracy}=\frac{TP+TN}{TP+TN+FP+FN}$$
$$\text{misclass accuracy}=\frac{FP+FN}{TP+TN+FP+FN}$$
## Hold-out sampling
- suitable when a large dataset is available
- using sampling methods to take distinct random, non-overlapping samples from a large dataset
- using these samples for training and testing a model
- Issues:
  1. requiring a large enough dataset for sampling
  2. misleading performance results
## k-Fold cross-validation
## Leave-one-out cross-validation
## Bootstrapping
## Out-of-time sampling

