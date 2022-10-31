---
Created: [[2022-10-30]]
Aliases: 
Types: Card
Tags: 
- 
---
# Heap
![[Pasted image 20221031110731.png]]
- an array object that can be viewed as a nearly complete binary tree
- commonly used in priority queues
```Pseudocode
Parent(i)
	return floor(i/2)
Left(i)
	return 2*i
Right(i)
	return 2*i+1
```
## Max-heap
- The **max-heap property** is that for every node i other than the root, 
  $A[Parent(i)]\geq A[i]$
- The largest element in a max-heap is stored at the root
## Min-heap
- The **min-heap property** is that for every node i other than the root, 
  $A[Parent(i)]\leq A[i]$
- The smallest element in a min-heap is stored at the root
