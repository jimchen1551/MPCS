---
Created: [[2022-07-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Barrel shifter
![[Pasted image 20220719130344.png]]
![[Pasted image 20220719130815.png]]
- multiple-bit position shifter
- left/right input and shamt (shift amount) input are required
- performing with [[Multiplexer|MUX]] and by using a right rotate:
	- p-position right shift: rotate p position to the right
	- p-position left shift: rotate (16-p, [[2's complement]]) position to the right

## 32-bit barrel shifter
![[Pasted image 20220721112021.png]]