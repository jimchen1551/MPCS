---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Priority scheduling
![[Screen Shot 2022-12-21 at 21.30.16.png]]
![[Screen Shot 2022-12-21 at 21.37.57.png|400]]
- preemptive or non-preemptive
- the [[Processor|CPU]] is allocated to the [[process]] with the highest priority
- equal-priority [[process]]es are scheduled in [[First-come, first-served scheduling|FCFS]] order (stable)
- priority of [[Shortest-job-first scheduling|SJF]] is the inverse of the next CPU burst
- Major problem: **indefinite blocking** (starvation)
  Some low-priority [[process]]es wait indefinitely. 
  → solution: 
  1. run at 2 AM Sunday
  2. crash and lose all unfinished low-priority [[process]]es
  3. **aging**: gradually increasing the priority of [[process]]es waiting in the system for a long time
  4. combining with [[Round-robin scheduling]]

![[Screen Shot 2022-12-21 at 21.50.58.png]]
![[Screen Shot 2022-12-21 at 21.51.15.png|400]]