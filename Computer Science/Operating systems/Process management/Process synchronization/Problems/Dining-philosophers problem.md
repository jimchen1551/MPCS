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
   to remedy the [[deadlock]] problem,
   1. Allow at most four philosophers to be sitting simultaneously at the table.
   2. Allow a philosopher to pick up her chopsticks only if both chopsticks are available. 
   3. Use an asymmetric solution. 
2. [[Monitors]]
```C
monitor DiningPhilosophers
{
	enum{THINKING, HUNGRY, EATING}state[5];
	condition self[5];
	void pickup(int i){
		state[i] = HUNGRY;
		test(i);
		if (state[i]!=EATING){
			self[i].wait();
		}
	}
	void putdown(int i){
		state[i] = THINKING;
		test((i+4)%5);
		test((i+1)%5);
	}
	void test(int i){
		if ((state[(i+4)%5]!=EATING)&&
			(state[(i+1)%5]!=EATING)&&
			(state[i]==HUNGRY)){
			state[i] = EATING;
			self[i].signal();
		}
	}
	initialization(){
		for (int i=0; i<5; i++){
			state[i] = THINKING;
		}
	}
}
```
