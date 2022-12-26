---
Created: [[2022-12-26]]
Aliases: 
Types: Card
Tags: 
- 
---
# Priority inversion
- when a higher-priority [[process]] needs to read or modify kernel data that are currently being accessed by a lower-priority [[process]]
- solution: implementing a **priority-inheritance protocol** (all [[process]]es only access resources from higher-priority [[process]]es)