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

**Device controllers**
1. maintaining **local buffer storage** and a set of special-purpose **[[Registers]]**
2. **moving data** b/w the peripheral devices
3. OS having a **device driver** for each device controller

**Device driver**
1. understanding device controllers
2. a **uniform interface** to the device for the rest of OS

## Processor
- **concurrent** and **parallel** executions of CPUs and device controller competing for memory cycles
- **[[Interrupt]]** occurs while device controller request access to [[Processor|CPU]] or while OS make a system call

## Memory
- Based on [[Processor|von Neumann architecture]], the **[[Memory]]** follow **hierarchical** design. 
- memory controller **synchronizing** the access to memory to ensure orderwise access to shared memory

## I/O
- Data transfer by interrupt is fine for small amounts of data but not for bulk data (e.g., [[Secondary memory#Nonvolatile memory devices]] [[IO]])
- To solve the bulk data transfer, **[[Direct memory access]]** (DMA) is used. 
