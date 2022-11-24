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

| Data handling            | Comment |
| ------------------------ | ------- |
| [[Analytics Base Table]] |         |
| [[Data Quality Report]]  |         |
| [[Data Quality Issues]]  | [[Missing values]]<br>[[Irregular cardinality]]<br>        |

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
>>providing an example scenario where the descriptive features are time-dependent but the target feature is not
>>used to determine the least expensive incentive that needs to be offered to a customer who is considering canceling a service


## Data Visualization
- to reduce the size of [[Analytics Base Table|ABT]] while two features are strongly related
### Both continuous features
![[Screen Shot 2022-10-11 at 16.19.57.png|400]]
- **scatter plot matrix** (SPLOM)
### Both categorical features
![[Screen Shot 2022-10-18 at 13.42.08.png|400]]
- **small multiples** (drawing the density of each level of feature)
![[Screen Shot 2022-10-18 at 13.43.28.png|400]]
- if the number of levels of one of the features is small, use **stacked bar plots** as an alternative
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
