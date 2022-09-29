---
Created: [[2022-09-23]]
Aliases: 
Types: Card
Tags: 
- 
---
# Cache memory
- closest to [[Processor|CPU]] in the level of the memory hierarchy
- commonly implemented by [[SRAM]] (static RAM)
## Direct mapped cache
![[Screen Shot 2022-09-26 at 16.26.52.png]]
- Location = Block address mod(number of blocks in cache)
- taking the low-order bits as address if block number is $2^k$
- storing
	- data: copied from [[Main memory]]
	- tag: taking the rest high-order bits
	- valid bit: 1 = present; 0 = absent
**not done here**
## Cache performance
## Cache coherence