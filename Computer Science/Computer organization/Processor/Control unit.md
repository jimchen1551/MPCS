---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Control unit
## Main control
![[Screen Shot 2022-07-29 at 16.27.05.png]]

| Signal   | 0           | 1                | Effect                         |
| -------- | ----------- | ---------------- | ------------------------------ |
| RegDst   | rt          | rd               | select for Write register      |
| RegWrite | none        | write            | determine whether to write     |
| ALUSrc   | read data 2 | extended address | select for ALU                 |
| PCSrc    | PC+4        | target address   | select for program counter     |
| MemRead  | none        | read data        | determine whether to read      |
| MemWrite | none        | write data       | determine whether to write     |
| MemtoReg | from ALU    | from memory      | select for register write data |

![[Screen Shot 2022-07-31 at 00.30.50.png]]

![[Screen Shot 2022-07-30 at 23.44.02.png]]

## ALU control
![[Screen Shot 2022-07-29 at 16.35.40.png]]

| Datapath by [[Arithmetic logic unit]]       | Instruction      | ALUOp | Funct  | ALU operation |
| ------------------------------------------- | ---------------- | ----- | ------ | ------------- |
| [[Arithmetic-logical instruction datapath]] | add              | 10    | 100000 | 0010          |
|                                             | subtract         | 10    | 100010 | 0110          |
|                                             | and              | 10    | 100100 | 0000          |
|                                             | or               | 10    | 100101 | 0001          |
|                                             | set on less than | 10    | 101010 | 0111          |
| [[Memory instruction datapath]]             | load             | 00    | xxxxxx | 0010          |
|                                             | store            | 00    | xxxxxx | 0010          |
| [[Branch instruction datapath]]             | branch if equal  | 01    | xxxxxx | 0110          |

![[Screen Shot 2022-07-30 at 21.56.27.png]]
$OP_3=0$
$OP_2=ALUOp_0+ALUOp_1\cdot F_1$
$OP_1=(ALUOp_1\cdot F_2)'$
$OP_0=ALUOp_1\cdot (F_0+F_3)$
