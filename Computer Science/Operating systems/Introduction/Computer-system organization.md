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

- **Device controllers** 
	1. maintaining **local buffer storage** and a set of special-purpose **[[Registers]]**
	2. **moving data** b/w the peripheral devices
	3. OS having a **device driver** for each device controller

- **Device driver**
	1. understanding device controllers
	2. a **uniform interface** to the device for the rest of OS

- **concurrent** and **parallel** executions of CPUs and device controller competing for memory cycles
- memory controller **synchronizing** the access to memory to ensure orderwise access to shared memory

 ## [[Interrupt]]
## [[Memory]]
## Storage structure
![[Screen Shot 2022-10-09 at 14.58.34.png]]
- 
- Based on [[Processor|von Neumann architecture]], the [[Memory]] follow hierarchical design. 

## I/O structure
- Data transfer by interrupt is fine for small amounts of data but not for bulk data (e.g., [[Secondary memory#Nonvolatile memory devices]] [[IO]])
- To solve the bulk data transfer, **direct memory access** (DMA) is used. 
#### Direct memory access
![[Screen Shot 2022-10-09 at 14.59.11.png|500]]
- After setting up **buffers**, **pointers**, and **counters** for the [[IO]] device, the device controller transfers an entire block of data **directly** (just like highway) to or from the device and main memory, with no intervention by the [[Processor|CPU]].
- Only **one interrupt** is generated **per block**, to tell the device driver that the operation has completed, rather than the one interrupt per byte generated for low-speed devices. 
- While the device controller is performing these operations, the [[Processor|CPU]] is **available** to accomplish other work.
- Multiple components can talk to other components **concurrently**, rather than competing for cycles on a shared bus.
