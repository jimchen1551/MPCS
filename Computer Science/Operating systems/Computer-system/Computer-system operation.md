---
Created: [[2022-10-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Computer-system operation
After a computer is powered on, 
1. [[Bootstrap program]] stored in EEPROM is the first program to run which can locate the OS kernel and load it into the [[Memory]]. 
2. [[System daemon]]s provide services outside of the kernel and run all the time the kernel is running. 
3. [[System call]]s are specific requests from a user program which would cause software interrupt to make OS execute some special operations. 
4. [[Interrupt]]s may be invoked by a [[Device controller]], an error, or an [[System call]]. 

| Operation            | Comment                      |
| -------------------- | ---------------------------- |
| [[Multiprogramming]] | efficiency                   |
| [[Multitasking]]     | time sharing                 |
| [[Multi-mode]]       | user and kernel modes        |
| [[Timer]]            | prevention of losing control |
