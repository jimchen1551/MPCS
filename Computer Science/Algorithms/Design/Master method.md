---
Created: [[2022-10-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Master method
Dealing with: 
$$T(n)=aT(n/b)+f(n)\text{ s.t. }a\geq1, b>1$$
where $f(n)$ is an asymptotically function
e.g., [[Strassen's algorithm]]: a=7, b=2, $f(n)=\Theta (n^2)$

[Medium explained](https://mycollegenotebook.medium.com/時間複雜度-遞迴-下-master-th-307ad4608ab6)

## Master theorem
Let $a\geq1$ and $b>1$ be consistants, let $f(n)$ be a function, and let $T(n)$ be defined on the nonnegative integers by the recurrence. 
$$T(n)=aT(n/b)+f(n)$$
Case 1:
$$\frac{f(n)}{n^{\log_ba}}=O(n^{-\epsilon})\rightarrow0\text{ as }n\rightarrow\infty(\because\epsilon>0)$$

Case 2:
$$\frac{f(n)}{n^{\log_ba}}=constant$$

Case 3:
$$\frac{f(n)}{n^{\log_ba}}=\Omega(n^\epsilon)\rightarrow\infty\text{ as }n\rightarrow\infty(\because \epsilon>0)$$
