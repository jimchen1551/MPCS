---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system operation
After a computer is powered on, 
1. [[Bootstrap program]] stored in EEPROM is the first program to run which can locate the OS kernel and load it into the [[Memory]]. 
2. [[System daemon]]s provide services outside of the kernel and run all the time the kernel is running. 
3. [[System call]]s are specific requests from a user program which would cause software interrupt to make OS execute some special operations. 
4. [[Interrupt]]s may be invoked by a device controller, an error, or an [[System call]]. 

## Multiprogramming
![[Screen Shot 2022-10-17 at 14.41.13.png]]
- A single program cannot keep either the [[Processor|CPU]] or the [[IO]] devices busy at all time. 
- Multiprogramming increases [[Processor|CPU]] utilization, as well as keeping users satisfied , by organizing programs so that the [[Processor|CPU]] always has one to execute. 
- The program in execution is termed a **process**. 
- **Batch system** for efficiency

1. OS keeps several processes in [[Memory]] simultaneously. 
2. OS picks and begins to execute one of these processes. 
3. Process may have to wait for some task to complete. 
	- in a **non-multiprogrammed** system, the [[Processor|CPU]] would sit idle. 
	- in a **multiprogrammed** system, when a process needs to wait, the OS switches to, and executes, another process
4. 1st process finishes waiting and gets the [[Processor|CPU]] back, if multiprogrammed. 

## Multitasking
- a logical extension of multiprogramming
- [[Processor|CPU]] switches processes so frequently that users can interact with each process while it is running, creating **interactive computing**. 
- **Response time** < 1 sec. 
- If several processes are ready to run at the same time, the system must choose which process will run next. $\Rightarrow$ [[CPU scheduling]]
- If processes don't fit in [[Memory]], **swapping** moves them in and out to run [[Virtual memory]] allows execution of processes not completely in [[Memory]]. 

## Dual-mode and multi-mode operation
![[Screen Shot 2022-10-17 at 15.31.15.png]]


## Timer
