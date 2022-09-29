---
Created: [[2022-07-25]]
Aliases: FP addition
Types: Card
Tags: 
- 
---
# Floating-point addition
![[Screen Shot 2022-07-25 at 15.35.28.png]]
1. Shifting the smaller number right to align with the larger number
2. Adding the significands
3. Normalizing the sum to the [[IEEE std 754]]
4. If overflow, exception; else, rounding the significand
5. If normalized, work done; else, jump to step 3. 

## Hardware
- If done in only one [[Clock cycle]], the [[Clock period]] might be too long. 
- Usually pipelined and done in several [[Clock cycle]]s

![[Screen Shot 2022-07-25 at 15.48.07.png]]