---
Created: [[2022-11-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Irregular cardinality
- an unusual number of distinct values for a feature
- Card. column in the [[Data Quality Report|DQR]]

## Identification and classes
1. **cardinality=1** (all the instances bearing the same value of this feature)
	- If not due to an [[Analytics Base Table|ABT]] generation error, correct the error and regenerate the [[Analytics Base Table|ABT]]. 
	- Else, though the feature is valid, it doesn't help while building a predictive model, so **delete** it! 
2. **categorical** feature incorrectly labeled as a **continuous** feature
	- If the cardinality of a continuous feature << the number of instances, $\Rightarrow$ investigate it!
3. **irregularly high cardinalitiy** of a **categorical** feature
	- Usually because of different labels of the same category, $\Rightarrow$ correct the error and regenerate the [[Analytics Base Table|ABT]]. 
4. **high cardinality** of a **categorical** feature with **valid** data
	- learning algorithm might struggle with such high cardinality; so, note it in the **data quality plan**