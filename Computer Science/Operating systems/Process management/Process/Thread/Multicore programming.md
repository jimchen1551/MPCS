---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multicore programming
- **Concurrency**: supporting more than one task making progress
![[Screen Shot 2022-11-08 at 15.36.24.png]]
- **Parallelism**: performing more than one task simultaneously
![[Screen Shot 2022-11-08 at 15.36.58.png]]
- considering [[Amdahl's law]], 
$$speedup\leq\frac{1}{s+\frac{1-s}{N}}$$
, where $s$ for serial portion and $N$ for processing cores

## Programming challenges
1. **Identifying tasks**: divide into separate and concurrent tasks (parallel better)
2. **Balance**: tasks in parallel perform equal work of equal value
3. **Data splitting**: data accessed and manipulated by the tasks must be divided
4. **Data dependency**: the execution of the tasks is synchronized
5. **Testing and debugging**

## Types of parallelism
1. Data parallelism
	distributing subsets of the same **data** across multiple cores 
	and performing the **same** operation on each
2. Task parallelism
	distributing **threads** across multiple cores 
	and performing **unique** operations on each