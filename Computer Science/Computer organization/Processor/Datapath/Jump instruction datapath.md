---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
### Jump instruction datapath
j Label  # $PC_{31:28}$: opcode; $PC_{27:2}$: Label address; $PC_{1:0}$: 00  
![[Screen Shot 2022-07-29 at 15.58.33.png]]
- for j (jump, [[MIPS J-format]]) instruction
  1. shifting the lower 28 bits of the instruction left by 2
  2. replacing the lower 28 bits of the [[Program counter|PC]] with the result of the shift
- Elements: 
  1. Instruction memory
  2. [[Program counter]]
  3. [[Carry lookahead adder]]
  4. Shift-left-2 unit