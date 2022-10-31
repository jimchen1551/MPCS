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
## Loop invariant

## Analysis
$$T_{wc}(n)=\Theta(n^2)$$
$$T_{ac}(n)=\Theta(n\lg n)$$
