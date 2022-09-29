---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Encoder
![[Pasted image 20220619041431.png]]
$$Y_0=m_0=(A_2', A_1', A_0')$$$$\dots$$$$Y_7=m_7=(A_2, A_1, A_0)$$
- turning [[Minterm]]s into binary codes
- limitations of encoder:
  1. one and only one input can be active at any given time
     Solution: [[#Priority encoder]]
  2. when all the inputs are 0, the output is 000
     Solution: Valid-output indicator

## Priority encoder
![[Pasted image 20220619041908.png]]

| I(3) | I(2) | I(1) | I(0) | O(0) | O(1) |  V  |
|:----:|:----:|:----:|:----:|:----:|:----:|:---:|
|  0   |  0   |  0   |  0   |  x   |  x   |  0  |
|  0   |  0   |  0   |  1   |  0   |  0   |  1  |
|  0   |  0   |  1   |  x   |  0   |  1   |  1  |
|  0   |  1   |  x   |  x   |  1   |  0   |  1  |
|  1   |  x   |  x   |  x   |  1   |  1   |  1  |

Priority: I(3)>I(2)>I(1)>I(0); V: valid-output indicator