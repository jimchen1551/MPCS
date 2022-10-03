---
Created: [[2022-10-03]]
Aliases: 
Types: Note
Tags: 
- 
---
# Linear systems
$$Ax=b$$
$$A\in R^{m\times n};x\in R^m; b\in R^n$$
- Underdetermined, n < m (short-fat $A$), $\infty$ solutions of $x$ given $b$
- Overdetermined, n > m (tall-skinny $A$), 0 solution of $x$ given $b$
While considering [[Singular value decomposition]], 

$$A=U\Sigma V^T\Rightarrow (U\Sigma V^T)x=b\Rightarrow x=(V\Sigma^{-1}U^T)b\Rightarrow A^\dagger=V\Sigma^{-1}U^T$$
$$A^\dagger\text{ is called pseudo-inverse of }A\text{ or Moore-Penrose pseudoinverse}$$
- So, for underdetemined case, we have $\min\|\tilde x\|_2\text{ s.t. }A\tilde x=b$
- And, for overdetermined case, we have the least square solution $\min \|A\tilde x-b\|_2$
If [[Singular value decomposition#Eckand-Young theorem]] is considered, 
$$A=\tilde U\tilde\Sigma V^T\Rightarrow A\tilde x=\tilde U\tilde\Sigma V^TV\tilde\Sigma^{-1}\tilde U^Tb=\tilde U\tilde U^Tb$$
- $\tilde U\tilde U^Tb$ is the projection of $b$ onto $span(\tilde U)=span(A)$
- this helps us to find the minimal 