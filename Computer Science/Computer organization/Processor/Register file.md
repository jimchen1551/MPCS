---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Register file
![[Pasted image 20220729145641.png]]

![[Screen Shot 2022-07-29 at 14.47.07.png]]
- a [[#State element]]
- an array of readable/writeable processor [[Registers]]s
- Inputs: 
  1. **Read register 1**: first source register (rs)
  2. **Read register 2**: second source register (rt)
  3. **Write register**: destination register (rd)
  4. **Write data**: data to be written to a register
  5. **RegWrite**: signal to determine whether to write data into the destination register
- Outputs: 
  1. **Read data 1**: contents of source register 1
  2. **Read data 2**: contents of source register 2
