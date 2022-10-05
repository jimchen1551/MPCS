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

![[Screen Shot 2022-09-14 at 10.32.30.png]]
- controlling the hardware ([[Processor|CPU]], [[Memory]], and [[IO]]) and coordinating its use among the various application programs for the various users (just like a resource allocator)
- designed primarily to optimize the utilization of hardware
- The one program running at all times on the computer is called the **kernel**. 

## Computer-system organization
![[Screen Shot 2022-09-14 at 10.54.19.png]]
- one or more CPUs and a number of device controllers connected through a common **bus** providing **access to shared memory**
- concurrent and parallel executions of CPUs and device controller competing for memory cycles
- For a computer to start running, (???)
	1. **Bootstrap program** stored in [[Read-only memory|ROM]] or EEROM (electrically erasable programmable [[Read-only memory|ROM]]) (both known by the general term **firmware**) initializes everything in computer , loads the operating system into the memory and starts executing it. 
	2. After the system programs loaded into memory at boot time, they become **system process** or **system daemons** running the entire time the kernel is running. 
	3. **Interrupt**: the occurrence of an event
	   Hardware triggers an interrupt at any time by **sending a signal** to the [[Processor|CPU]]. 
	   Software triggers an interrupt by executing **system call**. 
	4. When the [[Processor|CPU]] is interrupted, it stops doing original task and transfers execution to a **fixed location**. 
		1. The transfer is done by i  nvoking **interrupt-specific handler** to examine the interrupt info. 
		2. The fixed location usually contains the starting address where the **service routine** for the interrupt is located. 
		3. The interrupt routine is called indirectly through a table of pointers to interrupt routine (stored in low memory), with no intermediate routine needed. 
		4. The interrupt service routine executes; on completion, the [[Processor|CPU]] resumes the interrupted computation. 
		   ![[Screen Shot 2022-09-14 at 11.20.02.png]]
interrupt vector???
not done

![[Screen Shot 2022-09-14 at 11.41.48.png]]

not done
### Interrupts
### Storage structure
### I/O structure
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
