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

- Program: **passive** entity, an executable file stored in the [[Disk]]
- Process: **active** entity, a program in execution in the [[Memory]]
- Program → Process: executable file loaded into the [[Memory]]

![[Pasted image 20220709002201.png]]

| Memory layout     | Size    | Explanation        |
| ----------------- | ------- | ------------------ |
| Text section      | fixed   | executable code    |
| Data section      | fixed   | global variables   |
| [[Heap]] section  | dynamic | dynamic allocation |
| [[Stack]] section | dynamic | activation record  |

- needing resources such as [[CPU time]], [[Memory]], [[IO]], and Files
- executing concurrently by multiplexing on a single [[Processor|CPU]] core
- reclaiming any reusable resources after termination

- [[Process state]]: the state of a process, e.g., new, ready, running, etc.
- [[Process control block]]: the repository for data to (re)start a process
- [[Process operation]]: [[Process creation]] and [[Process termination]]
- [[Thread]]: lightweight process
