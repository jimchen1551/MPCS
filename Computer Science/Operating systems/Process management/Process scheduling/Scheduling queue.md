---
Created: [[2022-11-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Scheduling queue
![[Screen Shot 2022-11-07 at 20.25.19.png|500]]
![[Screen Shot 2022-11-07 at 20.34.44.png|500]]
## Job queue
- set of all [[process]]es in the system
## Ready queue
- set of all [[process]]es in the [[main memory]]
- ready and waiting to execute
- stored as a [[Linked list]]
	- a **ready-queue header** contains pointers to the first [[Process control block]]
	- each [[Process control block]] includes a **pointer field** pointing to the next
## Wait queue
- set of all [[process]]es in the [[main memory]]
- waiting for the event to occur
## Device queue
- set of [[process]]es waiting for an [[IO]] device