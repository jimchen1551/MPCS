---
Created: [[2022-07-29]]
Aliases: 
Types: Card
Tags: 
- 
---
# Single-cycle CPU
![[Screen Shot 2022-07-29 at 16.23.47.png]]
- To implement the full functionality of a CPU, it combines 
  1. [[Instruction fetch datapath]]
  2. [[Arithmetic-logical instruction datapath]]
  3. [[Memory instruction datapath]]
  4. [[Branch instruction datapath]]
  5. [[Jump instruction datapath]] 
  6. [[Control unit]]
- [[Cycles per instruction|CPI]] = 1
- Critical path: **load** (instruction memory → [[Register file]] → [[Arithmetic logic unit|ALU]] → data memory → [[Register file]])

![[Screen Shot 2022-07-30 at 23.44.02.png]]

![[Screen Shot 2022-07-30 at 23.38.42.png]]
- [[MIPS R-format]] instruction: 
  1. An instruction is fetched from the instruction memory and the [[Program counter|PC]] is incremented (Branch = 0 → PCSrc = 0). 
  2. Two [[Register]]s (rs, rt) are read from the [[Register file]]. 
  3. The [[Arithmetic logic unit|ALU]] operates on the data read from the [[Register file]] (ALUSrc = 0), using the function code (bits 5:0) to generate the [[Arithmetic logic unit|ALU]] function (ALUOp = 10). 
  4. The result from the [[Arithmetic logic unit|ALU]] is written into the [[Register file]] (MemtoReg = 0) using bits 15:11 of the instruction to select the destination [[Register]] (rd) (RegDst = 1; RegWrite = 1). 
(MemRead = 0; MemWrite = 0)

- **load** of [[MIPS I-format]] instruction: 
  1. An instruction is fetched from the instruction memory and the [[Program counter|PC]] is incremented (Branch = 0 → PCSrc = 0). 
  2. A [[Register]] (rs) is read from the [[Register file]]. 
  3. The [[Arithmetic logic unit|ALU]] computes the sum (ALUOp = 00) of the value read from the [[Register file]] and the sign-extended, lower 16 bits of the instruction (offset, ALUSrc = 1). 
  4. The sum from the [[Arithmetic logic unit|ALU]] is used as the address for the data memory. 
  5. The data from the memory unit is written into the [[Register file]] (MemWrite = 0; MemRead = 1; MemtoReg = 1; RegWrite = 1); the [[Register]] destination is given by bits 20:16 (rt) (RegDst = 0). 

- **store** of [[MIPS I-format]] instruction: 
  1. An instruction is fetched from the instruction memory and the [[Program counter|PC]] is incremented (Branch = 0 → PCSrc = 0). 
  2. A [[Register]] (rs) is read from the [[Register file]]. 
  3. The [[Arithmetic logic unit|ALU]] computes the sum (ALUOp = 00) of the value read from the [[Register file]] and the sign-extended, lower 16 bits of the instruction (offset, ALUSrc = 1). 
  4. The sum from the [[Arithmetic logic unit|ALU]] is used as the address for the data memory. 
  5. Write the data from the second [[Register]] (rt) into the data memory (MemWrite = 1; MemRead = 0; MemtoReg = x; RegDst = x; RegWrite = 0). 

- **beq** of [[MIPS I-format]] instruction: 
  1. An instruction is fetched from the instruction memory and the [[Program counter|PC]] is incremented (Branch = 0 → PCSrc = 0). 
  2. Two [[Register]]s (rs, rt) are read from the [[Register file]]. 
  3. The [[Arithmetic logic unit|ALU]] performs a subtract on the data value read from the [[Register file]] (ALUSrc = 0; ALUOp = 01). 
  4. The value of [[Program counter|PC]] + 4 is added to the sign-extended, lower 16 bits of the instruction (offset) shifted left by 2; the result is branch target address. 
  5. The Zero result from the [[Arithmetic logic unit|ALU]] is used to decide which address result to store into the [[Program counter|PC]] (PCSrc = ?). 
(MemRead = 0; MemWrite = 0; MemtoReg = x; RegDst = x; RegWrite = 0)

- [[MIPS J-format]] instruction: 
  1. An instruction is fetched from the instruction memory and the [[Program counter|PC]] is incremented (Branch = 0 → PCSrc = 0). 
  2. The upper 4 bits of [[Program counter|PC]] + 4 is concatenate with the lower 26 bits of the instruction shifted left by 2; the result is jump target address. 
  3. Store the target [[Program counter|PC]] into the [[Program counter|PC]]. 
  - Extension of datapath and control: 
    1. An additional [[Multiplexer|MUX]] to select the source of the new [[Program counter|PC]] between [[Program counter|PC]] + 4, branch target [[Program counter|PC]], or jump target [[Program counter|PC]]. 
    2. An additional control signal for the [[Multiplexer|MUX]]: **jump**
