---
Created: [[2022-07-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# Loop statement
```C
while (save[i]==k) i += 1;
\\ save→$s6, i→$s3, k→$s5
```
```MIPS
Loop:   sll  $t1, $s3, 2
		add  $t1, $t1, $s6
		lw   $t0, 0($t1)
		bne  $t0, $s5, Exit
		addi $s3, $s3, 1
		j    Loop
Exit: ...
```
- implemented with [[Shift operation]], [[Register operands]], [[Branch]], and [[Jump]]