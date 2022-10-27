---
Created: [[2022-09-28]]
Aliases: 
Types: Card
Tags: 
- 
---
# Insertion sort
## Pseudocode
![[Screen Shot 2022-10-11 at 11.33.40.png]]
```Pseudocode
INSERTIONSORT(A, n)
for i = 2 to n
	key = A[i]  \\ picking ith card as key
	j = i - 1   \\ previous card number j
	while j>0 and A[j]>key \\ visiting previous cards
		A[j+1] = A[j]      \\ making space for key
		j = j - 1          \\ previous card number
	A[j+1] = key           \\ stopped at smaller card
```

## Loop invariant
- At the start of each iteration of the `for` loop of lines 1~8, the subarray `A[1:i-1]` consists of the elements originally in `A[1:i-1]`, but in sorted order. 
1. Initialization: 
   when `i=2`, `A[1:i-1]=A[1]` → sorted, and  in original `A[1]`
2. Maintenance: 
   the body of `for` loop only moves the values in `A[1:`
3. Termination

## Analysis

