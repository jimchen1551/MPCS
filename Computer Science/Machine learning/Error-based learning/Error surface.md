---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Error surface
![[Screen Shot 2022-12-26 at 17.40.34.png]]
- each pair of weights ($w[0]$ and $w[1]$) represents a point in the **weight space**
- the SSE for the model with the weight determines the height of the **error surface**
- for simple problems, it's possible to find the best combination through the **brute-force search**
## Least square optimization
$$\frac{\partial}{\partial w[0]}\frac{1}{2}\sum_{i=1}^n(t_i-\mathbf{M}_w(d_i))^2=0$$
$$\frac{\partial}{\partial w[1]}\frac{1}{2}\sum_{i=1}^n(t_i-\mathbf{M}_w(d_i))^2=0$$
- because we can expect the error surface to be convex and possess a global minimum, we can find the optimal weights at the point where the **partial derivatives** of the error surface with respect to weight are equal to 0. 