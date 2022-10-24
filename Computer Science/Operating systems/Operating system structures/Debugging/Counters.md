---
Created: [[2022-10-24]]
Aliases: 
Types: Card
Tags: 
- 
---
# Counters
- OS keep track of system activity through a series of counters (# of [[System call]]s, # of operations performed to a network device or disk)
- most of the counter-based tools on Linux systems read statistics from the `/proc` file system (a pseudo file system existing only in kernel memory)
## Per-Process
`ps`: reports information for a single process or selection of processes
`top`: eports real-time statistics for current processes
## System-Wide
`vmstat`: reports memory-usage statistics
`netstat`: reports statistics for network interfaces
`iostat`: reports I/O usage for disks