---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Chaining
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

## Analysis
1. Searching: Proportional to the length of the list
2. Insertion: $T(n)=O(1)$
3. Deletion: $T(n)=O(1)$ if the lists are doubly linked
- [[Average case]]: **Load factor** $\alpha=n/m$ ; a slot containing $\alpha$ keys on the average
- [[Worst case]]: all $n$ keys hash to the same slot

## Independent uniform hashing
- an assumption that
  1. **uniform**: any given element is equally likely to hash into any of the $m$ slots
  2. **independent**: where a given element hashes to is independent of where any other elements hash to
- **Universality**: the chance that any 2 distinct keys $k_1$ and $k_2$ collide is at most $1/m$
- for j=0, 1, ..., m-1, denote the **length** of $T[j]$ by $n_j$, so that $n=n_0+n_1+\dots+n_{m-1}$
- the average value of $n_j$ is $E[n_j]=\alpha=n/m$
Theorem:
1. an unsuccessful search takes expected time $\Theta(1+\alpha)$ (1 for hash function)
2. a successful search takes average-case time $\Theta(1+\alpha)$
