---
Created: [[2022-12-26]]
Aliases: 
Types: Note
Tags: 
- 
---
# Dynamic programming
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
→ $r_n=max(p_n, r_1+r_{n-1}, r_2)
## Matrix-chain multiplication

## Longest common subsequence

## Optimal binary search tree
