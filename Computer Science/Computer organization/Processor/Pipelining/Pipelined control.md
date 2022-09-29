---
Created: [[2022-08-05]]
Aliases: 
Types: Card
Tags: 
- 
---
# Pipelined control
- based on the [[Control unit]]
- dividing the control lines into groups according to the stages:
  1. **IF**: none
  2. **ID**: none
  3. **EX**: RegDst, ALUOp, ALUSrc
  4. **MEM**: Branch, MemRead, MemWrite
  5. **WB**: MemtoReg, RegWrite
- According to the asynchronous implementation of control signals, we create the control info during instruction decode and **extend the pipeline register** to include control info. 
  ![[Screen Shot 2022-08-08 at 19.57.58.png]]
- e.g., 
```MIPS
lw  $10, 20($1)
sub $11, $2, $3
and $12, $4, $5
or  $13, $6, $7
add $14, $8, $9
```

Clock 1:
![[Screen Shot 2022-08-08 at 20.20.50.png]]

Clock 2: 
![[Screen Shot 2022-08-08 at 20.21.33.png]]

Clock 3: 
![[Screen Shot 2022-08-08 at 20.22.08.png]]

Clock 4: 
![[Screen Shot 2022-08-08 at 20.22.32.png]]

Clock 5: 
![[Screen Shot 2022-08-08 at 20.23.02.png]]

Clock 6: 
![[Screen Shot 2022-08-08 at 20.23.39.png]]

Clock 7: 
![[Screen Shot 2022-08-08 at 20.26.16.png]]

Clock 8: 
![[Screen Shot 2022-08-08 at 20.26.35.png]]
