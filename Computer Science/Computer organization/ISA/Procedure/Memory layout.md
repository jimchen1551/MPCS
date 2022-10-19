---
Created: [[2022-10-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# Memory layout
![[Pasted image 20220709002201.png]]

| Content      | Comment                         |
| ------------ | ------------------------------- |
| Text         | program code                    |
| Static data  | global variables, $gp           |
| Dynamic data | heap (malloc in C, new in Java) |
| [[Stack]]    | automatic storage               |