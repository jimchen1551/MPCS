---
Created: [[2022-11-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Queue
## Pseudocode
```Pseudocode
ENQUEUE(Q, x)
Q[Q.tail] = x
if Q.tail==Q.size
	Q.tail = 1
else Q.tail = Q.tail+1

DEQUEUE(Q)
x = Q[Q.head]
if Q.head==Q.size
	Q.head = 1
else Q.head = Q.head+1
return x
```