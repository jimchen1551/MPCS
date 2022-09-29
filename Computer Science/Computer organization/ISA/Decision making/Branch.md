---
Created: [[2022-07-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Branch
| Instruction | Comment                   |
| ----------- | ------------------------- |
| beq         | if equal branch to L1     |
| bne         | if not equal branch to L1 |
| blt         | if lesser branch to L1    |
| bgt         | if lesser branch to L1    |

```C
```
```MIPS
beq rs, rt, L1
bne rs, rt, L1
blt rs, rt, L1
bgt rs, rt, L1
```
- if true, branching to other [[Instruction set architecture#Basic block]]
- hardware for blt and bgt much slower than beq and bnq
- beq and bne are the common cases