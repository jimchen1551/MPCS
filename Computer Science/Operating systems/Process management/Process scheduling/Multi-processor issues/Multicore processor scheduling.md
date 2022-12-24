---
Created: [[2022-12-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multicore processor scheduling
- [[Multi-core design]] and [[Multicore programming]]
![[Screen Shot 2022-12-23 at 16.30.05.png|400]]
- a **multithreaded**, **multicore** [[processor]] actually requires 2 different levels of scheduling (not mutually exclusive)
  1. scheduling decisions made by the [[Operating systems|OS]] as it chooses which **software thread** to run on each **hardware thread** (logical [[Processor|CPU]])
     - any scheduling algorithm can be adopted
  2. scheduling how each **core** decides which **hardware thread** to run
     - [[Round-robin scheduling]]
     - [[Multilevel queue scheduling]]

![[Screen Shot 2022-12-23 at 15.53.28.png|500]]
![[Screen Shot 2022-12-23 at 16.03.21.png|500]]
- **Memory stall**: the time for data to transfer from [[memory]] to [[processor]] since the [[processor]] requested (because processor operate faster than memory) and a cache miss occurred
  → solution: **multithreaded processing** cores in which 2 or more **hardware threads** are assigned to each core, so that if one hardware thread stalls for memory, the core can switch to another thread

![[Screen Shot 2022-12-23 at 16.10.16.png|400]]
- **Chip multithreading** (CMT): for [[Operating systems|OS]], each **hardware thread** maintain its architectural state (instruction pointer and register set), and thus appears as a logical [[Processor|CPU]] available to run a software [[thread]]. 
- **Hyper-threading** (simultaneous multithreading): assigning multiple **hardware threads** to a single processing core
## Coarse-grained multithreading
- A [[thread]] executes on a core until a **long-latency event** such as a memory stall occurs. 
  → Because of the delay caused by the long-latency event, the core must switch to another [[thread]] to begin execution. 
  → However, the **cost of switching** between [[thread]]s is high, since the instruction pipeline must be **flushed** before the other [[thread]] can begin execution on the processor core. 
## Fine-grained multithreading
- switching b/w [[thread]]s at a much **finer level of granularity**, typically at the boundary of an instruction cycle
- the architectural design includes logic for thread switching
