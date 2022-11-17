---
Created: [[2022-11-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Select
![[Screen Shot 2022-11-17 at 09.51.45.png]]
Steps: 
- dividing the $n$ elements of the input array into $\lfloor n/5\rfloor$ groups of 5 elements each and at most one group made up of the remaining $n \mod5$ elements'
- finding the median of each of the $\lceil n/5\rceil$ groups by first insertion sorting the elements of each group and then picking its median
- using SELECT recursively to find the median $x$ of the medians found in previous step
- partitioning the input array around the median-of-medians $x$ using a modified version of partiotion
- letting $k$ be the number of elements on the lower side of the partition, so that $x$ is the $k$th smallest element and there are $n-k$ elements on the high side of the partition
- if $i=k$, then return $x$
- otherwise, using SELECT recursively to find the $i$th smallest element on the low side if $i<k$, or $i-k$th smallest element on the high side if $i>k$

## Pseudocode
```Pseudocode
SELECT(A, p, r, i)
while (r-p+1) mod 5 != 0
	for j=p+1 to r
		if A[p]>A[j]
			exchange A[p] with A[j]
	if i==1
		return A[p]
	p = p + 1
	i = i - 1
g = (r - p + 1)/5
for j=p to p+g-1
	sort {A[j], A[j+g], A[j+2g], A[j+3g], A[j+4g]} in place
x = SELECT(A, p+2g, p+3g-1, ceil(g/2))
q = PARTITION-AROUND(A, p, r, x)
k = q - p + 1
if i==k
	return A[q]
else if i<k
	return SELECT(A, p, q-1, i)
else
	return SELECT(A, q+1, r, i-k)
```

## Loop invariant

## Analysis
- the number of elements greater than $x$ is at least $3n/10-6$
$$T(n)\leq\begin{cases}$$