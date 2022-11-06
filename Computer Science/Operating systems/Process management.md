---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Process management
- [[Processor]]
## Process
- a program in execution
- a unit of work in a system (OS processes and user processes)
- Program: **passive** entity, binary words stored in [[Disk]]
- Process: **active** entity, a program in execution in [[Memory]]

![[Pasted image 20220709002201.png]]

| Memory layout     | Explanation                   |
| ----------------- | ----------------------------- |
| Text section      | executable code               |
| Data section      | global variables              |
| [[Heap]] section  | dynamic allocation            |
| [[Stack]] section | local variables and functions |

- needing resources such as [[CPU time]], [[Memory]], [[IO]], and Files
- executing concurrently by multiplexing on a single [[Processor|CPU]] core
- reclaiming any reusable resources after termination
### Process state
### Process control block
### Thread
- aka lightweight process
- a basic unit of CPU utilization
## Process scheduling
### Scheduling queue
### CPU scheduling
### Context switch
## Operation on process
### Process creation
### Process termination
## Interprocess communication
### in shared memory system
### in message-passing system
## Communication in Client-Server System
### Sockets
### Remote procedure call

