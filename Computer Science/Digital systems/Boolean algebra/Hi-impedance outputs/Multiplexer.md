---
Created: [[2022-07-14]]
Aliases: MUX
Types: Card
Tags: 
- 
---
# Multiplexer
$$f_1(IN_1, EN_1)\text{ connect }f_2(IN_2, EN_2)$$
![[MUX.gif]]
![[Pasted image 20220617045343.png]]

| IN1 IN2 | EN1 EN2 |  OL  |
|:-------:|:-------:|:----:|
|   xx    |   00    | Hi-Z |
|   0x    |   10    |  0   |
|   1x    |   10    |  1   |
|   x0    |   01    |  0   |
|   x1    |   01    |  1   |
|   00    |   11    |  0   |
|   11    |   11    |  1   |
|   10    |   11    |  ?   |
|   01    |   11    |  ?   |
