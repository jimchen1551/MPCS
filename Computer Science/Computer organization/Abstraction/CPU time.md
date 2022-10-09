---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# CPU time
$$\displaystyle\text{CPU time}=\text{CPU clock cycles}\cdot\text{Clock period}=\frac{\text{CPU clock cycles}}{\text{Clock rate}}=IC\cdot CPI\cdot T_C$$
IC: [[Instruction count]]; 
CPI: [[Cycles per instruction]]; 
$T_C$: [[Clock period|Cycle time]]
- Time spent for proccessing a given job
- comprising **user CPU time** (often used) and **system CPU time**
- Performance depends on

| Technology                            | [[Instruction count]] | [[Cycles per instruction]] | [[Clock period]] |
| ------------------------------------- |:---------------------:|:--------------------------:|:----------------:|
| Algorithm                             |          ✅           |             ✅             |        🚫        |
| Programming language                  |          ✅           |             ✅             |        🚫        |
| [[System program#Compiler]]          |          ✅           |             ✅             |        🚫        |
| [[Instruction set architecture]] |          ✅           |             ✅             |        ✅        |

## CPU clocking
![[Pasted image 20220705165329.png]]
- operation of digital hardware governed by a **constant-rate clock**
- Performance can be improved by
1. reducing # of **clock cycles**
2. increasing **clock rate**

| Term             | Comment |
| ---------------- | ------- |
| [[Clock period]] | duration of a clock cycle        |
| [[Clock rate]]   | clock cycles per second        |

## Instruction factors
| Term                       | Comment                                   |
| -------------------------- | ----------------------------------------- |
| [[Clock cycle]]            | $IC\cdot CPI$                             |
| [[Instruction count]]      | the number of instruction                 |
| [[Cycles per instruction]] | the number of clock cycle per instruction |

