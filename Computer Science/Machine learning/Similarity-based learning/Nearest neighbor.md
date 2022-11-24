---
Created: [[2022-11-24]]
Aliases: NN
Types: Card
Tags: 
- 
---
# Nearest neighbor
- similar things belong to the same class
- considered lazy learners
	- not really constructing a classification model
	- to classify a new data point x
	  1. identifying k nearest neighbors to x
	  2. assigning x to the class by the votes of the k neighbors

## Pseudocode
```Pseudocode
NEAREST-NEIGHBOR
Require a set of training instances

Require a query instance

Iterate accross the instances in memory to find the nearest neighbor--this is the instance with the shortest distance across the feature space to the query instance

Make a prediction for the query instance that is n
```