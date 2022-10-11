---
Created: [[2022-06-13]]
Modified: None
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
### Instance
$$S_n=\{s_i|i\in[1,n]\}\quad\text{,where } s_i\text{ is an instance (input) of the algorithm}$$
$$\sum_{s_i\in S_n} Pr\{s_i\}=1$$
$$t(s_i)\text{ is the time taken by the algorithm on the instance }s_i$$
### Asymptotic notation
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
- **Transitivity**: 
  $f(n)=\Theta(g(n))\text{ and }g(n)=\Theta(h(n))\Rightarrow f(n)=\Theta(h(n))$
  $f(n)=O(g(n))\text{ and }g(n)=O(h(n))\Rightarrow f(n)=O(h(n))$
  $f(n)=\Omega(g(n))\text{ and }g(n)=\Omega(h(n))\Rightarrow f(n)=\Omega(h(n))$
  $f(n)=o(g(n))\text{ and }g(n)=o(h(n))\Rightarrow f(n)=o(h(n))$
  $f(n)=\omega(g(n))\text{ and }g(n)=\omega(h(n))\Rightarrow f(n)=\omega(h(n))$
- **Reflexivity**: 
  $f(n)=\Theta(f(n))$
  $f(n)=O(f(n))$
  $f(n)=\Omega(f(n))$
- **Symmetry**: 
  $f(n)=\Theta(g(n))\leftrightarrow g(n)=\Theta(f(n))$
- **Transpose symmetry**: 
  $f(n)=O(g(n))\leftrightarrow g(n)=\Omega(f(n))$
  $f(n)=o(g(n))\leftrightarrow g(n)=\omega(f(n))$
### Standard notation
| Notation             | Explanation                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Monotonicity         | monotonically $\leq$ strictly                                                                                                                                                                                                                                                                                                                    |
| Floors and ceilings  | $\lfloor x \rfloor\leq x \leq \lceil x \rceil$<br>$\lfloor x\rfloor$: the **floor** of $x$, which is the greatest integer $\leq x$<br>$\lceil x\rceil$: the **ceil** of $x$, which is the least integer $\geq x$<br>The floor function is monotonically increasing, as is the ceil function.                                                     |
| Modular arithmetic   | $a\equiv b\ (\mod c$)                                                                                                                                                                                                                                                                                                                            |
| Polynomials          | **Polynomially bounded**:<br>if $f(n)=O(n^k)$ for some constant $k$                                                                                                                                                                                                                                                                              |
| Exponentials         |                                                                                                                                                                                                                                                                                                                                                  |
| Logarithms           | **Polylogarithmic bounded**:<br>if $f(n)=O(\log^kn)$ for some constant $k$                                                                                                                                                                                                                                                                       |
| Factorials           | $n!<n^n$<br>**Stirling's approximation**: <br>$n!=\sqrt{2\pi n}(\frac{n}{e})^n(1+\Theta(\frac{1}{n}))$<br>$\Rightarrow\begin{cases} n!=o(n^n)\\n!=\omega(2^n)\\ \log(n!)=\Theta(n\log n)\end{cases}$<br>$\Rightarrow n!=\sqrt{2\pi n}(\frac{n}{e})^ne^{\alpha_n},\quad \forall n\geq 1$<br>$\text{where }\frac{1}{12n+1}<\alpha_n<\frac{1}{12n}$ |
| Functional iteration | The function iteratively applied $i$ times to an initial value of $n$. <br> $f^{(i)}(n)=\begin{cases}n&\quad\text{if }i=0\\f(f^{(i-1)}(n)&\quad\text{if }i>0\end{cases}$<br>e.g., if $f(n)=2n$, then $F^{(i)}(n)=2^in$                                                                                                                           |
| Iterated algorithms  | $\log^*n=\min\{i\geq0:\log^{(i)}n\leq1\}$???                                                                                                                                                                                                                                                                                                     |
| Fibonacci iteration  |$F_i=\begin{cases}0&\quad\text{if }i=0\\1&\quad\text{if }i=1\\F_{i-1}+F_{i-2}&\quad\text{if }i=\geq2\end{cases}$<br>$=\frac{\phi^i-\hat\phi^i}{\sqrt5}=\lfloor\frac{\phi^i}{\sqrt5}+\frac{1}{2}\rfloor\because\frac{\mid \hat\phi^i \mid }{\sqrt5}<\frac{1}{\sqrt5}<\frac{1}{2}$                                                                                                                                                                                                                                                                                                                                                  |

## Design
| Algorithms                  | Examples           |
| --------------------------- | ------------------ |
| Incremental approach        | [[Insertion sort]]                   |
| [[Divide and conquer]]      | [[Merge sort]], [[Strassen's algorithm]]                   |
| [[Greedy algorithms]]       | [[Selection sort]] |
| [[Dynamic programming]]     |                    |
| [[Network flow algorithms]] |                    |

## Reference book
- Algorithms in a nutshell by George T. Heineman, Gary Pollice, and Stanley Selkow
- Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein

## Score
- Midterm: 30%
- Final: 30%
- Homework: 40%
