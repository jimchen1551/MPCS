---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# Register operands
| Operator | Comment           |
| -------- | ----------------- |
| add      | add               |
| addu     | add unsigned      |
| sub      | subtract          |
| subu     | subtract unsigned |
| mult     | multiply          |
| multu    | multiply unsigned |
| div      | divide            |
| divu     | divide unsigned   |

```C
f = (g+h) - (i+j)
// f→$s0, g→$s1, h→$s2, i→$s3, j→$s4
```
```MIPS
add $t0, $s1, $s2  % $t0=$s1+$s2
add $t1, $s3, $s4  % $t1=$s3+$s4
sub $s0, $t0, $t1  % $s0=$t0+$t1
```
- [[#MIPS]] has 32 32-bit register files. 
- numbered 0~31
- **$t0~9** for temporary values
- **$s0~7** for saved variables
- 32-bit data called a **word** (4 bytes)
- for **frequently accessed** data

![[Pasted image 20220706152735.png]]