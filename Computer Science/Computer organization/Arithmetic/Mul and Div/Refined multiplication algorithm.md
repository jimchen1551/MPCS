---
Created: [[2022-07-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Refined multiplication algorithm
![[Screen Shot 2022-07-21 at 11.47.06.png]]
- serving for unsigned multiplication
- The 64-bit product register is initialized with the multiplier and the left half is updated by the additive result of [[Arithmetic logic unit|ALU]] before the right shift on each step. 
- The 32-bit multiplicand doesn't need to shift left because of the right shift of the product. 
- The 32-bit multiplier is first written in the right half of the product register and shifts right 1 bit with the product on each step. 

![[Screen Shot 2022-07-21 at 16.24.42.png]]