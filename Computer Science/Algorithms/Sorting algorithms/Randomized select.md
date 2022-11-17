---
Created: [[2022-11-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Randomized select
![[Screen Shot 2022-11-17 at 09.22.25.png]]
- selecting the $i$th smallest element of the array $A[p:r]$

## Pseudocode
```Pseudocode
RANDOMIZED-SELECT(A, p, r, i)
if p==r
	return A[p]
q = RANDOMIZED-PARTITION(A, p, r)
k = q - p + 1
if i==k
	return A[q]
else if i<k
	return RANDOMIZED-SELECT(A, p, q-1, i)
else
	return RANDOMIZED-SELECT(A, q+1, r, i-k)
```

## Loop invariant

## Analysis
Indicator random variable: 
$$X_k=I\{\text{the subarray A[p:q] has exactly k elements}\}$$
$$E[X_k]=\frac{1}{n}$$
$$X_k=1\Rightarrow\text{exactly one value of k}$$
$$T(n)\leq\sum_{k=1}^nX_k\cdot(T(max(k-1, n-k))+O(n))$$
$$=\sum_{k=1}^n(X_k\cdot T(max(k-1, n-k))+O(n))$$
$$E[T(n)]\leq E[\sum_{k=1}^n(X_k\cdot T(max(k-1, n-k))+O(n))]$$
$$=\sum_{k=1}^n\frac{1}{n}E[T(max(k-1, n-k))]+O(n)$$
$$max(k-1, n-k)=\begin{cases}
k-1&\quad\text{if }k>\lceil n/2\rceil\\
n-k&\quad\text{if }k\leq\lfloor n/2\rfloor\end{cases}$$
$$\Rightarrow E[T(n)]\leq\frac{2}{n}\sum_{k=\lfloor n/2\rfloor}^{n-1}E[T(k)]+O(n)=\frac{2}{n}\sum_{k=\lfloor n/2\rfloor}^{n-1}ck+an=O(n)\text{, for }n\geq\frac{2c}{c-4a}$$

[[Average case]] running time: 
$$T(n)=O(n)$$

[[Worst case]] running time:
$$T(n)=\Theta(n^2)$$
