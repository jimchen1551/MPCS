---
Created: [[2022-12-19]]
Aliases: 
Types: 
Tags: 
- 
---
# Red-black tree
![[Screen Shot 2022-12-20 at 10.26.33.png]]
Attributes:
1. key
2. color
   satisfying the **red-black properties**
   1. Every node is either red or black
   2. The root is black
   3. Every leaf (NIL) is black
   4. If a node is red, then both its children are black
   5. For each node, all simple paths from the node to descendant leaves contain the **same number of black nodes**
3. satellite data
4. left 
5. right 
6. parent
- the number of black nodes on any simple path from, but not including, a node $x$ down to a leaf the **black-height** of the node, denoted $bh(x)$
- having height at most $2\lg(n+1)$ with $n$ internal nodes
## Rotation
