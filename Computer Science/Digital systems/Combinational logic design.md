---
Created: [[2022-07-14]]
Aliases: 
Types: Note
Tags: 
- 
---
# Combinational logic design
## Design concepts
| Design                             | Comment |
| ---------------------------------- | ------- |
| [[Hierarchical Design]]            |         |
| [[Computer-Aided Design]]          |         |
| [[Hardware Description Languages]] |         |
| [[Logic Synthesis]]                |         |

## Design space
[[Integrated circuit|IC]]
### Levels of integration
| Level                            | Comment |
| -------------------------------- | ------- |
| [[Small-scale integration]]      |         |
| [[Medium-scale integration]]     |         |
| [[Large-scale integration]]      |         |
| [[Very-large-scale integration]] |         |

### Implementation technology
| Tech                                        | Comment |
| ------------------------------------------- | ------- |
| [[Diode logic]]                             |         |
| [[Resistor-transistor logic]]               |         |
| [[Diode-transistor logic]]                  |         |
| [[Transistor-transistor logic]]             |         |
| [[Emitter-coupled logic]]                   |         |
| [[Metal-oxide semiconductor]]               |         |
| [[Complementary metal-oxide semiconductor]] |         |
| [[Gallium Arsenide]]                        |         |
| [[Silicon Germanium]]                       |         |

### Technology parameters
| Parameter             | Comment |
| --------------------- | ------- |
| [[Fan-in]]            |         |
| [[Fan-out]]           |         |
| [[Noise margin]]      |         |
| [[Cost for a gate]]   |         |
| [[Propagation delay]] |         |
| [[Power dissipation]] |         |

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
