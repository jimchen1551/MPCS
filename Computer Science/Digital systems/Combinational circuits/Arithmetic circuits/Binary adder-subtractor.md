---
Created: [[2022-07-16]]
Aliases: 
Types: 
Tags: 
- 
---
# Binary adder-subtractors
![[Pasted image 20220628150601.png]]
$$X=A$$$$Y=S\oplus B$$$$C_{in}=S$$
Selection input S is necessary for **switching** between adder and subtractor. 

| S   | X   | Y   | $C_{in}$ |
| --- | --- | --- | -------- |
| 0   | A   | B   | 0        |
| 1   | A   | B'  | 1        |

## Overflow detection
![[Pasted image 20220630115732.png]]
For unsigned numbers, $C=C_n$
For signed numbers, $V=C_{n-1}\oplus C_n$