---
Created: [[2022-11-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Select
![[Screen Shot 2022-11-17 at 09.51.45.png]]

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
	
```
## Loop invariant

## Analysis