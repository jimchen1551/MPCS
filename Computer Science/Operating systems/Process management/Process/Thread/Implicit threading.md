---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Implicit threading
- With the continued growth of [[Multi-core design]], more and more apps contain thousands of threads; the design of such apps faces the **challenges** mentioned in [[Multicore programming]] and the difficulties of **correctness**.
- transferring the **creation** and **management** of threading from app developers to **compilers** and **run-time libraries**
- requiring app developers to identify **tasks**, not threads, that can run in **parallel**
- the **task** is written as a function (run-time library then maps to a separate thread by [[Multithreading model#Many-to-Many model]])
## Thread pool
- **creating** several threads in a pool where they **await** work
- Advantages:
	1. faster to service a request with an existing thread than create a new one
	2. allowing the number of threads in the apps to be bound to the size of the pool
	3. separating the task to be performed from the mechanics of creating the task allows different strategies for running the task
## Fork-Join
![[Screen Shot 2022-12-21 at 16.34.44.png|500]]
## OpenMP

## Grand central dispatch
