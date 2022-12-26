---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Peterson's solution
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
