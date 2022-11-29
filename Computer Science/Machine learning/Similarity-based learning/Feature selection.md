---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Feature selection
![[Screen Shot 2022-11-25 at 10.47.11.png]]
- considered a **greedy local search problem**
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
- the trade-off b/w the number of descriptive features and the [[#Sampling density]] is known as the **curse of dimensionality**

## Rank and prune
- **filters**: measurements of the predictiveness of each feature
  e.g., [[Information gain]]
1. filtering irrelevant features before learning
   (independent of learning algorithms)
2. pruning outside the top $X\%$ of the features

## Wrapper
- evaluating a feature subset in terms of the potential performance of the models
- performing an evaluation experiment for each candidate feature subset (embedded w/i the learning algorithms)
- more computationally expensive than filters

## Forward sequential selection
- used when we expect lots of irrelevant features in the dataset
- faster
1. starting in a state with no features
2. using any approach described above and moving the search process to a new feature subset
3. teminating when no accessible feature subset is better than the current subset

## Backward sequential selection
- taking advantage that allowing the inclusion of sets of interacting featrues
- more accurate
1. starting with a feature subset including all the possible features in a dataset
2. using any approach described above and removing an extra feature in a move
3. terminating when no accessible feature subset is better than the current subset
