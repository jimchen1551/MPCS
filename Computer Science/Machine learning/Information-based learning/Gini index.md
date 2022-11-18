---
Created: [[2022-11-18]]
Aliases: 
Types: Card
Tags: 
- 
---
# Gini index
$$Gini(t, D)=1-\sum_{l\in levels(t)}P(t=l)^2$$
$t$ for target feature; $D$ for dataset
- calculating how often the target levels of instances in a dataset misclassified in prediction
- $IG(d, D)=Gini(t, D)-\sum_{l\in levels(d)}\frac{|D_{d=l}|}{|D|}\cdot Gini(t, D_{d=l})$
