---
Created: [[2022-06-16]]
Modified: None
Types: Note
Tags: 
- 
---
# Machine learning
- an automatic process that extracts patterns from data (or past experiences)
- A computer program is said to learn from **experience** ***E*** with respect to some class of **tasks** ***T*** and **performance** measure ***P***, if its performance at tasks in *T*, as measured by  *P*, improves with *E*. 

| Category               | Method                                                                                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supervised learning    | automatically learning a model of the relationship <br>b/w a set of descriptive features and a target <br>feature from a set of historical examples |
| Unsupervised learning  | no target feature                                                                                                                                   |
| Reinforcement learning | learning a policy (a sequence of actions)<br>no supervised actions but delayed rewards<br>credit assignment problem                                 |

## Data
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
| Aggregates   | difined over a group or period and<br> as the **count**, **sum**, **average**, **minimum**, or **maximum**<br> of the values within the group                     |
| Flags        | indicating **presence** or **absence** of some characteristic <br>within a dataset                                                                |
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
>![[Screen Shot 2022-09-27 at 16.11.43.png|300]]
>>**Propensity model**
>>1. Observation period: over which descriptive features are calculated
>>2. Outcome period: over which target features are calculated
>
>>**Next-best-offer model**
>>**not done here**

### Analytics Base Table
- aka **ABT**
- the basic structure in which we capture the historical datasets
- the columns divided into **a set of descriptive features** (inputs) and **a single target feature** (outcome)
- each row contains a value for each descriptive feature and the target feature and represents an **instance** about which a prediction can be made

### Data Quality Report
### Data Quality Issues
#### Missing values
#### Irregular cardinality
#### Outliers
### Data preparation
#### Normalization
#### Binning
#### Sampling
## Information-based learning
### Decision trees
### Shannon's entropy model
### Information gain
### ID3 algorithm
## Similarity-based learning
### Feature space
### Distance metrics
### Nearest neighbor algorithm
## Probability-based learning
### Bayes' theorem
### Bayesian prediction
### Conditional independence and factorization
### Naive Bayes model
## Error-based learning
### Simple linear regression
### Measuring error
### Error surfaces
### Multivariable linear regression
## Evaluation

## Reference book
- Fundamentals of Machine Learning for Predictive Data Analytics by John D. Kelleher, Brian Mac Namee, and Aoife D'Arcy
- Hands-on Machine Learning with Scikit-Learn, Keras, and Tensorflow by Aurelien Geron
- Foundations of Machine Learning by Mehryar Mohri, Afshin Rostamizadeh, and Ameet Talwalkar

## NCTU
Homework: 40%
Midterm: 30%
Final: 30%

## NYMU
Homework: 40%
Project: 40%
Final report: 5%
Performance: 15%








