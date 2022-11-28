---
Created: [[2022-11-28]]
Aliases: 
Types: Card
Tags: 
- 
---
# Smoothing
- taking some of the probability mass from the assignments with probability **greater than average** and spreading it across the probabilities **below average** or even **equal to zero** (zero probability problem)
- In general, it doesn't make sense to smooth the prior probabilities for the different target feature levels. 

## Laplace smoothing
$$P(f=l|t)=\frac{count(f=l|t)+k}{count(f|t)+k\times |Domain(f)|}$$
, where $|Domain(f)|$ is the number of levels in the domain of the feature
, and $k$ is a predetermined parameter
- larger $k$ → more smoothing 
  (taking more probability mass from the larger to the smaller)
- typically, $k=1, 2, 3$

## m-estimate
