---
Created: [[2022-10-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Timer
-  to prevent infinite loop or process hogging resources and **never returning control to the OS**
- set to interrupt the computer after a specified period

1. The OS sets the **counter**. (**[[Multi-mode#Privileged instruction]]**)
2. Every time the clock ticks, the counter is **decremented**. 
3. When the counter reaches **0**, an [[Interrupt]] occurs.
4. Before turning over control to the user, the OS ensures that the timer is set to interrupt.
5. If the timer interrupts, **control transfers automatically to the OS**, which may treat the [[Interrupt]] as a **fatal error** or may give the program **more time**.