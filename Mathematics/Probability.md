---
Created: [[2022-10-17]]
Aliases: 
Types: Note
Tags: 
- 
---
# Probability
## Axioms
1. $P(A)\geq0,\forall A\in S$
2. $P(S)=1$
3. $P(A_1\cup A_2\cup\dots\cup A_n)=P(A_1)+P(A_2)+\dots+P(A_n),\forall A_i \text{ mutually exclusive where }i\in [1, n]$
## Properties
1. $P(\phi)=0$
   $S\cap\phi=\phi\rightarrow\text{mutual exclusivity}$
   $S=S\cup\phi\rightarrow P(S)=P(S\cup\phi)=P(S)+P(\phi)$
   
2. $P(A)=1-P(A^C)$
   $A\cap A^C=\phi\rightarrow \text{mutual exclusivity}$
   $S=A\cup A^C\rightarrow P(S)=P(A)+P(A^C)$
   
3. $P(A)=P(A-B)+P(A\cap B)$
   $(A-B)\cap (A\cap B)=\phi\rightarrow \text{mutual exclusivity}$
   $A=(A-B)\cup (A\cap B)\rightarrow P(A)=P(A-B)+P(A\cap B)$
   
4. Principle of inclusion and exclusion (PIE)
   $P(A\cup B)=P(A)+P(B)-P(A\cap B)$
   
5. Total probability theorem
   $P(A)=\Sigma_{i=1}^nP(A\cap C_i)$
   $\forall \text{ }C_i\text{ and }C_j\text{ are mutually exclusive where i and j }\in [1, n] \text{ and } i\neq j$
   $\text{and }C_1\cup C_2\cup\dots\cup C_n=S$
   
6. Boole's inequality
   $P(\bigcup_{i=1}^nA_i)\leq\Sigma_{i=1}^nP(A_i)$
   
7. Bonferroni's inequality
   $P(\bigcap_{i=1}^nA_i)\geq1-\Sigma_{i=1}^nP(A_i^C)$

## Conditional probability
$$P(X|Y)=\frac{P(X\cap Y)}{P(Y)}$$
### Properties
1. $P(X|Y)\geq 0$
2. $P(Y|Y)=1$
3. $P(A\cup B|Y)=P(A|Y)+P(B|Y)\text{ while A and B are mutually exclusive}$
4. Total probability theorem
   $P(A)=\Sigma_{i=1}^nP(A|C_i)P(C_i)$
   $\forall \text{ }C_i\text{ and }C_j\text{ are mutually exclusive where i and j }\in [1, n] \text{ and } i\neq j$
   $\text{and }C_1\cup C_2\cup\dots\cup C_n=S$
5. Bayes' rule
   $\displaystyle P(C_i|A)=\frac{P(A|C_i)P(C_i)}{\Sigma_{j=1}^nP(A|C_j)P(C_j)}$

### Independence
$$P(A\cap B)=P(A)\cdot P(B)$$
$$P(A|B)=P(A)$$

## Random variable
- a way to simplify the outcome of an experiment with numbers
- $P(X=0, 1, 2, \dots)$

[[Probability mass function]]
[[Probability density function]]
[[Cumulative distribution function]]

## Expectation

## Probability distribution
[[Bernoulli distribution]]
[[Binomial distribution]]
[[Uniform distribution]]
[[Geometric distribution]]
[[Pascal distribution]]
[[Poisson distribution]]
[[Exponential distribution]]
[[Erlang distribution]]/[[Erlang distribution|Gamma distribution]]
[[Normal distribution]]/[[Normal distribution|Gaussian distribution]]
[[Standard normal distribution]]
