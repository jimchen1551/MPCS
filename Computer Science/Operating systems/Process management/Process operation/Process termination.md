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

## Zombie
- the [[process]] with no parents waiting

## Orphan
- the parent of the [[process]] terminates w/o invoking a `wait`

## UNIX
`exit()` [[system call]] deletes the [[process]] after execution
`wait()` [[system call]] returns data from child to parent
`abort()` [[system call]] terminates the execution of children [[process]]es
