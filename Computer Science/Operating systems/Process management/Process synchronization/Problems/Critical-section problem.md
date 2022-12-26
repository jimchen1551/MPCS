---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Critical-section problem
```C
while (true){
	entry section
		critical section
	exit section
		remainder section
}
```
- consider a system consisting of $n$ [[process]]es $\{P_0, \dots,P_{n-1}\}$
- each [[process]] has
  1. **entry section**: requesting permision to enter its critical section
  2. **critical section**: on execution, no other [[process]] is allowed to execute its own critical section
  3. **exit section**: following critical section
  4. **remainder section**: the remaining code
## Solution properties
![[Screen Shot 2022-12-26 at 11.21.59.png|500]]
1. **mutual exclusion**: if [[process]] $P_i$ is executing in its critical section, then no other [[process]]es can be executing in their critical sections
2. **progress**: if no [[process]] is executing in its critical section and some [[process]]es wish to enter their critical sections, then only those [[process]]es that are not executing in their remainder sections can participate in deciding which will enter its critical section next, and this selection cannot be postponed indefinitely. 
3. **bounded waiting**: there exists a bound, or limit, on the number of times that other [[process]]es are allowed to enter their critical sections after a [[process]] has made a request to enter its critical section and before that request is granted. 
## Critical sections handling
1. **preemptive kernels**: allowing a [[process]] to be preempted while it is running in kernel mode
   - needing to be designed against race conditions
   - difficult to design for [[Symmetric multiprocessing|SMP]] system, since it is possible for 2 kernel-mode [[process]]es to run simultaneously on different [[Processor|CPU]] cores
   - more responsive, since there is less risk that a kernel-mode [[process]] will run for an arbitrarily long period before relinquishing the processor to waiting processes
   - more suitable for [[Real-time embedded system]], as it will allow a real-time [[process]] to preempt a [[process]] currently running in the kernel
2. **nonpreemptive kernels**: not allowing a [[process]] running in kernel mode to be preempted; the [[process]] will run until it exits kernel mode, blocks, or voluntarily yields control of the [[Processor|CPU]]
   - free from race conditions
