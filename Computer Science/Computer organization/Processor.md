---
Created: [[2022-07-19]]
Aliases: CPU
Types: Note
Tags: 
- 
---
# Processor
![[Screen Shot 2022-08-17 at 16.27.41.png]]

## Instruction execution
![[Screen Shot 2022-07-19 at 13.57.33.png]]
1. The address written in the [[Program counter]] (in the [[Control unit]]) was loaded into the instruction memory to fetch instruction. 
2. The content of [[Program counter]] was updated with the target address or current value + 4. 
3. The content of corresponding registers was read out by the instruction. 
4. Decode the instruction. 
5. After decoding the instruction, the CPU may use [[Arithmetic logic unit|ALU]] to calculate corresponding operations depending on the instruction class.

## Logic design convention
### State element
- storing information
- [[Registers]]: storing data in a circuit
### Combinational element
- operating on data
- output is a function of input

## Datapath
| Datapath                                    | Comment                                                            |
| ------------------------------------------- | ------------------------------------------------------------------ |
| [[Instruction fetch datapath]]              | for fetching instructions and incrementing the [[Program counter]] |
| [[Arithmetic-logical instruction datapath]] | for [[MIPS R-format]] instructions <br>(add, sub, and, or, slt)        |
| [[Memory instruction datapath]]             | for load and store ([[MIPS I-format]]) instructions                |
| [[Branch instruction datapath]]             | for beq ([[MIPS I-format]]) instruction                            |
| [[Jump instruction datapath]]               | for j ([[MIPS J-format]]) instruction                              |

## Single-cycle implementation
- using **single clock cycle** for every instruction
  - any datapath resource cannot be used more than once per insrtuction
  - any element needed more than once must be duplicated
  - need a memory for instruction seperate from that for data
- After combination, we got [[Single-cycle CPU]]
- violating design principle "Making the common case fast"
- We may improve performance by [[#Multi-cycle implementation]] or [[#Pipelining]]

## Pipelining
![[Screen Shot 2022-08-02 at 13.59.31.png]]
- an implementation technique in which multiple instructions are overlapped in execution
  1. **IF**: instruction fetch from memory
  2. **ID**: instruction decode and register read
  3. **EX**: execute operation or calculate address
  4. **MEM**: accress memory operand
  5. **WB**: write result back to register
- Speedup: 
  $\displaystyle\text{Time b/w instrs}_{\text{pipelined}}=\frac{\text{Time b/w instrs}_{\text{nonpipelined}}}{\text{number of pipe stages}}$

### Datapath and control
![[Pasted image 20220808200702.png]]
1. [[Pipelined datapath]]
   - [[Single-clock-cycle pipeline diagram]]
   - [[Multi-clock-cycle pipeline diagram]]
2. [[Pipelined control]]

### Hazards
![[Pasted image 20220810213742.png]]
- situations in pipelining when the **next instruction cannot execute** in the following clock cycle
- [[Hazard detection]]

| Hazard                | Solutions                                                   |
| --------------------- | ----------------------------------------------------------- |
| [[Structural hazard]] | Duplication of hardware                                     |
| [[Data hazard]]       | [[Stalling]] and [[Forwarding]]                             |
| [[Control hazard]]    | [[Stalling]], [[Branch prediction]], and [[Delayed branch]] |

### MIPS design for pipelining
1. All [[MIPS]] instrucitons are the same length. 
   - easy to fetch instructions in **IF** stage and to decode them in **ID** stage
2. [[MIPS]] has only a few instruction formats, with the source register fields being located in the same place in each instruction. 
   - reducing redundant stages
3. Memory operands only appear in **load** and **store** in [[MIPS]]. 
   - using **EX** stage to calculate the memory address and to access memory in the following stage
4. Operands must be aligned in memory. 
   - The requested data can be transferred b/w processor and memory in a single stage. 

## Exception
![[Screen Shot 2022-08-11 at 00.56.58.png]]

**Exception**: arising within the CPU; e.g., undefined opcode, overflow, syscall, ...
**Interrupt**: from an external IO controller
- Another form of [[Control hazard]]
- In [[MIPS]], exceptions managed by a **system control coprocessor** (CP0)
  1. saving [[Program counter|PC]] of offending instruction into **exception program counter** (EPC)
  2. saving **indication** of the problem into **cause register**
  3. jumping to **handler** at 8000 00180

### Handler
- reading cause and transferring to relevant handler
- determining action required...
  - if restartable, taking corrective action and using EPC to return to program
  - otherwise, terminating program and reporting error using EPC, cause, ...

### Vectored interrupts
- handler address determined by the cause
- e.g., 
  undefined opcode: C000 0000
  overflow                 : C000 0020
  ...

### Precise exceptions
- dealing with exception from earliest instruction and flushing the subsequent instructions
- out-of-order completion
- hard to maintain but common

### Imprecise exceptions
- just stop pipeline and save state including exception causes
- let the handler work out (to complete or flush)
- simplifies hardware, but more complex handler software
- not feasible for complex multiple-issue out-of-order pipelines

## Instruction-level parallelism
- **Pipelining**: executing multiple instructions in parallel
  - ideal case: CPI = 1
- To increase parallelism, 
  1. deeper pipeline → less work per stage → shorter clock cycle
  2. multiple issue
     - replicating pipeline stages→multiple pipelines
     - starting multiple instructions per clock cycle
     - CPI < 1, so use IPC
     1. [[Speculation]]
     2. [[Static multiple issue]]
	3. [[Dynamic multiple issue]]

## ARM Cortex-A53 vs Intel Core i7 6700
![[Screen Shot 2022-08-17 at 15.44.57.png]]
### ARM Cortex-A53
![[Screen Shot 2022-08-17 at 15.52.42.png]]
### Intel Core i7 6700
![[Screen Shot 2022-08-17 at 16.07.00.png]]

## Fallacy
1. Pipelining is easy. 
2. Pipelining ideas can be implemented independently of technology. 

## Pitfall
1. Poor ISA design can make pipelining harder
