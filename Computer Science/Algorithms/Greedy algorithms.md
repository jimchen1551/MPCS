---
Created: [[2022-12-27]]
Aliases: 
Types: Card
Tags: 
- 
---
# Greedy algorithms
- similar to [[dynamic programming]]
- used for optimization problems
- not always yield an optimal solution
- making a **locally optimal choice** in the hope of getting a **globally optimal solution**
## Activity-selection problem
- given a set of activities $S\{a_1,\dots,a_n\}$
- $n$ activities require **exclusive** use of a common resource
- $a_i$ needs resource during period $[s_i, f_i)$, which is a half-open interval, where $s_i$ = start time and $f_i$ = finish time, where $0\leq s_i\leq f_i\leq\infty$
- If $a_i$ and $a_j$ are **compatible**, the intervals $[s_i, f_i)$ and $[s_j, f_j)$ do not overlap. 
- Selecting the largest possible set of **mutually compatible** activities
## Knapsack problem
## Huffman codes
- very effective technique for compressing data
- considering the data to be a sequence of characters
### Prefix codes
- no codeword is also a prefix of some other codeword
- the optimal data compression achievable by a character code can always be achieved with a prefix code
- prefix code are desirable because they simplify decoding
- representation for prefix code: **binary tree**
  - whose leaves are the given characters
  - interpretting the binary codeword for a character as the path from the root to that character
  - 0 means go to the left child
  - 1 means go to the right child
![[Screen Shot 2022-12-27 at 08.02.06.png]]
$$B(T)=\sum_{c\in C}c.freq\cdot d_T(c)$$
, where $B$ is the number of bits required, $c.freq$ is the frequency of $c$, and $d_T(c)$ is the depth of $c$'s leaf in the tree
- construction takes $O(n\lg n)$ time
### Huffman's greedy algorithm
- using a table of the frequencies of occurrence of the characters to build up an optimal way of representing each character as a binary string
