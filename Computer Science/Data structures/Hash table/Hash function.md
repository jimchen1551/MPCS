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

## Static hashing
- independent of any patterns that might exist in the data
- using a single, fixed hash function
- randomized distribution of input keys
### Division method
$$h(k)=k\bmod m$$
- $m$ must not be a power of 2, since if $m=2^p$, then $h(k)$ is just the $p$ lowest-order bits of $k$
- 
### Multiplication method
### Multiply-shift method

## Random hashing
- picking a hash functyion to be used at random from a suitable family of hashing functions (better [[Average case]] performance than creating the input keys at random)
- 

## Cryptographic hashing

## Design
