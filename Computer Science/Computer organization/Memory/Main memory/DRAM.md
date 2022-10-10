---
Created: [[2022-09-26]]
Aliases: dynamic RAM
Types: Card
Tags: 
- 
---
# DRAM
![[Pasted image 20220926152642.png]]
![[Screen Shot 2022-09-26 at 14.39.18.png]]
- volatile memory
- needing only 1 transistor
- stored as a charge in a **capacitor**
- consuming less power
- periodically **refreshed** (reading contents and writing back)
- accessing an entire row
- **Burst mode**: supply successive words from a row with reduced latency

## DDR DRAM
- double data rate DRAM
- transferring on rising and falling clock edges

## QDR DRAM
- quad data rate DRAM
- separating DDR inputs and outputs

## Performance factors
- Row buffer: allowing several words to be read and refreshed in parallel
- Synchronous DRAM: allowing for consecutive accesses in bursts w/o needing to send each address; improving bandwidth
- DRAM banking: allowing simultaneous access to multiple DRAMs; improving bandwidth