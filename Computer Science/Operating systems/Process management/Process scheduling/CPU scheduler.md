---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# CPU scheduler
- selecting a [[process]] from the processes ready to execute
- allocating the [[Processor|CPU]] to that [[process]]
- the ready queue can be implemented as a [[Queue]], a [[Priority queue]], a [[Binary search tree]], or even a [[Linked list]]
- the records in the queues are generally [[Process control block|PCB]] of the processes

| Scheduler                 | Explanation     |
| ------------------------- | --------------- |
| [[Short-term schedular]]  | ready → running |
| [[Medium-term schedular]] | ready → wait    |
| [[Long-term schedular]]   | new → ready     |
