---
Created: [[2022-10-31]]
Aliases: Iterative Dichotomizer 3
Types: Card
Tags: 
- 
---
# ID3 algorithm
- attempting to create the shallowest [[Decision tree]] that is consistent with the data given

## Pseudocode
```Pseudocode
if all the instances in D have the same target level C
	return a decision tree consisting of a leaf node with label C
else if d is empty
	return a decision tree consisting of a leaf node with the label of the majority target level in D
else if D is empty
	return a decision tree consisting of a leaf node with the label of the majority target level of the immediate parent node
else
	d[best]←arg max IG(d, D)
	make a new node, Node_d[best], and labv
```
d: a set of descriptive features
D: a set of training instances