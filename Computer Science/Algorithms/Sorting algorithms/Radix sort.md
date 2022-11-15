---
Created: [[2022-11-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Radix sort
![[Screen Shot 2022-11-15 at 09.20.41.png]]

## Pseudocode
```Pseudocode
RADIX-SORT(A, n, d)
for i=1 to d
	STABLE-SORT(A[1:n] on digit i)
```

## Loop invariant
1. **Initialization**
2. **Maintenance**
3. **Termination**

## Analysis
- given $n$ $d$-digit numbers in which each digit can take up to $k$ possible values, it correctly sorts these numbers in $\Theta(d(n+k))$
- when $d$ is constant and $k=O(n)$, it runs in linear time
- given $n$ $b$-bit numbers and any positive integer $r\leq b$, it correctly sorts these numbers in $\Theta((b/r)(n+2^r))$ if the stable sort it uses takes $\Theta(n+k)$ for inputs in the range 0 to $k$
