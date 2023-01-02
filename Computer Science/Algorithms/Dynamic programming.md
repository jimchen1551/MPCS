---
Created: [[2022-12-26]]
Aliases: 
Types: Note
Tags: 
- 
---
# Dynamic programming
- combining the solutions to subproblems like [[Divide and conquer]]
- when the subproblems **share subsubproblems**, each subsubproblem will be **solved once** and **saved** its answer in a **table**
- programming here means a **tabular method**
- **time-memory trade-off**: using additional memory to save computation time
- used for the **optimization problems**

To develop a dynamic-programming algorithm, 
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information

| Problems                                | Comment |
| --------------------------------------- | ------- |
| [[Rod cutting problem]]                 |         |
| [[Matrix-chain multiplication problem]] |         |
| [[Longest common subsequence problem]]  |         |
| [[Optimal binary search tree]]          |         |

## Optimal substructure
- optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently. 
  1. A solution to the problem consists of making a choice. Making this choice leaves one or more subproblems to be solved. 
  2. Suppose for a given problem, you are given a choice that leads to an optimal solution. 
  3. Given this choice, determine which subproblems ensue and how to characterize the resulting space of subproblems best. 
  4. Use the **cut-and-paste** technique to show that the solutions to the subproblems used within the optimal solution to the problem must themselves be optimal. 
## Overlapping subproblem
- 2 subproblems overlap if they are the same subproblem that occurs as a subproblem of different problems. 
- Dynamic programming solves each subproblem once and stores the solution in a table where it can be looked up when needed. 
## Cut-and-paste
- Suppose that one of the subproblem solutions is not optimal
- **Cut** it out and **Paste** in an optimal solution. 
- Get a better solution to the original problem. 
## Memoization
- making a table indexed by subproblem
1. lookup in the table
2. if the answer exists, use it
3. else, compute the answer and store it
## Running time
- depending on the product of:
  1. the number of subproblems overall
  2. how many choices to look at for each subproblem
