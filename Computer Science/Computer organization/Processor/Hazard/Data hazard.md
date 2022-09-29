---
Created: [[2022-08-03]]
Aliases: 
Types: Card
Tags: 
- 
---
# Data hazard
- An instruction depends on the result of a previous instruction not done. 
- caused by backward dependencies
- Classifications:
  1. True-dependency (read after write, **RAW**)
  2. Anti-dependency (write after read, **WAR**)
  3. Output dependency (write after write, **WAW**)
- Solutions: 
  1. Compiler scheme: 
     - **inserting independent instructions** b/w the instructions with backward dependency
     - **inserting nop (on op) instructions**, each of which takes one clock cycle
  2. Hardware scheme
     - [[Hazard detection]]
     - [[Forwarding]]
     - [[Stalling]]
- e.g., load-use data hazard ([[Forwarding]] can't save, but [[Stalling]] can)
  ![[Screen Shot 2022-08-03 at 21.16.07.png]]
  An instruction tries to read a register following a **load** instruction that writes the same register. 
