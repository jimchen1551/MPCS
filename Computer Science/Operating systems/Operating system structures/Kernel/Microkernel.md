---
Created: [[2022-10-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Microkernel
![[Screen Shot 2022-10-24 at 19.55.23.png]]
- as [[Monolithic kernel]] expanded, the kernel became large and difficult to manage
- removing all **nonessential components** from the kernel and implementing them as user-level programs residing in seperate address spaces

- providing minimal process and memory management, in addition to a comuunication facility
- providing **communication** (message passing) b/w the **client program** and the various **services** running in user space
- easier to extend (new services added to user space)
- easier to port from one hardware design to another
- more security and reliability (most are user processes)
- e.g., **Darwin** (kernel component of the macOS and iOS) and QNX (a [[Real-time embedded system]])
![[Pasted image 20221024200732.png]]
