---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# MIPS
- Microprocessor without Interlocked Pipelined Stages
- [[Reduced instruction set computer|RISC]] ISA
- Typical of many modern [[Instruction set architecture|ISA]]
- [[Instruction set architecture|ISA#Operands]]: 32 registers, $2^{30}$ memory words

![[Screen Shot 2022-07-06 at 17.04.47.png]]
[[MIPSReference.pdf]]
## Main program
```MIPS
.text          // declaration
.globl
main:
...
```
## Data types
```
.data          // declaration
name: .data_type data

.word 5        // 4-byte integer
.word 1, 3, 5  // integer array (3)
.half 5        // 2-byte integer
.float 3.14    // single-precision
.double 3.14   // double-precision
.ascii "Hi"    // string
.asciiz "Hi"   // string end with NULL
```
## Procedure
```MIPS
.text          // declaration
label:
...
```
[[MIPS syntax]]
## Assembler Pseudoinstructions
- most assembler instruction represent machine instructions one-to-one
- Pseudoinstructions: figment of the assemble's imagination
```MIPS
move $t0, $t1    // add $t0, $zero, $t1
blt $t0, $t1, L  // slt $at, $t0, $t1
                 // bne $at, $zero, L
```
## System calls
```MIPS
li $v0, n  \\ $v0=n
...
syscall
```
| $v0 | Event                       | Arguments                                                       |
| --- | --------------------------- | --------------------------------------------------------------- |
| 1   | print int                   | $a0=integer                                                     |
| 2   | print float                 | $f12=float                                                      |
| 3   | print double                | $f12=double                                                     |
| 4   | print string                | $a0=address of .asciiz                                          |
| 5   | read int                    | $a0=integer                                                     |
| 6   | read float                  | $f12=float                                                      |
| 7   | read double                 | $f12=double                                                     |
| 8   | read string                 | $a0=address of input, $a1=number to read                        |
| 9   | sbrk (allocate heap memory) | $a0=number to allocate                                          |
| 10  | exit                        |                                                                 |
| 11  | print character             | $a0=character                                                   |
| 12  | read character              | $a0=character                                                   |
| 13  | open file                   | $a0=address of .asciiz filename, $a1=flags, $a2=mode            |
| 14  | read file                   | $a0=file descriptor, $a1=address of input, $a2=number to read   |
| 15  | write file                  | $a0=file descriptor, $a1=address of output, $a2=number to write |
| 16  | close file                  | $a0=file descriptor                                             |
