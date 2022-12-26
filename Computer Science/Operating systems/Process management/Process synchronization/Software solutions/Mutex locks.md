---
Created: [[2022-12-26]]
Aliases: spinlock
Types: Card
Tags: 
- 
---
# Mutex locks
```C
while (true){
	acquire lock
		critical section
	release lock
		remainder section
}

acquire(){
	while (!available){
		/*busy wait*/
	}
	available = false;
}

release(){
	available = true;
}
```
- protecting critical sections and preventing race conditions
- `acquire()` acquires the lock
- `release()` releases the lock 
- Advantages: no need to do [[Context switch]]
- Flaws: **busy waiting** blocks the other [[process]]es while unavailable
