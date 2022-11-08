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

| Logical         | Implementation                                                      |
| --------------- | ------------------------------------------------------------------- |
| Naming          | [[Direct communication]]<br>[[Indirect communication]]              |
| Synchronization | [[Synchronous communication]]<br>[[Asynchronous communication]]     |
| Buffering       | [[Zero capacity]]<br>[[Bounded capacity]]<br>[[Unbounded capacity]] |

## UNIX
`send(message)`
`receive(message)`
