---
Created: [[2022-07-12]]
Aliases: 
Types: Card
Tags: 
- 
---
# Compiler
- also called assembler
- translating [[Application software#High-level language HLL]] code to [[Instruction set architecture#Instruction]]s
- using **[[Registers]] for variables** as much as possible
- only spilling to [[Memory]] for less frequently used variables
- **register optimization** is important for compiler
- providing info for building a complete program from:

| Content      | Comment                                         |
| ------------ | ----------------------------------------------- |
| Header       | described contents of the object module         |
| Text         | translated instructions                         |
| Static data  | data allocated for the program                  |
| Relocation   | for contents depending on the absolute location |
| Symbol table | global definitions and external references      |
| Debug        | for associating with source code                |

## Assembly language
- textual representation of [[Instruction set architecture#Instruction]]s
- [[Instruction set architecture|ISA]]: [[MIPS]]