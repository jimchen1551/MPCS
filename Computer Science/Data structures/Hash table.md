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
LIST-DELETE(T[h(x.key)], x)
```
- putting all the elements hashing to the same slot in a [[Linked list]]
### Analysis
1. Searching: Proportional to the length of the list
2. Insertion: $T(n)=O(1)$
3. Deletion: $T(n)=O(1)$ if the lists are doubly linked
- [[Average case]]: **Load factor** $\alpha=n/m$ ; a slot containing $\alpha$ keys on the average
- [[Worst case]]: all $n$ keys hash to the same slot
### Independent uniform hashing
- an assumption that
  1. **uniform**: any given element is equally likely to hash into any of the $m$ slots
  2. **independent**: where a given element hashes to is independent of where any other elements hash to
- **Universality**: the chance that any 2 distinct keys $k_1$ and $k_2$ collide is at most $1/m$
- for j=0, 1, ..., m-1, denote the **length** of $T[j]$ by $n_j$, so that $n=n_0+n_1+\dots+n_{m-1}$
- the average value of $n_j$ is $E[n_j]=\alpha=n/m$
Theorem:
1. an unsuccessful search takes expected time $\Theta(1+\alpha)$ (1 for hash function)
2. a successful search takes average-case time $\Theta(1+\alpha)$

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