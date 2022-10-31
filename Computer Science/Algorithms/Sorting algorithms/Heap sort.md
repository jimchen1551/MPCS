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

BUILD-MAX-HEAP(A)
A.heap-size = A.length
for i = floor(A.length/2) downto 1
	MAX-HEAPIFY(A, i)

HEAP-SORT(A, n)

```
- `MAX-HEAPIFY`: running in $O(\lg n)$ , the key to **maintaining** the max-heap property
- `BUILD-MAX-HEAP`: running in linear time, producing a max-heap from an **unordered** input array
- `HEAP-SORT`: running in $O(n\lg n)$, sorting an array in place

## Loop invariant
1. `BUILD-MAX-HEAP`
   At the start of each iteration of the for loop, each node $i+1, i+2, \dots, n$ is the root of a max-heap
   1. **Initialization**: 
      Prior to the first iteration of the loop, $i=\lfloor n/2\rfloor$
   2. **Maintenance**: 
      The children of node $i$ are both roots of max-heaps
      `MAX-HEAPIFY(A, i)` makes node $i$ a max-heap root
   3. **Termination**
      At temination $i=0$
## Analysis
1. `MAX-HEAPIFY`
   - The children's subtrees each have size at most 2n/3
   $$T(n)\leq T(2n/3)+\Theta(1)$$
   $$\Rightarrow T(n)=O(\lg n)$$
   2. `BUILD-MAX-HEAP`
      - each call to `MAX-HEAPIFY` cost $O(\lg n)$ time
      - calling $O(n)$ times