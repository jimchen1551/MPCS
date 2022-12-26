---
Created: [[2022-12-26]]
Aliases: 
Types: Note
Tags: 
- 
---
# Process synchronization
## Producer-consumer problem
```C
# producer
while (true) {
	/*produce an item in next_produced*/
	while (count==BUFFER_SIZE){
		/*do nothing*/
	}
	buffer[in] = next_produced;
	in = (in+1)%BUFFER_SIZE;
	count++;
}

# consumer
while (true){
	while (count==0){
		/*do nothing*/
	}
	next_consumed = buffer[out];
	out = (out+1)%BUFFER_SIZE;
	count--;
}
```
- if we allowed both [[process]]es to manipulate the variable `count` concurrently, the incorrect state (race condition) might occur due to separate registers to deal with `count++` and `count--`. 
## Critical-section problem
## Peterson's solution
## Memory barriers
## Hardware instructions
## Atomic variables
## Mutex locks
## Semaphores
## Monitors
## Liveness
## Evaluation
## Bounded-buffer problem
## Readers-writers problem
## Dining-philosophers problem
## Alternative approaches
