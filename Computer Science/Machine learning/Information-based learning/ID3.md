---
Created: [[2022-10-31]]
Aliases: Iterative Dichotomizer 3
Types: Card
Tags: 
- 
---
# ID3
- top-down induction of [[Decision tree]]
- attempting to create the shallowest [[Decision tree]] that is consistent with the data given
- building the tree in a recursive, depth-first manner, beginning at the root node and working down to the leaf nodes

## Pseudocode
```Pseudocode
ID3(d, D)
if all the instances in D have the same target level C
	return a decision tree consisting of a leaf node with label C
else if d is empty
	return a decision tree consisting of a leaf node with the label of the majority target level in D
else if D is empty
	return a decision tree consisting of a leaf node with the label of the majority target level of the immediate parent node
else
	d[best]←arg max IG(d, D)
	make a new node, Node_d[best], and label it with d[best]
partition D using d[best]
remove d[best] from d
for each partition D_i of D
	grow a branch from Node_d[best] to the decision tree created by rerunning ID3(d, D_i)
```
d: a set of descriptive features
D: a set of training instances

### Steps
1. beginning with choosing the best descriptive feature to the test using [[Information gain]]
2. adding a root node to the tree and labeled with the selected test feature
3. partitioning training dataset with the test feature
4. growing [[Decision tree]]s from each node with each partitioned dataset

### Time to stop
1. All instances in the sub-dataset have the same target value
2. No more descriptive features available for further partition
3. The sub-dataset is empty
