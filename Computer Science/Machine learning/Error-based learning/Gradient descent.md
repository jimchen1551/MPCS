---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Gradient descent
![[Screen Shot 2022-12-26 at 18.28.50.png]]
$$\frac{\partial}{\partial w[j]}L_2(\mathbf{M}_w, D)=\frac{\partial}{\partial w[j]}\frac{1}{2}(t-\mathbf{M}_w(d))^2=\frac{\partial}{\partial w[j]}\frac{1}{2}\|t-w^Td\|_2^2$$
$$=(t-w^Td)\frac{\partial}{\partial w[j]}(t-w^Td)=(t-w^Td)\cdot-d[j]$$
