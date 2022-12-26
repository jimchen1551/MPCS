---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Gradient descent
$$\frac{\partial}{\partial w[j]}L_2(\mathbf{M}_w, D)=\frac{\partial}{\partial w[j]}\frac{1}{2}\|t-w^Td\|_2^2$$
$$=\sum_{i=1}^n(t_i-w^Td_i)\frac{\partial}{\partial w[j]}(t_i-w^Td_i)=\sum_{i=1}^n(t_i-w^Td_i)\cdot-d_j^i$$
