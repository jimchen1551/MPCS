---
Created: [[2022-11-25]]
Aliases: 
Types: 
Tags: 
- 
---
# Hash table
- many apps require a dynamic set supporting only the dictionary operations: 
  INSERT, SEARCH ($T_{wc}=\Theta(n), E[T(n)]=O(1)$), and DELETE
  e.g., a [[Compiler]] maintaining a **symbol table**
- an efficient data structure for implementing dictionaries

## Direct addressing
![[Screen Shot 2022-11-25 at 14.52.53.png]]

```Pseudocode
DIRECT-ADDRESS-SEARCH(T, k)
return T[k]

DIRECT-ADDRESS-INSERT(T, x)
T[x.key] = x

DIRECT-ADDRESS-DELETE(T, x)
T[x.key] = NIL
```
- the universe $U$ of keys is reasonably small, $U=\{0, 1, \dots, m-1\}$
- using a linear array to represent the dynamic set $T[0:m-1]$

## Collision
## Chaining
## Hash functions
## Open addressing