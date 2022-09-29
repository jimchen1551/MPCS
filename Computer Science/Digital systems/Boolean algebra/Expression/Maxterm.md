---
Created: [[2022-07-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Maxterm
[[Standard forms]]
$$F(A, B, C)=\Pi f(A, B, C)$$
$$f(A, B, C)=aA+bB+cC|a, b, c\in\{0, 1\}$$
$$f(A, B, C)=M_i|i=(1-a)\cdot2^2+(1-b)\cdot2^1+(1-c)\cdot2^0$$
e.g., 
1. $$f(A, B, C, D)=A'+B+C'+D=M_{10}=m_{10}'$$
2. $$F'(A, B, C, D)=AB'+C'D$$$$F'(A, B, C, D)=m_1+m_5+m_8+m_9+m_{10}+m_{11}+m_{13}$$$$F(A, B, C, D)=M_1\cdot M_5\cdot M_8\cdot M_9\cdot M_{10}\cdot M_{11}\cdot M_{13}$$$$F(A, B, C, D)=\Pi M(1, 5, 8, 9, 10, 11, 13)$$