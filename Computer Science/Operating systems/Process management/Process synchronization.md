---
Created: [[2022-12-26]]
Aliases: 
Types: Note
Tags: 
- 
---
# Process synchronization

| Problems of synchronization     | Explanation |
| ------------------------------- | ----------- |
| [[Producer-consumer problem]]   |             |
| [[Critical-section problem]]    |             |
| [[Bounded-buffer problem]]      |             |
| [[Readers-writers problem]]     |             |
| [[Dining-philosophers problem]] |             |

| Hardware solutions        | Explanation                           |
| ------------------------- | ------------------------------------- |
| [[Memory barriers]]       | force to propagate                    |
| [[Hardware instructions]] | `test_and_set`<br>`compare_and_swap`  |
| [[Atomic variables]]      | mutual exclusion of a single variable |

| Software solutions      | Explanation                  |
| ----------------------- | ---------------------------- |
| [[Peterson's solution]] | `int turn`<br>`bool flag[2]` |
| [[Mutex locks]]         | `acquire()`<br>`release()`   |
| [[Semaphores]]          | `wait()`<br>`signal()`       |
| [[Monitors]]            | monitor type                      |

| Liveness failure       | Explanation                                    |
| ---------------------- | ---------------------------------------------- |
| [[Deadlock]]           | waiting for an event caused by other processes |
| [[Priority inversion]] | access resources from lower-priority processes |

## Evaluation

