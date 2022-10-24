---
Created: [[2022-10-24]]
Aliases: 
Types: 
Tags: 
- 
---
# Monolithic structure
- placing all of the functionality of the kernel into **a single, static binary file** running in **a single address space**

## Traditional UNIX system structure
![[Screen Shot 2022-10-24 at 18.59.50.png]]
1. Kernel
   - consisting of a series of interfaces and device drivers
   - below [[Run-time environment|system call interface]] and above physical hardware
2. [[System program]]
   - below user and above [[Run-time environment|system call interface]]
## Linux system structure
![[Screen Shot 2022-10-24 at 19.11.24.png|300]]
- based on UNIX