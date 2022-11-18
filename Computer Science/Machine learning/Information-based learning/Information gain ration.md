---
Created: [[2022-11-18]]
Aliases: GR, gain ratio
Types: 
Tags: 
- 
---
# Information gain ration
$$GainRatio(D, A)=\frac{IG(D, A)}{SplitInfo(D, A)}$$
$$SplitInfo(D, A)=-\sum_{i=1}^C\frac{|D_i|}{|D|}\cdot\lg\frac{|D_i|}{|D|}$$
, where $D_i$ is subset of $D$ for which $A$ has value $v_i$
## Drawback
- prefering features that produce uneven splits