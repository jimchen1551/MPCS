---
Created: [[2022-07-14]]
Aliases: XOR
Types: Card
Tags: 
- 
---
# Exclusive-OR
$$A\oplus B=AB'+A'B$$$$\overline{A\oplus B}=AB+A'B'$$
## Error detection
[[Alphanumeric codes#ASCII]] code (7 bits) + [[Parity bit]] = 8 bits
## Properties of XOR
$$A\oplus 0=A$$$$A\oplus 1=A'$$$$A\oplus A=0$$$$A\oplus A'=1$$$$A\oplus B'=\overline{A\oplus B}$$$$A\oplus B=B\oplus A$$$$(A\oplus B)\oplus C=A\oplus(B\oplus C)=A\oplus B\oplus C$$
## Odd function
$$A\oplus B\oplus C=\Sigma m(1, 2, 4, 7)$$
| A\BC | 00  | 01  | 11  | 10  |
|:----:|:---:|:---:|:---:|:---:|
|  0   |  0  |  1  |  0  |  1  |
|  1   |  1  |  0  |  1  |  0  |

$$A\oplus B\oplus C\oplus D=\Sigma m(1, 2, 4, 7, 8, 11, 13, 14)$$
| AB\CD | 00  | 01  | 11  | 10  |
|:-----:|:---:|:---:|:---:|:---:|
|  00   |  0  |  1  |  0  |  1  |
|  01   |  1  |  0  |  1  |  0  |
|  11   |  0  |  1  |  0  |  1  |
|  10   |  1  |  0  |  1  |  0  |

## Even function
$$(A\oplus B\oplus C\oplus D)=\Sigma m(0, 3, 5, 6, 9, 10, 12, 15)$$
| AB\CD | 00  | 01  | 11  | 10  |
|:-----:|:---:|:---:|:---:|:---:|
|  00   |  1  |  0  |  1  |  0  |
|  01   |  0  |  1  |  0  |  1  |
|  11   |  1  |  0  |  1  |  0  |
|  10   |  0  |  1  |  0  |  1  |
