---
Created: [[2022-12-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Priority-based scheduling
![[Screen Shot 2022-12-24 at 19.49.25.png|500]]
- for real-time scheduling, the scheduler must support preemptive, priority-based scheduling; however, it only guarantees the **soft real-time functionality** 
- for **hard** real-time systems, real-time tasks will be serviced in accordance with their deadline requirements, and making such guarantees require additional scheduling features
- [[Process]]es are **periodic** (fixed processing time $t$, a deadline $d$, and a period $p$; $0\leq t\leq d\leq p$).
- **Admission-control** algorithm: admitting the [[process]] or rejecting the request as impossible if it cannot guarantee that the task will be serviced by its deadline