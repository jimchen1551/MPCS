---
Created: [[2022-07-16]]
Aliases: 
Types: Note
Tags: 
- 
---
# Sequential circuits
![[Pasted image 20220618002040.png]]
- The inputs and stored values determine the outputs of logic gates. 

![[Pasted image 20220706233635.png]]

| [[Synchronous sequential circuit]] | [[Asynchronous sequential circuit]] |
| ---------------------------------- | ----------------------------------- |
| [[Flip-flop]]                      | [[Latch]]                           |
| [[Master-slave flip-flop]]         | [[SR latch]]                        |
| [[Edge-triggered flip-flop]]       | [[S'R' latch]]                      |
| [[JK flip-flop]]                   | [[D latch]]                         |
| [[T flip-flop]]                    |                                     |

## Direct input
- asynchronous input independent from the clock
- used to force the flip-flop to a particular state
- e.g., When a digital system is turned on, the state of the flip-flop is unknown; the direct inputs are useful for bringing all flip-flops in the system to a known starting state prior to the clocked operation. 
### Preset
- direct set
- setting flip-flop to 1
### Clear
- direct reset
- setting flip-flop to 0

## Timing
![[Pasted image 20220706121948.png]]

| Time                       | Meaning                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Setup time                 | the minimum time for which the D input must be maintained at a constant value prior to the occurrence of the clock transition |
| Hold time                  | the minimum time for which the D input must not change after the application of the positive transition of the clock          |
| [[Propagation delay]] time | the time interval between the trigger edge and the stabilization of the output to a new state                                 |

### Duty cycle
![[Pasted image 20220706125022.png]]

## Performance
[Performance](Computer%20organization.md#Performance)
- $t_{pd,FF}$: flip-flop [[Propagation delay]]
- $t_{pd, COMB}$: combinational [[Propagation delay]]
- $t_s$: flip-flop Setup time
- $t_h$: flip-flop Hold time
- $t_{slack}$: Slack time, the extra time allowed in the clock period beyong that required by the path

![[Screen Shot 2022-07-07 at 01.06.57.png]]
![[Screen Shot 2022-07-07 at 01.08.05.png]]
- $t_i$: the latest time that the input changes after the positive clock edge
- $t_o$: the latest time that the output is permitted to change prior to the next clock edge

![[Screen Shot 2022-07-07 at 01.13.40.png]]
$$t_p=t_{slack}+(t_{pd,FF}+t_{pd,COMB}+t_s)$$$$t_p\geq max(t_{pd,FF}+t_{pd,COMB}+t_s)=t_{p, min}$$
- If $t_p$ is too large t meet the circuit specifications: 
  employ faster logic cells
  change the circuit design to reduce the problematic path delays through the circuit

- $t_h$: Hold time
	- not appearing in the clock period equation
	- relating to another timing constraint equation dealing with one or both of 2 specific situations: 
		1. output changes arrive at the inputs of one or more flip-flops too soon
		2. clock signals reaching one or more flip-flops are somehow delayed (clock skew)

## Analysis
- obtaining a suitable description that demonstrates the time sequence of inputs, outputs, and states
  1. Flip-flop input & output equations
  2. Next state equations
  3. State table
     ![[Pasted image 20220707001346.png]]
  4. State diagram
     ![[Pasted image 20220707001305.png]]

## Simulation
![[Screen Shot 2022-09-23 at 10.46.59.png]]
- The input patterns must be applied in a sequence
- There must be some means to place the circuit in a known state. 
- Observe the state to verify correctness. 
- Deal with the timing of application of inputs and observation of output relative to the active clock edge
### Function simulation
- determination or verification of the function of the circuit
- assuming circuit components has no delay or a very small delay
### Timing simulation
- verification of the proper operation of the circuit in terms of timing
- assuming circuit components has realistic delays

## Design
![[Screen Shot 2022-09-23 at 11.09.37.png]]

| Procedure                     | Content                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Specificaiton                 | writing a spec for the circuit                                                                                          |
| [[Formulation]]               | obtaining either a state diagram or state table from the statement of the problem                                       |
| [[State reduction]]           | reducing the number of states if necessary                                                                              |
| [[State assignment]]          | assigning binary codes to the states and obtaining the binary-coded state table                                         |
| Input equation determination  | selecting the flip-flop type(s) and deriving the input equations from the next-state entries in the encoded state table |
| Output equation determination | deriving output equations from the output entries in the state table                                                    |
| Optimization                  | optimizing the input and output equations                                                                               |
| [[Technology mapping]]        | transforming the logic diagram to a new diagram using available technology                                              |
| [[Verification]]              | verifying the correctness of the final design                                                                           |
