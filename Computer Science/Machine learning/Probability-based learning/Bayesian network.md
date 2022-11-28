---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Bayesian network
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
