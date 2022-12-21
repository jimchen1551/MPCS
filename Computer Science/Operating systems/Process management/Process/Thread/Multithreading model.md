---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multithreading model
![[Screen Shot 2022-11-08 at 16.22.17.png]]
- **User thread**: managed by the user-level [[thread library]]
- **Kernel thread**: supported by the kernel

## Many-to-One model
![[Screen Shot 2022-11-08 at 16.25.51.png]]
- many user-level threads mapped to a single kernel thread
- thread management is done by the [[thread library]] in the user space (efficient)
- because only one thread can access the kernel at a time, multiple threads are unable to run in parallel on a [[Multi-core design]]
- Drawback: one thread blocking causes all to block

## One-to-One model
![[Screen Shot 2022-11-08 at 16.26.15.png]]
- each user thread mapped to a kernel thread
- providing more concurrency than the many-to-one model
- allowing multiple threads to run in parallel on a [[Multi-processor system]]
- Drawback: creating a user thread requires creating the corresponding kernel thread

## Many-to-Many model
![[Screen Shot 2022-11-08 at 16.26.32.png]]
- many user-level threads multiplexed to a smaller or equal number of kernel threads
- allowing to create a sufficient number of kernel threads

## Two-level model
![[Screen Shot 2022-11-08 at 16.27.14.png]]
- similar to the many-to-many model, except allowing a user thread to be bound to a kernel thread