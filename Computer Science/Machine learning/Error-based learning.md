---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Error-based learning
| Fundamental concepts | Content |
| -------------------- | ------- |
| [[Error function]]   |         |
| [[Error surface]]    |         |
| [[Gradient descent]] |         |

| Algorithms                           | Comment |
| ------------------------------------ | ------- |
| [[Linear regression]]                |         |
| [[Multivariable linear regression]]  |         |
| [[Logistic regression]]              |         |
| [[Multinominal logistic regression]] |         |
| [[Support vector machine]]           |         |

## For categorical features
![[Screen Shot 2022-12-26 at 19.57.08.png|500]]
- one-hot encoding
- for target features, $\mathbf{M}_w(d)=\begin{cases}1\ \text{if }w\cdot d\geq0\\0\ otherwise\end{cases}$, and convert the prediction surface to the decision surface. 
- using the **logistic function** to solve
  1. [[gradient descent]] not work