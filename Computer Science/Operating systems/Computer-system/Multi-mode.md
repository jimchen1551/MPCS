---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multi-mode
![[Screen Shot 2022-10-17 at 15.31.15.png]]
- In order to ensure the proper execution of the system, we must be able to distinguish between the execution of **operating-system code** and **user-defined code**.
- The approach taken by most computer systems is to provide hardware support (e.g., **mode bit**) that allows differentiation among various **modes** of execution. (e.g., **user mode** and **kernel mode**)

## Mode bit
- a bit added to the hardware of the computer to indicate the current mode 
  (e.g., kenel = 0; user = 1)
- [[System call]] change mode to kernel. The mode return from call resets. 

## Privileged instruction
- Hardware allows it to be executed only in **kernel mode**. 
- If an attempt is made to execute a privileged instruction in **user mode**, the hardware does not execute the instruction but rather treats it as illegal and **traps** (exceptions) it to the OS.