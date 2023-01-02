---
Created: [[2023-01-02]]
Aliases: 
Types: Card
Tags: 
- 
---
# Matrix-chain multiplication problem
- given a sequence $\langle A_1, \dots A_n\rangle$ of $n$ matrices to be multiplied, and we wish to compute the product $A_1A_2\dots A_n$
- **fully parenthesized**: a product of matrices is fully parenthesized if it is either a single matrix or the product of 2 fully parenthesized matrix products
- determine an order for multiplying matrices that has the lowest cost

- Naive method: counting the number of parenthesizations
  - let $P(n)$ denote the number of alternative parenthesizations of a sequence of $n$ matrices
  - the split b/w 2 subproducts may occur b/w the $k$th and $k+1$ st matrices, for $k\in[1:n-1]$
  - $P(n)=\begin{cases}1&\text{if }n=1\\\sum_{k=1}^{n-1}P(k)P(n-k)&\text{if }n\geq 2\end{cases}$
  - the solution to the recurrence is $\Omega(2^n)$

- Dynamic programming: 
  Step 1:
  1. adopting $A_{i\dots j}$, where $i\leq j$, for the matrix resulting from evaluating the product $A_iA_{i+1}\dots A_j$
  2. supposing that to optimally parenthesize $A_iA_{i+1}\dots A_j$, split the product b/w $A_k$ and $A_{k+1}$
  3. subchains $A_iA_{i+1}\dots A_k$ and $A_{k+1}A_{k+2}\dots A_j$ must be optimal parenthesization respectively
  Step 2: 
  1. determining the minimum cost of a parenthesization of $A_iA_{i+1}\dots A_j$ for $1\leq i\leq j\leq n$
  2. $m[i, j]$: the minimum number of scalar multiplications needed to compute the matrix $A_{i\dots j}$
     $m[i, j]=\begin{cases}0&\text{if }i=j\\\min_{i\leq k<j}(m[i, k]+m[k+1, j]+p_{i-1}p_kp_j)&\text{if }i<j\end{cases}$
  Step 3:
  1. there're relative few distinct subproblems: one subproblem for each choice of $i$ and $j$ satisfying $1\leq i\leq j\leq n$, $C_2^n+n=(n^2)$
  2. implementing the bottom-up method
```Pseudocode
MATRIX-CHAIN-ORDER(p)
n = p.length-1
let m[1:n, 1:n] and s[1:n-1, 2:n] be new tables
for i=1 to n
	m[i, j] = 0
for l=2 to n
	for i=1 to n-l+1
		j = i+l-1
		m[i, j] = infty
		for k=i to j-1
			q = m[i, k]+m[k+1, j]+p_{i-1}p_kp_j
			if q<m[i, j]
				m[i, j] = q
				s[i, j] = k
return m and s
```
  Step 4: 
  1. each entry $s[i, j]$ records a value of $k$ such that an optimal parenthesization of $A_iA_{i+1}\dots A_j$ splits the product b/w $A_k$ and $A_{k+1}$
![[Screen Shot 2022-12-27 at 00.32.00.png|500]]
![[Screen Shot 2022-12-27 at 00.32.54.png|500]]
- Using 2 subproblems
- $j-i$ choices to determine which way yields an optimal solution
→ $T(n)=\Theta(n^2)$