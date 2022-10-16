---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system architecture

- [[Computer Architecture]]
## Single-processor systems
**Core**: the component executing instructions and registers for storing data locally
- The **one** main [[Processor|CPU]] with its core is capable of executing a **general-purpose** instruction set, including instructions from processes. 
- The **other special-purpose** processors run on limited instruction set and do not run processes. 
1. OS **do manages** special-purpose processes: sending their next tasks and monitoring their status
2. OS **doesn't manage** special-purpose processes: low-level components and built in hardware

## Multi-processor systems
- Traditionally, **two** or **more single-core** [[Processor|CPU]] share **computer bus** and sometimes clock, memory, and peripheral devices. 
- Advantage: increased througput (not direct proportion to [[Processor|CPU]] #)
### Symmetric multiprocessing
![[Screen Shot 2022-10-14 at 21.20.25.png|400]]
- aka **SMP**
- Each peer [[Processor]] has its own set of [[Registers]] and performs all tasks, including OS functions and user processes. 
- All peer [[Processor]]s dynamically **share** physical **memory** over the system bus. 
- One may be sitting **idle** while another is **overloaded**, resulting in inefficiencies.
  Solution: sharing certain data structures
### Multi-core design
![[Screen Shot 2022-10-14 at 21.36.57.png|400]]
- Multiple cores reside on a single processor. 
- Each core has its own set of [[Registers]] and local cache (aka **L1 cache**). 
- All cores share cache (aka **L2 cache**) local to processor but global to cores. 
- **More efficient** because on-chip communication is faster than b/w-chip communication
- **Lesser power**
- For OS, a multi-core processor with N cores appears to have N standard [[Processor|CPU]]s. 
### Non-uniform memory access
![[Screen Shot 2022-10-14 at 21.46.26.png|400]]
- aka **NUMA**
- Excessively adding [[Processor|CPU]]s would make contention for system bus a bottleneck. 
- NUMA providing each [[Processor|CPU]] with its **own local memory** which is accessed via a small but fast **local bus**. 
- [[Processor|CPU]]s are connected by a **shared system interconnect**, so that all [[Processor|CPU]]s share one physical address space. 
- Advantage: not only **fast** but also **no contention** over system interconnect
- Drawback: increased latency when a [[Processor|CPU]] must access remote memory across system interconnect
### Blade servers
![[Pasted image 20221014220013.png]]
- Multiple processor boards, I/O boards, and networking boards are placed in the **same chassis**. 
- Blade-processor board **boots independently** and runs its **own OS**. 
- Each **multiprocessor systems** in the server is **independent**. 

## Clustered systems
![[Screen Shot 2022-10-14 at 22.05.05.png|500]]
- loosely coupled
- composed of **two or more individual systems** (nodes)
- **sharing storage** and closely **linked** via a local-area network **LAN**, wide-area network **WAN**, or storage-area network **SAN**
- providing **high-availability service** (system continues even if some sytems in cluster fail)
- We obtain high availability by adding a level of redundancy in the system. 
- A layer of **cluster software** runs on the cluster nodes. 
- Each node can **monitor** one or more of the others. (If monitored machine fails, monitoring machine takes ownership of its storage and restart the application. )

**Graceful degradation**: the ability to continue providing service proportional to the level of surviving hardware
**Fault tolerant**: suffering a failure of any single component and still continueing operation (requiring failure detection, diagnosis, and correction)

**Asymmetric clustering**: one machine is in **hot-standby mode** (do nothing but monitor the other active server) while the other is running apps
**Symmetric clustering**: two or more hosts are running apps and monitoring each other

**High-performance computing**: the app must have been written specifically to take advantage of the cluster (**parallelization**, dividing a program into seperate components to run parallel on individual cores)
**Distributed lock manager** (DLM): to provide shared accessed to a parallel cluster database, the system supply access control and locking to ensure that no conflicting operation occur. 
**Storage-area network** (SAN): allowing many sytems to attach to a pool of storage (cluster software can assign the app to run on any attached host)