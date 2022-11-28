---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bayesian network
![[Screen Shot 2022-11-28 at 14.40.04.png]]
$$P(x_1, \dots, x_n)=\prod_{i=1}^nP(x_i|Parents(x_i))$$
$$P(x_i|x_1, \dots, x_n)=P(x_i|Parents(x_i))\prod_{j\in children(x_i)}P(x_j|Parents(x_j))$$
e.g., $P(a, \neg b, \neg c, d)=P(\neg b|a, \neg c)\times P(a)\times P(\neg c|d)\times P(d)$

1. nodes: 
   representing each feature in a domain
2. edges: 
   encoding the influence and conditional independence relationships b/w nodes
3. conditional probability table (CPT) for each node: 
   listing the probability distribution of the feature conditioned on the other features  connected by edges

- using a **directed-acyclical-graph**-based representation to encode the structural relationships b/w subsets of features in a domain
- offering a useful compromise b/w model compactness and predictive accuracy
- Computing a conditional probability for a node becomes more complex if the value of one or more of the parent nodes is unknown. → use **summing out** in [[Joint probability distribution]]
e.g., if C is unknown

- more compact than full [[Joint probability distribution]]
- not assuming all features are conditional independent like the [[Naive Bayes model]]

## Markov blanket
![[Screen Shot 2022-11-28 at 14.55.50.png]]
- the set of nodes in a graph that makes a node independent of the rest of the graph
- the gray nodes define the Markov blanket of the black node
- the black node is conditionally independent of the white nodes given the state of the gray nodes