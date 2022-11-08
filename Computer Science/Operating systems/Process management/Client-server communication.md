---
Created: [[2022-11-08]]
Aliases: 
Types: Note
Tags: 
- 
---
# Client-server communication
## Socket
![[Screen Shot 2022-11-08 at 11.54.56.png]]
- endpoint for communication
- concatenation of **IP address** and **port** 
- communication consists b/w a pair of sockets
- all ports below 1024 are **well kenow** for standard services
- 127.0.0.1 to refer **itself**
## Remote procedure call
![[Screen Shot 2022-11-08 at 12.03.05.png|500]]
- abstracting [[procedure call]] b/w processes on networked systems
- **Stubs**: client-side proxy for the actual procedure on the server
	- **Server-side stub**
	- **Client-side stub**: 
		- calling OS to send directly to the server
		- **marshalling** the parameters
		- locating the server
## Pipe