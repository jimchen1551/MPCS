---
Created: [[2022-12-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# CPU-IO burst cycle
![[Screen Shot 2022-12-21 at 17.23.07.png|250]]
- **Process execution** consists of a cycle of 
  1. CPU execution
  2. IO wait
- Process execution begins with a **CPU burst**
- Then it's followed by an **IO burst** 
  (which is followed by another CPU burst, then another IO burst)
- Eventually, the **final CPU burst** ends with a system request to terminate the execution

Frequency curve of CPU burst durations: 
![[Screen Shot 2022-12-21 at 17.28.18.png|500]]
- An IO-bound program typically has many short CPU bursts
- A CPU-bound program might have a few long CPU burst
- The distribution is **important** when implementing **algorithms**