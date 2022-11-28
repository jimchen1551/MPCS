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
1. Select which probability distribution we believe will best model the distribution of the values of the feature. 
   - create a **density histogram** of the feature’s values and **compare the shape** of this histogram to the shapes of the standard distributions
2. Fit the parameters of the selected distribution to the feature values in the dataset.
   - fit the parameters, μ and σ (λ), of the [[normal distribution]] ([[exponential distribution]]) to a dataset by using the sample mean and standard deviation of the feature values in a dataset as estimates of μ and σ respectively
   - use **guided search** techniques, such as **gradient descent** algorithm, to fit other distributions (due to no closed form solution)

![[Screen Shot 2022-11-28 at 14.08.32.png|600]]
- [[Probability density function|PDF]] is an abstraction over a density histogram; therefor, to represent probabilities we need to calculate **area under the curve of [[Probability density function|PDF]]**
- In a [[Naive Bayes model]], we only need to calculate the relative likelihood of a continuous feature taking a value given different levels of a target feature
### [[Data Preparation#Binning]]
- binning to convert a continuous feature into a categorical feature
- used if it's hardd to tell the distribution from the shape of histogram
  or if it's a relatively small dataset