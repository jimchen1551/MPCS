---
Created: [[2022-10-10]]
Aliases: 
Types: Note
Tags: 
- 
---
# Operating system structures
![[Screen Shot 2022-10-21 at 12.33.44.png]]

| [[Operating systems]] | Content                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[User interface]]    | [[Command line interface]]<br>[[Graphic user interface]]<br>[[Touch screen interface]]                                                                                                                    |
| [[System call]]       | [[Application Programming interface]]<br>[[Run-time environment]]<br>[[Process control]]<br>[[File management]]<br>[[Device management]]<br>[[Status information]]<br>[[Communication]]<br>[[Protection]] |
| [[System service]]    | [[File management]]<br>[[Status information]]<br>[[File modification]]<br>[[Programming-language support]]<br>[[Program execution]]<br>[[Communication]]<br>[[System daemon]]                             |
| [[Kernel]]            | [[Monolithic kernel]]<br>[[Layered kernel]]<br>[[Microkernel]]<br>[[Modular kernel]]<br>[[Hybrid kernel]]                                                                                                 |

![[Pasted image 20221024200855.png]]
## OS generation
1. Write the OS source code. 
   Linux: download from http://www.kernel.org
2. Configure the OS. (configuration file)
   Linux: use `make menuconfig` and `.config` file generated
3. Compile the OS. (system build)
   Linux: use `make`, `vmlinuz` file generated, and then use `make modules`
4. Install the OS. 
   Linux: use `make modules_install` to install the kernel modules into `vmlinuz` and use `make install`
5. Boot the computer and its new OS. 

## System boot
1. [[Bootstrap program]] locates the kernel. 
2. Kernel is **loaded** into [[Memory]] and started. 
3. Kernel **initializes** hardware. 
4. **Root file system** is mounted. 

## OS debugging
### Failure analysis
- If a process fails, most OS write the error info to a **log file** to alert system admins or users that the problem occurred.
- The OS can also take a **core dump** (a capture of the memory of the process) and store it in a file for later analysis.
- Running programs and core dumps can be probed by a **debugger**, which allows a programmer to explore the code and memory of a process at the time of failure.
- A failure in the kernel is called a **crash**. 
- When a **crash** occurs, **error info** is saved to a log file, and the memory state is saved to a crash dump.
### Performance monitoring and tuning
### Tracing
### BCC
