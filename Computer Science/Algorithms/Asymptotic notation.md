---
Created: [[2022-10-25]]
Aliases: 
Types: Note
Tags: 
- 
---
# Asymptotic notation
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

## Instance
$$S_n=\{s_i|i\in[1,n]\}\quad\text{, where } s_i\text{ is an instance (input) of the algorithm}$$
$$\sum_{s_i\in S_n} Pr\{s_i\}=1$$
$$t(s_i)\text{ is the time taken by the algorithm on the instance }s_i$$

## Transitivity
  $f(n)=\Theta(g(n))\text{ and }g(n)=\Theta(h(n))\Rightarrow f(n)=\Theta(h(n))$
  $f(n)=O(g(n))\text{ and }g(n)=O(h(n))\Rightarrow f(n)=O(h(n))$
  $f(n)=\Omega(g(n))\text{ and }g(n)=\Omega(h(n))\Rightarrow f(n)=\Omega(h(n))$
  $f(n)=o(g(n))\text{ and }g(n)=o(h(n))\Rightarrow f(n)=o(h(n))$
  $f(n)=\omega(g(n))\text{ and }g(n)=\omega(h(n))\Rightarrow f(n)=\omega(h(n))$

## Reflexivity
  $f(n)=\Theta(f(n))$
  $f(n)=O(f(n))$
  $f(n)=\Omega(f(n))$

## Symmetry
  $f(n)=\Theta(g(n))\leftrightarrow g(n)=\Theta(f(n))$

## Transpose symmetry
  $f(n)=O(g(n))\leftrightarrow g(n)=\Omega(f(n))$
  $f(n)=o(g(n))\leftrightarrow g(n)=\omega(f(n))$
  