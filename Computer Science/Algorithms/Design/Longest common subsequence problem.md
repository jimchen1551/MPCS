---
Created: [[2023-01-02]]
Aliases: LCS
Types: Card
Tags: 
- 
---
# Longest common subsequence problem
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