---
Created: [[2022-10-31]]
Aliases: 
Types: Card
Tags: 
- 
---
# Priority queue
- a data structure for maintaining a set $S$ of elements, each with an associated value called a **key**
- implemented by [[Heap sort]]
## Max-priority queue
```Pseudocode
HEAP-MAXIMUM(A)
return A[1]

HEAP-EXTRACT-MAX(A)
if heap-size<1
	then error "heap underflow"
max = A[1]
A[1] = A[A.heap-size]
A.heap-size -= 1
MAX-HEAPIFY(A, 1)
return max

HEAP-INCREASE-KEY(A, i, key)
if key<A[i]
	then error "new key is smaller than current key"
A[i] = key
while i>1 and A[Parent(i)]<A[i]
	exchange A[i] with A[Parent(i)]
	i = Parent(i)

MAX-HEAP-INSERT(A, key)
A.heap-size += 1
A[A.heap-size] = -inf
HEAP-INCREASE-KEY(A, A.heap-size, key)
```
1. `HEAP-MAXIMUM`: $\Theta(1)$
2. `HEAP-EXTRACT-MAX`: $O(\lg n)$
3. `HEAP-INCREASE-KEY`: $O(\lg n)$
4. `MAX-HEAP-INSERT`: $O(\lg n)$
## Min-priority queue