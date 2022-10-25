---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Algorithms
- any well-defined **computational procedure** that transforms the **input** into the **output** for solving a well-specified (spec: the relationship b/w input and output) **computational problem**

| Algorithms                  | Comment |
| --------------------------- | ------- |
| [[Sorting algorithms]]      |         |
| [[Searching algorithms]]    |         |
| [[Graph algorithms]]        |         |

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

## Loop invariant
- a property of a program loop that is true before (and after) each iteration
- a logical assertion, sometimes checked within the code by an assertion call
- used to understand why an algorithm is correct
1. **Initialization**: It is true prior to the first iteration of the loop.
2. **Maintenance**: If it is true before an iteration of the loop, it remains true before the next iteration.
3. **Termination**: When the loop terminates, the invariant gives us a helpful property that helps show that the algorithm is correct.
### Floyd-Hoare logic
[Wiki explained](https://en.wikipedia.org/wiki/Hoare_logic)

## Analysis
- Analyzing an algorithm has come to mean **predicting the resources** (memory, communication bandwidth, or computer hardware) that the algorithm requires. 
- assuming a generic one-processor, random-access machine (**RAM**) model of computation as implementation technology
	- No concurrent operations
	- Not attempt to model the memory hierarchy
	- Instructions: arithmetic ([[Register operands]]), data movement ([[Memory operands]]), and control ([[Branch]], [[Jump]])
	- Data types: integer and floating point
- **Input size**: depending on the problem studied
  e.g., sorting or discrete Fourier transform: number of items in the inputs; multiplying 2 integers: total number of bits
- **Running time**: the number of primitive steps executed
- [[Instance]], [[Asymptotic notation]], [[Standard notation]]

## Design
| Algorithms                  | Examples                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Incremental method          | [[Insertion sort]]                                                                                                                               |
| [[Divide and conquer]]      | [[Merge sort]]<br>[[Strassen's algorithm]]<br>[[Substitution method]]<br>[[Recursion-tree method]]<br>[[Master method]]<br>[[Akra-Bazzi method]] |
| [[Greedy algorithms]]       | [[Selection sort]]                                                                                                                               |
| [[Dynamic programming]]     |                                                                                                                                                  |
| [[Network flow algorithms]] |                                                                                                                                                  |

## Reference book
- Algorithms in a nutshell by George T. Heineman, Gary Pollice, and Stanley Selkow
- Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein

## Score
- Midterm: 30%
- Final: 30%
- Homework: 40%
