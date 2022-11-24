---
Created: [[2022-11-24]]
Aliases: 
Types: Note
Tags: 
- 
---
## Data Preparation
- [[Covariance]]
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
