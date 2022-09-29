---
Created: [[2022-07-09]]
Aliases: 
Types: Card
Tags: 
- 
---
# Nested procedure
![[Screen Shot 2022-07-09 at 00.29.07.png]]
- Callee also calls other procedures. 
	- As a caller
		- saving on the [[Stack]] before calling its own $ra, $a0~3, $t0~9 needed after the call
		- restoring from the [[Stack]] after the call
```MIPS
L1:
...
addi $sp, $sp, -8
sw   $ra, 4($sp)
sw   $a0, 0($sp)
jal  L2
lw   $a0, 0($sp)
lw   $ra, 4($sp)
addi $sp, $sp, 8
...
L2:
...
jr $ra
```
