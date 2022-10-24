---
Created: [[2022-10-14]]
Aliases: boot loader
Types: Card
Tags: 
- 
---
# Bootstrap program
- the **first program** to run while power on
- locating the OS **kernel** and loading into memory
- After loaded into memory, the initial boot loader loads the second boot loader located at a fixed disk location called the **boot block** (sophisticated enough to load the entire [[Operating systems|OS]] into [[Memory]] and begin its execution)
- **initializing** all aspects of the systems
- stored in **BIOS** and technically in **EEP[[Read-only memory|ROM]]** (electrically erasable programmable read-only memory) or other forms of firmware (infrequently written and nonvolatile but slow)
- some replace **BIOS-based boot process** with **UEFI** (unified extensible firmware interface; a single, faster, and complete boot manager ; better support for 64-bit systems and larger disks)