---
Created: [[2022-07-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Leaf procedure
![[Screen Shot 2022-07-08 at 10.45.57.png]]
- Callee doesn't call other procedures. 
```C
int leaf(int g, h, i, j)
{
	int f;
	f = (g+h) - (i+j)
	return f
}
\\ g→$a0, h→$a1, i→$a2, j→$a3, f→$s0, return $v0
```
```MIPS
Leaf:   
		addi $sp, $sp, -4
		sw   $s0, 0($sp)    % save callee on stack
		
		add  $t0, $a0, $a1
		add  $t1, $a2, $a3
		sub  $s0, $t0, $t1
		add  $v0, $s0, $zero% result
		
		lw   $s0, 0($sp)
		addi $sp, $sp, 4    % restore caller from stack
		
		jr   $ra            % return
```