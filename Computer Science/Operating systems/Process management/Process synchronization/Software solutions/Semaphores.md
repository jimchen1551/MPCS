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
