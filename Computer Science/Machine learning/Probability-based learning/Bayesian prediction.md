---
Created: [[2022-11-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bayesian prediction
## False positive paradox
![[Pasted image 20221125132819.png|400]]
- test having a low probability of giving false positive gives more false positives than true positives overall
## Maximum a posteriori
$$\mathbf{M}(q)=\arg\max_{l\in levels(t)}P(t=l|q[1],\dots,q[m])$$
- aka **MAP** prediction
- returning the target level with the highest posterior probability given the state of the descriptive features in the query
$$P(t=l|q[1],\dots,q[m])=\eta\cdot P(q[1],\dots,q[m]|t=l)P(t=l)$$
