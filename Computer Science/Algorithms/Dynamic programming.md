---
Created: [[2022-12-26]]
Aliases: 
Types: Note
Tags: 
- 
---
# Dynamic programming
- **time-memory trade-off**: using additional memory to save computation time
- solving problems by combining the solutions to subproblems
- solving every subsubproblems just once and saving its answer in a table
- programming here means a **tabular method**
- used for the optimization problem
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information
## Rod cutting problem
- given a rod of length $n$ inches and a table of prices $p_i$, for $i=1, 2, \dots, n$
- determine the maximum revenue $r_n$ obtainable by cutting up the rod and selling the pieces
- rod lengths are always an integral number of inches
![[Screen Shot 2022-12-26 at 22.35.52.png|500]]
- there're $2^{n-1}$ different ways to cut a rod
- an optimal solution cuts the rod into $k$ pieces, for some $1\leq k\leq n$, then
  - $n=i_1+i_2+\dots+i_k$
  - $r_n=p_{i1}+p_{i2}+\dots+p_{ik}$
![[Screen Shot 2022-12-26 at 22.59.59.png|500]]
→ $r_n=\max_{1\leq i\leq n}(p_i+r_{n-i})$
- **Optimal substructure**: optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently. 
### Top-down method with memoization
```Pseudocode
MEMOIZED-CUT-ROD(p, n)
let r[0:n] be a new array
for i=0 to n
	r[i] = -infty
return MEMOIZED-CUT-ROD-AUX(p, n, r)

MEMOIZED-CUT-ROD-AUX(p, n, r)
if r[n]>=0
	return r[n]
if n==0
	q = 0
esle 
	q = -infty
	for i=1 to n
		q = max(q, p[i]+MEMOIZED-CUT-ROD-AUX(p, n-i, r))
r[n] = q
return q
```
- writing the procedure recursively in a natural manner, but modified to save the result of each subproblem
### Bottom-up method
```Pseudocode
BOTTOM-UP-CUT-ROD(p, n)
let r[0:n] be a new array
r[0] = 0
for j=1 to n
	q = -infty
	for i=1 to j
		q = max(q, p[i]+r[j-i])
	r[j] = q
return r[n]

EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
let r[0:n] and s[0:n] be new arrays
r[0] = 0
for j=1 to n
	q = -infty
	for i=1 to j
		if q<p[i]+r[j-1]
			q = p[i]+r[j-1]
			s[j] = i
	r[j] = q
return r and s
```
- solving any particular subproblem depends only on solving smaller subproblems
- extended method record not only the optimal value but also the choice that led to the optimal value
### Subproblem graph
![[Screen Shot 2022-12-26 at 23.17.34.png]]
- describing the set of subproblems involved and how subproblems depend on one another
- the time to compute the solution to a subproblem si proportional to the degree of the corresponding vertex in the subproblem graph
- the number of subproblems is equal to the number of vertices in the subproblem graph
- the running time of dynamic programming is linear in the number of vertices and edges
## Matrix-chain multiplication problem
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
## Longest common subsequence

## Optimal binary search tree
