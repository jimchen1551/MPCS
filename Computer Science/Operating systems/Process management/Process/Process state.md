---
Created: [[2022-11-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Process state
![[Screen Shot 2022-11-07 at 12.41.56.png|500]]

| State      | Explanation                           |
| ---------- | ------------------------------------- |
| New        | creating process                      |
| Ready      | waiting to be assigned to a processor |
| Running    | executing instructions                |
| Waiting    | waiting for some event to occur       |
| Terminated | finishing execution                   |

1. new → ready: [[Long-term schedular]]
2. ready → running: [[Short-term schedular]]
3. running → ready: [[Interrupt]] or time out
4. running → waiting: [[System call]] or IO request
5. waiting → running: Event occurs or IO complete
6. running → terminated: Finish

- only 1 process can be **running** on any processor core
- many processes may be **ready** and **waiting**
