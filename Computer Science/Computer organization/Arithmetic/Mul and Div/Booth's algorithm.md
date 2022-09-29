---
Created: [[2022-07-21]]
Aliases: 
Types: Card
Tags: 
- 
---
# Booth's algorithm
![[Pasted image 20220721122409.png]]

![[Screen Shot 2022-07-21 at 12.16.04.png]]

| State     | Action                                           |
| --------- | ------------------------------------------------ |
| Beginning | $\text{Product}-\text{Multiplicand After Shift}$ |
| Middle    | Do nothing                                       |
| End       | $\text{Product}+\text{Multiplicand After Shift}$ |

- serving for signed ([[Signed 2's complement]]) and unsigned multiplication
- Key insight: classifying groups of bits (multiplier) into the beginning, middle, or end of a run of 1s
- starting with a 0 for the bit to the right of the rightmost bit
- extending the sign when the product is shifted to the right
  
- e.g., 
  $2_{10} \times 6_{10} = 0010_2\times0110_2$
  $6_{10} =0110_2=1000_2-0010_2$
  $0010_2\times0110_2=0010_2\times1000_2-0010_2\times 0010_2$
  $=10000_2-00100_2=01100_2=12_{10}$, 
  
  $-3_{10}\times14_{10}=11111101_2\times00001110_2$
  $14_{10} =00001110_2=00010000_2-00000010_2$
  $11111101_2\times00001110_2$
  $=11111101_2\times00010000_2-11111101_2\times00000010_2$
  $=11010000_2-11111010_2=11010110_2=-42_{10}$
  
## 2-bit Booth encoding
![[Pasted image 20220721125108.png]]

![[Screen Shot 2022-07-21 at 12.55.29.png]]
- considering not only the previous bit but the next
- preventing the highly frequent bit change of multiplier