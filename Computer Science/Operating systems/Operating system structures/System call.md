---
Created: [[2022-10-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# System call
![[Screen Shot 2022-10-17 at 15.31.15.png]]
- a specific request from a user program that an OS service be performed by executing a special operation
- a **programming interface** to the [[System service]]
- typically written in **C/C++** or **assembly code**
- providing the means for a user program to ask the OS to perform tasks reserved for the OS on the user program’s behalf
- used by a process to request action by the OS
- usually taking the form of a trap to a specific location in the interrupt vector

| System call                 | Comment |
| --------------------------- | ------- |
| [[Process control]]         |         |
| [[File management]]         |         |
| [[Device management]]       |         |
| [[Information maintenance]] |         |
| [[Communication]]           |         |
| [[Protection]]              |         |

## System call implementation
1. If a system call is executed, it's typically treated by the hardware as a software [[Interrupt]]. 
2. Control passes through the [[Interrupt#Interrupt vector]] to a service routine in the OS; the mode bit is set to kernel mode. 
3. The kernel examines the interrupting instruction to determine what system call has occurred; a parameter indicates what type of service the user program is requesting.
4. The kernel verifies that the parameters are correct and legal, executes the request, and returns control to the instruction following the system call.

![[Screen Shot 2022-10-21 at 18.07.52.png|500]]
- The caller need only obey the [[Application Programming interface|API]] and understand waht the OS will do as a result of the execution of the system call. 
- Most of the details of the OS interface are hidden from the programmer by the [[Application Programming interface|API]] and managed by the [[Run-time environment|RTE]] (aka [[Run-time environment|system call interface]])

## System call parameter passing
![[Screen Shot 2022-10-21 at 18.50.04.png|500]]
- 3 ways to pass parameters to the OS
	1. $\leq$ 5 parameters, pass the **value** of parameters in **register**
	2. > 5 parameters, pass the **address** of parameters in **memory**
	3. **push** the parameters onto a [[Stack]] by the program 
	   and **pop** off the [[Stack]] by the OS
