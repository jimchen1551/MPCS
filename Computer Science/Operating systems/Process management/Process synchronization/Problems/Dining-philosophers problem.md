---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Dining-philosophers problem
![[Screen Shot 2022-12-26 at 15.28.32.png|300]]
- Consider five philosophers who spend their lives thinking and eating.
- The philosophers share a circular table surrounded by five chairs, each belonging to one philosopher.
- In the center of the table is a bowl of rice, and the table is laid with five single chopsticks. 
- When a philosopher thinks, she does not interact with her colleagues.
- From time to time, a philosopher gets hungry and tries to pick up the two chopsticks closest to her. 
- A philosopher may pick up only one chopstick at a time.
- She cannot pick up a chopstick that is already in the hand of a neighbor.
- When a hungry philosopher has both her chopsticks at the same time, she eats without releasing the chopsticks.
- When she is finished eating, she puts down both chopsticks and starts thinking again.
```C
while (true){
	wait(chopstick[i]);
	wait(chopstick[(i+1)%5]);
	/*eat for a while*/
	signal(chopstick[i]);
	signal(chopstick[(i+1)%5]);
	/*think for a while*/
}
```
- to allocate several resources among several processes in a deadlock-free and starvation-free manner
## Solutions
1. [[Semaphores]]
   
2. [[Monitors]]