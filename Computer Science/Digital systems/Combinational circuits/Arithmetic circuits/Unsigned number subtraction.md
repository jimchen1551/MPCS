---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Unsigned number subtraction
$M-N$
If no end borrow occurs ($M\geq N$):
- The result is $M-N$
If an end borrow occurs ($M\leq N$):
- The result is ($M-N+2^n$) in arithmetics
- [[2's complement]] of ($M-N+2^n$) is ($N-M$)
- The answer should be corrected by an negative symbol $-(N-M)$

The whole process can by simplified with the following steps:
1. Take $N'$ as the [[2's complement]] of $N$
2. Get $Ans'=M+N'$
3. True answer ($Ans$) is the negative of the [[2's complement]] of $Ans'$

Or the following steps:
1. Take $N'$ as the [[1's complement]] of $N$
2. Get $Ans'=M+N'$
3. If end carry occurs, the true answer ($Ans$) is $Ans'$ discarding the end carry and adding one to the sum. 
4. Else, the true answer($Ans$) is the negative of the [[1's complement]] of $Ans'$

$M-N=M+N'_2=M+N'_1+1$