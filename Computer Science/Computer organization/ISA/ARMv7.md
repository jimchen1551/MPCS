---
Created: [[2022-07-12]]
Aliases: 
Types: Card
Tags: 
- 
---
# ARM
- [[Reduced instruction set computer|RISC]]
- similar basic set of instructions to [[MIPS]]

|                   | ARM           | MIPS          |
| ----------------- | ------------- | ------------- |
| Date announced    | 1985          | 1985          |
| Instruction size  | 32 bits       | 32 bits       |
| Address space     | 32-bit flat   | 32-bit flat   |
| Data alignment    | aligned       | aligned       |
| Addressing modes  | 9             | 3             |
| Integer registers | 15 * 32-bit   | 31 * 32-bit   |
| I/O               | Memory mapped | Memory mapped |

## Addressing
![[Pasted image 20220716194329.png]]

## Compare and branch
- using **condition codes** (N: negative; C: carry; V: overflow; Z: zero) for result of an arithmetic/logical instruction
- compared instructions to set condition codes without keeping the result
- **Predicated instruction**: each instruction can be conditional
  Top 4 bits of instruction word are condition value
  avoiding branches over single instructions