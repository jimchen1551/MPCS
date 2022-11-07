---
Created: [[2022-11-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Context switch
![[Screen Shot 2022-11-07 at 13.06.12.png|500]]
- When an [[interrupt]] occurs, the system needs to save the current context of the [[process]] running on the [[Processor|CPU]] core to restore that context when its processing is done, essentially suspending the process and then resuming it.
- Generically, we perform a **state save** of the current state of the CPU core, be it in kernel or user mode, and then a **state restore** to resume operations.
- Context switch time is overhead. 

- The context is represented in the [[Process control block]].
- including 
	1. value of [[register]]
	2. [[process state]]
	3. [[memory management]]