---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Digital systems
| Digital systems                | Content                                                                                                                                                                                                                                                       |
|:------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Combinational logic design]] | Design concepts<br>Level of integration<br>Implementation tech<br>Tech parameters                                                                                                                                                                             |
| [[Combinational circuits]]     | [[Decoder]]<br>[[Encoder]]<br>[[Selection]]<br>[[Look-up table]]<br>[[Arithmetic block]]<br>[[Half adder]]<br>[[Full adder]]<br>[[Ripple carry adder]]<br>[[Carry lookahead adder]]<br>[[Binary adder-subtractor]]<br>[[Binary multiplication]]               |
| [[Sequential circuits]]        | [[Flip-flop]]<br>[[Master-slave flip-flop]]<br>[[Edge-triggered flip-flop]]<br>[[JK flip-flop]]<br>[[T flip-flop]]<br>[[Latch]]<br>[[SR latch]]<br>[[S'R' latch]]<br>[[D latch]]<br>Direct input<br>Timing<br>Performance<br>Analysis<br>Simulation<br>Design |
| [[Registers]]                  |                                                                                                                                                                                                                                                               |

## Number systems
| Number systems   | Content                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Coding           | [[Radix]]<br>[[Binary-coded decimal codes]]<br>[[Gray codes]]<br>[[Alphanumeric codes]]<br>[[Parity bit]] |
| Complement       | [[Radix complement]]<br>[[Diminished radix complement]]<br>[[1's complement]]<br>[[2's complement]]       |
| Sined complement | [[Signed magnitude]]<br>[[Signed 1's complement]]<br>[[Signed 2's complement]]                            |

## Boolean algebra
- addressed by George Bool
![[Pasted image 20220616183918.png]]

| Logic gate         | Algorithmic          | Properties       |
| ------------------ | -------------------- | ---------------- |
| [[And]]            | [[Universal set]]    | [[Commutative]]  |
| [[Or]]             | [[Empty set]]        | [[Distributive]] |
| [[Not]]            | [[Double negation]]  | [[Associative]]  |
| [[Exclusive-OR]]   | [[de Morgan's laws]] |                  |
| [[Universal gate]] |                      |                  |
| [[Complex gate]]   |                      |                  |

### Expression
| Expression                | Comment   |
| ------------------------- | --------- |
| [[Truth table]]           |           |
| [[Don't care conditions]] | x         |
| [[Terms and literals]]    |           |
| [[Standard forms]]        | SOP & POS |

### Minimization
| Cost criteria       | Karnaugh map                    | Optimization                |
| ------------------- | ------------------------------- | --------------------------- |
| [[Literal cost]]    | [[Karnaugh map simplification]] | [[Multilevel optimization]] |
| [[Gate input cost]] | [[Implicant]]                   |                             |
|                     | [[Prime implicant]]             |                             |
|                     | [[Essential prime implicant]]   |                             |

### Hi-impedance outputs
While there're multiple gates that **connect their outputs together**, the states of each gate may have:
- 0
- 1
- **Hi-Z** (high-impedance state, disconnect)

| Gate                  | Comment |
| --------------------- | ------- |
| [[Three-State Bus]]   |         |
| [[Multiplexer]]       |         |
| [[Transmission gate]] |         |


