---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Distance matric
- measuring the distance b/w 2 instances in a [[Feature space]]
Four criteria: 
1. Non-negativity: $metric(a, b)\geq 0$
2. Identity: $metric(a, b)=0\Leftrightarrow a=b$
3. Symmetry: $metric(a, b)=metric(b, a)$
4. Triangular inequality: $metric(a, b)\leq metric(a, c)+metric(b, c)$

## Manhattan distance
$$Manhattan(a, b)=\sum_{i=1}^m abs(a[i]-b[i])$$
## Euclidean distance
$$Euclidean(a, b)=\sqrt{\sum_{i=1}^m(a[i]-b[i])^2}$$
## Minkowski distance
$$Minkowski(a, b)=(\sum_{i=1}^m abs(a[i]-b[i])^p)^\frac{1}{p}$$
## Mahalanobis distance
$$d(a, b)=\sqrt{(a-b)^T\Sigma^{-1}(a-b)}$$
, where $\Sigma$ is the sample [[Data Preparation#Covariance]] matrix
- similar to [[#Euclidean distance]], also squares the difference of the features
- but rescale the difference so that all the features have **unit variance** and the effect of **covariance is removed**
## Cosine similarity
$$$$