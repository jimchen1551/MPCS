---
Created: [[2022-11-24]]
Aliases: NN
Types: Card
Tags: 
- 
---
# Nearest neighbor
![[Screen Shot 2022-11-24 at 14.43.30.png|500]]
- similar things belong to the same class
- considered lazy learners
- instances mapped to points on $R^n$

## Pseudocode
```Pseudocode
NEAREST-NEIGHBOR

Require a set of training instances

Require a query instance

Iterate accross the instances in memory to find the nearest neighbor -- this is the instance with the shortest distance across the feature space to the query instance

Make a prediction for the query instance that is equal to the value of the target feature of the nearest neighbor
```
- not really constructing a classification model
- to classify a new data point x
	1. identifying k nearest neighbors to x
	2. assigning x to the class by the votes of the k neighbors
	   if k is not given, k=1

## When to use
- relatively small feature set
- relatively large training dataset

## Advantages
- fast training
- dealing with complex target functions
- accommodating new instances easily
- no info loss

## Disadvantages
- slow in prediction (query)
- easily fooled by irrevelant features
- no predictive models actually contructed
- sensitive to noisy data
