---
Created: [[2022-07-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Combinational circuits
![[Pasted image 20220618002025.png]]
- The outputs of logic gates are determined **only by the inputs**. 

| Circuit           | Comment |
| ----------------- | ------- |
| [[Decoder]]       |         |
| [[Encoder]]       |         |
| [[Selection]]     |         |
| [[Look-up table]] |         |

## Rudimentary logic

| Function         | x=0 | x=1 |
| ---------------- | --- | --- |
| Value-fixing (0) | 0   | 0   |
| Value-fixing (1) | 1   | 1   |
| Transferring     | 0   | 1   |
| Inverting        | 1   | 0   |

### Enabling
- permitting an input to pass through to an output (transferring or value-fixing)
- requiring an additional input signal: EN
$$F=EN\cdot x$$

| x\EN | 0   | 1   |
| ---- | --- | --- |
| 0    | 0   | 0   |
| 1    | 0   | 1   |

$$F=x+EN'$$

| x\EN | 0   | 1   |
| ---- | --- | --- |
| 0    | 1   | 0   |
| 1    | 1   | 1   |

## Arithmetic circuits
### Iterative combinational circuits
[[Arithmetic block]]

### Binary adders
| Adder                     | Comment |
| ------------------------- | ------- |
| [[Half adder]]            |         |
| [[Full adder]]            |         |
| [[Ripple carry adder]]    |         |
| [[Carry lookahead adder]] |         |

#### Speeding addition
1. employing faster gates with reduced delays
2. increasing the complexity to reduce the carry delay time (e.g., [[Carry lookahead adder]])

### Binary subtraction
| Subtraction                                | Comment |
| ------------------------------------------ | ------- |
| [[Unsigned number subtraction]]            |         |
| [[Signed number addition and subtraction]] |         |

### Binary adder-subtractors
[[Binary adder-subtractor]]

### Binary multiplication
[[Binary multiplication]]

### Other arithmetic functions
#### Incrementer
- adding a fixed value to an arithmetic variable
- $A+1=A+B+C_0$ with $B=1, C_0=0$
#### Decrementer
- adding a fixed negative value to an arithmetic variable
#### Multiplication by $2^i$
#### Division by $2^i$
#### Greater than comparison
#### Lesser than comparison
#### Zero fill
#### Sign extension