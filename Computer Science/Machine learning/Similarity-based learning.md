---
Created: [[2022-10-19]]
Aliases: 
Types: Note
Tags: 
- 
---
# Similarity-based learning
| Fundamental concepts  | Comment                                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Feature space]]     |                                                                                                                                                                                         |
| [[Distance matric]]   | Manhattan distance<br>Euclidean distance<br>Minkowski distance<br>Mahalanobis distance<br>Cosine similarity<br>Russel-Rao similarity<br>Sokal-Michener similarity<br>Jaccard similarity |
| [[Feature selection]] |                                                                                                                                                                                         |

| Algorithms             | Comment |
| ---------------------- | ------- |
| [[Nearest neighbor]]   |         |
| [[k-nearest neighbor]] |         |

## Data normalization
If the ranges of different descriptive features differ greatly, [[Data Preparation#Normalization]] should be implemented. 

## For continuous target features
for [[k]]returning the average value in the neighborhood: 
$$M_k(q)=\frac{1}{k}\sum_{i=1}^kt_i$$