---
Created: [[2022-09-28]]
Aliases: 
Types: Note
Tags: 
- 
---
# Merge sort
```Pseudocode
MERGE(A, p, q, r)
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
```
## Loop invariant
## Analysis