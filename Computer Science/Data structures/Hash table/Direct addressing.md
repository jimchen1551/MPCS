---
Created: [[2022-11-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Direct addressing
![[Screen Shot 2022-11-25 at 14.52.53.png|500]]

```Pseudocode
DIRECT-ADDRESS-SEARCH(T, k)
return T[k]

DIRECT-ADDRESS-INSERT(T, x)
T[x.key] = x

DIRECT-ADDRESS-DELETE(T, x)
T[x.key] = NIL
```

- the universe $U$ of keys is reasonably small, $U=\{0, 1, \dots, m-1\}$
- using a linear array to represent the dynamic set $T[0:m-1]$
- if $U$ is large, storing $T$ of size $|U|$ is impractical
