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
![[Screen Shot 2022-12-20 at 12.50.33.png|500]]
![[Screen Shot 2022-12-20 at 12.59.50.png|500]]
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
else x.parent.right = y
y.left = x
x.parent = y
```
- a local operation preserves the **binary-search-tree property**
- changing the pointer structure
## Insertion
![[Screen Shot 2022-12-20 at 14.08.12.png|500]]
Case 1: z's uncle y is red
![[Screen Shot 2022-12-20 at 14.09.31.png|500]]
Case 2: z's uncle y is black and z is a right child
Case 3: z's uncle y is black and z is a left child
![[Screen Shot 2022-12-20 at 14.10.14.png|500]]
```Pseudocode
RB-INSERT(T, z)
x = T.root
y = T.nil
while x!=T.nil
	y = x
	if z.key<x.key
		x = x.left
	else x = x.right
z.p = y
if y==T.nil
	T.root = z
else if z.key<y.key
	y.left = z
else y.right = z
z.left = T.nil
z.right = T.nil
z.color = RED
RB-INSERT-FIXUP(T, z)

RB-INSERT-FIXUP(T, z)
while z.parent.color==RED
	if z.parent==z.parent.parent.left
		y = z.parent.parent.right
		if y.color==RED
			z.parent.color = BLACK
			y.color = BLACK
			z.parent.parent.color = RED
			z = z.parent.parent
		else
			if z==z.parent.right
				z = z.parent
				LEFT-ROTATE(T, z)
			z.parent.color = BLACK
			z.parent.parent.color = RED
			RIGHT-ROTATE(T, z.parent.parent)
	else
		y = z.parent.parent.left
		if y.color==RED
			z.parent.color = BLACK
			y.color = BLACK
			z.parent.parent.color = RED
			z - z.parent.parent
		else
			if z==z.parent.left
				z = z.parent
				RIGHT-ROTATE(T, z)
			z.parent.color = BLACK
			z.parent.parent.color = RED
			LEFT-ROTATE(T, z.parent.parent)
T.root.color = BLACK
```
- differing TREE-INSERT in 4 ways
  1. T.nil replaces all instances of NIL in TREE-INSERT
  2. lines 14-15 set z.left and z.right to T.nil, in order to maintain the proper tree structure
  3. line 16 colors z red
  4. because coloring z red may cause a violation of one of the red-black properties, line 17 calls RB-INSERT-FIXUP(T, z) in order to restore the red-black properties
## Deletion
```Pseudocode
RB-TRANSPLANT(T, u, v)
if u.p==T.nil
	T.root = v
else if u==u.p.left
	u.p.left = v
else u.p.right = v
v.p = u.p

RB-DELETE(T, z)
y = z
y-original-color = y.color
if z.left==T.nil
	x = z.right
	RB-TRANSPLANT(T, z, t.right)
else if z.right==T.nil
	x = z.left
	RB-TRANSPLANT(T, z, z.left)
else
	y = TREE-MINIMUM(z.right)
	y-original-color = y.color
	x = y.right
	if y.p==z
		x.p = y
	else
		RB-TRANSPLANT(T, y, y.right)
		y.right = z.right
		y.right.p = y
	RB-TRANSPLANT(T, z, y)
	y.left = z.left
	y.left.p = y
	y.color = z.color
if y-original-color==BLACK
	RB-DELETE-FIXUP(T, x)

RB-DELETE-FIXUP(T, x)
while x!=T.root and x.color==BLACK
	if x==x.p.left
		w = x.p.right
		if w.color==RED
			w.color = BLACK
			x.p.color = RED
			LEFT-ROTATE(T, x, p)
			w = x.p.right
		if w.left.color==BLACK and w.right.color==BLACK
			w.color = RED
			x = x.p
		else if w.right.color==BLACK
			w.left.color = BLACK
			w.color = RED
			RIGHT-ROTATE(T, w)
			w = x.p.right
		w.color = x.p.right
		x.p.color = BLACK
		w.right.color = BLACK
		LEFT-ROTATE(T, x.p)
		x = T.root
	else ()
```
- taking $O(\lg n)$ time