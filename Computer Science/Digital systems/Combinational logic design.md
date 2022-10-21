---
Created: [[2022-07-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Combinational logic design
| [[Integrated circuit]] | Content                                                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Design concepts        | [[Hierarchical Design]]<br>[[Computer-Aided Design]]<br>[[Hardware Description Languages]]<br>[[Logic Synthesis]]                                                                                                                                                               |
| Level of integration   | [[Small-scale integration]]<br>[[Medium-scale integration]]<br>[[Large-scale integration]]<br>[[Very-large-scale integration]]                                                                                                                                                  |
| Implementation tech    | [[Diode logic]]<br>[[Resistor-transistor logic]]<br>[[Diode-transistor logic]]<br>[[Transistor-transistor logic]]<br>[[Emitter-coupled logic]]<br>[[Metal-oxide semiconductor]]<br>[[Complementary metal-oxide semiconductor]]<br>[[Gallium Arsenide]]<br>[[Silicon Germanium]] |
| Tech parameters        | [[Fan-in]]<br>[[Fan-out]]<br>[[Noise margin]]<br>[[Cost for a gate]]<br>[[Propagation delay]]<br>[[Power dissipation]]                                                                                                                                                          |

## Design procedure
| Procedure              | Comment                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Specification          | writing a spec for the circuit                                                                                           |
| Formulation            | defining the required relationships between inputs and outputs                                                           |
| Optimization           | applying two-level or multi-level optimization and drawing a logic diagram or providing a netlist                        |
| [[Technology mapping]] | transforming the logic diagram or netlist to a new diagram or netlist using the available [[#Implementation technology]] |
| [[Verification]]           | verifying the correctness of the final design                                                                            |

## Programmable logic device (PLD)
- An IC with programmable gates divided into an [[And]] array and an [[Or]] array to provide an AND-OR sum of product implementation. 
-  establishing or breaking interconnection (major)
- building lookup tables (minor)
- controlling transistor switching (minor)

| Technology                   | Comment |
| ---------------------------- | ------- |
| [[Read-only memory]]         |         |
| [[Programmable logic array]] |         |
| [[Programmable array logic]] |         |
