---
Created: [[2022-10-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Modular kernel
- the best current methodology for OS design involves using **loadable kernel modules** (LKMs)
- having a set of core components
- linking in additional services via modules
- providing core services, while other services are implemented dynamically, as the kernel is running
- e.g., Linux, macOS, Solaris, Windows