---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multilevel feedback queue scheduling
![[Screen Shot 2022-12-21 at 22.08.28.png|400]]
- allowing a [[process]] to move b/w [[queue]]s
- separating [[process]]es according to the characteristics of their CPU bursts
- If a [[process]] uses too much [[CPU time]], it will be moved to a lower-priority [[queue]]. 
- If a [[process]] waits too long in a lower-priority [[queue]], it may be moved to a higher-priority [[queue]].
- Generally, the scheduler is defined by the following parameters:
  1. number of [[queue]]s
  2. scheduling algorithm for each [[queue]]
  3. method used to determine when to upgrade a [[process]] to a higher-priority [[queue]]
  4. method used to determine when to demote a [[process]] to a lower-priority [[queue]]
  5. method used to determine which [[queue]] a [[process]] will enter when that [[process]] needs service