---
Created: [[2022-10-31]]
Aliases: 
Types: Card
Tags: 
- 
---
# Decision trees
![[Screen Shot 2022-10-31 at 18.45.33.png]]
- consisting of a root node (or starting node), interior nodes, and leaf nodes (or terminating nodes) that are connected by branches
- Each non-leaf node in the tree specifies a test to be carried out on a descriptive feature. 
- The number of possible levels that a descriptive feature can take determines the number of downward branches from a non-leaf node. 
- Each of the leaf nodes specifies a predicted level of the target feature. 
## How to build
- We prefer the decision trees with fewer tests (shallower)
- To build a shallow tree, we put the descriptive features that best discriminate b/w instances toward the top of tree 
- To determine how well a descriptive feature is, we need [[Shannon's entropy model]] because we keep reducing the uncertainty while splitting the nodes and making them more and more pure (concept of [[Information gain]])
## When to use
- used while
  1. instances describable by attribute value pairs
  2. target function is discrete valued
  3. disjunctive hypothesis may be required
  4. possibly noisy training data
- e.g., 
  1. equipment or medical diagnosis
  2. credit risk prediction
  3. modeling purchase preferences
## Analysis
$$T(n)=(n\times m\lg m)$$
