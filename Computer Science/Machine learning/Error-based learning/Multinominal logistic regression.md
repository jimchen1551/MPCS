---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multinominal logistic regression
![[Screen Shot 2022-12-26 at 20.36.26.png|500]]
![[Screen Shot 2022-12-26 at 20.48.41.png|500]]
$$\mathbf{M}_{wi}(d)=logistic(w_i\cdot d)\text{, where }i\in[1,r]$$
$$\mathbf{M}'_{wi}(d)=\frac{\mathbf{M}_{wi}(d)}{\sum_{l\in levels(t)}\mathbf{M}_{wl}(d)}$$
$$L_2(\mathbf{M}_{wk}, D)=\frac{1}{2}\sum_{i=1}^n(t_i-\mathbf{M}_{wk}(d_i[1]))^2$$
$$\mathbf{M}(q)=\arg\max_{l\in levels(t)}\mathbf{M}_{wl}(q)$$
- for more than 2 categories to separate
- using a set of **one-versus-all** models (if we have $r$ target levels, create $r$ logistic regression models) and normalizing their results