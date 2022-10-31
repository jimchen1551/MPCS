---
Created: [[2022-10-11]]
Aliases: 
Types: Card
Tags: 
- 
---
# Heap sort
![[Pasted image 20221031111237.png]]
- utilizing max-[[Heap]] to manage info
- like [[Merge sort]], it's running time is $O(n\lg n)$
- like [[Insertion sort]], it sorts in place
## Psuedocode
```Pseudocode
MAX-HEAPIFY(A, i)
l = Left(i)
r = Right(i)
if l<=A.heap-size and A[l]>A[i]
	largest = l
else largest = i
if r<=A.heap-size and A[r]>A[largest]
	largest = r
if largest!=i
	exchange A[i] with A[largest]
	MAX-HEAPIFY(A, largest)

BUILD-MAX-HEAP
HEAP-SORT(A, n)

```
- MAX-HEAPIFY: running in $O(\lg n)$ , the key to **maintaining** the max-heap property
- BUILD-MAX-HEAP: running in linear time, producing a max-heap from an **unordered** input array
- HEAP-SORT: running in $O(n\lg n)$, sorting an array in place