---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Feature selection
- considered a **search problem**
  1. Search space: all possible feature subsets
  2. State: a legal feature subset
  3. Operator: feature subset generator
  4. Goal state: terminal condition

- the number of descriptive features in a dataset increases → the predictive power of an induced model decreases
- The **predictive power** of an induced model is based on one of the following: 
  1. Partitioning the [[Feature space]] into regions based on clusters of training instances with the same target value, and assigning a query located in a **region** the target value of the cluster that defines that region
  2. Assigning a query a target value interpolated from the target values of individual training instances that are **near** the query in the feature space

| Descp. feature | Explanation                              |
| -------------- | ---------------------------------------- |
| Predictive     | providing useful info                    |
| Interacting    | becoming informative with other features |
| Redundant      | having strong correlation with another   |
| Irrelevant     | not providing useful info                |

## Sampling density
$$density=k^{\frac{1}{m}}$$
, where $k$ is the **number of instances** inside the hypercube
, and $m$ is the **number of dimensions** of the feature space

- the **average density of training instances** across the [[Feature space]]
- if too low, large regions of the feature space don't contain any training instances
   → not making sense to associate such region with any cluster of training instances nor to look for training instances that are nearby

## Curse of dimensionality
![[Screen Shot 2022-11-25 at 10.24.21.png|500]]
- the dimensionality of [[Feature space]] increases, the [[#Sampling density]] decreases
- the trade-off b/w the number of descriptive features and the [[#Sampling density]] is known a the **curse of dimensionality**

## Rank and prune