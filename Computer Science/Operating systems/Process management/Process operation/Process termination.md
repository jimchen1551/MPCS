---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Process termination

## Cascading termination
- If a [[process]] terminates, then all its children must also be terminated. 
- initiated by the OS

## UNIX
`exit()` [[system call]] deletes the [[process]] after execution
`wait()` [[system call]] returns data from child to parent
`abort()` [[system call]] terminates the execution of children [[process]]es
