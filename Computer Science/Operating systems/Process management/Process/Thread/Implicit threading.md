---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Implicit threading
- With the continued growth of [[Multi-core design]], more and more apps contain thousands of threads; the design of such apps faces the **challenges** mentioned in [[Multicore programming]] and the difficulties of **correctness**.
- transferring the creation and management of threading from app developers to compilers and run-time libraries
- requiring app developers to identify **tasks**, not threads, that can run in **parallel**
- the **task** is written as a function (run-time library then maps to a separate thread by [[Multithreading model#Many-to-Many model]])
## Thread pool
- creating several threads in a pool where they await work
- Advantages:
	1. faster to service a request with an existing thread than creating a new one
	2. allowing the number of threa
## Fork-Join

## OpenMP

## Grand central dispatch