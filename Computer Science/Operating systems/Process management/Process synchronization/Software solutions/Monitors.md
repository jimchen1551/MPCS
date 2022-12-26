---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Monitors
![[Screen Shot 2022-12-26 at 14.39.04.png|500]]
```Pseudocode
monitor monitor_name
{
	/*shared variable declarations*/
	function P1(){
	}
	function P2(){
	}
	...
	function Pn(){
	}
	initialization(){
	}
}
```
- An **abstract data type** (ADT) encapsulates data with a set of functions to operate on that data that are independent of any specific implementation of the ADT. 
- A **monitor type** is an ADT that includes a set of programmer-defined operations provided with mutual exclusion within the monitor. It also declares the variables whose values define the state of an instance of that type, along with the bodies of functions that operate on those variables. 

- A function defined within a monitor can access only those variables declared locally within the monitor and its formal parameters. 
- Only the local functions can access a local variable of a monitor. 
- The monitor construct ensures that only one thread at a time is active within the monitor.
- Condition variables with 3 special operations: `wait`, `signal`, and `broadcast`
- No public variables allowed
![[Screen Shot 2022-12-26 at 14.39.30.png|500]]
