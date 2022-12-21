---
Created: [[2022-12-21]]
Aliases: SJF
Types: Card
Tags: 
- 
---
# Shortest-job-first scheduling
- preemptive (shortest-remaining-time-first) or non-preemptive
- **shortest-next-CPU-burst** algorithm
- depending on the **length of the next CPU burst** of a process, rather than its total length
- not implemented at the level of CPU scheduling 
  (there's no way to know the length of the next CPU burst)
  
  → solution is to **approximate** the length of the next CPU burst
  → prediction is made by the **exponential average** of the measured lengths of previous CPU bursts
  
  The next CPU burst is predicted as $\tau_{n+1}=\alpha t_n+(1-\alpha)\tau_n$, where $0\leq\alpha\leq1$, $t_n$ contains most recent info, and $\tau_n$ stores the past history. 
  
  The extension of $\tau_{n+1}$ is $\alpha t_n+(1-\alpha)\alpha t_{n-1}+\dots+(1-\alpha)^j\alpha t_{n-j}+\dots+(1-\alpha)^{n+1}\tau_0$. 
  
Prediction of the length of the next CPU burst: 
![[Screen Shot 2022-12-21 at 20.29.38.png]]