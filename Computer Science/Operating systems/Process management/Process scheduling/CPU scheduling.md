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

| Scheduling algorithm                   | Explanation |
| -------------------------------------- | ----------- |
| [[Priority-based scheduling]]          |             |
| [[Rate-monotonic scheduling]]          |             |
| [[Earliest-deadline-first scheduling]] |             |
| [[Proportional share scheduling]]      |             |

## Algorithm evaluation
### Deterministic modeling
### Queueing models
### Simulations
### Implementation