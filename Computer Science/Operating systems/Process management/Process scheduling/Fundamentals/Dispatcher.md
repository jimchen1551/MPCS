---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Dispatcher
1. switching **context** from one [[process]] to another
2. switching to **user mode**
3. jumping to the proper location in the user program to **resume** that program
![[Screen Shot 2022-12-21 at 19.34.52.png|250]]
- the module that gives control of the [[Processor|CPU]]'s core to the [[process]] selected by the [[CPU scheduler]]
- invoked during every [[context switch]]
- **dispatch latency**: the time to stop one [[process]] and start another running