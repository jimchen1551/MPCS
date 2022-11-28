---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Missing values
- some instances may miss values for one or more features
- % Miss. column in the [[Data Quality Report|DQR]]
- causes are miscellaneous

## Classes
1. Missing completely at random (MCAR)
	The distribution of an example with a missing value for a certain attribute is **independent** of the observed data and the missing value.
2. Missing at random (MAR)
	The distribution of an example with a missing value for a certain attribute **depends on the observed data** but **not depends on the value which is missing**.
3. Missing not at random (MNAR)
	The distribution of an example with a missing value for a certain attribute **depends on the value which is missing**.

## Handling
1. General approach: 
   if % Miss. > 60%, **remove** the feature. 
2. Alternative approach: 
   deriving a new **missing indicator feature** (aka dummy variable) from them (e.g., 0=absense and 1=presence) and discarding the original feature
3. **Complete case analysis**: 
   aka listwise deletion
   deleting instances missing one or more feature values (usually only for target feature)
4. **Imputation**: 
   if % Miss. > 30% (reluctant threshold) or 50% (strongly not recommended threshold), **replacing** missing feature values with a plausible value based on the feature values present 
	- negatively biasing the relationships b/w a descriptive feature and a target feature $\because$ changing the underlying data and causing the variation with a feature to be underestimated
	- **Single imputation**: commonly replaced by a measure of the central tendency, e.g., 
		continuous: median or mean; 
		categorical:  most common mode
	- **Multiple imputation**: imputing the missing data several times to produce several different complete-data models and combining these models into and overall one, e.g., MCMC
	- Methods: 
	  mean value imputation, 
	  most frequent value imputation, 
	  **PCA** (principal component analysis, by linear combination of PC), 
	  **MICE** (multiple imputation by chained equations), 
	  **kNN** (k-neariest neighbors, by mean of neighbors), 
	  **EM** (expectation-maximization), 
	  **MissForest** (generating a forest of decision tree and using trees to predict), 
	  **GAIN** (generative adversarial imputation networks)

>**Markov chain Monte Carlo** (MCMC): 
>1. initializing parameter values
>2. making regression of variable with missing values on other variables
>3. predicting missing values and adding some random errors to mitigate bias in covariance
>4. recalculating means, covariance matrix from complete-data table
>5. repeating 2~4 times until converge
