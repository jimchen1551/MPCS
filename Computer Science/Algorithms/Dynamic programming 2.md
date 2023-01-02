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
## Optimal substructure
- optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently. 
  1. A solution to the problem consists of making a choice. Making this choice leaves one or more subproblems to be solved. 
  2. Suppose for a given problem, you are given a choice that leads to an optimal solution. 
  3. Given this choice, determine which subproblems ensue and how to characterize the resulting space of subproblems best. 
  4. Use the **cut-and-paste** technique to show that the solutions to the subproblems used within the optimal solution to the problem must themselves be optimal. 
## Overlapping subproblem
- 2 subproblems overlap if they are the same subproblem that occurs as a subproblem of different problems. 
- Dynamic programming solves each subproblem once and stores the solution in a table where it can be looked up when needed. 
## Cut-and-paste
- Suppose that one of the subproblem solutions is not optimal
- **Cut** it out and **Paste** in an optimal solution. 
- Get a better solution to the original problem. 
## Memoization
- making a table indexed by subproblem
1. lookup in the table
2. if the answer exists, use it
3. else, compute the answer and store it
## Running time
- depending on the product of:
  1. the number of subproblems overall
  2. how many choices to look at for each subproblem
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
- a rod of size $n$ uses just one subproblem
- $n$ choices for $i$ in order to determine which one yields an optimal solution
→ $T(n)=\Theta(n)$
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
![[Screen Shot 2022-12-27 at 00.32.00.png|500]]
![[Screen Shot 2022-12-27 at 00.32.54.png|500]]
- Using 2 subproblems
- $j-i$ choices to determine which way yields an optimal solution
→ $T(n)=\Theta(n^2)$
## Longest common subsequence problem
- aka LCS
- given 2 sequences $X$ and $Y$, find a maximum-length common subsequence of $X$ and $Y$
Step 1: 
- given a sequence $X$, the $i$th prefix of $X$, for $i=1, 2,\dots, m$ is $X_i=\langle x_1, \dots, x_i\rangle$
- Optimal substructure:
  Let $X=X_m$ and $Y=Y_n$ be sequences, and let $Z=Z_k$ be any LCS of $X$ and $Y$
  1. If $x_m=y_n$, then $z_k=x_m=y_n$ and $Z_{k-1}$ is an LCS of $X_{m-1}$ and $Y_{n-1}$
  2. If $x_m\neq y_n$, then $z_k\neq x_m$ implies $Z$ is an LCS of $X_{m-1}$ and $Y$
  3. If $x_m\neq y_n$, then $z_k\neq y_n$ implies $Z$ is an LCS of $X$ and $Y_{n-1}$
Step 2: 
- Let $c[i, j]$ be the length of an LCS of the sequence $X_i$ and $Y_j$
  $c[i, j]=\begin{cases}0&\text{if }i=0\text{ or }j=0\\c[i-1, j-1]+1&\text{if }i, j>0\text{ and }x_i=y_j\\\max(c[i, j-1], c[i-1, j]&\text{if }i, j>0\text{ and }x_i\neq y_j\end{cases}$
Step 3: 
- storing the $c[i, j]$ values in a table $c[0:m, 0:n]$ whose entries are computed in **row-major** order
- $b[i, j]$ points to the table entry corresponding to the optimal subproblem solution chosen when computing $c[i, j]$
![[Screen Shot 2022-12-27 at 06.39.06.png]]
```Pseudocode
LCS-LENGTH(X, Y)
m = X.length
n = Y.length
let b[1:m, 1:n] and c[0:m, 0:n] be new tables
for i=1 to m
	c[i, 0] = 0
for j=0 to n
	c[0, j] = 0
for i=1 to m
	for j=1 to n
		if x_i==y_j
			c[i, j] = c[i-1, j-1]+1
			b[i, j] = "left-up"
		else if c[i-1, j]>=c[i, j-1]
			c[i, j] = c[i-1, j]
			b[i, j] = "up"
		else
			c[i, j] = c[i, j-1]
			b[i, j] = "left"
return c and b
```
→ $T(m, n) = O(mn)$
## Optimal binary search tree
- given a sorted sequence $K=k_1, k_2, \dots, k_n$ of $n$ distinct keys
- to build a [[Binary search tree]] from the keys
- for $k_i$, have probability $p_i$ that a search is for $k_i$
- for unsuccessful search, we have $n+1$ dummy keys $d_0, \dots, d_n$
- for $d_i$, have probability $q_i$
- actual cost = the number of items examined. 
  For key $k_i$, cost = depth_T($k_i$)+1, where depth_T($k_i$) = depth of $k_i$ in [[Binary search tree|BST]]
  $\sum_{i=1}^np_i+\sum_{i=0}^nq_i$
  $E[\text{search cost in T}]=\sum_{i=1}^n(depth_T(k_i)+1)\cdot p_i+\sum_{i=0}^n(depth_T(d_i)+1)\cdot q_i$
  ![[Screen Shot 2022-12-27 at 07.07.03.png]]
  ![[Screen Shot 2022-12-27 at 07.06.51.png]]
Step 1:
Step 2:
Step 3:
Step 4: