---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Memory instruction datapath
For load instruction, rt = Memory[rs + extended offset]
![[Screen Shot 2022-07-29 at 15.24.24.png]]

For store instruction, Memory[rs + extended offset] = rt
![[Screen Shot 2022-07-29 at 15.24.51.png]]
- for **load** and **store** ([[MIPS I-format]]) instructions
  load: lw rt, address_offset(rs)
  store: sw rt, address_offset(rs)
  1. **extending** relative address of 16-bit offset to 32 bits
  2. computing a memory address by **adding** the address of **base register** (rs, 32-bit) to the extended relative address of **offset** (32-bit)
  3. loading data from data memory to register/storing data from register to data memory
- Elements: 
  1. [[Register file]]: loading data into or storing data from
  2. [[Arithmetic logic unit|ALU]]: adding the address of base register and offset
  3. Sign-extension unit: extending the offset to 32 bits
  4. Data memory: controlled by **MemRead** and **MemWrite**

- Combined version: 
![[Screen Shot 2022-07-29 at 15.27.51.png]]
