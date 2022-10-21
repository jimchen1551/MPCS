---
Created: [[2022-07-29]]
Aliases: 
Types: Note
Tags: 
- 
---
# Register
- consisting of a group of [[Flip-flop]]s capable of storing binary info and gates that determine how the info is transferred into the register
## Simplest register
![[Screen Shot 2022-10-22 at 01.17.53.png|200]]
![[Screen Shot 2022-10-22 at 01.17.17.png|200]]
- consisting of only [[Flip-flop]]s w/o any gates
## Register with parallel load

loading control input through the C inputs of the [[Flip-flop]] → **clock gating**
  preventing the clock from reaching the clock input to the circuit if the contents of the register are to be left unchanged
  $\text{C inputs}=Load'+Clock'$
  
- Approach 2: loading control input throuhg the D inputs of the [[Flip-flop]]
## Shift register
# Counter
- a register that goes through a predetermined sequence of states
## Ripple counter
## Synchronous binary counter