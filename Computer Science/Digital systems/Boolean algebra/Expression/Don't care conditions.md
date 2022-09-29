---
Created: [[2022-07-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Don't care conditions
- denoted by $\times$ in [[Truth table]]
- the **unspecified [[Minterm]]** of a function
e.g., $$F(A, B, C, D)=\Sigma m(1, 3, 7, 11, 15)$$$$d(A, B, C, D)=\Sigma m(0, 2, 5)$$

| AB\CD | 00  | 01  | 11  | 10  |
|:-----:|:---:|:---:|:---:|:---:|
|  00   |  x  |  1  |  1  |  x  |
|  01   |  0  |  x  |  1  |  0  |
|  11   |  0  |  0  |  1  |  0  |
|  10   |  0  |  0  |  1  |  0  |

$F$ can be represented as $A'B'+CD$ or $A'D+CD$ or $D(A'+C)$. 