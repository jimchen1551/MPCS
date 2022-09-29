---
Created: [[2022-07-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Ordinary division algorithm
![[Screen Shot 2022-07-21 at 13.55.01.png]]
- The 64-bit remainder register is initialized with the dividend and updated by the subtractive result of [[Arithmetic logic unit|ALU]] if the result is not negative or else not updated. 
- The 32-bit divisor starts in the left half of the divisor register and shifts right 1 bit on each step. 
- The 32-bit quotient is shifted left 1 bit on each step and filled with 1 if the result of [[Arithmetic logic unit|ALU]] >=0, else 0. 

![[Screen Shot 2022-07-21 at 16.25.37.png]]