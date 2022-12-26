---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Error-based learning
| Fundamental concepts  | Content |
| --------------------- | ------- |
| [[Error function]]    |         |
| [[Error surface]]     |         |
| [[Gradient descent]]  |         |

| Algorithms                           | Comment |
| ------------------------------------ | ------- |
| [[Linear regression]]                |         |
| [[Multivariable linear regression]]  |         |
| [[Logistic regression]]              |         |
| [[Multinominal logistic regression]] |         |

## For categorical features
![[Screen Shot 2022-12-26 at 19.57.08.png|500]]
- one-hot encoding
- for target features, $\mathbf{M}_w(d)=\begin{cases}1\ \text{if }w\cdot d\geq0\\0\ otherwise\end{cases}$, and convert the prediction surface to the decision surface. 
- using the **[[logistic function]]** to solve
  1. [[gradient descent]] not working
  2. faraway point prediction problems

## For non-linear relationships
![[Screen Shot 2022-12-26 at 20.22.09.png|500]]
![[Screen Shot 2022-12-26 at 20.29.03.png|500]]
1. define $b$ basis functions ($\phi_k(d)$) and use them to transform data to capture non-linear relationships. 
2. define the model as a linear combination of the $b$ basis functions. 
   $\mathbf{M}_w(d_i)=\sum_{k=0}^bw_k\cdot\phi_k(d_i)$, where $d_i$ is a data entity described by $m$ descriptive features, and $\phi_k$ is a basis function. 
3. find $w_k$ by gradient descent