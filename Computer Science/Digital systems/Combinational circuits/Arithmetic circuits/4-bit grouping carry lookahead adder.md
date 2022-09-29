---
Created: [[2022-07-16]]
Aliases: 
Types: 
Tags: 
- 
---
# 4-bit grouping carry lookahead adder
![[Pasted image 20220628130847.png]]
![[Screen Shot 2022-06-28 at 13.21.55.png]]
![[Screen Shot 2022-06-28 at 13.25.07.png]]
$$C_4=G_{0-3}+P_{0-3}\cdot C_0$$
Maximal [[Fan-in]] = 2
It takes **4(log n/log 4)+2** gate delays to propagate. 
## Group generate function
$$G_{0-3}=G_3+P_3\cdot G_2+P_3\cdot P_2\cdot G_1+P_3\cdot P_2\cdot P_1\cdot G_0$$
Maximal [[Fan-in]] = 4
## Group propagate function
$$P_{0-3}=P_3\cdot P_2\cdot P_1\cdot P_0$$
Maximal [[Fan-in]] = 4