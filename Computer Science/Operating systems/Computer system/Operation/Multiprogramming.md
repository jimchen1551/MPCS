---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multiprogramming
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

- **Degree of multiprogramming**: the number of [[process]]es currently in [[memory]]
