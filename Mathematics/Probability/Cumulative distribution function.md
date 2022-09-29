---
Created: [[2022-09-21]]
Aliases: CDF
Types: Card
Tags: 
- 
---
# Cumulative distribution function
$$F_X(x)=P(X\leq x)$$
$$F(-\infty)=0$$
$$F_X(\infty)=1$$
for **discrete** random variables, 
$F_X(x)=\Sigma_{n=-\infty}^{\lfloor x\rfloor}P(x=n)$
$F_X(x^+)=F_X(x)$
$F_X(x^-)=F_X(x)-P(X=x)$

for **continuous** random variables, 
$F_X(x)=\int_{-\infty}^xP(X=n)\cdot dn$
$F_X(x^-)=F_X(x)=F_X(x^+)$