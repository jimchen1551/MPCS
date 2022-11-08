---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Remote procedure call
![[Screen Shot 2022-11-08 at 12.03.05.png|500]]
- abstracting [[procedure call]] b/w processes on networked systems
- data representation handled via **external data** (XDR)
- **Stubs**: client-side proxy for the actual procedure on the server
	- **Client-side stub**: 
		- locating the server
		- **marshalling** the parameters
		- calling OS to send directly to the server
		- waiting for result-return from the server
	- **Server-side stub**: 
		- receiving a call from a client
		- **unpacking** the parameters
		- calling the corresponding procedure
		- returning results to the caller
