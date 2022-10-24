---
Created: [[2022-10-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Hybrid kernel
- most OS **combining** different structures
## macOS and iOS
![[Pasted image 20221024200732.png]]
![[Screen Shot 2022-10-24 at 21.19.25.png|400]]
Architecture of macOS and iOS
1. User experience: 
   [[Graphic user interface|GUI]]
   Aqua for macOS; Springboard for iOS
2. Application frameworks: 
   [[Application Programming interface|API]] for Objective-C and Swift
   Cocoa for macOS; Cocoa Touch for iOS
3. Core frameworks: 
   supporting graphics and media
   Quicktime and OpenGL
4. Kernel environment
   Darwin (including Mach [[Microkernel]] and BSD UNIX kernel)

![[Screen Shot 2022-10-24 at 21.19.41.png|400]]
Structure of Darwin
- providing 2 [[Run-time environment|system call interface]]s: 
	1. Mach [[System call]]: providing fundamental [[System service]]s
	2. BSD [[System call]]
- providing an IO kit for development of [[Device driver]]s and dynamically [[Modular kernel|loadable kernel module]]s
- combining Mach, BSD, IO kit, and any kernel extensions into a single address space (to reduce message passing of [[Microkernel]])

## Android
![[Screen Shot 2022-10-24 at 21.21.39.png|400]]
Architecture of Android
- developed by Open Handset Alliance
- based on Linux kernel but modified
- runtime environment includes core set of libraries and Dalvik [[Virtualization|VM]]
- apps developed in Java plus Android [[Application Programming interface|API]]
- libraries including frameworks for web browser (webkit), database (SQLite), multimedia, smaller libc
