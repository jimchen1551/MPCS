---
Created: [[2022-07-19]]
Aliases: 
Types: Card
Tags: 
- 
---
# 32-bit ALU
![[Screen Shot 2022-07-21 at 18.44.32.png]]
- Just like [[1-bit ALU]], it also has AInvert, BInvert, and Operation inputs to determine which function to implement. 
- The design resembles [[Ripple carry adder]]; however, in the real case, the design much resembles [[Carry lookahead adder]]. 
- While at set-on-less-than mode, zero is True for the result, because the result will be [[Or]] and [[Not]] before passing out. 