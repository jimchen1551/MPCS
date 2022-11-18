---
Created: [[2022-10-31]]
Aliases: 
Types: Card
Tags: 
- 
---
# Shannon's entropy model
$$H(t, D)=-\sum_iP(t=i)\lg P(t=i)$$
$t$ for target feature; $D$ for dataset
- measuring the uncertainty of a probability distribution (or the impurity, heterogeneity of a set)
- The higher $Probability$ an outcome has the lower $Entropy$ it implies. 
- If we have $M$ uniform outcomes in total, we need $\lceil\lg M\rceil$ bits ($\lceil\lg Pr\rceil$, also can be seen as the number of uncertainty) at least to encode each outcome. 
