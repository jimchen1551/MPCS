---
Created: [[2022-10-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Instruction-level parallelism
- **Pipelining**: executing multiple instructions in parallel
  - ideal case: CPI = 1
- To increase parallelism, 
  1. deeper pipeline → less work per stage → shorter clock cycle
  2. multiple issue
     - replicating pipeline stages→multiple pipelines
     - starting multiple instructions per clock cycle
     - CPI < 1, so use IPC
     1. [[Speculation]]
     2. [[Static multiple issue]]
	3. [[Dynamic multiple issue]]