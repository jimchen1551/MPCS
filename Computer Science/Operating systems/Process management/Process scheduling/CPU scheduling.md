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

| Scheduling algorithms                    | Explanation |
| ---------------------------------------- | ----------- |
| [[First-come, first-served scheduling]]  |             |
| [[Shortest-job-first scheduling]]        |             |
| [[Round-robin scheduling]]               |             |
| [[Priority scheduling]]                  |             |
| [[Multilevel queue scheduling]]          |             |
| [[Multilevel feedback queue scheduling]] |             |

## Scheduling criteria
1. **CPU utilization**: keep the [[Processor|CPU]] as busy as possible
2. **Throughput**: number of processes completed per time unit
3. **Turnaround time**: time to execute a particular process
4. **Waiting time**: time for a [[process]] waiting in the **ready** queue
5. **Response time**: time for a request to be responded

## Thread scheduling

## Multi-processor issue
### Multiple processors
### Multicore processor
### Load balancing
### Processor affinity
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