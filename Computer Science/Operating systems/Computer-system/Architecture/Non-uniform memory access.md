---
Created: [[2022-10-17]]
Aliases: NUMA
Types: Card
Tags: 
- 
---
# Non-uniform memory access
![[Screen Shot 2022-10-14 at 21.46.26.png|400]]
- aka **NUMA**
- Excessively adding [[Processor|CPU]]s would make contention for system bus a bottleneck. 
- NUMA providing each [[Processor|CPU]] with its **own local memory** which is accessed via a small but fast **local bus**. 
- [[Processor|CPU]]s are connected by a **shared system interconnect**, so that all [[Processor|CPU]]s share one physical address space. 
- Advantage: not only **fast** but also **no contention** over system interconnect
- Drawback: increased latency when a [[Processor|CPU]] must access remote memory across system interconnect