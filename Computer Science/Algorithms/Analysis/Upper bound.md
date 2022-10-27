---
Created: [[2022-09-28]]
Aliases: big-o notation
Types: Card
Tags: 
- 
---
# Upper bound
$$T_{wc}(n)=O(f(n))$$
$$O(f(n))=g(n)\ \exists\ c \text{ and } n_0 \text{ such that }0\leq g(n)\leq c\cdot f(n)\ \forall n\geq n_0$$
- considering only the leading term of the [[Worst case]] running time
- $g(n)$ is **asymptotically nonnegative**
## little-o notation
- While the upper bound isn't asymptotically tight, 
$$o(f(n))=g(n)\ \forall c>0\ \exists\  n_0>0 \text{ such that }0\leq g(n)< c\cdot f(n)\ \forall n\geq n_0$$
$$o(f(n))=g(n)\Leftrightarrow \lim_{n\to\infty}\frac{g(n)}{f(n)}=0$$
