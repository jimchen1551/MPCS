---
Created: [[2022-07-06]]
Aliases: CO
Types: Note
Tags: 
- 
---
# Computer organization
| Computer organization            | Content |
|:-------------------------------- | ------- |
| [[Instruction set architecture]] |         |
| [[Arithmetics]]                  |         |
| [[Processor]]                    |         |
| [[Memory]]                       |         |

## Core ideas
1. Use **abstraction** to simplify design
2. Make the **common case** fast
3. Performance via **parallelism**
4. Performance via **pipelining**
5. Performance via **prediction**
6. **Hierarchy** of memories
7. **Dependability** via redundancy

## From Softwares to Hardwares
![[Pasted image 20220706132457.png]]
### Softwares
| Class                    | Comment                                                            |
| ------------------------ | ------------------------------------------------------------------ |
| [[Application program]] | [[Program execution]], <br>[[Instruction set architecture#Procedures]] |
| [[System program]]      | [[Compiler]], <br>[[Compiler#Assembly language]]                       |

### Hardware
![[Pasted image 20220705165648.png]]

| Hardware      | Elements                                                              |
| ------------- | --------------------------------------------------------------------- |
| [[Processor]] | [[Processor]], [[Cache memory]]                                       |
| [[Memory]]    | [[Main memory]], [[Secondary memory]], [[Cache memory]] |
| [[IO]]        |                                                                       |

---

## Performance
### Response time
- the time it takes to do a task
### Throughput
- the work done in a unit of time
### Relative performance
$$\displaystyle\text{Performance} =\frac{1}{\text {Execution time}}=\frac{1}{\text{CPU time}}$$
- [[Elapsed time]]
- [[CPU time]]

### Millions of instructions per second
$$\displaystyle\text{MIPS}=\frac{\text{Instruction count}}{\text{Execution time}\cdot 10^6}=\frac{IC}{\frac{IC\cdot CPI}{\text{Clock rate}\cdot 10^6}}=\frac{\text{Clock rate}}{CPI\cdot 10^6}$$

## Amdahl's law
$$\displaystyle T_{improved}=\frac{T_{affected}}{\text{improvement factor}}+T_{unaffected}$$
- The performance enhancement possible with a given improvement is limited by the amount that the improved feature is used. 
- Corollary: Make the common cases fast!

## Power wall
$$\displaystyle\text{Enery}\propto \text{Capacitive load}\cdot \text{Voltage}^2$$
$$\displaystyle\text{Power}\propto \text{Capacitive load}\cdot \text{Voltage}^2\cdot \text{Frequency}$$
- Voltage can't be reduced further
- Heat cant't be removed anymore
---

## Benchmarking
### Standard performance evaluation corp (SPEC)
- developing benchmarks for CPU, I/O, ect.
- [[SPEC CPU2017]]
- [[SPEC Power]]

## Fallacies
1. Power used is proportional to Workload
2. Performance and energy efficiency trade off each other
3. [[#Millions of instructions per second]] as a performance metric
	- differences in [[Instruction set architecture|ISA]]s between computers
	- differences in complexity between instructions

## Reference book
