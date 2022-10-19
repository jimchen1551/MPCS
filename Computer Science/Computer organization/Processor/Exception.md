---
Created: [[2022-10-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Exception
![[Screen Shot 2022-08-11 at 00.56.58.png]]
**Exception**: arising within the [[Processor|CPU]]; e.g., undefined opcode, [[Overflow]], [[System call]], ...
**[[Interrupt]]**: from an external IO controller
- Another form of [[Control hazard]]
- In [[MIPS]], exceptions managed by a **system control coprocessor** (CP0)
  1. saving [[Program counter|PC]] of offending instruction into **exception program counter** (EPC)
  2. saving **indication** of the problem into **cause register**
  3. jumping to **handler** at 8000 00180

[[Handler]]
[[Vectored interrupt]]

### Precise exceptions
- dealing with exception from earliest instruction and flushing the subsequent instructions
- out-of-order completion
- hard to maintain but common

### Imprecise exceptions
- just stop pipeline and save state including exception causes
- let the handler work out (to complete or flush)
- simplifies hardware, but more complex handler software
- not feasible for complex multiple-issue out-of-order pipelines