---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Probability-based learning
| Fundamental concepts                 | Content                                                                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [[Probability]]                      |                                                                                                                                 |
| [[Probability mass function]]        | **PMF**, $p_X(x)=P(X=x)$<br>for discrete random variables                                                                       |
| [[Probability density function]]     | **PDF**, $f_X(x)=F'_X(x)$<br>for continuous random variables                                                                    |
| [[Cumulative distribution function]] | **CDF**, $F_X(x)=P(X\leq x)$                                                                                                    |
| [[Joint probability distribution]]   | a prob. dist. over multiple features                                                                                            |
| [[Bayes' theorem]]                   | $P(A\text{ given }B)=\frac{P(B\text{ given }A)P(A)}{P(B)}$                                                                      |
| [[Bayesian prediction]]              | False positive paradox<br>Maximum a posteriori (**MAP**)<br>Maximum likelihood (**ML**)<br>Minimum description length (**MDL**) |

| Algorithms            | Comment |
| --------------------- | ------- |
| [[Naive Bayes model]] |         |
| [[Bayesian network]]  |         |

## Zero probability problem
- replacing zero with an infinitesimal number $\eta$ (quick but dirty fix)
- adding pseudocount ($m$-estimate or Laplace smoothing)