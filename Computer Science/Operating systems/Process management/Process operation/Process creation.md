---
Created: [[2022-11-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Process creation
![[Screen Shot 2022-11-07 at 23.03.33.png|500]]
- **Parent** process creates **children** process.
- OS identifies processes according to a unique **process identify** (pid, an integer)

## Resource sharing
1. Parent and children share all resources. 
2. Children share subset of parent's resources. 
3. Parent and child share no resources. 

## Execution
1. Parent and children execute concurrently. 
2. Parent waits until children terminate. 

## Address space
1. Child duplicate of parent. 
2. Child has a program loaded into it. 

## UNIX
`fork()` [[system call]] creates new [[process]]
`exec()` [[system call]] used after a `fork()` to replace the process' memory space with a new program