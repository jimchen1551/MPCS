---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Readers-writers problem
```C
semaphore rw_mutex = 1;
semaphore mutex = 1;
int read_count = 0;

# writer
while (true){
	wait(rw_mutex);
	/*writing is performed*/
	signal(rw_mutex);
}
# reader
while (true){
	wait(mutex);
	read_count++;
	if (read_count==1){
		wait(rw_mutex);
	}
	signal(mutex);
	/*reading is performed*/
	wait(mutex);
	read_count--;
	if (read_count==0){
	signa}
}
```
- a dataset is shared among several concurrent [[process]]es
- some of these want to read, and others want to write
- to prevent race conditions, we require that the writers have exclusive access to the shared database while writing
- 