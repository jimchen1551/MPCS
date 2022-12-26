---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Critical-section problem
- consider a system consisting of $n$ [[process]]es $\{P_0, \dots,P_{n-1}\}$
- each [[process]] has
  1. **entry section**: requesting permision to enter its critical section
  2. **critical section**: on execution, no other [[process]] is allowed to execute its own critical section
  3. **exit section**: following critical section