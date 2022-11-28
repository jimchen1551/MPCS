---
Created: [[2022-11-24]]
Aliases: 
Types: Note
Tags: 
- 
---
# Data Visualization
- to reduce the size of [[Analytics Base Table|ABT]] while two features are strongly related
## Both continuous features
![[Screen Shot 2022-10-11 at 16.19.57.png|400]]
- **scatter plot matrix** (SPLOM)
## Both categorical features
![[Screen Shot 2022-10-18 at 13.42.08.png|400]]
- **small multiples** (drawing the density of each level of feature)
![[Screen Shot 2022-10-18 at 13.43.28.png|400]]
- if the number of levels of one of the features is small, use **stacked bar plots** as an alternative
## Cross-data-type features
![[Screen Shot 2022-10-18 at 13.55.36.png|400]]
- **small multiples** (drawing a density histogram of the values of the continuous feature for each level of the categorical feature)
- if the features are related, the shapes and/or the central tendencies of the histogram will be different.
![[Screen Shot 2022-11-25 at 11.20.39.png|400]]
![[Screen Shot 2022-10-18 at 13.56.15.png|400]]
- **box plots** (less detail than histogram but better suited when the categorical feature has many levels(>4))
