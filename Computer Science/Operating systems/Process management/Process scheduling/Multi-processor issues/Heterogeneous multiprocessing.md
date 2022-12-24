---
Created: [[2022-12-24]]
Aliases: HMP
Types: Card
Tags: 
- 
---
# Heterogeneous multiprocessing
- systems are designed using cores that run the same instruction set, yet vary in terms of their clock speed and power management
- for ARM processors that support it, this is known as **big.LITTLE** where higher-performance **big** cores are combined with energy-efficient **LITTLE** cores
  - **big** cores consume greater energy and should only be used for short periods
  - **LITTLE** cores use less energy and can be used for longer periods
- [[CPU scheduler]] can assign tasks that do not require high performance but may need to run for longer periods to **LITTLE** cores, thereby helping to preserve a battery charge