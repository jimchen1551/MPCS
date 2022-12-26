---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Producer-consumer problem
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
![[Screen Shot 2022-12-26 at 10.44.27.png|500]]
- if we allowed both [[process]]es to manipulate the variable `count` concurrently, the incorrect state (race condition) might occur due to different cores dealing with `count++` and `count--`. 