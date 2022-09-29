---
Created: [[2022-08-09]]
Aliases: 
Types: Card
Tags: 
- 
---
# Hazard detection for forwarding
1. **RegWrite** = 1 and
2. EX/MEM[rd] = ID/EX[rs] (EX hazard) or
3. EX/MEM[rd] = ID/EX[rt] (EX hazard) or
4. MEM/WB[rd] = ID/EX[rs] (MEM hazard) or
5. MEM/WB[rd] = ID/EX[rt] (MEM hazard) and
6. MEM/WB[rd] $\neq$ 0 or
7. EX/MEM[rd] $\neq$ 0

# Hazard detection unit
- used while **load-use** hazard
- operating during the **ID** stage
- inserting the **stall** b/t the load and its use
  - forcing control values in ID/EX pipeline register to 0
    (EX, MEM, WB do no-operation)
  - preventing update of PC and IF/ID pipeline register
  - 1-cycle stall allowing MEM to read data for load instruction and forward to EX stage
1. ID/EX[MemRead] = 1 and
2. ID/EX[rt] = IF/ID[rs] or
3. ID/EX[rt] = IF/ID[rt]