---
Created: [[2022-07-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Karnaugh map simplification
![[Pasted image 20220615183121.png]]
| ab\cd |    00    |    01    |    11    |    10    |
|:-----:|:--------:|:--------:|:--------:|:--------:|
|  00   |  $m_0$   |  $m_1$   |  $m_3$   |  $m_2$   |
|  01   |  $m_4$   |  $m_5$   |  $m_7$   |  $m_6$   |
|  11   | $m_{12}$ | $m_{13}$ | $m_{15}$ | $m_{14}$ |
|  10   |  $m_8$   |  $m_9$   | $m_{11}$ | $m_{10}$ |

## Flow of finding the simplified expression
$$F=\Sigma m(i)$$
1. Determine all [[Prime implicant]]s.
2. Determine all [[Essential prime implicant]]s. 
3. $F=\Sigma \text{ all EPIs}+\Sigma \text{ necessary PIs}$
   While selecting necessary PIs, we should **prevent overlap** of [[Implicant]]s. 