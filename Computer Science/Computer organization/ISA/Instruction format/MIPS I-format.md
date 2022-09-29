---
Created: [[2022-07-06]]
Aliases: 
Types: Card
Tags: 
- 
---
# MIPS I-format
![[Screen Shot 2022-07-06 at 16.06.40.png]]
- **immediate** arithmetic and **load/store** instruction
1. op: operation code, 6 bits
2. rs: first source register number, 5 bits
3. rt: destination or source register number, 5 bits
4. constant or address: 16 bits
   - constant: $-2^{15}$ ~ $2^{15}-1$
   - address: offset added to base addess in rs

![[Screen Shot 2022-07-06 at 16.07.14.png]]
![[Screen Shot 2022-07-06 at 16.07.59.png]]
![[Screen Shot 2022-07-06 at 16.08.31.png]]
## 32-bit constant
Due to the only 16 bits for constant in [[MIPS I-format]], if there's a 32-bit constant to load...
```MIPS
lui $s0, 61          \\ copying 16-bit constant to $s0
                     \\ clears right 16 bits of $s0 to 0
ori $s0, $s0, 2304   
```