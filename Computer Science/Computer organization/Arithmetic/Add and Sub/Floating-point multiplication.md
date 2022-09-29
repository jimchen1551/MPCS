---
Created: [[2022-07-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Floating-point multiplication
![[Screen Shot 2022-07-25 at 15.53.27.png]]
1. Adding the exponents and subtracting bias to get a new exponent
2. Multiplying the significands
3. Normalizing the product to the [[IEEE std 754]]
4. If overflow, exception; else, rounding the significand
5. If normalized, work done after setting sign bit; else, jump to step 3. 

## Hardware
- The complexity of multiplication resembles that of [[Floating-point addition|FP addition]]. 
- So the floating-point arithmetic hardware usually does addition, subtraction, multiplication, division, reciprocal, and square root. 
- Usually pipelined and done in several [[Clock cycle]]s