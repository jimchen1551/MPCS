---
Created: [[2022-11-18]]
Aliases: GR, gain ratio
Types: Card
Tags: 
- 
---
# Information gain ratio
$$GainRatio(d, D)=\frac{IG(d, D)}{-\sum_{l\in levels(d)}(P(d=l)\cdot\lg P(d=l))}$$
$d$ for feature; $D$ for dataset
- [[Information gain]] divided by the entropy of the dataset $D$ with respect to the feature $d$
- e.g., 
$$GR(Slope, D)=\frac{IG(Slope, D)}{-\sum_{l\in\{flat,moderate,steep\}}(P(Slope=l)\cdot\lg P(Slope=l))}$$

## Drawback
- preferring features that produce uneven splits