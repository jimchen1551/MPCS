---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Open addressing
- All elements occupy the hash table itself. 
- Each table entry contains either an element of the dynamic set of NIL
- When searching for an element, examine table slots until the desired element is found, or not in the table. 
- Instead of following pointers, we compute the sequence of slots be examined. 

## Probe
- To perform insertion using open addressing, successively examine the hash table until you find an empty slot in which to put the key. 
- The sequence of positions probed depends upon the key being inserted. 
- To determine which slots to probe, the [[Hash function]] includes the probe number as a second input. 
$$h:U\times\{0, 1, \dots, m-1\}\rightarrow\{0, 1, \dots, m-1\}$$
- For every key $k$, the **probe sequence** $\langle h(k, 0), h(k, 1), \dots, h(k, m-1)\rangle$ be a permutation of $\langle 0, 1, \dots, m-1\rangle$
```Pseudocode
HASH-INSERT(T, k)
i=0
repeat
	q=h(k, i)
	if T[q]==NIL
		T[q]=k
		return q
	else i=i+1
until i==m
error "hash table overflow"

HASH-SEARCH(T, k)
i=0
repeat
	q=h(k, i)
	if T[q]==k
		return q
	i=i+1
until T[q]==NIL or i==m
return NIL
```
- for deletion, 
  1. marking the slot by storing in ti the special value DELETED instead of NIL, 
  2. if storing a NIL, we might be unable to retrieve any key $k$ during whose insertion we had probed slot $i$ and found it occupies. 
- True uniform hashing is difficult to implement
  - Commonly used techniques to compute the probe sequences
    1. [[#Double hashing]]
    2. [[#Linear probing]]
    3. [[#Quadratic probing]]
  - None of them is capable of generating more than $m^2$ different probe sequences
## Double hashing
$$h(k, i)=(h_1(k)+i\cdot h_2(k))\bmod m$$
, where $h_1$ and $h_2$ are **auxiliary hash functions**
![[Screen Shot 2022-12-02 at 14.57.29.png]]
- The initial probe goes to position $T[h_1(k)]$. 
- The successive probe positions are offset from previous positions by the amount $h_2(k)$, modulo $m$. 

- In order for the entire [[Hash table]] to be searched, the value $h_2(k)$ must be relatively prime to the [[Hash table]] size $m$. 
  - Implementation 1: let $m$ be an exact power of 2 and design $h_2$ so that it always produces an odd number
  - Implementation 2: let $m$ be prime and design $h_2$ so that it always returns a positive integer less than $m$. 

- producing $\Theta(m^2)$ probe sequences, since each possible
## Linear probing
$$h_2(k)=1,\forall k$$
$$h(k, i)=(h_1(k)+i)\bmod m$$
- a special case of [[#Double hashing]]
- the simplest open addressing approach to resolving collisions
- If slot $T[h_1(k)]$ is already occupied, probe the next position $T[h_1(k)+1]$
- Keep going as necessary, on up to slot $T[m-1]$, and then wrap around to slot $T[0]$, $T[1]$, and so on, but never going past slot $T[h_1(k)+1]$
## Quadratic probing
$$h(k,i)=(h'(k)+c_1i+c_2i^2)\bmod m,\ for\ i\in[0,m-1],c_1>0, c_2>0$$
- initial probe is $T[h'(k)]$
- to make full use of hash table, the values of $c_1, c_2$ and $m$ are constrained
- **Secondary clustering**: 
  - If 2 keys have the same initial probe position, then their probe sequences are the same, since $h(k_1,0)=h(k_2,0)$ implies $h(k_1, i)=h(k_2, i)$
  - only $m$ distinct probe sequences are used
## Analysis
skipped temporarily