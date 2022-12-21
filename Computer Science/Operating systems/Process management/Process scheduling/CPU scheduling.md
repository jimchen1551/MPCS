---
Created: [[2022-11-07]]
Aliases: 
Types: Note
Tags: 
- 
---
# CPU scheduling
- switching the [[Processor|CPU]] among [[Process]]es to make the computer more productive
- A [[process]] is executed until it must wait. 
  In a simple computer system, the [[Processor|CPU]] then sits **idle**.
  With [[Multiprogramming]], when one [[process]] has to wait, another [[process]] can **take over** the use of the [[Processor|CPU]]. 

| Fundamentals              | Explanation |
| ------------------------- | ----------- |
| [[CPU-IO burst cycle]]    |             |
| [[Preemptive scheduling]] |             |
| [[Dispatcher]]            |             |

| [[CPU schedular]]         | Explanation     |
| ------------------------- | --------------- |
| [[Short-term schedular]]  | ready → running |
| [[Medium-term schedular]] | ready → wait    |
| [[Long-term schedular]]   | new → ready     |

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