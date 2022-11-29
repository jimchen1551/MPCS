---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Hash function
$$h:U\rightarrow {0, 1, \dots, m-1}$$
- an element with key $k$ is stored in slot $h(k)$
- $h$ maps $U$ of keys into the slots of $T[0:m-1]$
- to reduce the range of array indices that need to be handled
- A good function satisfies **independent uniform hashing** ([[Chaining#Independent uniform hashing]])
- If the keys are random real number $k$ independently and uniformly distributed in the range $[0,1)$, then $h(k)=\lfloor km\rfloor$ satisfies the condition of simple hash function. 
- 

## Static hashing

## Random hashing

## Cryptographic hashing

## Design
