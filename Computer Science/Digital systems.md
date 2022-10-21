---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Digital systems
| Digital systems                | Content                                                                                                                                                                                                                                         |
|:------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Combinational logic design]] | Design concepts<br>Level of integration<br>Implementation tech<br>Tech parameters                                                                                                                                                               |
| [[Combinational circuits]]     | [[Decoder]]<br>[[Encoder]]<br>[[Selection]]<br>[[Look-up table]]<br>[[Arithmetic block]]<br>[[Half adder]]<br>[[Full adder]]<br>[[Ripple carry adder]]<br>[[Carry lookahead adder]]<br>[[Binary adder-subtractor]]<br>[[Binary multiplication]] |
| [[Sequential circuits]]        | [[Flip-flop]]<br>[[Master-slave flip-flop]]<br>[[Edge-triggered flip-flop]]<br>[[JK flip-flop]]<br>[[T flip-flop]]<br>[[Latch]]<br>[[SR]]                                                                                                                                                                                                                                                |
| [[Registers]]                  |                                                                                                                                                                                                                                                 |

## Number systems
| Content                        |           Study           |           Test            |          Review           |
|:------------------------------ |:-------------------------:|:-------------------------:|:-------------------------:|
| [[Radix]]                      | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Binary-coded decimal codes]] | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Gray codes]]                 | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Alphanumeric codes]]         | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |
| [[Parity bit]]                 | <input type="checkbox" /> | <input type="checkbox" /> | <input type="checkbox" /> |

### Complement
| Content | Study | Test | Review |
| :------ | :---: | :--: | :----: |
|[[Radix complement]]|<input type="checkbox" />|<input type="checkbox" />|<input type="checkbox" />|
|[[Diminished radix complement]]|<input type="checkbox" />|<input type="checkbox" />|<input type="checkbox" />|
|[[1's complement]]|<input type="checkbox" />|<input type="checkbox" />|<input type="checkbox" />|
|[[2's complement]]|<input type="checkbox" />|<input type="checkbox" />|<input type="checkbox" />|

#### Signed complement
| Representation             | +9       | -9       |
| -------------------------- | -------- | -------- |
| [[Signed magnitude]]      | 00001001 | 10001001 |
| [[Signed 1's complement]] | 00001001 | 11110110 |
| [[Signed 2's complement]] | 00001001 | 11110111 |

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


