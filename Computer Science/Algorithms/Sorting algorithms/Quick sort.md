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

HOARE-PARTITION(A, p, r)
x = A[p]
i = p - 1
j = r + 1
while TRUE
	repeat
		j -= 1
	until A[j]<=x
	repeat
		i += 1
	until A[i]>=x
	if i<j
		exchange A[i] with A[j]
	else return j

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
   When $A[j]>x$, the only action in the loop is to increment $j$. After incrementation, the second condition holds for $A[j-1]$ and all other entries remain unchanged. When $A[j]\leq x$, the loop increments $i$, swaps $A[i]$ and $A[j]$, and then increments $j$. Because of the swap, we now have that $A[i]\leq x$, and condition 1 is satisfied. Similarly, we also have that $A[j-1]>x$, since the item that was swapped into $A[j-1]$ is, by the loop invariant, greater than $x$. 
   ![[Screen Shot 2022-10-31 at 14.13.22.png]]
3. **Termination**: 
   At termination, $j=r$
## Analysis
$$T_{wc}(n)=\Theta(n^2)$$
$$T_{ac}(n)=\Theta(n\lg n)$$
