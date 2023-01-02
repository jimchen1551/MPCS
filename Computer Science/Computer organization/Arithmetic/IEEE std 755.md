---
Created: [[2022-07-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# IEEE std 754
- floating point standard
- single-precision (32-bit)
- double-precision (64-bit)
- announced at 1985
- developed in response to divergence of representations (for **portability**)

![[Screen Shot 2022-07-25 at 14.43.13.png]]

- S: **sign** bit
- Fraction: 
  For single, $\text{Precision}=2^{-23}\approx10^{-7}$. 
  For double, $\text{Precision}=2^{-52}\approx10^{-17}$. 
- Exponent: **excess representation** (actual exponent + bias) to ensure the exponent is unsigned; for single, bias=127; for double, bias=1023

![[Screen Shot 2022-07-25 at 14.57.15.png]]

- Exponent = 0 is reserved for **0** and **denormalized numbers**
- Exponent = 255/2047 is reserved for **infinity** and **NaN** (not a number)

- The **smallest** value for single-precision FP: 
  exponent = 00000001
  fraction = 00...0
  $x=\pm 1.0\times2^{-126}\approx\pm1.2\times10^{-38}$
- The **largest** value for single-precision FP: 
  exponent = 11111110
  fraction = 11...1
  $x=\pm(2.0-2^{-23})\times2^{127}\approx\pm3.4\times10^{38}$

## Denormalized number
![[Screen Shot 2022-07-25 at 15.28.06.png]]
- Exponent = 00000000
- Fraction $\neq$ 0

## Infinity
- Exponent = 11111111
- Fraction = 000...0
- used for avoiding the need for overflow check

## Not a Number
- aka NaN
- Exponent = 11111111
- Fraction $\neq$ 0
- used for representation of illegal or undefined result

## Extra bits for accurate arithmetic
1. Guard bit and round bit: keeping 2 extra bits on the right during intermediate calculations of floating-point numbers
2. Sticky bit: is set whenever there are nonzero bits to the right of the round bit
---

## Rounding mode
1. Always round up (get closer to $+\infty$)
2. Always round down (get closer to -$\infty$)
3. Truncate
4. Round to nearest even (most commonly used)
