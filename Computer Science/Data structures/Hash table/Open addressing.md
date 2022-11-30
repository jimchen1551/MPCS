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
## Double hashing
$$h(k, i)=(h_1())$$
## Linear probing
## Quadratic probing
