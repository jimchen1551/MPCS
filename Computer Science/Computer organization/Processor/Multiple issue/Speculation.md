---
Created: [[2022-08-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Speculation
- commonly used in [[Static multiple issue]] and [[Dynamic multiple issue]]
- guessing what to do with an instruction
  - starting ASAP
  - checking whether the guess was right
- Implementation: 
  1. [[Compiler]]: 
     - reordering instructions
     - including **fix-up** instructions to recover from incorrect guess
  2. Hardware: 
     - looking ahead for instructions to execute
     - buffering results until it determines they are actually needed
     - flushing buffers on incorrect speculation
- e.g., branch prediction (not committing until branch outcome determined) and load speculation (avoiding load and cache miss delay, predicting the effective address and value, loading before completing outstanding stores, bypassing stored values to load unit, not committing load until speculation cleard)

## Static speculation
- adding ISA support for deferring exceptions

## Dynamic speculation
- buffering exceptions until instruction completion
