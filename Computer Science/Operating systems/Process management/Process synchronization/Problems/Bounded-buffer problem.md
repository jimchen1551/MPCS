---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bounded-buffer problem
```C
int n;
semaphore mutex = 1;
semaphore empty = n;
semaphore full = 0;

# producer
while (true){
	/*produce an item in next_produced*/
	wait(empty);
	wait(mutex);
	/*add next_produced to the buffer*/
	signal(mutex);
	signal(full);
}
# consumer
while (true){
	wait(full);
	wait(mutex);
	/*remove an item from buffer to next_consumed*/
	signal(mutex);
	signal(empty);
	/*consume the item in next_consumed*/
}
```
- $n$ buffers, each can hold one item