---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Semaphores
```C
wait(semaphore* S){
	S->value--;
	if (S->value<0){
		add this process to S->list;
		sleep();
	}
}

signal(semaphore* S){
	S->value++;
	if (S->value<=0){
		remove a process P from S->list;
		wakeup(P);
	}
}

typedef struct{
	int value;
	struct process* list;
}semaphore;
```
- an integer variable that is accessed only through 2 standard atomic operations: `wait()` and `signal()`
- **counting semaphore**: ranging over an unrestricted domain
- **binary semaphore**: ranging only b/w 0 and 1, similar to [[Mutex locks]]