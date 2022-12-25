---
Created: [[2022-11-07]]
Aliases: 
Types: Note
Tags: 
- 
---
# CPU scheduling
- switching the [[Processor|CPU]] among [[Process]]es to make the computer more productive
- Basic concepts: 
  1. A [[process]] is executed until it must wait. 
  2. In a simple computer system, the [[Processor|CPU]] then sits **idle**.
  3. With [[Multiprogramming]], when one [[process]] has to wait, another [[process]] can **take over** the use of the [[Processor|CPU]]. 

| Fundamentals              | Content                                                                          |
| ------------------------- | -------------------------------------------------------------------------------- |
| [[CPU-IO burst cycle]]    | CPU burst<br>IO burst                                                            |
| [[CPU scheduler]]         | [[Short-term schedular]]<br>[[Medium-term schedular]]<br>[[Long-term schedular]] |
| [[Preemptive scheduling]] | Preemptive scheduling<br>Non-preemptive scheduling                               |
| [[Dispatcher]]            | Dispatch latency                                                                 |

| Scheduling algorithms                    | Explanation                  |
| ---------------------------------------- | ---------------------------- |
| [[First-come, first-served scheduling]]  | FIFO [[queue]]               |
| [[Shortest-job-first scheduling]]        | shortest CPU burst           |
| [[Round-robin scheduling]]               | time quantum                 |
| [[Priority scheduling]]                  | priority                     |
| [[Multilevel queue scheduling]]          | multiple fixed [[queue]]s    |
| [[Multilevel feedback queue scheduling]] | allowing to cross [[queue]]s |

## Scheduling criteria
1. **CPU utilization**: keep the [[Processor|CPU]] as busy as possible
2. **Throughput**: number of processes completed per time unit
3. **Turnaround time**: time to execute a particular process
4. **Waiting time**: time for a [[process]] waiting in the **ready** queue
5. **Response time**: time for a request to be responded

## Thread scheduling
- most modern [[Operating systems|OS]] scheduling [[kernel]]-level [[thread]]s
- and [[thread library]] managing user-level [[thread]]s (independent of the [[kernel]])
- ultimately user-level [[thread]]s are mapped to an associated [[kernel]]-level [[thread]] indirectly or by using a **lightweight process** (LWP)
- **Process-contention scope** (PCS): 
  In **many-to-one** and **many-to-many** models, the [[thread library]] schedules user-level [[thread]]s to run on an available LWP
- To decide which [[kernel]]-level [[thread]] to schedule onto a [[Processor|CPU]], the [[kernel]] uses **system-contention scope** (SCS)
- Typically, PCS is done according to priority and preempts the current thread in favor of a higher-priority thread. 

## Multi-processor issue
[[Multi-processor system]]
- **Multi-processor**: 
  1. multiple [[Processor|CPU]]s
  2. multi-threaded cores
  3. [[Non-uniform memory access|NUMA]] systems
  4. heterogeneous multiprocessing
- **Load sharing**: multiple [[thread]]s running in parallel

| Issues                             | Content                                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Multiple processors scheduling]] | Asymmetric multiprocessing<br>[[Symmetric multiprocessing]]                                                                                                       |
| [[Multicore processor scheduling]] | Memory stall<br>Software thread<br>Hardware thread<br>Chip multithreading<br>Hyper-multithreading<br>Coarse-grained multithreading<br>Fine-grained multithreading |
| [[Load balancing]]                 | Push migration<br>Pull migration                                                                                                                                  |
| [[Processor affinity]]             | Soft affinity<br>Hard affinity                                                                                                                                    |
| [[Heterogeneous multiprocessing]]  |                                                                                                                                                                   |

## Real-time computing issue
[[Real-time embedded system]]
- **Soft real-time systems** provide no guarantee when a critical real-time process is scheduled but guarantee the process will be given preference over noncritical processes. 
- **Hard real-time systems** restrict that a task must be serviced by its deadline; service, after the deadline has expired, is the same as no service at all. 
- The system is waiting for an event in real-time to occur. 
- When an event occurs, the system must respond to and service it as quickly as possible. 
- **Event latency**: the time that elapses from when an event occurs to when it is serviced. 
  ![[Screen Shot 2022-12-24 at 12.03.31.png|400]]
  1. **Interrupt latency**: the time from the arrival of an [[interrupt]] at the [[Processor|CPU]] to the start of the routine that services the [[interrupt]]
     - crucial for real-time systems to **minimize** interrupt latency to ensure that real-time tasks receive immediate attention
     - one important factor is the time interrupts may be disabled while kernel data structures are being updated
     ![[Screen Shot 2022-12-24 at 12.09.16.png|400]]
  2. **Dispatch latency**: the time for the [[dispatcher]] to stop one [[process]] and start another one
     - providing **preemptive kernels** to lower the dispatch latency
     - The **conflict phase** of dispatch latency has 2 components:
       1. Preemption of any [[process]] running in the [[kernel]]
       2. Release by low-priority [[process]]es of resources needed by a high-priority [[process]]
       ![[Screen Shot 2022-12-24 at 12.23.41.png|400]]

| Scheduling algorithm                   | Explanation |
| -------------------------------------- | ----------- |
| [[Priority-based scheduling]]          |             |
| [[Rate-monotonic scheduling]]          |             |
| [[Earliest-deadline-first scheduling]] |             |
| [[Proportional share scheduling]]      |             |

## Algorithm evaluation
### Deterministic modeling
- one type of **analytic evaluation**
- taking a particular predetermined workload
- defining the performance of each algorithm for that workload
### Queueing models
- the distribution of [[CPU-IO burst cycle]]s can be determined
- the computer system is described as a network of servers
- each server has a [[queue]] of **waiting** [[process]]es
- the [[Processor|CPU]] is a server with its **ready** [[queue]], as is the [[IO]] system with its device [[queue]]s
- **Queueing-network analysis**: knowing the arrival rate and service rate, we can compute utilization, average queue length, average wait time, and so on. 
- **Little's formula**: $n=\lambda\times W$, where $n$ is the average long-term queue length, $\lambda$ is the average arrival rate, and $W$ is the average waiting time in the queue. 
### Simulations
![[Screen Shot 2022-12-26 at 02.30.37.png|500]]
- more accurate than queueing models
- programmed model of computer system
- clock is a variable
- garthering statistics indicating algorithm performance
- data to drive simulation gathered via
  1. random number generator
  2. distribution defined
  3. trace tapes record sequence of real events in real systems
### Implementation
- implementing new scheduler and testing in real systems