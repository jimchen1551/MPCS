---
Created: [[2022-12-17]]
Aliases: 
Types: 
Tags: 
- 
---
# Binary search tree
![[Screen Shot 2022-12-17 at 10.09.41.png|500]]
Attributes: 
1. key
   satisfying the **binary-search-tree property**
   Let $x$ be a node in a binary search tree. 
   If $y$ is a node in the left subtree of $x$, then $y.key\leq x.key$. 
   If $y$ is a node in the right subtree of $x$, then $y.key\geq x.key$. 
2. satellite data
3. left
4. right 
5. parent
## Inorder tree walk
```Pseudocode
INORDER-TREE-WALK(x)
if x!=NIL
	INORDER-TREE-WALK(x.left)
	visit x.key
	INORDER-TREE-WALL(x.right)
```
- visiting all the keys in **sorted** order by a simple recusive algorithm because of binary-search-tree property
- visiting the root b/w visiting its left subtree and its right subtree (so called inorder)
- taking $\Theta(n)$ time to walk an $n$-node binary search tree
## Tree search
```Pseudocode
TREE-SEARCH(x, k)
if x==NIL or k==x.key
	return x
if k<x.key
	return TREE-SEARCH(x.left, k)
else return TREE-SEARCH(x.right, k)

ITERATIVE-TREE-SEARCH(x, k)
while x!=NIL and k!=x.key
	if k<x.key
		x = x.left
	else x = x.right
return x
```
- running in $O(h)$ time, where $h$ is the height of the tree
## Tree minimum and maximum
```Pseudocode
TREE-MINIMUM(x)
while x.left!=NIL
	x = x.left
return x

TREE-MAXIMUM(x)
while x.right!=NIL
	x = x.right
return x
```
- running in $O(h)$ time, where $h$ is the height of the tree
## Tree successor and predecessor
```Pseudocode
TREE-SUCCESSOR(x)
if x.right!=NIL
	return TREE-MINIMUM(x.right)
y = x.p
while y!=NIL and x==y.right
	x = y
	y = y.p
return y
```
- the successor of a node is the next node visited in an inorder tree walk
- running in $O(h)$ time, where $h$ is the height of the tree
## Tree insert
![[Screen Shot 2022-12-19 at 13.02.21.png]]
```Pseudocode
TREE-INSERT(T, z)
x = T.root
y = NIL
while x!=NIL
	y = x
	if z.key<x.key
		x = x.left
	else x = x.right
z.p = y
if y==NIL
	T.root = z
else if z.key
	y.left = z
else y.right = z
```
- the pointer $x$ tracing a simple path downward looking for a NIL to replace with the input node $z$
- maintaining the **trailing pointer** $y$ as the parent of $x$
- running in $O(h)$ time, where $h$ is the height of the tree
## Tree delete
![[Screen Shot 2022-12-19 at 13.04.34.png|500]]
```Pseudocode
TREE-DELETE(T, z)
if z.
```
Case 1: If the node has no child
Case 2: If the node has only a single child
Case 3: If the node has two children