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
![[Screen Shot 2022-12-20 at 12.50.33.png]]
```Pseudocode
LEFT-ROTATION(T, x)
y = x.right
x.right = y.left
if y.left!=T.nil
	y.left.parent = x
y.parent = x.parent
if x.parent==T.nil
	T.root = y
else if x==x.parent.left
	x.parent.left = y
else x.parent.ri
```
- a local operation preserves the **binary-search-tree property**
- changing the pointer structure