---
Created: [[2022-12-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Load balancing
- for [[Symmetric multiprocessing|SMP]] to keep the workload evenly distributed across all [[processor]]
## Push migration
A specific task periodically checks the load on each [[processor]], and if an imbalance is found, evenly distributes the load by moving [[thread]]s from overloaded to idle or less-busy [[processor]]s
## Pull migration
When an idle [[processor]] pulls a waiting task from a busy [[processor]], it occurs. 
