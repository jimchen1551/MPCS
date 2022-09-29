---
Created: [[2022-07-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Overflow
- Some languages (e.g., C) ignore overflow
  using [[MIPS]] addu, addiu, subu
- Other languages require raising an **exception**
  using [[MIPS]] add, addi, sub
  on overflow, invoking **exception handler**
  1. saving [[Program counter]] in **exception program counter** (EPC) register
  2. jumping to **predefined handler address**
  3. **mfc0** (move from coprocessor register) instruction can retreive EPC value, to return after corrective action
## Partitioned carry chain
- while using 64-bit adder, we can operate on 8 * 8-bit, 4 * 16-bit, or 2 * 32-bit vectors
- SIMD (single-instruction, multiple-data)
## Saturating operations
- on overflow, result is largest representable value (2's complement modulo arithmetic)