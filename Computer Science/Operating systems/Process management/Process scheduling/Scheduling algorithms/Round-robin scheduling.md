---
Created: [[2022-12-21]]
Aliases: RR
Types: Card
Tags: 
- 
---
# Round-robin scheduling
![[Screen Shot 2022-12-21 at 21.13.40.png]]
- preemptive
- similar to [[First-come, first-served scheduling|FCFS]] but adding **preemption** to enable the system to switch b/w processes
- the **ready** queue served as a **circular** queue
- [[CPU scheduler]] visits around the ready queue, allocating the [[Processor|CPU]] to each [[process]] for a time interval up to 1 time quantum
  1. Picks the first process from the ready queue
  2. Sets a timer to interrupt after 1 time quantum
  3. Dispatches the process
- **time quantum** (time slice): a small unit of time, generally 10~100 milliseconds
  1. time quantum too large → same as the [[First-come, first-served scheduling|FCFS]]
  2. time quantum too small → substantial [[context switch]]es 
- in practice, the [[context switch]] takes 10 microseconds
- a rule of thumb is that 80% of the CPU bursts should be shorter than the time quantum
- the size of the time quantum also affects **turnaround time**
![[Screen Shot 2022-12-21 at 21.27.19.png]]
