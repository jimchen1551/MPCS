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

- **Device controllers** 
	1. maintaining **local buffer storage** and a set of special-purpose **[[Registers]]**
	2. **moving data** b/w the peripheral devices
	3. OS having a **device driver** for each device controller

- **Device driver**
	1. understanding device controllers
	2. a **uniform interface** to the device for the rest of OS

- **concurrent** and **parallel** executions of CPUs and device controller competing for memory cycles
- memory controller **synchronizing** the access to memory to ensure orderwise access to shared memory
### Interrupts
![[Screen Shot 2022-10-09 at 14.53.26.png]]
1. To start an operation of any device, the device driver loads the appropriate [[Registers]] in the device controller. 
2. Device controller examines the contents of these [[Registers]] to determine what action to take. 
3. Device controller starts the transfer of data from the device to its local buffer. 
4. **Device controller informs the device driver once the trasfer is complete.** 
5. Device driver gives control to other parts of OS. 

- the way how device controller informs its device driver (hardware interrupt)
- the way how OS interacts hardware (software interrupt)
- allowing a device to **change the flow of control** in the [[Processor|CPU]] via **interrupt-request line** (hardware interrupt)
- transferring control to **interrupt service routine** (aka **interrupt handler**, **interrupt-handler routine**)

| Hardware interrupt                           | Software interrupt                        |
| -------------------------------------------- | ----------------------------------------- |
| invoked by **external devices**              | invoked by **errors** or **system calls** |
| sending a signal to [[Processor]]            | using the instruction **INT**             |
| **not** incrementing the [[Program counter]] | incrementing the [[Program counter]]      |
| asynchronous event                           | synchronous event                         |
| **lowest** priority                          | **highest** priority                      |
| 1. Maskable 2. Non-maskable                  | 1. Normal interrupt 2. Exception          |

1. Maskable interrput: able to be turned off by [[Processor|CPU]] before execution of critical instruction sequences that must not be interrupted; used by device requests. 
2. Non-maskable interrupt: reserved for events such as unrecoverable memory errors. 

In modern computer, [[Processor|CPU]] and **interrupt-controller hardware** provide: 
1. the ability to **defer** interrupt handling during critical processing
   (e.g., maskable interrupt)
2. the efficient way to **dispatch** to the proper interrupt handler for a device 
   (e.g., interrupt chaining)
3. **multilevel interrupts** so that OS can distinguish b/w high- and low-**priority** interrupts and can respond with the appropriate degree of **urgency**. 
   (e.g., interrupt priority levels)
#### Interrupt service routine
1. Device controller **raises** an interrupt by asserting **interrupt number** on **interrupt-request line**. 
2. [[Processor|CPU]] **catches** the interrupt, **reads** the interrupt number and **dispatch** to interrupt handler by using **interrupt vector**. 
5. [[Program counter]] loads the starting address of interrupt service routine (**fixed location**) instead of next instruction address. 
6.  [[Processor|CPU]] executes **interrupt service routine** / Interrupt handler **clears** the interrupt.  
7. On completion, [[Processor|CPU]] **resumes** the interrupted computation. 

![[Screen Shot 2022-10-09 at 15.16.56.png|500]]
#### Interrupt vector
![[Screen Shot 2022-10-09 at 15.40.47.png|500]]
Intel interrupt vector: 0~31 (nonmaskable) and 32~255 (maskable)

- Interrupts must be handled **quickly**, as they occur very **frequently**. 
- To provide the speed, 
	1. Interrupt routines are called indirectly through **a table of pointers** to them. 
	2. The table of pointers is stored in **low memory**. 
	3. Each **interrput vector** (array) of address is indexed by the corresponding **interrupt number** (transferred by interrupt-request line) to provide the **address of interrupt service routine** for devices. 

- **Interrupt chaining**: 
  Every interrupt vector points to the head of a list of interrupt handlers to solve the {devices # > address elements #} problem. 
	1. Interrupt are raised. 
	2. Handlers on the corresponding list are called one by one until the one found. 
### Storage structure
![[Screen Shot 2022-10-09 at 14.58.34.png]]
- For **bootstrap program** (the first program to run while power on), [[Main memory]] is not suitable to store on account of its volatility. We store it on EEP[[Read-only memory|ROM]] (electrically erasable programmable read-only memory) and other forms of **firmware** (infrequently written and nonvolatile but slow)
- Based on [[Processor|von Neumann architecture]], the [[Memory]] follow hierarchical design. 
### I/O structure
![[Screen Shot 2022-10-09 at 14.59.11.png|500]]
- Data transfer by interrupt is fine for small amounts of data but not for bulk data (e.g., [[Secondary memory#Nonvolatile memory devices]] I/O)
- To solve the bulk data transfer, **direct memory access** (DMA) is used. 
#### Direct memory access
- After setting up buffers, pointers, and counters for the I/O device, the device controller transfers an entire block of data directly to or from the device and main memory, with no intervention by the CPU.
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
