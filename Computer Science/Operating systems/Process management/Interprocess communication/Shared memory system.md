---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Shared memory system
- a region of [[memory]] shared by the cooperating [[process]]es
- [[process]]es can exchange info by reading and writing data to the region
- faster than [[message passing system]] because a [[system call]] is required only to establish a shared memory region

## Producer-consumer problem
- **producer** process produces info that is consumed by a **consumer** process
- providing a useful metaphor for the [[Client-server communication]]

- **unbounded-buffer** places no practical limit on the size of the buffer
- **bounded-buffer** assumes that there's a fixed buffer size
