---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system architecture
## Single-processor systems
**Core**: the component executing instructions and registers for storing data locally
- The **one** main [[Processor|CPU]] with its core is capable of executing a **general-purpose** instruction set, including instructions from processes. 
- The **other special-purpose** processors run on limited instruction set and do not run processes. 
1. OS **do manages** special-purpose processes: sending their next tasks and monitoring their status
2. OS **doesn't manage** special-purpose processes: low-level components and built in hardware

## Multi-processor systems
- Traditionally, **two** or **more single-core** [[Processor|CPU]] share **computer bus** and sometimes clock, memory, and peripheral devices. 
- Advantage: increased througput (not directly ratio to [[Processor|CPU]] #)
### Symmetric multiprocessing
![[Screen Shot 2022-10-14 at 21.20.25.png|400]]
- aka **SMP**
- Each peer [[Processor]] has its own set of [[Registers]] and performs all tasks, including OS functions and user processes. 
- All peer [[Processor]]s dynamically **share** physical **memory** over the system bus. 
- One may be sitting **idle** while another is **overloaded**, resulting in inefficiencies.
  Solution: sharing certain data structures
### Multi-core
- Multiple cores reside on a single processor. 
- More efficient because on-chip communication is faster tha

## Clustered systems
