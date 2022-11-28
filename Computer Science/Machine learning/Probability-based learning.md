---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Probability-based learning
| Fundamental concepts               | Content                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [[Probability]]                    |                                                                                                                                 |
| [[Joint probability distribution]] | a prob. dist. over multiple features                                                                                            |
| [[Bayes' theorem]]                 | $P(A\text{ given }B)=\frac{P(B\text{ given }A)P(A)}{P(B)}$                                                                      |
| [[Bayesian prediction]]            | False positive paradox<br>Maximum a posteriori (**MAP**)<br>Maximum likelihood (**ML**)<br>Minimum description length (**MDL**) |
| [[Smoothing]]                      | zero probability problem<br>Laplace smoothing<br>$m$-estimate                                                                   |

| Algorithms            | Comment |
| --------------------- | ------- |
| [[Naive Bayes model]] |         |
| [[Bayesian network]]  |         |

## For continuous features
### [[Probability density function]]
![[Screen Shot 2022-11-28 at 12.35.01.png|600]]
![[Screen Shot 2022-11-28 at 12.35.57.png|600]]
![[Screen Shot 2022-11-28 at 13.57.57.png|600]]
- no closed form solution to calculate the parameters to fit a mixture of [[Normal distribution|Gaussian distribution]] to a set of feature values, as there is for the [[Normal distribution]]s and the [[Exponential distribution]]s
- **guided search** techniques, such as **gradient descent** algorithm, are used to fit

### [[Data Preparation#Binning]]
