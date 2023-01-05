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

| Data handling            | Comment                                                                     |
| ------------------------ | --------------------------------------------------------------------------- |
| [[Analytics Base Table]] | the basic structure of the dataset<br>Descriptive feature<br>Target feature |
| [[Data Quality Report]]  | Tabular reports<br>Histograms                                               |
| [[Data Quality Issues]]  | [[Missing values]]<br>[[Irregular cardinality]]<br>[[Outliers]]             |
| [[Data Visualization]]   | Scatter plot matrix<br>Small multiples<br>Box plots                         |
| [[Data Preparation]]     | Covariance<br>Correlation<br>Normalization<br>Binning<br>Sampling           |

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



