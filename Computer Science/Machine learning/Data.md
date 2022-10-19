---
Created: [[2022-10-18]]
Aliases: 
Types: Note
Tags: 
- 
---
# Data
| Data type   | Explanation                              |
| ----------- | ---------------------------------------- |
| Numeric     | allowing all arithmetic operations       |
| Interval    | allowing ordering and subtraction        |
| Ordinal     | allowing ordering                        |
| Categorical | a finite set not allowing any operations |
| Binary      | a set of just 2 values                   |
| Textual     | free-form                                |

| Feature type | Explanation                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Aggregates   | defined over a group or period and<br> as the **count**, **sum**, **average**, **minimum**, or **maximum**<br> of the values within the group                     |
| Flags        | indicating the **presence** or **absence** of some characteristic within a dataset                                                                |
| Ratios       | capturing the **relationship** b/w 2 or more raw data values                                                                              |
| Mappings     | converting **continuous** features into **categorical** features <br>and reducing the number of unique values that a model <br>will have to deal with |

>**Data availability**
>1. The key objects in the company's data model and the data available regarding them. 
>2. The connections that exist b/w key objects in the data model. 
>3. The granularity of the data that the business has available. 
>4. The volume of data involved. 
>5. The time horizon for which data is available. 

>**Handling time**
>![[Screen Shot 2022-09-27 at 15.46.25.png|300]]
>![[Screen Shot 2022-09-27 at 16.11.43.png|500]]
>>**Propensity model**
>>inherently having a temporal element
>>1. Observation period: over which descriptive features are calculated
>>2. Outcome period: over which target features are calculated
>
>>**Next-best-offer model**
>>providing an example scenario where the descriptive features are time dependent but the target feature is not
>>used to determine the least expensive incentive that needs to be offered to a customer who is considering caceling a service

## Analytics Base Table
- aka **ABT**
- the basic structure in which we capture the historical datasets
- the columns are divided into **a set of descriptive features** (inputs) and **a single target feature** (outcome)
- each row contains a value for each descriptive feature and the target feature and represents an **instance** about which a prediction can be made

## Data Quality Report
![[Screen Shot 2022-10-04 at 13.44.27.png|500]]
![[Screen Shot 2022-10-04 at 13.47.57.png|500]]
- aka **DQR**
- most important tool of the data exploration process
- including **tabular reports** 
	- describing the characteristics of each feature in an ABT using standard statistical measures of **central tendency** (mean, mode, and median) and **variation** (standard deviation and percentiles)
	- accompanied by **data visualizations** that illustrate the distribution of the values in each feature in an ABT
- including a **hitogram** ~~for each continuous feature~~
	- if the cardinality < 10, using **bar plots** instead
- **continuous** features: 
	- minimum, 1st quartile, mean, median, 3rd quartile, maximum, and standard deviation, total number of instances, percentage of instances missing the feature, and the cardinality of each feature
	- The shapes of histograms relate to one of the [Probability distribution](Probability#Probability distribution)
- **categorical** features: 
	- using descriptive statistics
	- 2 most frequent levels for the feature (mode and 2nd mode), frequency of appearance, percentage of instances missing the feature, and the cardinaligy of the feature

## Data Quality Issues
- defined as anything unusual about the data in an ABT
- due to
	1. **invalid data**: by errors in the process of generating an ABT
	   solution: correct immediately and recreate the DQR)
	2. **valid data**: arising for a range of domain-specific reasons
	   solution: not correct or recording the issue in the **data quality plan** while affecting training process
![[Screen Shot 2022-10-04 at 14.36.12.png|500]]
### Missing values
- some instances may miss values for one or more features
- % Miss. column in the DQR
- causes are misillaneous

Classes: 
1. Missing completely at random (MCAR)
	The distribution of an example with a missing value for a certain attribute is **independent** of the observed data and the value which is missing.
2. Missing at random (MAR)
	The distribution of an example with a missing value for a certain attribute **depends on the observed data**, but **not depends on the value which is missing**.
3. Missing not at random (MNAR)
	The distribution of an example with a missing value for a certain attribute **depends on the value which is missing**.

Handling: 
1. General approach: 
   if % Miss. > 60%, **remove** the feature. 
2. Alternative approach: 
   deriving a new **missing indicator feature** (aka dummy variable) from them (e.g., 0=absense and 1=presence) and discarding the original feature
3. **Complete case analysis**: 
   aka listwise deletion
   deleting instances missing one or more feature values (usually only for target feature)
4. **Imputation**: 
   if % Miss. < 30% (reluctant threshold) or 50% (strongly not recommended threshold), **replacing** missing feature values with a plausible value based on the feature values present 
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

### Irregular cardinality
- unusual number of distinct values for a feature
- Card. column in the DQR

Identification and classes: 
1. **cardinality=1** (all the instances bearing the same value of this feature)
	- If not due to an ABT generation error, correct the error and regenerate the ABT. 
	- Else, though the feature is valid, it doesn't useful while building predictive model; so, **delete** it! 
2. **categorical** feature incorrectly labelled as **continuous** feature
	- If the cardinality of a continuous feature << the number of instances, $\Rightarrow$ investigate it!
3. **irregularly high cardinalitiy** of a **categorical** feature
	- Usually because of different labels of the same category, $\Rightarrow$ correct the error and regenerate the ABT. 
