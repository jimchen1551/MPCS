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
- one or more CPUs and a number of device controllers connected through common **buses** providing access to **shared memory**
- concurrent and parallel executions of CPUs and device controller competing for memory cycles
### Interrupts
![[Screen Shot 2022-10-09 at 14.53.26.png]]
- allowing a device to **change the flow of control** in the [[Processor|CPU]]
- Hardware trigger an interrupt at any time by **sending a signal** to [[Processor|CPU]]
- Software trigger an interrupt either by an **error** or by a **user request**
- Modern OS are interrupt-driven. 
![[Screen Shot 2022-10-09 at 15.16.56.png|500]]

### Storage structure
![[Screen Shot 2022-10-09 at 14.58.34.png]]

### I/O structure
![[Screen Shot 2022-10-09 at 14.59.11.png|500]]

## Computer-system architecture
![[Screen Shot 2022-09-14 at 11.42.19.png]]
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
