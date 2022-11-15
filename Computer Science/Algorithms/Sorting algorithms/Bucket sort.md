---
Created: [[2022-11-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bucket sort
![[Screen Shot 2022-11-15 at 10.32.51.png]]

## Pseudocode
```Pseudocode
BUCKET-SORT(A, n)
let B[0:n-1] be a new array
for i=0 to n-1
	make B[i] an empty list
for i=1 to n
	insert A[i] into B[floor(n*A[i])]
for i=0 to n-1
	sort list B[i] with insertion sort
concatenate the list B[0], B[1], ..., B[n-1] together in order
return the concatenated lists
```

## Loop invariant
1. **Initialization**
2. **Maintenance**
3. **Termination**

## Analysis
