---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# SPEC CPU2017
- [[Elapsed time]] to execute a selection of program neglating I/O
- **normalizing** relative to reference machine
- summarizing as **geometric mean** of performance ratios
$$\displaystyle\sqrt[n]{\Pi_{i=1}^n\text{Execution time ratio}_i}$$
## SPECspeed 2017 integer
Memory access: 200ps
ALU operation: 100ps
Register file: 50ps
| instruction | percentage |
| ----------- | ---------- |
| load        | 25%        |
| store       | 10%        |
| ALU         | 52%        |
| branch      | 11%        |
| jump        | 2%         |

## SPECspeed 2017 floating point