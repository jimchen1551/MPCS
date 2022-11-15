---
Created: [[2022-11-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Counting sort
![[Screen Shot 2022-11-15 at 09.05.40.png]]
- assuming all the $n$ input elements integers in the range 0 to $k$
- for each input element $x$, the number of elements less than $x$
- **Stable** property: numbers with the same value appear in the output array in the same order as they do in the input array
- often used as a subroutine in [[Radix sort]]

## Pseudocode
```Pseudocode
COUNTING-SORT(A, n, k)
let B[1:n] and C[0:k] be new arrays
for i=0 to k
	C[i] = 0
for j=1 to n
	C[A[j]] = C[A[j]] + 1
for i=1 to k
	C[i] = C[i] + C[i-1]
for j=n down to 1
	B[C[A[j]]] = A[j]
	C[A[j]] = C[A[j]] - 1
return B
```

## Loop invariant
1. **Initialization**
2. **Maintenance**
3. **Termination**

## Analysis
Running time: 
$$T(n)=\Theta(n)$$