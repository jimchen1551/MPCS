---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Clustered system
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