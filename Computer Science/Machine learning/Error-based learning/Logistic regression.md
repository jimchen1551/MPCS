---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Logistic regression
![[Screen Shot 2022-12-26 at 20.05.05.png|600]]
![[Screen Shot 2022-12-26 at 20.07.10.png|600]]
$$\mathbf{M}_w(d)=logistic(w\cdot d)$$
- [[gradient descent]] works
$$errorDelta(D, w[j])=\frac{\partial}{\partial w[j]}L_2(logistic(w\cdot d), D)$$
$$=(t-logistic(w\cdot d))\cdot logistic(w\cdot d)(1-logistic(w\cdot d))\cdot d[j]$$
