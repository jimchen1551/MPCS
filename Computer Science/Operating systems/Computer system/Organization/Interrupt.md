---
Created: [[2022-10-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Interrupts
![[Screen Shot 2022-10-09 at 14.53.26.png]]
1. To start an operation of any device, the [[Device driver]] loads the appropriate [[Registers]] in the [[Device controller]]. 
2. [[Device controller]] examines the contents of these [[Registers]] to determine what action to take. 
3. [[Device controller]] starts the transfer of data from the device to its local buffer. 
4. **[[Device controller]] informs the [[Device driver]] once the trasfer is complete.** 
5. [[Device driver]] gives control to other parts of OS. 

- the way how [[Device controller]] informs its [[Device driver]] (hardware interrupt)
- the way how OS interacts hardware (software interrupt)
- allowing a device to **change the flow of control** in the [[Processor|CPU]] via **interrupt-request line** (hardware interrupt)
- transferring control to **interrupt service routine** (aka **interrupt handler**, **interrupt-handler routine**)

| Hardware interrupt                           | Software interrupt                             |
| -------------------------------------------- | ---------------------------------------------- |
| invoked by **external devices**              | invoked by **errors** or **[[System call]]s**  |
| sending a signal to [[Processor]]            | using the instruction **INT**                  |
| **not** incrementing the [[Program counter]] | incrementing the [[Program counter]]           |
| asynchronous event                           | synchronous event                              |
| **lowest** priority                          | **highest** priority                           |
| 1. Maskable<br>2. Non-maskable               | 1. Normal interrupt<br>2. [[Exception]] (trap) |

1. Maskable interrput: able to be turned off by [[Processor|CPU]] before execution of critical instruction sequences that must not be interrupted; used by device requests. 
2. Non-maskable interrupt: reserved for events such as unrecoverable memory errors. 

In modern computer, [[Processor|CPU]] and **interrupt-controller hardware** provide: 
1. the ability to **defer** interrupt handling during critical processing
   (e.g., maskable interrupt)
2. the efficient way to **dispatch** to the proper interrupt handler for a device 
   (e.g., interrupt chaining)
3. **multilevel interrupts** so that OS can distinguish b/w high- and low-**priority** interrupts and can respond with the appropriate degree of **urgency**. 
   (e.g., interrupt priority levels)

## Interrupt service routine
1. [[Device controller]] **raises** an interrupt by asserting **interrupt number** on **interrupt-request line**. 
2. [[Processor|CPU]] **catches** the interrupt, **reads** the interrupt number and **dispatch** to interrupt handler by using **interrupt vector**. 
5. [[Program counter]] loads the starting address of interrupt service routine (**fixed location**) instead of next instruction address. 
6.  [[Processor|CPU]] executes **interrupt service routine** / Interrupt handler **clears** the interrupt.  
7. On completion, [[Processor|CPU]] **resumes** the interrupted computation. 

![[Screen Shot 2022-10-09 at 15.16.56.png|500]]

## Interrupt vector
![[Screen Shot 2022-10-09 at 15.40.47.png|500]]
Intel interrupt vector: 0~31 (nonmaskable) and 32~255 (maskable)

- [[Vectored interrupt]]
- Interrupts must be handled **quickly**, as they occur very **frequently**. 
- To provide the speed, 
	1. Interrupt routines are called indirectly through **a table of pointers** to them. 
	2. The table of pointers is stored in **low memory**. 
	3. Each **interrput vector** (array) of address is indexed by the corresponding **interrupt number** (transferred by interrupt-request line) to provide the **address of interrupt service routine** for devices. 

- **Interrupt chaining**: 
  Every interrupt vector points to the head of a list of interrupt handlers to solve the {devices # > address elements #} problem. 
	1. Interrupt are raised. 
	2. Handlers on the corresponding list are called one by one until the one found.