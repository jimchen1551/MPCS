---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Algorithms
- any well-defined **computational procedure** that transforms the **input** into the **output** for solving a well-specified (spec: the relationship b/w input and output) **computational problem**

| Algorithms               | Content                                                                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Sorting algorithms]]   | [[Insertion sort]]<br>[[Merge sort]]<br>[[Heap sort]]<br>[[Quick sort]]<br>[[Selection sort]]<br>[[Counting sort]]<br>[[Radix sort]]<br>[[Bucket sort]]<br>[[Randomized select]]<br>[[Select]] |
| [[Searching algorithms]] |                                                                                                                                                                                                |

## Typical problems
- Shortest path problem
- The longest common subsequence of two ordered sequences of symbols
- Topological sorting problem
- Convex hull problem

## Hard problems
- the usual measure of efficiency: **speed**
- NP problems
	- Nondeterministic polynomial
- NP-complete problems
	- a subspace of NP problems
	- no efficient algorithm found
	- unknown whether or not efficient algorithms exist
	- If an efficient algorithm exists for any one of them, then efficient algorithms exist for all of them. 

## Pseudocode
![[Screen Shot 2022-10-03 at 16.41.00.png]]
1. **Indentation** indicates block structure. 
2. The looping constructs while, for, and repeat and the **conditional constructs** if, then, and else have interpretations similar to those in **Pascal**. 
3. **Multiple assignments of the form i ← j ← e assigns to both variables i and j the value expression e. It should be treated as j ← e followed by i ← j. 
4. **Variables are local** to the given procedure. We shall not use global variables without explicit indication. 
5. **Array elements** are accessed by specifying the array name followed by the index in square brackets. 
6. Compound data are typically organized into **objects**, which are composed of attributes or fields. A **particular field** is accessed using the field name followed by the name of its object in square brackets. 
7. Parameters are **passed** to a procedure **by value**. 
8. The boolean operators "and" and "or" are short-circuiting. 

## Analysis
| Analysis                | Content                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| [[Loop invariant]]      | Initialization<br>Maintenance<br>Termination                                                                  |
| [[Asymptotic notation]] | [[Upper bound]]<br>[[Lower bound]]<br>[[Tight bound]]                                                         |
| [[Standard notation]]   | Monotonicity<br>Ceil and floor<br>Polynomially bounded<br>Polylogarithmic bounded<br>Stirling's approximation |

- Analyzing an algorithm has come to mean **predicting the resources** (memory, communication bandwidth, or computer hardware) that the algorithm requires. 
- assuming a generic one-processor, random-access machine (**RAM**) model of computation as implementation technology
	- No concurrent operations
	- Not attempt to model the memory hierarchy
	- Instructions: arithmetic ([[Register operands]]), data movement ([[Memory operands]]), and control ([[Branch]], [[Jump]])
	- Data types: integer and floating point
### Input size
- depending on the problem studied
- e.g., sorting or discrete Fourier transform: number of items in the inputs; multiplying 2 integers: total number of bits
### Running time
- the number of primitive steps executed

## Design
| Technique               | Examples                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Incremental method      | [[Insertion sort]]                                                                                                                               |
| [[Divide and conquer]]  | [[Merge sort]]<br>[[Strassen's algorithm]]<br>[[Substitution method]]<br>[[Recursion-tree method]]<br>[[Master method]]<br>[[Akra-Bazzi method]] |
| [[Dynamic programming]] | [[Rod cutting problem]]<br>[[Matrix-chain multiplication problem]]<br>[[Longest common subsequence problem]]<br>[[Optimal binary search tree]]   |
| [[Greedy algorithms]]   | [[Selection sort]]<br>[[Activity-selection problem]]<br>[[Knapsack problem]]<br>[[Huffman codes]]                                                |

## Reference book
- Algorithms in a nutshell by George T. Heineman, Gary Pollice, and Stanley Selkow
- Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein

## Score
- Midterm: 30%
- Final: 30%
- Homework: 40%
