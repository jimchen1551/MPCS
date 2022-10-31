---
Created: [[2022-10-31]]
Aliases: 
Types: Card
Tags: 
- 
---
# Quick sort
![[Pasted image 20221031135130.png]]
- sorting in place
## Pseudocode
```Pseudocode
PARTITION(A, p, r)
x = A[r]
i = p - 1
for j = p to r - 1
	if A[j]<=x
		i = i + 1
		exchange A[i] with A[j]
exchange A[i+1] with A[r]
return i+1

QUICKSORT(A, p, r)
if p<r
	q = PARTITION(A, p, r)
	QUICKSORT(A, p, q-1)
	QUICKSORT(A, q+1, r)
```
- based on [[Divide and conquer]]
  1. **Divide**: partitioning A[p:r] into A[p:q-1] and A[q+1:r], such that A[p:q-1] is less than or equal to A[q] and A[q] is less than or equal to A[q+1:r]
  2. **Conquer**: sorting A[p:q-1] and A[q+1:r] by recursive calls to quick sort
  3. **Combine**: no work is needed to combine them
![[Screen Shot 2022-10-31 at 14.03.42.png]]
## Loop invariant
1. $\text{if } p\leq k\leq i,\text{then }A[k]\leq x$
2. $\text{if } i+1\leq k\leq j-1, \text{then }A[k]>x$
3. $\text{if }k=r,\text{then }A[k]=x$

1. **Initialization**: 
   Prior to the first iteration of the loop, we have $i=p-1$ and $j=p$. Because no values b/w $p$ and $i$, and no values b/w $i+1$ and $j-1$, the first 2 conditions are trivially satisfied. 
2. **Maintenance**: 
   
   ![[Screen Shot 2022-10-31 at 14.13.22.png]]
3. **Termination**: 
   At termination, $j=r$
## Analysis
$$T_{wc}(n)=\Theta(n^2)$$
$$T_{ac}(n)=\Theta(n\lg n)$$
