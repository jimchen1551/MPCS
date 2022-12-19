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
## Tree minimum and maximum
## Tree successor and predecessor
## Tree insert
## Tree delete