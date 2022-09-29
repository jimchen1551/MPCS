---
Created: [[2022-08-03]]
Aliases: Bypassing
Types: Card
Tags: 
- 
---
# Forwarding
![[Screen Shot 2022-08-03 at 21.10.43.png]]

![[Screen Shot 2022-08-09 at 02.04.18.png]]

![[Screen Shot 2022-08-09 at 02.05.53.png]]

- a **shortcut for data** b/w instructions with **data hazards**
- implemented by the **Forwarding unit** at the **EX** stage
- EX hazard: 
  EX/MEM[RegWrite] = 1 and 
  EX/MEM[rd] $\neq$ 0 and
  1. EX/MEM[rd] = ID/EX[rs] → ForwardA = 10
  2. EX/MEM[rd] = ID/EX[rt] → ForwardB = 10
- MEM hazard: 
  MEM/WB[RegWrite] = 1 and 
  MEM/WB[rd] $\neq$ 0 and
  1. ~(EX hazard 1. ) and (MEM/WB[rd] = ID/EX[rs]) → ForwardA = 01
  2. ~(EX hazard 2. ) and (MEM/WB[rd] = ID/EX[rt]) → ForwardB = 01

![[Screen Shot 2022-08-09 at 14.33.43.png]]
