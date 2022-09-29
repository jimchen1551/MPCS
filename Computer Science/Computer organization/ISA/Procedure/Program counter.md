---
Created: [[2022-07-08]]
Aliases: instruction pointer, instruction address register, instruction counter, PC
Types: Card
Tags: 
- 
---
# Program counter
![[Pasted image 20220708103442.png]]
- also called instruction pointer, instruction address register, or instruction counter
- a CPU register which has the address of the next instruction to be executed from memory
- passing instruction address to the memory address register as part of the execution cycle/standard fetch
- increasing the stored value by one as the next instruction is fetched
- control transfer instructions ([[Branch]], [[Jump]]) change the sequence by placing a new value in the program counter
- A [[Branch]] provides that the next instruction is fetched from elsewhere in memory. 