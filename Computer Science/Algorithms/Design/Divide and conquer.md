---
Created: [[2022-10-11]]
Aliases: 
Types: Note
Tags: 
- 
---
# Divide and conquer
If a problem doesn't involve a recursive invocation, $\Rightarrow$**base case**.
Else, $\Rightarrow$**recursive case**.

- **Divide** the problem into a number of subproblems. 
- **Conquer** the subproblems by solving them recursively. 
- **Combine** the solutions to the subproblems into the solution for the original problem. 

- e.g., [[Merge sort]], [[Strassen's algorithm]]

## Recurrence
The recurrence is **well defined** if there's at least one function satisfying; otherwise, **ill defined**. 

A recurrence $T(n)$ is **algorithmic** if, $\forall$ sufficiently large **threshold constant** $n_0>0$, the following 2 properties hold:
1. $\forall n<n_0$, we have $T(n)=\Theta(1)$
2. $\forall n\geq n_0$, every path of recursion **terminates** in a defined **base case** within a finite number if recursive invocations. 

### Solution
1. [[Substitution method]]
2. [[Recursion-tree method]]
3. [[Master method]]
4. Akra-Bazzi method