---
Created: [[2022-06-13]]
Modified: None
Types: Note
Tags: 
- 
---
# Algorithms
- any well-defined **computational procedure** that transforms the **input** into the **output** for solving a well-specified (spec: the relationship b/w input and output) **computational problem**

## Alogorithm pattern format
1. Name
2. Synopsis: A high-level description of the algorithms and what it is designed to do. 
3. Context: A description of a problem that illustrate the"sweet spot" for the algorithm.
4. Forces: A description of the properties of the problem/solution that must be addressed and maintained for a successful implementation. 
5. Solution: The algorithm description using real working code with documentation. 
6. Consequences: Identifies and discuss the advantages/disadvantages and anti-patterns for this algorithm. 
7. Analysis
8. Related algorithms

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
1. **Indentation** indicates block structure. 
2. The **looping constructs while, for, and repeat and the **conditional constructs** if, then, and else have interpretations similar to those in **Pascal**. 
3. A **multiple assignments of the form i <- j ← e assigns to both variables i and j the value expression e. It should be treated as j ← e followed by i <- j. 
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
3. **Termination**: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.
### Floyd-Hoare logic

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
### Instance
$$S_n=\{s_i|i\in[1,n]\}\quad\text{,where } s_i\text{ is an instance (input) of the algorithm}$$
$$\sum_{s_i\in S_n} Pr\{s_i\}=1$$
$$t(s_i)\text{ is the time taken by the algorithm on the instance }s_i$$
| Case             | Bound           | Asymptotic notation                                                                                       |
| ---------------- | --------------- | --------------------------------------------------------------------------------------------------------- |
| [[Worst case]]   | [[Upper bound]] | $O(f(n))=\DeclareMathOperator*{\argmax}{arg\,max\ }T_{wc}(n)\equiv\argmax_t t(s_i),\forall s_i\in S$      |
| [[Average case]] |                 | $\quad\quad\quad\quad\quad T_{ac}(n)=\sum_{s_i\in S_n}t(s_i)Pr\{s_i\}$                                    |
| [[Best case]]    | [[Lower bound]] | $\Omega(f(n))=\DeclareMathOperator*{\argmin}{arg\,min\ }T_{wc}(n)\equiv\argmin_t t(s_i),\forall s_i\in S$ |
|                  | [[Tight bound]] | $\Theta(f(n))\leftrightarrow(\Omega(f(n))\land O(f(n)))$                                                  |
- considering the leading term
- ignoring the leading term's constant coefficient
- The equal sign means **set membership**. 
- When asymptotic notation appears in a formula, it stands for an **anonymous function**. (the right-hand side is coarser than the left-hand side)
- Transitivity: $f(n)=\Theta(g(n))\cap$
- Reflexivity
- Symmetry
- Transpose symmetry

## Design
### Incremental approach
- e.g., [[Insertion sort]]
### Divide-and-conquer approach
- **Divide** the problem into a number of subproblems. 
- **Conquer** the subproblems by solving them recursively. 
- **Combine** the solutions to the subproblems into the solution for the original problem. 
- e.g., [[Merge sort]]

| Algorithms                  | Comment |
| --------------------------- | ------- |
| [[Sorting algorithms]]      |         |
| [[Searching algorithms]]    |         |
| [[Graph algorithms]]        |         |
| [[Network flow algorithms]] |         |


## Reference book
- Algorithms in a nutshell by George T. Heineman, Gary Pollice, and Stanley Selkow
- Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein