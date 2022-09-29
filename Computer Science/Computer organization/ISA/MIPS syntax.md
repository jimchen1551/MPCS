---
Created: [[2022-07-07]]
Aliases: 
Types: 
Tags: 
- 
---
# MIPS syntax
![[Screen Shot 2022-07-07 at 15.52.03.png]]
![[Screen Shot 2022-07-07 at 15.53.51.png]]

## Floating-point arithmetic
| Instr  | Comment                          |
| ------ | -------------------------------- |
| lwc1   | load word coprocessor 1          |
| ldc1   | load double coprocessor 1        |
| swc1   | save word coprocessor 1          |
| sdc1   | save double coprocessor 1        |
| add.s  | addition for single-precision    |
| sub.s  | subtraction for SP               |
| mul.s  | multiplication for SP            |
| div.s  | division for SP                  |
| add.d  | addition for double-precision    |
| sub.d  | subtraction for DP               |
| mul.d  | multiplication for DP            |
| div.d  | division for DP                  |
| c.xx.s | xx=eq, neq, lt, le, gt, ge       |
| c.xx.d | xx=eq, neq, lt, le, gt, ge       |
| bclt   | branch if the condition is true  |
| bclf   | branch if the condition is false |
