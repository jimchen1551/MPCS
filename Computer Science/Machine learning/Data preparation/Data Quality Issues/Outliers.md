---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Outliers
- instances with values far away from the central tendency

## Classes
1. **invalid outliers**
	- inclusion of a sample through error (causes are misillaneous, e.g., ~~fat finger lol~~)
	- often refered to as noise in the data
2. **valid outliers**
	- correct values just far away from the rest of instances

## Identification
1. examining the **minimum** and **maximum** values for each feature: 
	- usually find out the invalid outliers
2. comparing the gaps b/w the **median, minimum, maximum, 1st quartile, 3rd quartile**
	- Maximum - 3rd quartile >> 3rd quartile - median, $\Rightarrow$ maximum is unusual and likely to be the outlier. 
	- 1st quartile - minimum >> median - 1st quartile, $\Rightarrow$ minimum is unusual and likely to be the outlier. 
	- usually find out the valid outliners, $\Rightarrow$ note it in the **data quality plan**
3. **Exponential** or **skewed** distribution in histogram

## Handling
**Clamp transformation**: 
- The upper and lower thresholds can be set manually based on domain knowledge or caluculated from data. 
- Commonly,
  $lower=1^{st}\text{quartile}-1.5\times \text{inter-quartile range}$; $upper=3^{rd}\text{quartile}+1.5\times \text{inter-quartile range}$
  or 
  $lower=mean-2\times SD$; 
  $upper=mean+2\times SD$
$$a_i=\begin{cases}lower&\quad\text{if }a_i<lower\\upper&\quad\text{if }a_i>upper\\a_i&\quad \text{otherwise}\end{cases}$$
