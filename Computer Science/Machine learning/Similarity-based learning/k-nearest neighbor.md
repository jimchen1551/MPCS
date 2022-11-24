---
Created: [[2022-11-24]]
Aliases: k-NN
Types: Card
Tags: 
- 
---
# k-nearest neighbor
$$M_k(q)=\arg \min_{l\in levels(t)}\sum_{i=1}^k\delta(t_i, l)$$
, where $M_k(q)$ is the prediction of the model $M$ for the query $q$ given the paramenter of the model $k$; 
$levels(t)$ is the set of levels in the domain of the target feature, and $l$ is an element of this set; 
$i$ iterates over the instances $d_i$ in increasing 
- a simple and direct solution to noisy data
- **diluting** the influence of a single instances
- modifying the [[Nearest neighbor]] to return the majority target level w/i the set of $k$ nearest neighbors to the query $q$