---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Hardware instructions
```C
bool test_and_set(bool* target){
	bool rv = *target;
	*target = true;
	return rv;
}

int compare_and_swap(int* value, int expected, int new_value){
	int temp = *value;
	if (*value==expected){
		*value = new_value;
	}
	return temp;
}

# Mutual exclusion with test and set
do{
	while (test_and_set(&lock)){
		/*do nothing*/
	}
	/*critical section*/
	lock = false;
	/*remainder section*/
}while (true);

# Mutual exclusion with compare and swap
while (true){
	while (compare_and_swap(&lock, 0, 1)!=0){
		/*do nothing*/
	}
	/*critical section*/
	lock = 0;
	/*remainder section*/
}
```
- allowing either to test and modify the content of a word or to swap the contents of 2 words **atomically** (as 1 uninterruptible unit)
