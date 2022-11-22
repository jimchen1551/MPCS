---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Information-based learning

| Fundamental concepts        | Comment                                      |
| --------------------------- | -------------------------------------------- |
| [[Decision tree]]           | for discrete target feature                  |
| [[Regression tree]]         | for continuous target feature                |
| [[Shannon's entropy model]] | $H(t, D)=-\sum_iP(t=i)\lg P(t=i)$            |
| [[Information gain]]        | $IG(d, D)=H(t, D)-rem(d, D)$                 |
| [[Information gain ratio]]  | $GR(d, D)=\frac{IG(d, D)}{H(d, D)}$          |
| [[Gini index]]              | $Gini(t, D)=1-\sum_{l\in levels(t)}P(t=l)^2$ |

| Algorithms        | Comment |
| ----------------- | ------- |
| [[ID3]] |         |
| C4.5              |         |
| CART                  |         |

## Tree pruning
### Prepruning
### Postpruning
## Model ensembles
### Boosting
### Bagging

