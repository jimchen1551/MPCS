---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Arithmetic-logical instruction datapath
![[Screen Shot 2022-07-29 at 15.06.41.png]]
- for [[MIPS R-format]] instructions (add, sub, and, or, slt)
- Elements: 
  1. [[Register file]]: reading 2 data (rs & rt) from it and writing 1 data (rd) into it if **RegWrite** signal is 1
  2. [[Arithmetic logic unit|ALU]]: controlled by **ALU control**