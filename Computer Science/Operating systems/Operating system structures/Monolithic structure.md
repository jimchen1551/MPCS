---
Created: [[2022-10-24]]
Aliases: tightly coupled system
Types: Card
Tags: 
- 
---
# Monolithic structure
- aka **tightly coupled system** (one modification with wide-ranging effects)
- placing all of the functionality of the kernel into **a single, static binary file** running in **a single address space**
- **dificult** to implement and to extend
- **very little overhead** in the [[Run-time environment|system call interface]]
- **fast communication** within the kernel

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
- apps typically use the `glibc` standard C library when communicating with the [[Run-time environment|system call interface]] to the kernel
- it also has [[Modular structure]] allowing the kernel to be modified during run time