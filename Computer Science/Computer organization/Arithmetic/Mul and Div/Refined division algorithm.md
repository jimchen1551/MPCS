---
Created: [[2022-07-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Refined division algorithm
![[Screen Shot 2022-07-21 at 15.55.55.png]]
- The 64-bit remainder register is initialized with the dividend and the left half is updated by the subtractive result of [[Arithmetic logic unit|ALU]] if the result is not negative after shifting left and filled with quotient (=negative?0:1) on each step. 
- The 32-bit divisor doesn't need to shift left because of the left shift of the remainder and quotient. 

![[Screen Shot 2022-07-21 at 16.26.12.png]]