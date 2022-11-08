---
Created: [[2022-11-08]]
Aliases: 
Types: 
Tags: 
- 
---
# Direct communication
## Symmetry
- processes must name each other explicitly
- `send(P, message)`: send a message to P
- `receive(Q, message)`: receive a message from Q
- the link established automatically
- the link associated with exactly one pair of communicating processes
- uni-directional or bi-directional

## Asymmetry
- only the sender names the recipient
- the recipient is not required to name the sender
- `send(P, message)`: send a message to process P
- `receive(id, message)`: receive a message from Q
