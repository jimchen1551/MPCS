---
Created: [[2022-08-03]]
Aliases: 
Types: Card
Tags: 
- 
---
# Control hazard
- Arising from the flow of instruction address is not what the pipeline expected. 
- assuming branch not taken and discarding instructions if the branch is taken
  - **flushing** instructions in the **IF**, **ID**, and **EX** stages of the pipeline
  - reducing the delay is an issue for speeding
    - moving the branch execution from MEM to ID stage (flushing only one stage)
      1. easy part: moving up the branch address calculation
      2. hard part: the branch decision
         - for branch equal, comparing the two register reads during the ID stage to see if they are equal (XOR every respective bit and NOR all the results)

![[Screen Shot 2022-08-10 at 20.48.46.png]]

- Solutions: [[Stalling]], [[Branch prediction]], and [[Delayed branch]]
- e.g., [[Branch]] needs to compare register and compute target early (**ID** stage) in the pipeline. So the [[Program counter]] waits until branch outcome determined before fetching next instruction. (**Stall on branch**)
![[Screen Shot 2022-08-03 at 21.46.52.png]]
