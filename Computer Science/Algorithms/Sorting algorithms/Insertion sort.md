---
Created: [[2022-09-28]]
Aliases: 
Types: Card
Tags: 
- 
---
# Insertion sort
```Pseudocode
INSERTION-SORT(A, n)
for i = 2 to n
	key = A[i]
	j = i - 1
	while j>0 and A[j]>key
		A[j+1] = A[j]
		j = j - 1
	A[j+1] = key
```
## Loop invariant
## Analysis