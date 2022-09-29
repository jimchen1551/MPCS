---
Created: [[2022-08-17]]
Aliases: 
Types: Card
Tags: 
- 
---
# Static multiple issue
 - [[Compiler]] groups instructions to be issued together
 - packaging them into **issue slots** or **issue packets** (determined by pipeline resources)
   - the issue packet is a very long instruction word (**VLIW**)
 - [[Compiler]] detects and avoids hazards
   1. reordering instructions into **issue packets**
   2. **no dependencies** within a packet
   3. possibly some dependencies b/w packets
   4. padding with **nop** if necessary

## Static dual issue
![[Screen Shot 2022-08-17 at 13.02.26.png]]
- Two-issued packets
  1. 1 ALU/branch instruction
  2. 1 load/store instruction
  3. 64-bit aligned
- requiring fetching and decoding 64 bits of instructions
- requiring additional hardware for [[Hazard detection]]
- needing extra ports in the [[Register file]]
- needing a separate adder to calculate the effective address for data transfers
- without these extra resources would cause [[Structural hazard]]

![[Screen Shot 2022-08-17 at 13.15.09.png]]

## Loop unrolling
![[Screen Shot 2022-08-17 at 14.12.45.png]]

![[Screen Shot 2022-08-17 at 14.15.20.png]]
- replicating loop body to expose more parallelism
- reducing loop-control overhead
- using different registers per replication ([[Dynamic multiple issue#Register renaming]])
- avoiding loop-carried **anti-dependencies** (WAR, aka **name dependence**)