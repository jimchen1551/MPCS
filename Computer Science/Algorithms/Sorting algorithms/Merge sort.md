---
Created: [[2022-09-28]]
Aliases: 
Types: Note
Tags: 
- 
---
# Merge sort
![[Pasted image 20221027152436.png]]

## Pseudocode
```Pseudocode
# MERGE(A, p, q, r)
n_L = q - p + 1
n_R = r - q
let L[0:n_L-1] and R[0:n_R-1] be new array
for i = 0 to n_L - 1
	L[i] = A[p+i]
for j = 0 to n_R - 1
	R[j] = A[q+j+1]
i = 0
j = 0
k = p
while i<n_L and j<n_R
	if L[i]<=R[j]
		A[k] = L[i]
		i = i + 1
	else A[k] = R[j]
		j = j + 1
	k = k + 1
while i<n_L
	A[k] = L[i]
	i = i + 1
	k = k + 1
while j<n_R
	A[k] = R[j]
	j = j + 1
	k = k + 1

# MERGE-SORT(A, p, r)
if p>=r
	return
MERGE-SORT(A, p, q)
MERGE-SORT(A, q+1, r)
MERGE(A, p, q, r)
```

[[Divide and conquer]]:
1. **Divide** the subarray `A[p:r]` to be sorted into two adjacent subarrays, each of half the size. To do so, compute the midpoint `q` of `A[p:r]`, and divide `A[p:r]` into subarrays `A[p:q]` and `A[q+1:r]`
2. **Conquer** by sorting each of the two subarrays recursively using merge sort. 
3. **Combine** by merging the two sorted subarrays back into `A[p:r]`

## Loop invariant
- At the start of each iteration of the `for` loop of lines 12~17, the subarray `A[p:k-1]` contains the k-p smallest elements of `L[1:`$n_1$`+1]` and `R[1:`$n_2$`+1]`, in sorted order.  
1. **Initialization**: 
   The loop invariant holds prior to the first iteration of the loop. Here,` i = j = 1`, and S is completely empty. `L[1]` is the smallest element of `L`, while `R[1]` is the smallest element of `R`, so the initialization step holds.
2. **Maintenance**: 
   To see that each iteration maintains the loop invariant, suppose without loss of generality that `L[i] ≤ R[j]`. Then `L[i]` is the smallest element not yet copied to S. The current nonempty part of S consists of the `k − 1` smallest elements, so after the loop is over and `L[i]` is copied to S, the nonempty part of S will consist of the `k` smallest elements. Incrementing `k` (in the for loop update) and `i` reestablishes the loop invariant for the next iteration.
3. **Termination**: 
   At termination, `k = m + 1`. By the loop invariant, S contains the `m` smallest elements of `L` and `R`, in sorted order. This is the result that we wanted (i.e. the merging of the two sorted arrays to produce a new sorted array).
[Proof by Stanford](http://web.stanford.edu/class/archive/cs/cs161/cs161.1176/Sections/161-section-1.pdf)

## Analysis
1. Divide: $D(n)=\Theta(1)$
2. Conquer: $2T(n/2)$
3. Combine: $C(n)=\Theta(n)$

