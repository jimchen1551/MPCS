---
Created: [[2022-12-23]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multiple processors scheduling
- **Asymmetric multiprocessing** (AMP): 
  one core (master server) handles all scheduling decisions, IO processing, etc. , and the other cores execute only user code
  Flaw: the master server becomes 
- **[[Symmetric multiprocessing]]** (SMP): 
  each [[processor]] is self-scheduling
  2 strategies for organizing the [[thread]]s eligible to be scheduled: 
  1. all [[thread]]s may be in a common **ready** [[queue]]
     - having a possible **race condition** on the shared ready queue
     - must ensure that 2 separate processors do not choose to schedule the same thread and that threads are not lost from the queue
  2. each [[processor]] may have its own private queue of [[thread]]
     - not suffering from the possible performance problems associated with a shared run queue
     - more efficient use of [[cache memory]]
     - most common approach for SMP
![[Screen Shot 2022-12-23 at 15.37.35.png|500]]