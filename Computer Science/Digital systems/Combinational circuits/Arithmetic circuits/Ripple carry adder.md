---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Ripple carry adder
![[Pasted image 20220620170946.png]]
$$S_i=A_i\oplus B_i\oplus C_i$$$$C_{i+1}=A_iB_i+C_i(A_i\oplus B_i)$$
- also called parallel adder
- concatenating n full adders in parallel and in cascade with all input bits applied simultaneously

## Carry propagation
- It takes **2n+2** gate delays to propagate through the full adders. 
- Assumption delay of XOR gate=2; the # of bits of the inputs=n