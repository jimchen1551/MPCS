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
- more accurate if the prior probability is known
$$P(t=l|q[1],\dots,q[m])=\eta\cdot P(q[1],\dots,q[m]|t=l)P(t=l)$$
## Maximum likelihood
$$\mathbf{M}(q)=\arg\max_{l\in levels(t)}P(q[1],\dots,q[m]|t=l)$$
- aka **ML** prediction
- returning the target level with the highest conditional probability given the state of the descriptive features in the query
## Minimum description length
$$h_{MDL}=\arg\min_{h\in H}L_{C1}(h)+L_{C2}(D|h)$$
, where $L_C(x)$ is the description length of $x$ under coding $C$; 
$L_{C1}(h)=$ # bits to describe a [[Decision tree]] $h$; 
$L_{C2}(D|h)=$ # bits to describe training data $D$ given $h$; 
- aka **MDL** principle
- preferring the simplest hypothesis