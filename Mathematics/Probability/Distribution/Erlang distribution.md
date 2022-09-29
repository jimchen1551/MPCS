---
Created: [[2022-09-21]]
Aliases: Gamma distribution
Types: Card
Tags: 
- 
---
# Erlang distribution
$$X\sim Erlang (n,\lambda)$$
## Continuous form
[[Probability density function|PDF]]: 
$$f_X(x)=
\begin{cases}
\frac{1}{(n-1)!}\lambda^nx^{n-1}e^{-\lambda x}&\quad, x\geq0\\
0 &\quad ,otherwise
\end{cases}$$
[[Cumulative distribution function|CDF]]: 
$$F_X(x)=
\begin{cases}
1-\Sigma_{k=0}^{n-1}\frac{(\lambda x)^k}{k!}e^{-\lambda x}&\quad, x\geq0\\
0 &\quad ,otherwise
\end{cases}$$
