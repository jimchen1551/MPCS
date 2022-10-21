---
Created: [[2022-10-21]]
Aliases: CLI, command interpreter
Types: Card
Tags: 
- 
---
# Command line interface
- called **shell** on systems with multiple CLIs to choose from
- e.g., C shell (csh), Z shell (zsh), Bourne-Agian shell (bash), Korn shell (ksh)
- a special program that is running when a process is initiated or when a user first logs on
- getting and executing the next user-specified command
## Command implementation
- two way to implement: 
1. containning the code to execute the command
2. implementing most commands through system programs
   (loading the corresponding command file into memory)
   (in this way, programmers can add new commands to the system easily by creating new files with the proper program logic)