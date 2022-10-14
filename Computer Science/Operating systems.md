---
Created: [[2022-06-16]]
Modified: None
Types: Note
Tags: 
- 
---
# Operating systems
| Content                         |           Study           |           Test            |          Review           |
|:------------------------------- |:-------------------------:|:-------------------------:|:-------------------------:|
| [[Operating system structures]] | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Process management]]          | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Memory management]]           | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Storage management]]          | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[File systems]]                | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Security and protection]]     | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |

![[Screen Shot 2022-09-14 at 10.32.30.png|500]]
- **Kernel**: the program running at all times
- **Control program**: controlling the execution of user programs and operation of [[IO]] to prevent errors and improper use
- **Resource allocator**: allocating and managing resources of hardware ([[Processor|CPU]], [[Memory]], and [[IO]]) among [[Application program]]s from various users

## Computer-system organization
![[Screen Shot 2022-09-14 at 10.54.19.png|500]]
- one or more CPUs and several device controllers connected through common **buses** providing access to **shared memory**

- **device controllers** 
	1. maintaining **local buffer storage** and a set of special-purpose **registers**
	2. **moving data** b/w the peripheral devices
	3. OS having a **device driver** for each device controller

- **device driver**
	1. understanding device controllers
	2. a **uniform interface** to the device for the rest of OS

- **concurrent** and **parallel** executions of CPUs and device controller competing for memory cycles
- memory controller **synchronizing** the access to memory to ensure orderwise access to shared memory
### Interrupts
![[Screen Shot 2022-10-09 at 14.53.26.png]]
- allowing a device to **change the flow of control** in the [[Processor|CPU]]

| Hardware interrupt                           | Software interrupt                        |
| -------------------------------------------- | ----------------------------------------- |
| invoked by **external devices**              | invoked by **errors** or **system calls** |
| sending a signal to [[Processor]]            | using the instruction **INT**             |
| **not** incrementing the [[Program counter]] | incrementing the [[Program counter]]      |
| asynchronous event                           | synchronous event                         |
| **lowest** priority                          | **highest** priority                      |
| 1. Maskable 2. Non-maskable                  | 1. Normal interrupt 2. Exception          |

![[Screen Shot 2022-10-09 at 15.16.56.png|500]]
![[Screen Shot 2022-10-09 at 15.40.47.png|500]]
### Storage structure
![[Screen Shot 2022-10-09 at 14.58.34.png]]
- [[Memory]]
- Caching
- Coherency and Consistency
### I/O structure
![[Screen Shot 2022-10-09 at 14.59.11.png|500]]

## Computer-system architecture
### Single-processor systems
### Multi-processor systems
### Clustered systems
## Computer-system operation
### Multiprogramming and multitasking
### Dual-mode and multi-mode operation
### Timer
## Resource management
### Process management
### Memory management
### File-system management
### Mass-storage management
### Cache management
### I/O system management
## Protection and security
## Virtualization
## Distributed systems
## Kernel data structures
### Lists
### Stacks
### Queues
### Trees
### Hash functions and maps
### Bit maps
## Computing environments
### Traditional computing
### Mobile computing
### Client-server computing
### Peer-to-peer computing
### Cloud computing
### Real-time embedded systems
## Open-source operating systems

## Score
- Midterm: 30%
- Final: 30%
- Project: 40%