4. **high cardinality** of a **categorical** feature with **valid** data
	- learning algorithm might struggle with such high cardinality; so, note it in the **data quality plan**

### Outliers
- instances with values far away from the central tendency

Classes: 
1. **invalid outliers**
	- inclusion of a sample through error (causes are misillaneous, e.g., ~~fat finger lol~~)
	- often refered to as noise in the data
2. **valid outliers**
	- correct values just far away from the rest of instances

Identification: 
1. examining the **minimum** and **maximum** values ofor each feature: 
	- usually find out the invalid outliers
2. comparing the gaps b/w the **median, minimum, maximum, 1st quartile, 3rd quartile**
	- Maximum - 3rd quartile >> 3rd quartile - median, $\Rightarrow$ maximum is unusual and likely to be the outlier. 
	- 1st quartile - minimum >> median - 1st quartile, $\Rightarrow$ minimum is unusual and likely to be the outlier. 
	- usually find out the valid outliners, $\Rightarrow$ note it in the **data quality plan**
3. **Exponential** or **skewed** distribution in histogram

Handling: 
1. **Clamp transformation**: 
	- The upper and lower thresholds can be set manually based on domain knowledge or caluculated from data. 
	- Commonly,
      $lower=1^{st}\text{quartile}-1.5\times \text{inter-quartile range}$; $upper=3^{rd}\text{quartile}+1.5\times \text{inter-quartile range}$
      or 
      $lower=mean-2\times SD$; 
      $upper=mean+2\times SD$
   $$a_i=\begin{cases}lower&\quad\text{if }a_i<lower\\upper&\quad\text{if }a_i>upper\\a_i&\quad \text{otherwise}\end{cases}$$

## Data Visualization
- to reduce the size of ABT while two features are strongly related
### Both continuous features
![[Screen Shot 2022-10-11 at 16.19.57.png|400]]
- **scatter plot matrix** (SPLOM)
### Both categorical features
![[Screen Shot 2022-10-18 at 13.42.08.png|400]]
- **small multiples** (drawing the density of each level of feature)
![[Screen Shot 2022-10-18 at 13.43.28.png|400]]
- if the number of levels of one of the feature is small, use **stacked bar plots** as an alternative
### Cross-data-type features
![[Screen Shot 2022-10-18 at 13.55.36.png|400]]
- **small multiples** (drawing a density histogram of the values of the continuous feature for each level of the categorical feature)
- if the features are related, the shapes and/or the central tendencies of the histogram will be different.
![[Screen Shot 2022-10-18 at 13.56.15.png|400]]
- **box plots** (less detail than histogram but better suited when the categorical feature has many levels(>4))

## Data Preparation
### Covariance
$$cov(a, b)=\frac{\displaystyle \sum_{i=1}^n(a_i-\bar{a})\times(b_i-\bar{b})}{n-1}$$
$$\displaystyle \sum_{\{a, b, \dots, z\}}=
\begin{bmatrix}
var(a)&cov(a, b)&\dots&cov(a, z)\\
cov(b, a)&var(b)&\dots&cov(b, z)\\
\vdots&\vdots&\ddots&\vdots\\
cov(z, a)&cov(z, b)&\dots&var(z)
\end{bmatrix}$$
- sensitive to feature scales
### Correlation
$$corr(a, b)=\frac{cov(a, b)}{sd(a)\times sd(b)}$$
$$\text{correlation}_{\{a, b, \dots, z\}}=
\begin{bmatrix}
corr(a, a)&corr(a, b)&\dots&corr(a, z)\\
corr(b, a)&corr(b, b)&\dots&corr(b, z)\\
\vdots&\vdots&\ddots&\vdots\\
corr(z, a)&corr(z, b)&\dots&corr(z, z)
\end{bmatrix}$$
common mistake: 
- correlation does not necessarily imply causation
- ignoring 3rd important, but hidden, feature
### Normalization
#### Range normalization
$$a_i'=\frac{a_i-min(a)}{max(a)-min(a)}\times(high-low)+low$$
- high, low: the expected range
- sensitive to the presense of outliers
#### Standardization
$$a_i'=\frac{a_i-\bar{a}}{sd(a)}$$
### Binning
![[Screen Shot 2022-10-18 at 15.06.01.png|500]]
- converting a continuos feature into a categorical feature
- the number of bins are difficult to find
	- if too small, then lose info
	- if too large, then too few instance in a bin
#### Equal-width binning
- splitting the range of the feature values into b bins, each of size (Max-Min)/b
#### Equal-frequency binning
- sorting the continuous feature values into ascending order
- placing an equal number of instances into each bin
### Sampling
- too many available data and no need to use all
- having no access to the population
- ensuring the representation of the samples
#### Top sampling
- selecting the top s% of instances from a dataset
- causing a serious risk of introducing bias
#### Random sampling
- randomly selecting a proportion of s% of the instances from a large dataset
#### Stratified sampling
- ensuring that the relative frequencies of the levels of a specific stratification feature are maintained in the sampled dataset
1. instances in a dataset are divided into groups (strata), where each group contains only instances having a particular level for the stratification feature
2. s% of the instances in each statum are randomly selected
3. these selections are combined to give all overall sample of s% of the original dataset
#### Under-sampling

#### Over-sampling