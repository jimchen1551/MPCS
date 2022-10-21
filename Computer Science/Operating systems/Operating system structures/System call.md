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

1. If a system call is executed, it's typically treated by the hardware as a software [[Interrupt]]. 
2. Control passes through the [[Interrupt#Interrupt vector]] to a service routine in the OS; the mode bit is set to kernel mode. 
3. The kernel examines the interrupting instruction to determine what system call has occurred; a parameter indicates what type of service the user program is requesting.
4. The kernel verifies that the parameters are correct and legal, executes the request, and returns control to the instruction following the system call.
## Application Programming interface
![[Screen Shot 2022-10-21 at 15.20.32.png|500]]
- aka **API**
- a set of funcitons available to an app programmer
- programmers access APIs via a library of code provided by the operating system (libc for UNIX and Linux)
- providing better **portability** rather than system call
- easier to design for app programmers
- e.g., Windows API, POSIX API, and Java API
## Run-time environment
- aka **RTE**
- the full suite of software needed to execute app written in a given programming language, including its compilers or interpreters as well as other software, such as libraries and loaders
- 
## Process control
## File management
## Device management
## Information maintenance
## Communication
## Protection