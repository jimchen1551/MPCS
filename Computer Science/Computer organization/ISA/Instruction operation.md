---
Created: [[2022-10-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Instruction operation
## Logics
| Operation   | C   | Java | MIPS                |
| ----------- | --- | ---- | ------------------- |
| Shift left  | <<  | <<   | [[Shift operation]] |
| Shift right | >>  | >>   | [[Shift operation]] |
| And         | &   | &    | [[And operation]]   |
| Or          |     |      | [[Or operation]]    |
| Not         | ~   | ~    | [[Not operation]]   |

## Decision making
| Instruction    | Application      |
| -------------- | ---------------- |
| [[Branch]]     | [[If statement]] |
| [[Jump]]       |[[Loop statement]]                  |
| [[Comparison]] |                  |

### Basic block
![[Pasted image 20220707180952.png]]
- a sequence of intructions with 
  1. **No branch in** except to the entry
  2. **No branch out** except at the exit
- A [[Compiler]] identifies basic blocks for optimization
- An advanced processor can accelerate execution of basic blocks