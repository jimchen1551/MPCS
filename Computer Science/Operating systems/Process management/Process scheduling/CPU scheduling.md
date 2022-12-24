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

### Multicore processor scheduling
- [[Multi-core design]] and [[Multicore programming]]
![[Screen Shot 2022-12-23 at 16.30.05.png|400]]
- a **multithreaded**, **multicore** [[processor]] actually requires 2 different levels of scheduling (not mutually exclusive)
  1. scheduling decisions made by the [[Operating systems|OS]] as it chooses which **software thread** to run on each **hardware thread** (logical [[Processor|CPU]])
     - any scheduling algorithm can be adopted
  2. scheduling how each **core** decides which **hardware thread** to run
     - [[Round-robin scheduling]]
     - [[Multilevel queue scheduling]]

![[Screen Shot 2022-12-23 at 15.53.28.png|500]]
![[Screen Shot 2022-12-23 at 16.03.21.png|500]]
- **Memory stall**: the time for data to transfer from [[memory]] to [[processor]] since the [[processor]] requested (because processor operate faster than memory) and a cache miss occurred
  → solution: **multithreaded processing** cores in which 2 or more **hardware threads** are assigned to each core, so that if one hardware thread stalls for memory, the core can switch to another thread

![[Screen Shot 2022-12-23 at 16.10.16.png|400]]
- **Chip multithreading** (CMT): for [[Operating systems|OS]], each **hardware thread** maintain its architectural state (instruction pointer and register set), and thus appears as a logical [[Processor|CPU]] available to run a software [[thread]]. 
- **Hyper-threading** (simultaneous multithreading): assigning multiple **hardware threads** to a single processing core

#### Coarse-grained multithreading
- A [[thread]] executes on a core until a **long-latency event** such as a memory stall occurs. 
  → Because of the delay caused by the long-latency event, the core must switch to another [[thread]] to begin execution. 
  → However, the **cost of switching** between [[thread]]s is high, since the instruction pipeline must be **flushed** before the other [[thread]] can begin execution on the processor core. 
#### Fine-grained multithreading
- switching b/w [[thread]]s at a much **finer level of granularity**, typically at the boundary of an instruction cycle
- the architectural design includes logic for thread switching

### Load balancing
- for **SMP** to keep the workload evely distributed across all [[processor]]
#### Push migration
A specific task periodically checks the load on each [[processor]], and if an imblance found, evenly distributes the load by moving [[thread]]s from overloaded to idle or less-busy [[processor]]s
#### Pull migration
When an idle [[processor]] pulls a waiting task from a busy [[processor]], it occurs. 
### Processor affinity
![[Screen Shot 2022-12-23 at 17.07.35.png|500]]
- Because of the high cost of **invalidating** and **repopulating** [[Cache memory|cache]]s, most [[Operating systems|OS]] with **SMP** support try to **avoid migrating** a thread from one [[processor]] to another and instead attempt to keep a [[thread]] running on the same [[processor]] and take advantage of a warm [[Cache memory|cache]].
- a [[process]] has an **affinity** for the [[processor]] on which it is currently running
- the [[main memory]] architecture can affect processor affinity issues
- If the [[Operating systems|OS]]'s [[Short-term schedular|CPU schedular]] and memory-placement algorithms are **NUMA-aware** and work together, then a [[thread]] that has been scheduled onto a particular [[Processor|CPU]] can be allocated [[memory]] closest to where the [[Processor|CPU]] resides. 
#### Soft affinity
- When an [[Operating systems|OS]] has a policy of attempting to keep a [[process]] running on the same [[processor]] but **not guarantee** that it will do so
- still possible for the [[process]] to migrate during load balancing
#### Hard affinity
- allowing a [[process]] to specify a subset of [[processor]]s on which it can run
### Heterogeneous multiprocessing

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