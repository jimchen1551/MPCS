---
Created: [[2022-11-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bayes' theorem
$$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$
$$\displaystyle P(A_i|B)=\frac{P(B|A_i)P(A_i)}{\Sigma_{j=1}^nP(B|A_j)P(A_j)}=\eta\cdot P(B|A_i)\cdot P(A_i)$$
$$\eta=\frac{1}{P(B)}=\frac{1}{\Sigma_{j=1}^nP(B|A_j)P(A_j)}$$
, where $\eta$ is normalization constant
- the probability that an event has happened given a set of evidence for it is equal to the probability of the evidence being caused by the event multiplied by the probability of the event itself

## Generalized Bayes' theorem
$$P(t=l|q[1],\dots, q[m])=\frac{P(q[1],\dots, q[m]|t=l)P(t=l)}{P(q[1],\dots, q[m])}$$
, where $t$ for target feature and $q$ for a set of descriptive features from a query instance

Prior probability: 
$$P(t=l)$$
Joint probability: 
$$P(q[1],\dots, q[m])=P(q[1])P(q[2]|q[1])\dots P(q[m]|q[m-1]\dots q[1])$$
Conditional probability: 
$$P(q[1],\dots, q[m]|t=l)=P(q[1]|t=l)\dots P(q[m]|q[m-1]\dots q[1],t=l)$$
Posterior probability:
$$P(t=l|q[1],\dots, q[m])$$