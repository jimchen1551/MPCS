---
Created: [[2022-07-12]]
Aliases: 
Types: Card
Tags: 
- 
---
# Loader
- loading from image file on disk into memory
  1. reading header to determine segment sizes
  2. creating virtual address space
  3. copying text and initialized data into memory
  4. setting up arguments on stack
  5. initializing registers including $sp, $fp, $gp
  6. jumping to startup routine
     - copying arguments to $a0, ... and calls main
     - when main returns, do exit syscall