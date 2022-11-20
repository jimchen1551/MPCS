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
| [[Decision tree]]           |                                              |
| [[Shannon's entropy model]] | $H(t, D)=-\sum_iP(t=i)\lg P(t=i)$            |
| [[Information gain]]        | $IG(d, D)=H(t, D)-rem(d, D)$                 |
| [[Information gain ratio]]  | $GR(d, D)=\frac{IG(d, D)}{H(d, D)}$          |
| [[Gini index]]              | $Gini(t, D)=1-\sum_{l\in levels(t)}P(t=l)^2$ |

| Algorithms        | Comment |
| ----------------- | ------- |
| [[ID3]] |         |
| C4.5              |         |
| CART                  |         |

## Continuous descriptive features
![[Screen Shot 2022-11-20 at 16.29.22.png|500]]
![[Screen Shot 2022-11-20 at 16.29.55.png|500]]

- defining a threshold within the range of values to partition the instances
1. sorting the instances according to the continuous values
2. identifying the adjacent values with the different classifications
3. finding the best threshold by [[Information gain]]
4. letting the categorized feature compete with other available features
5. repeating the same procedure at each node as the tree grows

## Continuous target features


## Tree pruning

## Model ensembles
### Boosting
### Bagging

