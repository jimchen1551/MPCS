---
Created: [[2022-12-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Processor affinity
![[Screen Shot 2022-12-23 at 17.07.35.png|500]]
- Because of the high cost of **invalidating** and **repopulating** [[Cache memory|cache]]s, most [[Operating systems|OS]] with **SMP** support try to **avoid migrating** a thread from one [[processor]] to another and instead attempt to keep a [[thread]] running on the same [[processor]] and take advantage of a warm [[Cache memory|cache]].
- a [[process]] has an **affinity** for the [[processor]] on which it is currently running
- the [[main memory]] architecture can affect processor affinity issues
- If the [[Operating systems|OS]]'s [[Short-term schedular|CPU schedular]] and memory-placement algorithms are **NUMA-aware** and work together, then a [[thread]] that has been scheduled onto a particular [[Processor|CPU]] can be allocated the [[memory]] closest to where the [[Processor|CPU]] resides. 
## Soft affinity
- When an [[Operating systems|OS]] has a policy of attempting to keep a [[process]] running on the same [[processor]] but **not guarantee** that it will do so
- still possible for the [[process]] to migrate during load balancing
## Hard affinity
- allowing a [[process]] to specify a subset of [[processor]]s on which it can run
