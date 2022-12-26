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
return MEMOIZED-CUT
```
- writing the procedure recursively in a natural manner, but modified to save the result of each subproblem
### Bottom-up method
## Matrix-chain multiplication

## Longest common subsequence

## Optimal binary search tree
