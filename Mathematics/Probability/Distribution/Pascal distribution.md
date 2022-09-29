---
Created: [[2022-09-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Pascal distribution
$$X\sim Pascal(k,p)$$
## Discrete form
[[Probability mass function|PMF]]: 
$$p_X(x)=
\begin{cases}
\binom {x-1}{k-1}\cdot(1-p)^{x-k}\cdot p^k & \quad ,x=k, k+1, \dots\\
0 &\quad ,otherwise
\end{cases}$$
[[Cumulative distribution function|CDF]]: 
$$F_X(x)=P(Y\geq k), Y\sim BIN(x, p)$$
