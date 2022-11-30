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

## Double hashing
## Linear probing
## Quadratic probing
