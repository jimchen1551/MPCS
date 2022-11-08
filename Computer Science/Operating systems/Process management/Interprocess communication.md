---
Created: [[2022-11-08]]
Aliases: IPC
Types: 
Tags: 
- 
---
# Interprocess communication
![[Screen Shot 2022-11-08 at 10.26.24.png|500]]
- **independent**: no share data with any other [[process]]
- **cooperating**: affecting other [[process]]es or affected by other [[process]]es

- allowing [[process]]es to exchange data

## Reasons
1. Information sharing
2. Computation speedup
3. Modularity

## Models
### Shared memory
- a region of [[memory]] shared by the cooperating [[process]]es
- [[process]]es can exchange info by reading and writing data to the region
### Message passing
- 