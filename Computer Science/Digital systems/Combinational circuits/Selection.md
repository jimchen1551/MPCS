---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Selection
## [[Multiplexer]] implementation
$$OUT=(SI_0'SI_1'SI_2')IN_0+\dots+(SI_0SI_1SI_2)IN_7$$$$OUT=\Sigma^7_{i=0}m_i\cdot IN_i$$

| SI  | m   | OUT |
| --- | --- | --- |
| 000 | 0   | IN0 |
| 001 | 1   | IN1 |
| 010 | 2   | IN2 |
| 011 | 3   | IN3 |
| 100 | 4   | IN4 |
| 101 | 5   | IN5 |
| 110 | 6   | IN6 |
| 111 | 7   | IN7 |

- A [[Multiplexer]] is abbreviated as MUX and is also called a data selector. 
- If we got n selection inputs, we could determine which of the $2^n$ inputs to pass into the output. 
- This can be implemented with the combination of a decoder for selection inputs and enabling circuits for each inputs. 
- 
![[Screen Shot 2022-06-20 at 13.11.06.png]]
Gate-input count=22

## [[Three-State Bus]] implementation

![[Pasted image 20220620134856.png]]

Gate-input count=18

## [[Transmission gate]] implementation

![[Pasted image 20220620135757.png]]

Gate-input count=8