---
Created: [[2022-11-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Joint probability distribution
$$\mathbf{P}(H,F, V, M)=\begin{bmatrix}
P(h, f, v, m)&P(\neg h, f, v, m)\\
P(h, f, v, \neg m)&P(\neg h, f, v, \neg m)\\
P(h, f, \neg v, m)&P(\neg h, f, \neg v, m)\\
P(h, f, \neg v, \neg m)&P(\neg h, f, \neg v, \neg m)\\
P(h, \neg f, v, m)&P(\neg h, \neg f, v, m)\\
P(h, \neg f, v, \neg m)&P(\neg h, \neg f, v, \neg m)\\
P(h, \neg f, \neg v, m)&P(\neg h, \neg f, \neg v, m)\\
P(h, \neg f, \neg v, \neg m)&P(\neg h, \neg f, \neg v, \neg m)\\
\end{bmatrix}$$
- a probability distribution over more than one feature assignment
- a multi-dimensional matrix where each cell lists the probability for one of the events in the sample space defined by the combination of feature values
- the dimension of the matrix depends on the number of features and the number of values in the domains of the features
- the sum of all elements is 1

## Full joint probability distribution
- a joint probability distribution over all the features in a domain

## Marginalization
$$P(h)=\sum_{P\in\mathbf{P}(H,F, V, M)}P(H=h)$$
- aka **summing out**
