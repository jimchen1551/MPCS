---
Created: [[2022-11-17]]
Aliases: 
Types: 
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