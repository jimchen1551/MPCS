---
Created: [[2022-08-03]]
Aliases: 
Types: Card
Tags: 
- 
---
# Delayed branch
![[Screen Shot 2022-08-03 at 22.43.53.png]]
- always executing the next sequential instruction, with the branch taking place after that one instruction delay
- [[Compiler]]s and assemblers try to place an instruction that always executes after the branch in the branch **delay slot**. 
- Scheduling the branch delay slot from: 
  1. before
  2. target
  3. fall through

![[Screen Shot 2022-08-10 at 23.30.23.png]]