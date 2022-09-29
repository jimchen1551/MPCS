---
Created: [[2022-07-16]]
Aliases: 
Types: Note
Tags: 
- 
---
# Arithmetic
## Addition and Subtraction
| Arithmetic                | Implementation                       |
| ------------------------- | ------------------------------------ |
| [[Integer addition]]      | [[Carry lookahead adder]]           |
| [[Integer subtraction]]   | [[Unsigned number subtraction]]      |
|                           | [[Signed 2's complement]]            |
| [[Overflow]]              | [[Overflow#Partitioned carry chain]] |
|                           | [[Overflow#Saturating operations]]   |
| [[Arithmetic logic unit]] | [[1-bit ALU]], [[1-bit ALU for MSB]] |
|                           | [[32-bit ALU]]                       |
| [[Shifter]]               | [[Single-bit position shifter]]      |
|                           | [[Barrel shifter]]                   |

## Multiplication and Division
| Arithmetic     | Implementation                                   |
| -------------- | ------------------------------------------------ |
| Multiplication | [[Ordinary multiplication algorithm]] (unsigned) |
|                | [[Refined multiplication algorithm]] (unsigned)  |
|                | [[Booth's algorithm]] (signed and unsigned)      |
| Division       | [[Ordinary division algorithm]] (unsigned)       |
|                | [[Refined division algorithm]] (unsigned)        |

According to the resemblance of the circuits of the [[Refined multiplication algorithm]] and the [[Refined division algorithm]], they can be combined and switched by a control input. 
![[Screen Shot 2022-07-21 at 17.03.23.png]]

### Acceleration
- For multiplication, using **multiple adders** and **pipelining** the circuit are ways to accelerate. 
- For division, it can't be accelerated by parallel design like multiplication because of the ambiguity of the subtraction. However, **generating multiple quotient bits per step** (e.g., SRT division) may help but little. 

## Floating point
Standard: [[IEEE std 754]]

| Arithmetic                        | Implementation                              |
| --------------------------------- | ------------------------------------------- |
| [[Floating-point addition]]       |pipelined and done in several clock cycles |
| [[Floating-point multiplication]] | similar to that of addition                                            |

Hardware for floating-point arithmetic is **coprocessor 1** in [[MIPS]] ([[MIPS syntax#Floating-point arithmetic]]), which has its own **floating-point registers** ($f0~31; single-precision: $fx; double-precision: $fx, $fx+1). 

---

## Subword parallelism
- aka data-level parallelism, vector parallelism, or single instruction multiple data (**SIMD**)
- Graphics and audio applications can take advantage of performing simultaneous operations on short vectors. 
- e.g., 128-bit adder can be used to do 16 * 8-bit addtions, 8 * 16-bit additions, or 4 * 32-bit addtions. 
- [[Streaming SIMD Extensions]], [[Advanced Vector Extensions]]

---

## Fallacy
1. **Right shift** can replace integer division by a power of 2
   - For unsigned integer, it's true. 
   - For signed integer, it's true only with an arithmetic right shift. 
2. Only theoretical math care about **floating-point accuracy**. 
   - e.g., [[x86#Pentium]] FDIV bug (Pentium Chronicles by Colwell)

## Pitfall
1. [[Floating-point addition]] is not associative
   - because of the inaccuracy of [[IEEE std 754#Rounding mode]] called by [[Floating-point addition]] and [[Floating-point multiplication]] algorithms
   - **Parallel programs** may interleave operations in unexpected orders, so we need to validate parallel programs under varying degrees of parallelism. 
