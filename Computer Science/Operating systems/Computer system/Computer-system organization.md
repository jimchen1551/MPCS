---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system organization
![[Screen Shot 2022-09-14 at 10.54.19.png|500]]
- one or more CPUs and several device controllers connected through common **buses** (just like flat road) providing access to **shared memory**
- [[Computer Organization]]
- [[Operating systems|OS]] $\rightleftarrows$ [[Device driver]] $\rightleftarrows$ [[Device controller]]

## Processor
- **concurrent** and **parallel** executions of CPUs and [[Device controller]] competing for memory cycles
- **[[Interrupt]]** occurs while [[Device controller]] request access to [[Processor|CPU]] or while OS make a [[System call]]

## Memory
- Based on [[Processor|von Neumann architecture]], the **[[Memory]]** follow **hierarchical** design. 
- memory controller **synchronizing** the access to memory to ensure orderwise access to shared memory

## IO
- Data transfer by interrupt is fine for small amounts of data but not for bulk data (e.g., [[Secondary memory#Nonvolatile memory devices]] [[IO]])
- To solve the bulk data transfer, **[[Direct memory access]]** (DMA) is used. 
