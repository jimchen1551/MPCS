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
e.g., $P(a, \neg b, \neg c, d)=P(\neg b|a, \neg c)\times P(a)\times P(\neg c|d)\times P(d)$

1. nodes: 
   representing each feature in a domain
2. edges: 
   encoding the influence and conditional independence relationships b/w nodes
3. conditional probability table (CPT) for each node: 
   listing the probability distribution of the feature conditioned on the other features  connected by edges

- using a **directed-acyclical-graph**-based representation to encode the structural relationships b/w subsets of features in a domain
- offering a useful compromise b/w model compactness and predictive accuracy

- more compact than full [[Joint probability distribution]]
- not assuming all features are conditional independent like the [[Naive Bayes model]]

## Markov blanket
![[Screen Shot 2022-11-28 at 14.55.50.png]]
- the set of nodes in a graph that makes a node independent of the rest of the graph