---
Created: [[2023-01-02]]
Aliases: 
Types: Card
Tags: 
- 
---
# Optimal binary search tree
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