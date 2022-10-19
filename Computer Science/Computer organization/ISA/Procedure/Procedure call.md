---
Created: [[2022-10-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Procedure call
![[Screen Shot 2022-07-07 at 14.04.34.png|400]]
PC: [[#Program counter]]

If [[#Program counter]] meets procedure call at caller instruction sequence, 
1. Place parameters accessible to callee instruction sequence. $a0~3
2. (PC) Transfer control to procedure. $ra
3. Acquire storage needed for procedure. 
4. Perform desired task. 
5. Place result accessible to caller. $v0, $v1
6. (PC) Return control to caller. $ra

![[Pasted image 20220707141706.png|400]]
* Caller-saved: $t0~9
* Callee-saved: $s0~7

| Content             | Comment                      |
| ------------------- | ---------------------------- |
| [[Program counter]] | Instruction address register |
| [[Caller saving]]   | Register allocation          |
| [[Callee saving]]   | Register allocation          |
| [[Jump and link]]   | jal                          |
| [[Jump register]]   | jr                           |
| [[Procedure frame]] | $sp, $fp                     |
