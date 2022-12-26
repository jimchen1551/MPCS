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
$$errorDelta(D, w[j])=\frac{\partial}{\partial w[j]}L_2(\mathbf{M}_w, D)=\frac{\partial}{\partial w[j]}\frac{1}{2}\|t-w^Td\|_2^2$$
$$=\sum_{i=1}^n(t_i-w^Td_i)\frac{\partial}{\partial w[j]}(t_i-w^Td_i)=\sum_{i=1}^n(t_i-w^Td_i)\cdot-d_i[j]$$
- **batch gradient descent**: one adjustment is made to each weight at each iteration of the algorithm based on summing the squared error
## Learning rate
![[Screen Shot 2022-12-26 at 19.20.44.png|500]]
- based on rules of thumb or trial and error
- **learning rate decay**: starting with a larger learning rate and then decaying according to a prespecified schedule
  e.g., $\alpha_t=\alpha_0\frac{c}{c+t}$, where $c$ is a control parameter for rate decay
