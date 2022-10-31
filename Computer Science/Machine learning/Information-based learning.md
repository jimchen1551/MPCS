---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Information-based learning
[[Information theory]]
## Decision trees
![[Screen Shot 2022-10-31 at 18.28.17.png]]
- consisting of a root node (or starting node), interior nodes, and leaf nodes (or terminating nodes) that are connected by branches
- Each non-leaf node in the tree specifies a test to be carried out on a descriptive feature. 
- The number of possible levels that a descriptive feature can take determines the number of downward branches from a non-leaf node. 
- Each of the leaf nodes specifies a predicted level of the target feature. 

- preferring the decision trees with fewer tests (shallower)
- putting the descriptive features that best discriminate b/w instances toward the top of tree to build a shallow tree (to do this we need a way to measure)

- used while
  1. instances describable by attribute value pairs
  2. target function is discrete valued
  3. disjunctive hypothesis may be required
  4. possibly noisy training data
- e.g., 
  1. equipment or medical diagnosis
  2. credit risk prediction
  3. modeling 
## Shannon's entropy model

## Information gain

## ID3 algorithm

## Alternative feature selection

## Impurity metrics

## Tree pruning

## Model ensembles

