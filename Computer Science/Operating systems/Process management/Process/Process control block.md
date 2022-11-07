---
Created: [[2022-11-07]]
Aliases: task control block, PCB
Types: Card
Tags: 
- 
---
# Process control block
![[Screen Shot 2022-11-07 at 12.55.16.png]]

| Info                  | Explanation                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [[Process state]]     | new, ready, etc.                                                                                                                      |
| [[Program counter]]   | the next instruction                                                                                                                  |
| [[Register]]          | saved while [[Interrupt]] occurs<br>1. accumulator<br>2. index register<br>3. stack pointer<br>4. general-purpose register<br>5. etc. |
| [[CPU scheduling]]    | 1. process priority<br>2. pointer to scheduling queue<br>3. etc.                                                                      |
| [[Memory management]] | 1. value of base and limit register<br>2. page table<br>3. segment table<br>4. etc.                                                   |
| Accounting            | 1. amount of CPU<br>2. real time used<br>3. time limit<br>4. account number<br>5. process number<br>6. etc.                           |
| IO status             | 1. list of IO allocated to the process<br>2. list of open files<br>3. etc.                                                            |

- the representation of each [[process]] in [[Operating systems|OS]]
- the repository for all data needed to start (restart) a [[process]]

![[Screen Shot 2022-11-07 at 13.06.12.png|500]]
