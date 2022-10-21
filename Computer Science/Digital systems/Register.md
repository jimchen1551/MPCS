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
### Register with parallel load
![[Screen Shot 2022-10-22 at 01.22.18.png]]
![[Screen Shot 2022-10-22 at 01.20.48.png]]
Approach 1: 
![[Screen Shot 2022-10-22 at 01.36.27.png]]
![[Screen Shot 2022-10-22 at 01.36.46.png]]
- loading control input through the **C** inputs of the [[Flip-flop]]s → **clock gating**
- preventing the clock from reaching the clock input to the circuit if the contents of the register are to be left unchanged
- $\text{C inputs}=Load'+Clock'$
- Inserting gates in the clock pulse path produces different [[Propagation delay]]s b/w clock and the inputs of [[Flip-flop]]s w/ and w/o clock gating → **clock skew**

Approach 2: 
![[Screen Shot 2022-10-22 at 01.39.29.png]]
- loading control input through the **D** inputs of the [[Flip-flop]]s
- $D_i=Load\cdot I_i+Load'\cdot Q_i$
## Shift register
Unidirection: 
![[Screen Shot 2022-10-22 at 01.43.31.png]]
Bidirection: (0 → left; 1 → right)
![[Screen Shot 2022-10-22 at 01.50.24.png]]
- a register capable of **shifting its binary info** in one or both direction
- $D_i=direction\cdot A_{i+1}+direction'\cdot A_{i-1}$
### Shift register with parallel load
Unidirection: 
![[Screen Shot 2022-10-22 at 01.47.24.png]]
![[Screen Shot 2022-10-22 at 01.45.03.png]]
- $D_i=Shift'\cdot Load\cdot I_i+Shift'\cdot Load'\cdot Q_i+Shift\cdot Q_{i-1}$
Bidirection: 
![[Screen Shot 2022-10-22 at 01.53.28.png]]
![[Screen Shot 2022-10-22 at 01.54.12.png]]
- $D_i=S_1'S_0'Q_i+S_1'S_0Q_{i-1}+S_1S_0'Q_{i+1}+S_1S_0I_i$
# Counter
- a register that goes through a predetermined sequence of states
## Ripple counter
## Synchronous binary counter
### Binary counter with JK Flip-Flops
### Up-down binary counter
### Binary counter with parallel load
## BCD counter