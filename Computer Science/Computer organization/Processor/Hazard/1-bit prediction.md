---
Created: [[2022-08-10]]
Aliases: 
Types: Card
Tags: 
- 
---
# 1-bit prediction
- It has a small memory indexed by the **lower portion of the address** of the branch instruction. 
- The memory contains **a bit** in each entry that says whether the branch was **recently taken or not**. 
- Prediction is just a hint that is assumed to be correct, so fetching begins in the predicted direction. 
- If the hint turns out to be wrong, the prediction bit is inverted and stored back, and the proper sequence is executed. 