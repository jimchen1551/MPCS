---
Created: [[2022-07-14]]
Aliases: 
Types: Card
Tags: 
- 
---
# Multilevel optimization
- The usage of a set of transformations under cost evaluation(e.g., circuit, timing, power, etc.)
## Factoring
$$AB+AC=A(B+C)$$
## Decomposition
$$A\Rightarrow AB+AB'$$
## Extraction
$$X\Rightarrow f(A, B, C, D)$$
## Substitution
$$A+B\Rightarrow X$$$$A'B'\Rightarrow X'$$
## Elimination
$$X\Rightarrow A+B$$
## Delay reduction
### Path delay
- the time it takes from input to output
### Critical path
- the path with the longest path delay
### Strategy
- Reduce the # of gates in series
1. [[#Elimination]] to reduce the [[#Path delay]] of [[#Critical path]]
2. Remove [[#Factoring]]
3. etc. 