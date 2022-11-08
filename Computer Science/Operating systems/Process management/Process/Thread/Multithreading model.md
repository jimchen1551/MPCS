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
- thread management 
- one thread blocking causes all to block
## One-to-One model
![[Screen Shot 2022-11-08 at 16.26.15.png]]

## Many-to-Many model
![[Screen Shot 2022-11-08 at 16.26.32.png]]

## Two-level model
![[Screen Shot 2022-11-08 at 16.27.14.png]]
