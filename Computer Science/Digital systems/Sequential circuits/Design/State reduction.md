---
Created: [[2022-09-23]]
Aliases: 
Types: Card
Tags: 
- 
---
# State reduction
- implementing a sequential circuit with the fewest possible states
- the least number of flip-flops
- fewest states usually lead to more opportunities for don't care

## Methods
- identifying and combining states that have equivalent behavior
### Row matching method
![[Screen Shot 2022-09-23 at 12.03.33.png]]
![[Screen Shot 2022-09-23 at 12.03.59.png]]
- If such states transition to the same next state, they are equivalent
- combining into a single new renamed state
- repeating until no new states are combined
Advantage: straightforward to understand and easy to implement
Disadvantage: not allowing yield of the most reduced state table

### Implication chart method
![[Screen Shot 2022-09-23 at 12.05.45.png]]
![[Screen Shot 2022-09-23 at 12.06.16.png]]
![[Screen Shot 2022-09-23 at 12.07.02.png]]
![[Screen Shot 2022-09-23 at 12.07.45.png]]
- enumerating all possible combinations of states taken two at a time
- filling in the implication chart
- Detailed algorithm:
	1. Construct an implication chart, one square for each combination of states taken two at a time.
	2. Square labeled (Si, Sj). If outputs differ then the square gets "×". Otherwise, write down implied state pairs for all input combinations. 
	3. Advance through the chart top-to-bottom and left-to-right. If square (Si, Sj) contains the next state pair Sm, Sn and that pair labels a square already labeled " × ", then (Si, Sj) is labeled " × ".
	4. Continue executing Step 3 until no new squares are marked with " × ".
	5. For each remaining unmarked square (Si, Sj), then Si and Sj are equivalent.
