---
Created: [[2022-11-25]]
Aliases: 
Types: 
Tags: 
- 
---
# Hash table
![[Screen Shot 2022-11-25 at 14.59.13.png|500]]
- many apps require a dynamic set supporting only the dictionary operations: 
  INSERT, SEARCH ($T_{wc}=\Theta(n), E[T(n)]=O(1)$), and DELETE
  e.g., a [[Compiler]] maintaining a **symbol table**
- an efficient data structure for implementing dictionaries

## Hash function
$$h:U\rightarrow {0, 1, \dots, m-1}$$
- an element with key $k$ is stored in slot $h(k)$
- $h$ maps $U$ of keys into the slots of $T[0:m-1]$
- to reduce the range of array indices that need to be handled

## Collision
![[Screen Shot 2022-11-25 at 15.06.06.png|500]]
- 2 keys hash to the same slot
- this situation should be avoided
- solution: choosing suitable hash function which appear to be random

## Chaining
![[Screen Shot 2022-11-25 at 15.16.22.png|500]]
```Pseudocode
CHAIN-HASH-SEARCH(T, k)
return LIST-SEARCH(T[h(k)], k)

CHAIN-HASH-INSERT(T, x)
LIST-PREPEND(T[h(x.key), x])

CHAIN-HASH-DELETE(T, x)
T[x.key] = NIL
```
- putting all the elements hashing to the same slot in a [[Linked list]]

## Direct addressing
![[Screen Shot 2022-11-25 at 14.52.53.png|500]]

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
- if $U$ is large, storing $T$ of size $|U|$ is impractical

## Open addressing