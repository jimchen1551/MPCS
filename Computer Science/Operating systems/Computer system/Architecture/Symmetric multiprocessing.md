---
Created: [[2022-10-17]]
Aliases: SMP
Types: Card
Tags: 
- 
---
# Symmetric multiprocessing
![[Screen Shot 2022-10-14 at 21.20.25.png|400]]
- aka **SMP**
- Each peer [[Processor]] has its own set of [[Register]] and performs all tasks, including OS functions and user processes. 
- All peer [[Processor]]s dynamically **share** physical **memory** over the system bus. 
- One may be sitting **idle** while another is **overloaded**, resulting in inefficiencies.
  Solution: sharing certain data structures
- [[Multiple processors scheduling]]
