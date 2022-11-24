---
Created: [[2022-11-24]]
Aliases: DQI
Types: Card
Tags: 
- 
---
# Data Quality Issues
- defined as anything unusual about the data in an [[Analytics Base Table|ABT]]
- due to
	1. **invalid data**: by errors in the process of generating an [[Analytics Base Table|ABT]]
	   solution: correct immediately and recreate the [[Data Quality Report|DQR]]
	2. **valid data**: arising for a range of domain-specific reasons
	   solution: not correcting or recording the issue in the **data quality plan** while affecting the training process
![[Screen Shot 2022-10-04 at 14.36.12.png|500]]

| Class                     | Content                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| [[Missing values]]        | MCAR<br>MAR<br>MNAR<br>Removal<br>Missing indicator feature<br>Complete case analysis<br>Imputation |
| [[Irregular cardinality]] | cardinality=1<br>categorical→continuous<br>1 category→n labels<br>high cardinality in categories    |


### Outliers
- instances with values far away from the central tendency

Classes: 
1. **invalid outliers**
	- inclusion of a sample through error (causes are misillaneous, e.g., ~~fat finger lol~~)
	- often refered to as noise in the data
2. **valid outliers**
	- correct values just far away from the rest of instances

Identification: 
1. examining the **minimum** and **maximum** values for each feature: 
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
