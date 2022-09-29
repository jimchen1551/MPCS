---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# Memory operands
| Operator | Comment            |
| -------- | ------------------ |
| lb       | load byte          |
| lbu      | load byte unsigned |
| lh       | load half          |
| lhu      | load half unsigned |
| lw       | load word          |
| sb       | save byte          |
| sh       | save half          |
| sw       | save word          |

```C
g = h + A[8];  % g→$s1, h→$s2, A→$s3
```
```MIPS
lw  $t0, 32($s3)  % load word A[8]
add $s1, $s2, $t0 % $s1=$s2+$t0
```

```C
A[12] = h + A[8];  % A→s3, h→$s2
```
```MIPS
lw  $t0, 32($s3)  % load word A[8]
add $t0, $s2, $t0 % $t0=$s2+$t0
sw  $t0, 48($s3)  % store word A[12]
```
- [[#MIPS]] is [[#Big Endian]]. 
- [[Memory#Main memory]] used for composite data (arrays, structures, dynamic data)
- [[Memory]] is byte addressed (8 bits a byte, 4 bytes a word). 
- Words are aligned in [[Memory]]. 
- **loading** values from memory into registers
- **storing** result from register to memory

![[Pasted image 20220706154817.png]]
##### Big Endian
- most significant byte at least address of a word
##### Little Endian
- least significant byte at least address of a word