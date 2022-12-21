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
| [[Preemptive scheduling]] |                                                                                  |
| [[Dispatcher]]            |                                                                                  |

| Scheduling algorithms                    | Explanation |
| ---------------------------------------- | ----------- |
| [[First-come, first-served scheduling]]  |             |
| [[Shortest-job-first scheduling]]        |             |
| [[Round-robin scheduling]]               |             |
| [[Priority scheduling]]                  |             |
| [[Multilevel queue scheduling]]          |             |
| [[Multilevel feedback queue scheduling]] |             |

## Scheduling criteria

## Thread scheduling

## Multi-processor scheduling
### Multicore processor
### Load balancing
### Processor affinity
### Heterogeneous multiprocessing
## Real-time CPU scheduling
### Minimizing latency
### Priority-based scheduling
### Rate-monotonic scheduling
### Earliest-deadline-first scheduling
### Proportional share scheduling
## Algorithm evaluation
### Deterministic modeling
### Queueing models
### Simulations
### Implementation