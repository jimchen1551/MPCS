---
Created: [[2022-09-28]]
Aliases: big-omega notation
Types: Card
Tags: 
- 
---
# Lower bound
$$T_{bc}(n)=\Omega(f(n))$$
$$\Omega(f(n))=g(n)\ \exists\ c \text{ and } n_0 \text{ such that }0\leq c\cdot f(n)\leq g(n)\ \forall n\geq n_0$$
- considering only the leading term of the [[Best case]] running time
## small-omega notation
- While the lower bound isn't asymptotically tight, 
$$\omega(f(n))=g(n)\ \forall c>0\ \exists\  n_0>0 \text{ such that }0\leq c\cdot f(n)\leq g(n)\ \forall n\geq n_0$$
$$\omega(f(n))=g(n)\Leftrightarrow \lim_{n\to\infty}\frac{g(n)}{f(n)}=\infty$$
