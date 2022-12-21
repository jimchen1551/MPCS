---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Preemptive scheduling
4 circumstances when making CPU-scheduling decisions:
1. When a [[process]] switches from **running** to **waiting**
2. When a [[process]] switches from **running** to **ready**
3. When a [[process]] switches from **waiting** to **ready**
4. When a [[process]] terminates

For cases 1 and 4, it's **non-preemptive** (cooperative) scheduling
- selecting a new [[process]] for execution
- once the [[Processor|CPU]] has been allocated to a [[process]], 
  the [[process]] keeps the [[Processor|CPU]] until it releases it 
  (by termination or by switching to the waiting state)

For cases 2 and 3, it's **preemptive** scheduling
- resulting in **race conditions** when data are shared among several [[process]]es
- affecting the design of the [[Operating systems|OS]] [[kernel]]
  (during the processing of a [[system call]], 
  the [[kernel]] may be busy with activity on behalf of a [[process]], 
  and such activities may involve changing important [[kernel]] data)
  → a non-preemptive [[kernel]] will wait 
  1. for a [[system call]] to complete or 
  2. for a [[process]] to block while waiting for IO to complete
  before doing a [[context switch]]
  → a simple structure to ensure not preempting a [[process]] while the [[kernel]] data structures are in an inconsistent state