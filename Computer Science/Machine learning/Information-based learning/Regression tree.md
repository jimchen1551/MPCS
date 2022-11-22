---
Created: [[2022-11-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Regression tree
$$var(t, D)=\frac{\sum_{i=1}^n(t_i-\bar{t})^2}{n-1}$$
$$\text{d}_{[best]}=\arg \min_{d\in\text{d}}\sum_{l\in levels(d)}\frac{|D_{d=l}|}{|D|}\times var(t, D_{d=l})$$
- similar to a [[decision tree]]
- different feature selection criteria for splitting a node
- [[Shannon's entropy model]] → variance
- reducing variance to improve the purity of subdataset