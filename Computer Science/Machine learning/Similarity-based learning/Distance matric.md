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
$$Mahalanobis(a, b)=\sqrt{(a-b)^T\Sigma^{-1}(a-b)}$$
, where $\Sigma$ is the sample [[Data Preparation#Covariance]] matrix
- similar to [[#Euclidean distance]], also squares the difference of the features
- but rescale the difference so that all the features have **unit variance** and the effect of **covariance is removed**
- able to be undertstood as defining an **orthogonal coordinate system** with
  1. an origin at the instance we are calculating the distance from
  2. a primary axis aligned with the direction of the greatest spread in the dataset
  3. the units of all the axes scaled so that the dataset has unit variance along each axis
![[Screen Shot 2022-11-24 at 15.33.17.png]]
Origin: (a) (50, 50), (b) (63, 71), (c) (42, 35)
## Cosine similarity
$$Sim_{\cos}(a, b)=\frac{a\cdot b}{|a|\cdot|b|}$$
## For symbolic features
$$d_1, d_2\text{ is symbolic features}$$
$$CP(d_1, d_2)=n((d_1==T)and(d_2==T))$$
$$CA(d_1, d_2)=n((d_1==F)and(d_2==F))$$
$$PA(d_1, d_2)=n((d_1==T)and(d_2==F))$$
$$AP(d_1, d_2)=n((d_1==F)and(d_2==T))$$
- based on Boolean features
- CP for co-presence
- CA for co-absence
- PA for presence-absence
- AP for absence-presence
### Russel-Rao similarity
$$Sim_{RR}=\frac{CP(d_1, d_2)}{|d_1|}$$
### Sokal-Michener similarity
$$Sim_{SM}=\frac{CP(d_1, d_2)+CA(d_1, d_2)}{|d_1|}$$
### Jaccard similarity
$$Sim_{J}=\frac{CP(d_1, d_2)}{CP(d_1, d_2)+PA(d_1, d_2)+AP(d_1, d_2)}$$
