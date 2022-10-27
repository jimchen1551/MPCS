---
Created: [[2022-09-28]]
Aliases: 
Types: Note
Tags: 
- 
---
# Merge sort
![[Pasted image 20221027152436.png]]

## Pseudocode
```Pseudocode
# MERGE(A, p, q, r)
n_L = q - p + 1
n_R = r - q
let L[0:n_L-1] and R[0:n_R-1] be new array
for i = 0 to n_L - 1
	L[i] = A[p+i]
for j = 0 to n_R - 1
	R[j] = A[q+j+1]
i = 0
j = 0
k = p
while i<n_L and j<n_R
	if L[i]<=R[j]
		A[k] = L[i]
		i = i + 1
	else A[k] = R[j]
		j = j + 1
	k = k + 1
while i<n_L
	A[k] = L[i]
	i = i + 1
	k = k + 1
while j<n_R
	A[k] = R[j]
	j = j + 1
	k = k + 1

# MERGE-SORT(A, p, r)
if p>=r
	return
MERGE-SORT(A, p, q)
MERGE-SORT(A, q+1, r)
MERGE(A, p, q, r)
```

[[Divide and conquer]]:
1. **Divide** the subarray `A[p:r]` to be sorted into two adjacent subarrays, each of half the size. To do so, compute the midpoint `q` of `A[p:r]`, and divide `A[p:r]` into subarrays `A[p:q]` and `A[q+1:r]`
2. **Conquer** by sorting each of the two subarrays recursively using merge sort. 
3. **Combine** by merging the two sorted subarrays back into `A[p:r]`

## Loop invariant
- At the start of each iteration of the `for` loop of lines 12~17, the subarray `A[p:k-1]` contains the k-p smallest elements of `L[1:`$n_1$`+1]` and `R[1:`$n_2$ 

## Analysis