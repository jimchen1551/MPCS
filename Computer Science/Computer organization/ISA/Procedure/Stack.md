---
Created: [[2022-07-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Stack
![[Pasted image 20220709002201.png]]
- a data structure for spilling registers
- organized as a last-in-first-out (LIFO) queue
## Pseudocode
```Pseudocode
STACK-EMPTY(S)
if S.top==0
	return True
else return False

PUSH(S, x)
if S.top==S.size
	error "overflow"
else S.top = S.top+1
	S[S.top] = x

POP(S)
if STACK-EMPTY(S)
	error "underflow"
else S.top = S.top-1
	return S[S.top+1]
```
## Stack pointer $sp
- a value denoting the most recently allocated address in a stack
## Push
```MIPS
```
- add element to stack
## Pop
```MIPS
```
- remove element from stack
## Activation record
- Each time a function is called, an activation record containing function parameters, local variables, and the return address is pushed onto the stack. 