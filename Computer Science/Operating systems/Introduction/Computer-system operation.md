---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system operation
1. [[Bootstrap program]]
2. [[System daemon]]s
3. [[System call]]
4. [[Interrupt]]s

## Multiprogramming
![[Screen Shot 2022-10-17 at 14.41.13.png]]
- A single program cannot keep either the [[Processor|CPU]] or the [[IO]] devices busy at all time. 
- Multiprogramming increases [[Processor|CPU]] utilization, as well as keeping users satisfied , by organizing programs so that the [[Processor|CPU]] always has one to execute. 
- The program in execution is termed a **process**. 

1. OS keeps several processes in [[Memory]] simultaneously. 
2. OS picks and begins to execute one of these processes. 
3. Process may have to wait for some task to complete. 
	- in a non-multiprogrammed system, the [[Processor|CPU]] would sit idle. 
	- in a multiprogrammed system, the OS switches to, and executes, another process
## Multitasking

## Dual-mode and multi-mode operation

## Timer
