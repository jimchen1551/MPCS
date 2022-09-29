---
Created: [[2022-08-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Dynamic multiple issue
 - **Superscalar** processor (common now)
 - CPU examines the instruction stream and chooses instructions to issue each cycle. (avoiding [[Structural hazard]] and [[Data hazard]])
 - [[Compiler]] can help by reordering instructions
 - **CPU** resolves hazards using advanced techniques at runtime. 

## Dynamic pipeline scheduling
![[Screen Shot 2022-08-17 at 15.10.29.png]]
 - allowing the CPU to **execute** instructions **out of order** to avoid stalls but committing **results** to register **in order**
1. An instruction fetch and issue unit
   - fetching instructions, decoding them, and sending each instruction to the reservation station of the corresponding functional unit of the execute stage
2. Multiple function units
   - **Reservation station**: each functional unit has buffers
   - As soon as the buffer contains all its operands and the functional unit is ready to execute, the result is calculated. 
3. A commit unit
   - deciding when it is safe to put the result into the [[Register file]] or into memory

## Register renaming
- **Reservation stations** and **Reorder buffer** effectively provide register renaming
- On instruction issue to reservation station
  1. if the operand is available in [[Register file]] or **reorder buffer**, 
     - copied to reservation station
     - overwritten because no longer required in the register
	2. if the operand is not yet available, 
	   - provided to the reservation station by a **function unit**
	   - not required for register update