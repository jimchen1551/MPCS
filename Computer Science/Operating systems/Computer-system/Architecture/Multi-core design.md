---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multi-core design
![[Screen Shot 2022-10-14 at 21.36.57.png|400]]
- Multiple cores reside on a single processor. 
- Each core has its own set of [[Registers]] and local cache (aka **L1 cache**). 
- All cores share cache (aka **L2 cache**) local to processor but global to cores. 
- **More efficient** because on-chip communication is faster than b/w-chip communication
- **Lesser power**
- For OS, a multi-core processor with N cores appears to have N standard [[Processor|CPU]]s. 