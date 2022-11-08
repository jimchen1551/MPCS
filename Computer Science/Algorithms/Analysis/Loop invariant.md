---
Created: [[2022-11-08]]
Aliases: 
Types: Card
Tags: 
- 
---
# Loop invariant
- a property of a program loop that is true before (and after) each iteration
- a logical assertion, sometimes checked within the code by an assertion call
- used to understand why an algorithm is correct
1. **Initialization**: It is true prior to the first iteration of the loop.
2. **Maintenance**: If it is true before an iteration of the loop, it remains true before the next iteration.
3. **Termination**: When the loop terminates, the invariant gives us a helpful property that helps show that the algorithm is correct.
## Floyd-Hoare logic
[Wiki explained](https://en.wikipedia.org/wiki/Hoare_logic)