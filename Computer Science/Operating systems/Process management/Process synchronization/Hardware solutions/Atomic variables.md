---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Atomic variables
```C
void increment(atomic_int* v)
{
	int temp;
	do{
		temp = *v;
	}while (temp!=compare_and_swap(v, temp, temp+1));
}
```
- providing atomic operations on basic data types (e.g., int and bool)
- used to ensure mutual exclusion in situations where there may be a data race on a single variable while it is being updated, as when a counter is incremented
- providing atomic updates and not solving entire race conditions