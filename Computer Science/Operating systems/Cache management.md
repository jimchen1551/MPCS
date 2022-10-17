---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Cache management
- [[Cache memory]]
## Caching
![[Screen Shot 2022-10-17 at 18.09.16.png|500]]
- Info in use copied from slower to faster storage temporarily
- Faster storage checked first to determine if info is there
	- If it is, info used directly from the cache
	- If not, data copied to cache and used there
## Coherency
- The same data may appear in different levels. 
- If [[Multitasking]] or Multi-processor system, the access of the data needs to obtain the most recent value. 