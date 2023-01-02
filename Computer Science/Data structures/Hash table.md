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

| Issue                 | Comment                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| [[Hash function]]     | $h:U\rightarrow {0, 1, \dots, m-1}$<br>Static hashing<br>Random hashing                                 |
| [[Collision]]         | 2 keys hash to the same slot                                                                            |
| [[Chaining]]          | storing collided elements in a [[Linked list]]                                                          |
| [[Direct addressing]] | $T[x.key]=x$                                                                                            |
| [[Open addressing]]   | Probe<br>Double hashing: $h(k, i)=(h_1(k)+i\cdot h_2(k))\bmod m$<br>Linear probing: $h(k, i)=(h_1(k)+i)\mod m$<br>Quadratic probing: $h(k, i)=$ |
