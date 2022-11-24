---
Created: [[2022-10-19]]
Aliases: 
Types: Note
Tags: 
- 
---
# Similarity-based learning
| Fundamental concepts  | Content                                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Feature space]]     |                                                                                                                                                                                         |
| [[Distance matric]]   | Manhattan distance<br>Euclidean distance<br>Minkowski distance<br>Mahalanobis distance<br>Cosine similarity<br>Russel-Rao similarity<br>Sokal-Michener similarity<br>Jaccard similarity |
| [[Feature selection]] |                                                                                                                                                                                         |

| Algorithms             | Comment |
| ---------------------- | ------- |
| [[Nearest neighbor]]   |         |
| [[k-nearest neighbor]] |         |

## Data normalization
If the ranges of different descriptive features differ significantly, [[Data Preparation#Normalization]] should be implemented. 


## For continuous target features
for [[k-nearest neighbor|k-NN]] returning: 
$$M_k(q)=\frac{1}{k}\sum_{i=1}^kt_i$$
for weighted [[k-nearest neighbor|k-NN]] returning: 
$$M_k(q)=\frac{\sum_{i=1}^k\frac{1}{dist(q, d_i)^2}\times t_i}{\sum_{i=1}^k\frac{1}{dist(q, d_i)^2}}$$
