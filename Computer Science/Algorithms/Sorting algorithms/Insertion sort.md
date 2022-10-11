---
Created: [[2022-09-28]]
Aliases: 
Types: Card
Tags: 
- 
---
# Insertion sort
![[Screen Shot 2022-10-11 at 11.33.40.png]]
```Pseudocode
INSERTIONSORT(A, n)
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