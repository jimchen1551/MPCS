---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multinominal logistic regression
![[Screen Shot 2022-12-26 at 20.36.26.png|500]]
$$\mathbf{M}_{wi}(d)=logistic(w_i\cdot d)\text{, where }i\in[1,r]$$

- for more than 2 categories to separate
- using a set of **one-versus-all** models (if we have $r$ target levels, create $r$ logistic regression models)