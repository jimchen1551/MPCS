---
Created: [[2022-10-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Recursion-tree method
$$T(n)=3T(n/4)+\Theta(n^2)$$
![[Screen Shot 2022-10-25 at 13.40.06.png|500]]
$$T(n)=T(n/3)+T(2n/3)+\Theta(n)$$
![[Screen Shot 2022-10-25 at 13.55.18.png|500]]
- sometimes [[Substitution method]] doesn't work (hard to guess)
- each node represents the cost of a single subproblem somewhere in the set of recursive function invocations
1. summing the costs within each level of the tree to obtain the per-level costs (each level of combine)
2. summing all the per-level costs to determine the total cost of all levels of the recursion (total combine)

[Medium explained](https://mycollegenotebook.medium.com/時間複雜度-遞迴-上-f6d51a462394)
