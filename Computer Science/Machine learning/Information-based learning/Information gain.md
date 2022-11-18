---
Created: [[2022-10-31]]
Aliases: 
Types: Card
Tags: 
- 
---
# Information gain
![[Screen Shot 2022-10-31 at 19.25.51.png]]
$$IG(d, D)=H(t, D)-rem(d, D)$$
$$rem(d, D)=\sum_{l\in levels(d)}\frac{|D_{d=l}|}{|D|}\cdot H(t, D_{d=l})$$
- a measure of the **reduction in the overall entropy** of a set of instances that is achieved by testing on a descriptive feature. 

1. Compute the entropy of the original dataset with respect to target feature. 
   
2. For each descriptive feature, create the sets that result by partitioning the instances in the dataset using their feature values, and then sum the entropy scores of each of these sets. 
   - [[Shannon's entropy model]] should be rewritten as $H(t, D)=\sum_{l\in levels(t)}(P(t=l)\lg(P(t=l)))$, where t is the target feature. 
   - The entropy remaining also should be defined as $rem(d, D)=\sum_{l\in levels(d)}\frac{|D_{d=l}|}{|D|}H(t, D_{d=l})$, where d is the descriptive feature to partition the dataset D; $|D|$ is the size of the (partitioned) dataset
3. Subtract the remaining entropy value from the original entropy value to give the information gain. 
   - $IG(d, D)=H(t, D)-rem(d, D)$

- e.g., 
  $$IG(WORDS, D)=H(Class, D)-rem(WORD, D)$$
  $$=[-((\frac{3}{6}\lg\frac{3}{6})+(\frac{3}{6}\lg\frac{3}{6}))]-[\frac{3}{6}(-((\frac{3}{3}\lg\frac{3}{3})+(\frac{0}{3}\lg\frac{0}{3})))+\frac{3}{6}(-((\frac{0}{3}\lg\frac{0}{3})+(\frac{3}{3}\lg\frac{3}{3})))]$$
  $$=1\text{ bit}-0\text{ bit}=1\text{ bit}$$
  
## Drawback
1. preferring features with many values
2. selecting meaningless features for partition and creating too many tiny subsets