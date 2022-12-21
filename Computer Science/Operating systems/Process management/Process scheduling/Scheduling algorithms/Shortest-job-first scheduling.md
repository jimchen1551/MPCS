---
Created: [[2022-12-21]]
Aliases: SJF
Types: Card
Tags: 
- 
---
# Shortest-job-first scheduling
- shortest-next-CPU-burst algorithm
- depending on the length of the next CPU burst of a process, rather than its total length
- not implemented at the level of CPU scheduling (because there's no way to know the length of the next CPU burst)
  → solution is to **approximate** the length of the next CPU burst
  → prediction is made by the **exponential average** of the measured lengths of previous CPU bursts