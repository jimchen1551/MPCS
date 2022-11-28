---
Created: [[2022-11-24]]
Aliases: DQI
Types: Note
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
| [[Outliers]]              | Invalid outliers<br>Valid outliers<br>Clamp transformation                                          |



