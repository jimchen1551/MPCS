---
Created: [[2022-12-26]]
Aliases: memory fences
Types: Card
Tags: 
- 
---
# Memory barriers
2 categories of memory model:
1. **Strongly ordered**, where a [[memory]] modification on one [[processor]] is immediately visible to all other [[processor]]s
2. **Weakly ordered**, where modifications to [[memory]] on one [[processor]] may not be immediately visible to other [[processor]]s
- instructions that **force** any changes in [[memory]] to be propagated to all other [[processor]]s, thereby ensuring that [[memory]] modifications are visible to [[thread]]s running on other [[processor]]s
- when performed, the system ensures that all loads and stores are completed before any subsequent load or store operations are performed
- considered very low-level operations
- typically used by kernel developers when writing specialized code ensuring mutual exclusion