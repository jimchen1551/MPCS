---
Created: [[2022-10-24]]
Aliases: loadable kernel module, LKM
Types: Card
Tags: 
- 
---
# Modular kernel
- the best current methodology for OS design involves using **loadable kernel modules** (LKMs)
- LKM can be inserted into the kernel as booted or during run time and can be removed from the kernel during runtime

- having a set of core components
- linking in additional services via modules

- providing **core services**, while other services are implemented dynamically, as the kernel is running
- **linking services dynamically** is preferable to adding new features directly to the kernel (requiring recompiling the kernel every time)

- building [[CPU scheduling]] and [[Memory management]] algorithms directly into the kernel
- adding support for different file systems by way of loadable modules

- more flexible than [[Layered kernel]] (each module can call each other)
- more efficient than [[Microkernel]] (no need to invoke message passing)
- e.g., Linux, macOS, Solaris, Windows