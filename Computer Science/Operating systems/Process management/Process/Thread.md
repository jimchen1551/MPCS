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
- benefits
	1. Responsiveness
		allowing continued execution if part of the process is blocked
	2. Resource sharing
		easier than [[Shared memory system]] and [[Message passing system]]
	3. Economy
		cheaper than process creation and lower overhead than a [[Context switch]]
	4. Scalability
		taking advantage of a [[Multi-processor system]]

## Multicore programming
- **Concurrency**: supporting more than one task making progress
![[Screen Shot 2022-11-08 at 15.36.24.png]]
- **Parallelism**: performing more than one task simultaneously
![[Screen Shot 2022-11-08 at 15.36.58.png]]
### Programming challenges
1. **Identifying tasks**: divide into separate and concurrent tasks (parallel better)
2. **Balance**: tasks in parallel perform equal work of equal value
3. **Data splitting**: data accessed and manipulated by the tasks must be divided
4. **Data dependency**: the execution of the tasks is synchronized
5. **Testing and debugging**: 
### Types of parallelism
1. Data parallelism
	distributing subsets of the same **data** across multiple cores 
	and performing the **same** operation on each
2. Task parallelism
	distributing **threads** across multiple cores 
	and performing **unique** operations on each

## Multithreading models

## Thread libraries

## Implicit threading

## Threading issue
