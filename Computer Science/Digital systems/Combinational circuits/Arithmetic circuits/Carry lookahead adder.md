---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Carry lookahead adder
![[Pasted image 20220628131134.png]]
$$S_i=P_i\oplus C_i$$$$C_{i+1}=G_i+P_i\cdot C_i$$
- reducing delay at price of more complex hardware
- The arithmetic process is similar to that of [[Full adder]] but defining two custom function: [[#Carry propagate function]] & [[#Carry generate function]]

## Carry propagate function
$$P_i=A_i\oplus B_i$$
## Carry generate function
$$G_i=A_i\cdot B_i$$
## Carry lookahead expansion
$$C_1=G_0+P_0\cdot C_0$$$$C_2=G_1+P_1\cdot(G_0+P_0\cdot C_0)$$$$C_3=G_2+P_2\cdot(G_1+P_1\cdot(G_0+P_0\cdot C_0))$$$$\dots$$![[Pasted image 20220628131549.png]]
- Due to that maximal [[Fan-in]] # is **5**, concatenation of [[#Carry lookahead adder]] must causes **excessive fan-in**. 
- [[Hierarchical design]] ([[4-bit grouping carry lookahead adder]]) is considered to solve this problem. 
