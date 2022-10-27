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
1. **Initialization**: 
   when `i=2`, `A[1:i-1]=A[1]` → sorted, and  in original `A[1]`
2. **Maintenance**: 
   the body of `for` loop only moves the values in `A[i-1]` ... by one position to the right until finding the proper posistion for `A[i]`
   → `A[1:i]` consists of the elements in original `A[1:i]` but sorted
3. **Termination**: 
   `for` loop teminates at `i=n+1`
   → `A[1:n]` consists of the elements in original `A[1:n]` but sorted

## Analysis
![[Screen Shot 2022-10-27 at 14.19.48.png]]
Running time: 
$$T(n)=c_1n+c_2(n-1)+c_4(n-1)+c_5\sum^n_{i=2}t_i+c_6\sum^n_{i=2}(t_i-1)+c_7\sum^n_{i=2}(t_i-1)+c_8(n-1)$$
[[Best case]]: $t_i=1$
$$T_{bc}(n)=(c_1+c_2+c_4+c_5+c_8)n-(c_2+c_4+c_5+c_8)$$
$$T_{bc}=\Theta(n)$$
[[Worst case]]: $t_i=i$
$$T_{wc}(n)=\frac{c_5+c_6+c_7}{2}n^2-(c_1+c_2+c_4+\frac{c_5-c_6-c_7}{2}+c_8)n-(c_2+c_4+c_5+c_8)$$
$$T_{wc}=\Theta(n^2)$$
