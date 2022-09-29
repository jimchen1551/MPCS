---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# Immediate operands
| Operator | Operator | Operator |
| -------- | -------- | -------- |
| addi     | lhi      | beq      |
| addiu    | llo      | bne      |
| andi     | slti     | bgt      |
| ori      | sltiu    | blt      |
| xori     | lw       | sw       |
| lbu      | lb       | sb       |
| lhu      | lh       | sh       |

```MIPS
addi $s1, $s1, 2  # add immediate
```
- constant data specified in an [[Instruction set architecture#Instruction]]
- no subtract immediate instruction
