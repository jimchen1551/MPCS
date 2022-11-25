---
Created: [[2022-11-24]]
Aliases: k-NN
Types: Card
Tags: 
- 
---
# k-nearest neighbor
![[Screen Shot 2022-11-24 at 14.44.09.png|500]]
- a simple and direct solution to noisy data
- **diluting** the influence of a single instances
- $k$ cannot be too large when dataset is imbalanced (major class will dominate minor class in voting)
- modifying the [[Nearest neighbor]] to return the majority target level w/i the set of $k$ nearest neighbors to the query $q$
$$M_k(q)=\arg \max_{l\in levels(t)}\sum_{i=1}^k\delta(t_i, l)$$
, where 
1. $M_k(q)$ is the prediction of the model $M$ for the query $q$ given the paramenter of the model $k$
2. $levels(t)$ is the set of levels in the domain of the target feature, and $l$ is an element of this set
3. $i$ iterates over the instances $d_i$ in increasing distance from the query $q$
4. $t_i$ is the value of the **target feature** for instance $d_i$
5. $\delta(t_i, l)$ is the **Kronecker delta function** taking 2 parameters and returning 1 if they are equal and 0 otherwise

## Weighted k-nearest neighbor
![[Screen Shot 2022-11-24 at 14.50.39.png|500]]
- able to use all instances instead of $k$ (Shepard's method)
- here using **distance weighted** to deal with imbalanced dataset
$$M_k(q)=\arg \max_{l\in levels(t)}\sum_{i=1}^k\frac{1}{dist(q, d_i)^2}\times\delta(t_i, l)$$

## For continuous target features
for [[k-nearest neighbor|k-NN]] returning: 
$$M_k(q)=\frac{1}{k}\sum_{i=1}^kt_i$$
for weighted [[k-nearest neighbor|k-NN]] returning: 
$$M_k(q)=\frac{\sum_{i=1}^k\frac{1}{dist(q, d_i)^2}\times t_i}{\sum_{i=1}^k\frac{1}{dist(q, d_i)^2}}$$
