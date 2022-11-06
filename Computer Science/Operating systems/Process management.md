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
![[Pasted image 20220709002201.png]]

| Memory layout | Explanation |
| ------------- | ----------- |
| Text section  |             |
| Data s              |             |

Program: passive entity, binary stored in [[Disk]]
Process: active entity, a program in execution in [[Memory]]
- a program in execution
- a unit of work in a system (OS processes and user processes)
- needing resources such as [[CPU time]], [[Memory]], [[IO]], and Files
- executing concurrently by multiplexing on a single [[Processor|CPU]] core
- consisting of 
  1. **Code section**: text
  2. **Data section**: global variables
  3. [[Stack]]: temporary local variables and functions
  4. [[Heap]]: dynamically allocated variables or classes
  5. Current activity: [[Program counter]], [[Register]] content
  6. A set of associated resources
- OS is responsible for
	1. Creating and deleting both user and system processes
	2. Threads and CPU scheduling
	3. Suspending and resuming processes
	4. Process synchronization
	5. Process communication
- OS reclaiming any reusable resources after termination
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

