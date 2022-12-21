---
Created: [[2022-11-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Thread
![[Screen Shot 2022-11-08 at 14.04.59.png|500]]
- a basic unit of [[Processor|CPU]] utilization
- comprising
	1. thread ID
	2. [[program counter]]
	3. [[register]]
	4. [[stack]]
- sharing with other threads belonging to the same process
	1. code section
	2. data section
	3. OS resources
- benefits: 
	1. Responsiveness
		allowing continued execution if part of the process is blocked
	2. Resource Sharing
		easier than a [[Shared memory system]] and [[Message passing system]]
	3. Economy
		cheaper than process creation and lower overhead than a [[Context switch]]
	4. Scalability
		taking advantage of a [[Multi-processor system]]

| Issues                    | Content                                                                        |
| ------------------------- | ------------------------------------------------------------------------------ |
| [[Multicore programming]] | Concurrency<br>Parallelism                                                     |
| [[Multithreading model]]  | Many-to-One model<br>One-to-One model<br>Many-to-Many model<br>Two-level model |
| [[Thread library]]        | Pthreads<br>Windows threads<br>Java threads                                    |
| [[Implicit threading]]    | Thread pool<br>Fork-Join<br>OpenMP<br>Grand central dispatch                   |

## Threading issue
