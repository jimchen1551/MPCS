---
Created: [[2022-08-03]]
Aliases: 
Types: Card
Tags: 
- 
---
# Branch prediction
![[Screen Shot 2022-08-03 at 21.56.20.png]]
([[MIPS]] with predict "Not Taken")
- predicting the outcome of the branch at the **IF** stage ([[#Dynamic branch prediction]])
- Because deeper and superscalar pipelines can't readily determine branch outcomes early, the stall penalty becomes unacceptable. 
- Only stall if the prediction is wrong (misprediction). 

## Static branch prediction
- based on typical branch behavior by [[Compiler]]
- e.g., loop and if-statement branches
  - predicting backward branches: taken
  - predicting forward branches: not taken

## Dynamic branch prediction
- Hardware measures actual branch behavior
- assuming future behavior will continue the trend
- **Branch prediction buffer**
  - aka branch history table
  - kind of memory
  - Steps: 
    1. check the table at the IF stage and expect the same outcome
    2. start to fetch from fall-through or target
    3. flush pipeline and flip prediction if the prediction is wrong
- **Branch target buffer**
  - cache of  target addresses
  - indexed by [[Program counter|PC]] when instruction fetched
  - avoiding from penalty caused by calculaiton of target address
- e.g., recording the recent history of each branch
- [[1-bit prediction]] and [[2-bit prediction]]
