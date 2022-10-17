---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multi-processor system
- Traditionally, **two** or **more single-core** [[Processor|CPU]] share **computer bus** and sometimes clock, memory, and peripheral devices. 
- Advantage: increased througput (not direct proportion to [[Processor|CPU]] #)

| Multi-processor system | Comment |
| ---------------------- | ------- |
| [[Symmetric multiprocessing]]                       |         |

## Multi-core design
![[Screen Shot 2022-10-14 at 21.36.57.png|400]]
- Multiple cores reside on a single processor. 
- Each core has its own set of [[Registers]] and local cache (aka **L1 cache**). 
- All cores share cache (aka **L2 cache**) local to processor but global to cores. 
- **More efficient** because on-chip communication is faster than b/w-chip communication
- **Lesser power**
- For OS, a multi-core processor with N cores appears to have N standard [[Processor|CPU]]s. 
## Non-uniform memory access
![[Screen Shot 2022-10-14 at 21.46.26.png|400]]
- aka **NUMA**
- Excessively adding [[Processor|CPU]]s would make contention for system bus a bottleneck. 
- NUMA providing each [[Processor|CPU]] with its **own local memory** which is accessed via a small but fast **local bus**. 
- [[Processor|CPU]]s are connected by a **shared system interconnect**, so that all [[Processor|CPU]]s share one physical address space. 
- Advantage: not only **fast** but also **no contention** over system interconnect
- Drawback: increased latency when a [[Processor|CPU]] must access remote memory across system interconnect
## Blade servers

![[Pasted image 20221014220013.png]]
- Multiple processor boards, I/O boards, and networking boards are placed in the **same chassis**. 
- Blade-processor board **boots independently** and runs its **own OS**. 
- Each **multiprocessor systems** in the server is **independent**. 
