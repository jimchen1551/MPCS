---
Created: [[2022-07-06]]
Aliases: 
Types: Note
Tags: 
- 
---
# Memory
## Principle of locality
| Locality | Comment                                                           |
| -------- | ----------------------------------------------------------------- |
| Temporal | Items accessed recently are likely <br>to be accessed again soon      |
| Spatial  | Items near those accessed recently <br>are likely to be accessed soon |

## Memory hierarchy and technology
![[Screen Shot 2022-10-09 at 14.58.34.png]]
![[Screen Shot 2022-10-17 at 18.05.34.png]]
- storing everything on the [[Secondary memory]]
- copying recently accessed items to the [[Main memory]]
- copying more recently accessed items to the [[Cache memory]]

**Hit**: accessed data is present in the upper level
**Miss**: accessed data is absent in the upper level (then copy from the lower level)

| Memory               | Function               | Technology         | Unit  |
| -------------------- | ---------------------- | ------------------ | ----- |
| [[Register]]        |                        |                    |       |
| [[Cache memory]]     |                        | [[SRAM]]           | Line  |
| [[Main memory]]      | instruction and data   | [[DRAM]]           | Page  |
| [[Secondary memory]] | system and app program | [[Disk]], NVM      | Block |
| [[Tertiary memory]]  | backup                 | [[Flash]], CD, DVD |       |

## Virtual machine
## Virtual memory
## Memory hierarchy
## Finite-state machine
## Redundant arrays of disks
## ARM Cortex-A8 vs Intel Core i7
## Fallacies
## Pitfalls