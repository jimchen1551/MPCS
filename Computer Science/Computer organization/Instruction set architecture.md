---
Created: [[2022-07-06]]
Aliases: ISA
Types: Note
Tags: 
- 
---
# Instruction
- also called machine code
- encoded in binary ([[Signed 2's complement]])
- stored in [[Memory]]

# Instruction set
- the repertoire of instructions of a computer
- typically have 32-bit (4-byte) words per instruction
- the partition bits in each word into operator & operands
- the # of bits for each depends on the # of instructions, # of registers, etc. 

| ISC                                  |                  Example                   |
|:------------------------------------ |:------------------------------------------:|
| [[Complex instruction set computer]] |                  [[x86]]                   |
| [[Reduced instruction set computer]] | [[MIPS]], [[RISC-V]], [[ARMv7]], [[ARMv8]] |

---

# Instruction set architecture
- Principles of ISA design
  1. Simplicity favors **regularity**
  2. **Smaller** is faster
  3. Make the **common case** fast
  4. Good design demands **good compromises**
- Registers: 
  1. rs: source register
  2. rt: target register
  3. rd: destination register
  4. ra: address register

| Instruction set architecture          | Content                                                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [[Instruction format and addressing]] | [[MIPS R-format]]<br>[[MIPS I-format]]<br>[[MIPS J-format]]                                                                   |
| [[Instruction operands]]              | [[Register operands]]<br>[[Memory operands]]<br>[[Immediate operands]]<br>[[Constant]]                                        |
| [[Instruction operation]]             | [[Shift operation]]<br>[[And operation]]<br>[[Or operation]]<br>[[Not operation]]<br>[[Branch]]<br>[[Jump]]<br>[[Comparison]] |

## Procedures
- a set of coded instructions that tell a computer how to run a program or calculation
- e.g., [[Stack]], [[Leaf procedure]], [[Nested procedure]]
| Mechanism          | Content                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [[Procedure call]] | [[Program counter]]<br>[[Caller saving]]<br>[[Callee saving]]<br>[[Jump and link]]<br>[[Jump register]]<br>[[Procedure frame]] |
| [[Memory layout]]  |                                                                                                                                |

## Synchronization
- If there're 2 processors sharing an area of memory without synchronization, **Data racing** occurs. 
- Synchronization implemented by **lock** and **unlock** synchronous operations →**mutual exclusion region**
- Hardware support required
	- atomic read/write memory operation
	- no other access to the location allowed between read and write
- Approaches
	- a single instruction (atomic swap of register<->memory)
	- an atomic pair of instructions (MIPS: ll and sc)
- Load linked
```MIPS
ll rt, offset(rs)
```
- Store conditional
	- succeeds if the contents of the location have not changed since the ll (storing the value of register rt in memory and returning 1 in rt)
	- Fail if the location has changed (returning 0 in rt)
```MIPS
sc rt, offset(rs)
```
- Atomic swap
	- $s4<->Memory[ $s1 ]
```MIPS
try: add $t0, $zero, $s4 // copy locked value
     ll  $t1, 0($s1)     // load linked
     sc  $t0, 0($s1)     // store conditional
     beq $t0, $zero, try // branch if store fails
     add $s4, $zero, $t1 // put load value in $s4
```

## Array vs Pointer
![[Screen Shot 2022-07-12 at 14.16.15.png]]
### Array
- A[i] = base address + i * element size
- shifting inside loop
### Pointer
- directly to memory addresses
- avoiding indexing complexity
- [[Compiler]] can achieve same effect as manual use of pointers
- induction variable elimination
- better to make program clearer and safer

## Fallacy
1. More powerful instructions mean higher performance
	- [[Compiler]]s are good at making fast code from simple instructions
2. Write in assembly language to obtain the highest performance
	- modern [[Compiler]]s are better at dealing with modern processors
	- more lines of code→more errors and less productivity
3. The importance of commercial binary compatibility means successful instruction sets don't change

## Pitfall
1. Forgetting that sequential word addresses in machines with byte addressing do not differ by one
	- incremented by 4, not by 1
2. Using a pointer to an automatic variable outside its defining procedure
