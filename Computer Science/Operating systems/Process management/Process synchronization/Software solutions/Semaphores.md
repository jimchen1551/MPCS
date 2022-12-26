---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Semaphores
```C
wait(S){
	while(S<=0){
		/*busy wait*/
	}
	S--;
}
signal(S){
	S++;
}
```
- an integer variable that is accessed only through 2 standard atomic operations: `wait()` and `signal()`
- **counting semaphore**: ranging over an unrestricted domain
- **binary semaphore**: ranging only b/w 0 and 1