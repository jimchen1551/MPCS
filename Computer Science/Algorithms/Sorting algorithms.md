---
Created: [[2022-09-28]]
Aliases: 
Types: Note
Tags: 
- 
---
# Sorting algorithms
Input: $\langle a_1, a_2, \dots,a_n\rangle$
Output: $\langle a_1',a_2',\dots, a_n'\rangle$ s.t. $a_1'\leq a_2'\leq\dots\leq a_n'$

| Sorting            | Design                       | [[Asymptotic notation]] |
| ------------------ | ---------------------------- | ----------------------- |
| [[Insertion sort]] | Incremental approach         | $\Theta(n^2)$           |
| [[Merge sort]]     | [[Divide and conquer]]       | $\Theta(n\lg n)$        |
| [[Heap sort]]      | [[Heap]]                     | $O(n\lg n)$             |
| [[Quick sort]]     | [[Divide and conquer]]       | Avg: $\Theta(n\lg n)$   |
| [[Counting sort]]  | For integers                 | $\Theta(n)$             |
| [[Radix sort]]     | By digit                     | $\Theta(d(n+k))$        |
| [[Bucket sort]]    | For [[Uniform distribution]] | Exp: $\Theta(n)$        |

## Decision-tree model
![[Screen Shot 2022-11-15 at 08.40.30.png]]
- a full binary tree representing the comparison b/w elements performed by a particular sorting on an input of a given size
- the execution of the sorting algorithm corresponds to tracing a path from the root of the decision tree to a leaf
- the [[Lower bound]] for the [[Worst case]] is the length of the longest path from the root to any reachable leaves
- any comparison sort algorithm requires $\Omega(n\lg n)$ comparisons in the worst case
	- considering a decision tree of height $h$ with $l$ reachable leaves corresponding to a comparison sort on $n$ numbers
	- $n!\leq l\leq 2^h\Rightarrow h\geq\lg(n!)=\Omega(n\lg n)$

## Order statistics
- The $i$th order statistic of a set of $n$ elements is the $i$th smallest element. 
- Maximum: $i=n$
- Minimum: $i=1$
- Lower median: $i=\lfloor (n+1)/2\rfloor$
- Upper median: $i=\lceil (n+1)/2\rceil$

## Selection problem
Input: $A=\{a_j|\forall j\in[1, n]\}$ and $i$ for the selected order statistic
Output: The element $x\in A$ that is larger than exactly $i-1$ other elements of $A$. 
Solution:
1. Sorting $A$ ($O(n\lg n)$)
2. Indexing the $i$th element
### Selection in expected linear time
### Selection in worst linear time

