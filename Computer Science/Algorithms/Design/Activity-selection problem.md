---
Created: [[2023-01-02]]
Aliases: 
Types: Card
Tags: 
- 
---
# Activity-selection problem
- given a set of activities $S\{a_1,\dots,a_n\}$
- $n$ activities require **exclusive** use of a common resource
- $a_i$ needs resource during period $[s_i, f_i)$, which is a half-open interval, where $s_i$ = start time and $f_i$ = finish time, where $0\leq s_i\leq f_i\leq\infty$
- If $a_i$ and $a_j$ are **compatible**, the intervals $[s_i, f_i)$ and $[s_j, f_j)$ do not overlap. 
- Selecting the largest possible set of **mutually compatible** activities