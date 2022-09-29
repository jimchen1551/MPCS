---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Branch instruction datapath
beq rs, rt, offset  # if (rs == rt) go to [[Program counter|PC]] + 4 + (4 * offset)
![[Screen Shot 2022-07-29 at 15.40.04.png]]
- for beq (branch if equal, [[MIPS I-format]]) instruction 
  1. computing the branch target address
     [[Program counter|PC]] = [[Program counter|PC]] + 4 + (4 * offset)  # times 4 by [[Shifter]]; sums up by [[Arithmetic logic unit|ALU]]
  2. comparing the contents of rs and rt by subtraction of [[Arithmetic logic unit|ALU]]
- Elements: 
  1. [[Register file]]: fetching rs and rt
  2. [[Arithmetic logic unit|ALU]]: computing target address and comparing rs and rt
  3. Sign-extension unit: extending the offset to 32 bits
  4. Shift-left-2 unit: performing 4 * offset