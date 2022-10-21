---
Created: [[2022-10-21]]
Aliases: system call interface, RTE
Types: Card
Tags: 
- 
---
# Run-time environment
![[Screen Shot 2022-10-21 at 18.07.52.png|500]]
- aka **RTE**
- the full suite of software needed to execute app written in a given programming language, including its **compilers** or **interpreters** as well as **libraries** and **loaders**
- providing a **system-call interface** that serves as the link to [[System call]]s made available by the OS

1. the system-call interface **intercepts function calls** in the [[Application Programming interface|API]] and invoking the necessary [[System call]]s within the OS
2. a number is associated with each [[System call]], and the system-call interface **maintains a table indexed** according to these numbers. 
3. the system-call interface then **invokes the intended [[System call]]** in the OS kernel and **returns the status** of the [[System call]]
