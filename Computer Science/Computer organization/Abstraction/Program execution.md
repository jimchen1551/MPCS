---
Created: [[2022-07-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Program execution
![[Pasted image 20220707161000.png]]

| Translator   | Comment                                             |
| ------------ | --------------------------------------------------- |
| [[Compiler]] | translate the program into machine instructions     |
| [[Linker]]   | link object modules and produce an executable image |
| [[Loader]]   | loading from image file on disk into memory         |

| Linking             | Comment                                      |
| ------------------- | -------------------------------------------- |
| [[Static linking]]  | running in very limited environments         |
| [[Dynamic linking]] | only link/load library procedure when called |
| [[Lazy linking]]    |                                              |

## System service
1. absolute [[Loader]]
2. relocatable [[Loader]]
3. linkage editors
4. overlay-loader
5. debugging system for [[Application program#High-level language HLL]] and machine language