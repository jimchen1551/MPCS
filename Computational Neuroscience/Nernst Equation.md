---
created: [[2022-06-08]]
aliases: The Nernst equation
types: Note
tags: 
- Thermodynamics
---
# Ideal gas law → Nernst equation
$$\displaystyle PV=NkT$$
$$\displaystyle \Rightarrow P=\frac{NkT}{V}$$
$$\because W \equiv \int \vec{F} \cdot \mathrm{d}\vec{s}$$
$$\therefore W=\int \frac{NkT}{V}A\cdot \mathrm{d}s$$
$$\Rightarrow W=\int \mathrm{d}(NkT\cdot \ln s)$$
$$\Rightarrow W=NkT\cdot \ln\frac{L}{L'}$$
$$\Rightarrow W=NkT(\ln\frac{L}{L'}+\ln\frac{A}{A}-\ln\frac{N}{N})$$
$$\Rightarrow W=NkT\cdot \ln\frac{[X]'}{[X]}$$

# Notation
|   Symbol   | Definition                                     |
|:----------:|:---------------------------------------------- |
|    $X$     | ion                                            |
|    $z$     | the charge number of *X*                       |
| $[X]_{in}$ | the concentration of *X* inside                |
| $[X]_{ex}$ | the concentration of *X* outside               |
|   $W_e$    | the work done against the **electrical field** |
|   $W_d$    | the work done against the **concentration**    |
|    $v$     | membrane potential                             |
|   $v_X$    | Nernst equilibrium potential of *X*                   |
|    $q$     | unit charge                                    |

# Nernst equilibrium potential
## Potential 
The diffusional and electrical effects are in **equilibrium** if 
$$\displaystyle W_{e} + W_{d} = 0$$
$$\displaystyle W_e = zqv$$$$\displaystyle W_d = kT\cdot ln\frac{[X]_{in}}{[X]_{out}}$$
$$\displaystyle \Rightarrow v_X = \frac{kT}{zq} ln\frac{[X]_{ex}}{[X]_{in}}$$

## Current
| Symbol | Definition                                  |
| ------ | ------------------------------------------- |
| $I_X$  | electrical current while X-channel are open |
| $g_X$       |conductance(the reciprocal of resistance)                                             |
According to the Ohm's law, while the X-channels are open, the electric current by the flow of X-ions would be
$$\displaystyle I_X=g_X(v_X-v)$$
