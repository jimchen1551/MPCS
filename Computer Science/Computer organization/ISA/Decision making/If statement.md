---
Created: [[2022-07-07]]
Aliases: 
Types: Card
Tags: 
- 
---
# If statement
```C
if (i==j) f = g+h;
else f = g-h;
\\ f→$s0, g→$s1, h→$s2, i→$s3, j→$s4
```
```MIPS
...
		bne $s3, $s4, Else
		add $s0, $s1, $s2   % if block
		j   Exit
Else:   sub $s0, $s1, $s2   % else block
Exit:   ...
```
- implemented with [[Branch]] and [[Jump]]