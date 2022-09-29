---
Created: [[2022-07-16]]
Aliases: ROM
Types: Card
Tags: 
- 
---
# Read-only memory
![[Pasted image 20220617230030.png]]
![[Pasted image 20220617230528.png]]
- a non-volatile memory (storing permanent binary info)
## Fixed AND array
1. The inputs will be duplicated and conjugated by the [[Not]] gates. 
2. With the fixed links, the inputs can be sent parallel and represented as 00, 01, 10, and 11 for each row. 
3. Signals from each row will pass into the [[And]] gates; hence, the outputs of these gates would represent all possible [[Minterm]]s. 
## Programmable OR array
1. Depending on the user's requirement, the outputs of the [[#Fixed AND array]] can be determined whether to fuse and to pass into the [[Or]] gates. 
2. Each output of the [[Or]] gates can correspond with any kind of Boolean function due to the versatilities of fuse link in [[#Programmable OR array]]. 
3. The whole process is supposed to be the sum of [[Minterm]]. 