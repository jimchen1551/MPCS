---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Message passing system
- messages exchanged b/w the cooperating [[process]]es
- suitable for a small amount of data
- easier to implement in a [[Distributed system]]
- implemented using [[system call]]s
- **communication link**: established by the [[process]]es to communicate

Physical implementation: 
1. Shared memory
2. Hardware bus
3. Network

Logical implementation: 
1. Direct/indirect communication
2. Sync/async communication
3. Automatic/explicit buffering

## Naming
### Direct communication
### Indirect communication
## Synchronization
### Synchronous communication
### Asynchronous communication
## Buffering
### Automatic buffering
### 
## UNIX
`send(message)`
`receive(message)`
