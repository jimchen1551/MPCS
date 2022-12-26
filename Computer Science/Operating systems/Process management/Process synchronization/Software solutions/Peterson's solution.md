---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Peterson's solution
![[Screen Shot 2022-12-26 at 12.17.13.png]]
```C
while (true){
	flag[i] = true;
	turn = j;
	while (flag[j]&&turn==j){
		/*do nothing*/
	}
	/*critical section*/
	flag[i] = false;
	/*remainder section*/
}
```
- restricted to 2 [[process]]es that alternate execution b/w their critical sections and remainder sections
- requiring the 2 [[process]]es to share 2 data items
  1. `int turn`
  2. `bool flag[2]`
- not guaranteed to work on modern computer architectures
## Peterson's lock
```C++
class CriticalSection_PetersonLock
{
	int victim;
	bool flag[2];
public:
	void lock()
	{
		int i = ThreadID.get();
		int j = 1-i;
		flag[i] = true;
		victim = i;
		while (flag[j]&&victim==i);
	}
	void unlock()
	{
		int i = ThreadID.get();
		flag[i] = false;
	}
};
```
