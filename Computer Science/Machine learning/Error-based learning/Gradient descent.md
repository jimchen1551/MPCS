---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Gradient descent
![[Screen Shot 2022-12-26 at 18.28.50.png|500]]
```Pseudocode
Require: a set of training instances D
Require: a learning rate alpha
Require: a function, errorDelta
Require: a convergence criterion
w ← random starting point in the weight space
repeat
	for each w[j] in w do
		w[j] ← w[j]+alpha*errorDelta(D, w[j])
until convergence occurs
```
![[Screen Shot 2022-12-26 at 18.45.35.png|500]]
$$\frac{\partial}{\partial w[j]}L_2(\mathbf{M}_w, D)=\frac{\partial}{\partial w[j]}\frac{1}{2}(t-\mathbf{M}_w(d))^2=\frac{\partial}{\partial w[j]}\frac{1}{2}\|t-w^Td\|_2^2$$
$$=(t-w^Td)\frac{\partial}{\partial w[j]}(t-w^Td)=(t-w^Td)\cdot-d[j]$$
