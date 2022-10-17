---
Created: [[2022-10-14]]
Aliases: DMA
Types: Card
Tags: 
- 
---
# Direct memory access
![[Screen Shot 2022-10-09 at 14.59.11.png|500]]
- After setting up **buffers**, **pointers**, and **counters** for the [[IO]] device, the [[Device controller]] transfers an entire block of data **directly** (just like highway) to or from the device and main memory, with no intervention by the [[Processor|CPU]].
- Only **one interrupt** is generated **per block**, to tell the [[Device driver]] that the operation has completed, rather than the one interrupt per byte generated for low-speed devices. 
- While the [[Device controller]] is performing these operations, the [[Processor|CPU]] is **available** to accomplish other work.
- Multiple components can talk to other components **concurrently**, rather than competing for cycles on a shared bus.