---
Created: [[2022-11-24]]
Aliases: DQR
Types: Card
Tags: 
- 
---
# Data Quality Report
![[Screen Shot 2022-10-04 at 13.44.27.png|500]]
![[Screen Shot 2022-10-04 at 13.47.57.png|500]]
- a most important tool of the data exploration process
- including **tabular reports** 
	- describing the characteristics of each feature in an [[Analytics Base Table|ABT]] using standard statistical measures of **central tendency** (mean, mode, and median) and **variation** (standard deviation and percentiles)
	- accompanied by **data visualizations** that illustrate the distribution of the values in each feature in an [[Analytics Base Table|ABT]]
- including a **histogram** ~~for each continuous feature~~
	- if the cardinality < 10, use **bar plots** instead

## Continuous features
- minimum, 1st quartile, mean, median, 3rd quartile, maximum, and standard deviation, the total number of instances, the percentage of instances missing the feature, and the cardinality of each feature
- The shapes of histograms relate to one of the [Probability distribution](Probability#Probability distribution).

## Categorical features
- using descriptive statistics
- 2 most frequent levels for the feature (mode and 2nd mode), frequency of appearance, percentage of instances missing the feature, and the cardinality of the feature
