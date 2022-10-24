---
Created: [[2022-10-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Layered kernel
![[Screen Shot 2022-10-24 at 19.20.57.png|300]]
- **dividing the system** into separate, layered, and smaller components with specific and limited funtionality
- **simplifying** design, implementation, debugging, and system verification
- hard to appropriately define the funcitonality of each layer
- poor performance due to the ovehead of requiring a user program to traverse through multiple layers to obtain a [[System service]]

- the bottom layer (layer 0) is the hardware
- the highest layer (layer N) is the [[User interface]]
- the middle layer (layer M) is the [[Operating systems]]
	- consisting of [[Data structures]] and a set of functions that can invoked by higher-level layers
	- invoking operations on lower-level layers

- each layer hiding the existence of certain [[Data structures]], operations, and hardware from higher-level layers
- e.g., TCP/IP and web apps