---
Created: [[2022-11-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Counting sort
![[Screen Shot 2022-11-15 at 09.05.40.png]]
## Pseudocode
```Pseudocode
COUNTING-SORT(A, n, k)
let B[1:n] and C[0:k] be new arrays
for i=0 to k
	C[i] = 0
for j=1 to n
	C[A[j]] = C[A[j]] + 1
for i=1 to k
	C[i]
```
## Loop invariant
## Analysis