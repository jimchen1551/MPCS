---
Created: [[2022-08-05]]
Aliases: 
Types: Card
Tags: 
- 
---
# Pipelined datapath
![[Screen Shot 2022-08-04 at 14.16.55.png]]
- The wires from 2nd [[Ripple carry adder]] to [[Multiplexer|MUX]] before [[Program counter]] send the address of next instruction at **MEM** stage and lead to [[Data hazard]]s
- The wires from [[Multiplexer|MUX]] after data memory to [[Register file]] send the result back at the **WB** stage and lead to [[Control hazard]]s
- e.g., for load instruction
  1. IF stage: 
     ![[Screen Shot 2022-08-05 at 01.38.48.png]]
     IF/ID[instruction] = Memory[PC]  // storing info into the pipeline register
     PC = PC+4
     IF/ID[next instruction address] = PC + 4
  2. ID stage: 
     ![[Screen Shot 2022-08-05 at 01.42.18.png]]
     ID/EX[next instruction address] = IF/ID[next instruction address]
     ID/EX[A] = Reg[IF/ID[instruction25:21]]
     ID/EX[B] = Reg[IF/ID[instruction20:16]]
     ID/EX[C] = instruction20:16
     ID/EX[se-offset] = sign-extend(IF/ID[instruction15:0])
  3. EX stage
     ![[Screen Shot 2022-08-05 at 01.51.21.png]]
     EX/MEM[ALUOut] = ID/EX[A] + ID/EX[se-offset]
     EX/MEM[rt] = ID/EX[C]
  4. MEM stage
     ![[Screen Shot 2022-08-05 at 01.53.42.png]]
     MEM/WB[Data] = Memory[EX/MEM[ALUout]]
     MEM/WB[rt] = ID/EX[rt]
  5. WB stage
     ![[Screen Shot 2022-08-05 at 02.03.18.png]]
     Reg[MEM/WB[rt]] = MEM/WB[Data]