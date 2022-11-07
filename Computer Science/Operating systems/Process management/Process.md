---
Created: [[2022-11-07]]
Aliases: 
Types: Note
Tags: 
- 
---
# Process
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
- [[Process state]]
- [[Process control block]]

## Thread