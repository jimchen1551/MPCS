---
Created: [[2022-09-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Uniform distribution
$$X\sim\text{UNIF}(m, n)$$
## Discrete form
[[Probability mass function|PMF]]: 
$$p_X(x)=
\begin{cases}
\frac{1}{n-m+1} & \quad x\in [m, n]\\
0 & \quad \text{otherwise}
\end{cases}$$
[[Cumulative distribution function|CDF]]: 
$$F_X(x)=
\begin{cases}
0 & \quad x<m\\
\frac{\lfloor x\rfloor-m+1}{n-m+1} & \quad m\leq x<n\\
1 & \quad n\leq x
\end{cases}
$$

## Continuous form
[[Probability density function|PDF]]: 
$$f_X(x)=
\begin{cases}
\frac{1}{n-m} & \quad m\leq x\leq n\\
0 & \quad \text{otherwise}
\end{cases}$$
[[Cumulative distribution function|CDF]]: 
$$F_X(x)=
\begin{cases}
0 & \quad x\leq m\\
\frac{x-m}{n-m} & \quad m< x\leq n\\
1 & \quad n< x
\end{cases}
$$
